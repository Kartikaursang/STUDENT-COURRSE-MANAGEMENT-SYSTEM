# Student and Course Management System

This project is a web-based Student and Course Management System built using Python (Flask) and MySQL. It provides a platform for students and administrators to manage profiles, courses, and notifications. The system includes features for user and admin login, profile updates, course management, and notifications.

## Features

### Student Features:
- **User Login:** Students can log in with their credentials.
- **Dashboard:** After login, students can view their profile details and course information.
- **Profile Update:** Students can update their name and email.
- **Notifications:** Students can view the latest notifications from the admin.

### Admin Features:
- **Admin Login:** Admins can log in with their credentials.
- **Dashboard:** Admins can manage courses, students, and notifications.
- **Add Courses:** Admins can add new courses.
- **Add Students:** Admins can add new students.
- **Send Notifications:** Admins can send notifications to students.
- **Delete Courses, Students, and Notifications:** Admins can delete records from the system.

## Technologies Used

- **Backend:** Python (Flask)
- **Database:** MySQL
- **Frontend:** HTML, CSS, JavaScript
- **Others:** MySQL Connector for Python (`mysql-connector`)

# Database Schema - `studentdb`

## Tables

### 1. `admin`
Stores information about the administrators of the system.

| Field     | Type         | Null | Key | Default | Extra          |
|-----------|--------------|------|-----|---------|----------------|
| id        | int          | NO   | PRI | NULL    | auto_increment |
| email     | varchar(255) | NO   | UNI | NULL    |                |
| password  | varchar(255) | NO   |     | NULL    |                |

### 2. `course`
Stores details about courses available in the system.

| Field           | Type         | Null | Key | Default | Extra          |
|-----------------|--------------|------|-----|---------|----------------|
| course_id       | int          | NO   | PRI | NULL    | auto_increment |
| course_name     | varchar(100) | NO   |     | NULL    |                |
| course_code     | varchar(50)  | NO   | UNI | NULL    |                |
| course_duration | int          | NO   |     | NULL    |                |

### 3. `notification`
Stores notifications to be sent to users, with a timestamp of creation.

| Field           | Type      | Null | Key | Default           | Extra             |
|-----------------|-----------|------|-----|-------------------|-------------------|
| notification_id | int       | NO   | PRI | NULL              | auto_increment    |
| message         | text      | NO   |     | NULL              |                   |
| created_at      | timestamp | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |

### 4. `student`
Stores information about students enrolled in courses.

| Field         | Type         | Null | Key | Default | Extra          |
|---------------|--------------|------|-----|---------|----------------|
| student_id    | int          | NO   | PRI | NULL    | auto_increment |
| student_name  | varchar(100) | NO   |     | NULL    |                |
| student_email | varchar(100) | NO   | UNI | NULL    |                |
| course_id     | int          | YES  | MUL | NULL    |                |
| password      | varchar(255) | NO   |     | NULL    |                |

