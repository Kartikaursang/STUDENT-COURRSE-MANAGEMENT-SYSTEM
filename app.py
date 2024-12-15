from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from werkzeug.security import check_password_hash 
from flask import session
from flask import Response
import csv
from io import StringIO
from flask import Flask, render_template, request, redirect, flash


app = Flask(__name__)


def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Rakshu@12345',
        database='studentdb'
    )
    return connection

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/user-login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        if 'email' in request.form and 'password' in request.form:
            email = request.form['email']
            password = request.form['password']
            print(f"Attempting login with email: {email} and password: {password}")

            
            connection = get_db_connection()
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM student WHERE student_email = %s", (email,))
            user = cursor.fetchone()
            print(f"User found: {user}")

        
            if user and user[4] == password:  
                print("Login successful!")
                user_id = user[0]  
                return redirect(url_for('user_dashboard', user_id=user_id))
            else:
                print("Invalid login attempt.")
                return render_template('user_login.html', error='Invalid email or password.')

        else:
            return render_template('user_login.html', error='Email and password are required.')

    return render_template('user_login.html')



@app.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(f"Attempting login with email: {email} and password: {password}")

     
        connection = get_db_connection()
        cursor = connection.cursor()

       
        cursor.execute("SELECT * FROM admin WHERE email = %s", (email,))
        admin = cursor.fetchone()
        print(f"Admin found: {admin}") 

        if admin and admin[2] == password:
            print("Login successful!")
            return redirect(url_for('admin_dashboard'))
        else:
            print("Invalid login attempt.")
            return render_template('admin_login.html', error='Invalid email or password.')

    return render_template('admin_login.html')






@app.route('/user-dashboard/<int:user_id>', methods=['GET', 'POST'])
def user_dashboard(user_id):
    connection = get_db_connection()
    cursor = connection.cursor()

  
    cursor.execute("SELECT * FROM student WHERE student_id = %s", (user_id,))
    student = cursor.fetchone()


    cursor.execute("SELECT * FROM course WHERE course_id = %s", (student[3],))  
    course = cursor.fetchone()


    cursor.execute("SELECT * FROM Notification ORDER BY created_at DESC LIMIT 5")
    notifications = cursor.fetchall()


    if request.method == 'POST':
        new_name = request.form.get('name')
        new_email = request.form.get('email')
        cursor.execute("UPDATE student SET student_name = %s, student_email = %s WHERE student_id = %s",
                       (new_name, new_email, user_id))
        connection.commit()
        return redirect(url_for('user_dashboard', user_id=user_id))

    return render_template('user_dashboard.html', student=student, course=course, notifications=notifications)







@app.route('/admin_dashboard', methods=['GET', 'POST'])
def admin_dashboard():
    connection = get_db_connection()
    cursor = connection.cursor()
   
    if request.method == 'POST':
        action = request.form.get('action')
       
        if action == 'add_course':
            course_name = request.form.get('course_name')
            course_code = request.form.get('course_code')
            course_duration = request.form.get('course_duration')

            cursor.execute('''
                INSERT INTO Course (course_name, course_code, course_duration)
                VALUES (%s, %s, %s)
            ''', (course_name, course_code, course_duration))
            connection.commit()
        
        elif action == 'add_student':
            student_name = request.form.get('student_name')
            student_email = request.form.get('student_email')
            student_course = request.form.get('student_course') 
            student_password = request.form.get('student_password')  

            cursor.execute('''
                INSERT INTO Student (student_name, student_email, course_id, password)
                VALUES (%s, %s, %s, %s)
            ''', (student_name, student_email, student_course, student_password))
            connection.commit()

       
        elif action == 'send_notification':
            notification_message = request.form.get('notification_message')

            cursor.execute('''
                INSERT INTO Notification (message)
                VALUES (%s)
            ''', (notification_message,))
            connection.commit()

       
        elif action == 'delete_student':
            student_id = request.form.get('student_id')

            cursor.execute('''
                DELETE FROM Student WHERE student_id = %s
            ''', (student_id,))
            connection.commit()

        
        elif action == 'delete_course':
            course_id = request.form.get('course_id')

            cursor.execute('''
                DELETE FROM Course WHERE course_id = %s
            ''', (course_id,))
            connection.commit()


        elif action == 'delete_notification':
            notification_id = request.form.get('notification_id')

            cursor.execute('''
                DELETE FROM Notification WHERE notification_id = %s
            ''', (notification_id,))
            connection.commit()

   
    cursor.execute('SELECT course_id, course_name, course_code, course_duration FROM Course')
    courses = cursor.fetchall()

    cursor.execute('SELECT student_id, student_name, student_email, course_id FROM Student')
    students = cursor.fetchall()

    cursor.execute('''
        SELECT 
            Student.student_name, 
            Course.course_name 
        FROM 
            Student
        INNER JOIN 
            Course 
        ON 
            Student.course_id = Course.course_id
    ''')
    enrollments = cursor.fetchall()

    cursor.execute('SELECT notification_id, message, created_at FROM Notification ORDER BY created_at DESC LIMIT 5')
    notifications = cursor.fetchall()

   
    cursor.close()
    connection.close()

    return render_template(
        'admin_dashboard.html',
        courses=courses,
        students=students,
        enrollments=enrollments,
        notifications=notifications
    )

@app.route('/logout')
def logout():   
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)