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

# Flask Routes

## 1. Home Route
### `GET /`
- **Description**: Renders the home page.
- **Function**: `home()`

## 2. User Login Route
### `GET /user-login`
### `POST /user-login`
- **Description**: Handles user login, allowing students to log in with their email and password.
- **Function**: `user_login()`
  - On `POST`: Checks user credentials and redirects to the user dashboard if successful, otherwise shows an error.

## 3. Admin Login Route
### `GET /admin-login`
### `POST /admin-login`
- **Description**: Handles admin login, allowing the admin to log in with their email and password.
- **Function**: `admin_login()`
  - On `POST`: Checks admin credentials and redirects to the admin dashboard if successful, otherwise shows an error.

## 4. User Dashboard Route
### `GET /user-dashboard/<int:user_id>`
### `POST /user-dashboard/<int:user_id>`
- **Description**: Displays the dashboard for the logged-in student, including their information, enrolled course, and recent notifications.
- **Function**: `user_dashboard(user_id)`
  - On `POST`: Allows the student to update their name and email.

## 5. Admin Dashboard Route
### `GET /admin-dashboard`
### `POST /admin-dashboard`
- **Description**: Displays the admin dashboard, where the admin can manage courses, students, and notifications.
- **Function**: `admin_dashboard()`
  - On `POST`: Handles various actions:
    - `add_course`: Adds a new course to the database.
    - `add_student`: Adds a new student to the database.
    - `send_notification`: Sends a new notification to students.
    - `delete_student`: Deletes a student from the database.
    - `delete_course`: Deletes a course from the database.
    - `delete_notification`: Deletes a notification.

## 6. Logout Route
### `GET /logout`
- **Description**: Logs the user out and redirects to the home page.
- **Function**: `logout()`

#  Screenshots 

## 1. Home Page
### Description:
The home page serves as the landing page of the application, providing links to the user login and admin login pages. It welcomes the user and offers an overview of the site’s functionalities.
    ![Home Page Screenshot](/screenshots/mainpage.png)

---

## 2. User Login Page
### Description:
The user login page allows students to log in using their email and password. Upon successful login, the student will be redirected to the user dashboard. If the credentials are incorrect, an error message is shown prompting the user to retry.
    ![User Login Screenshot](path_to_user_login_screenshot.png)

---

## 3. Admin Login Page
### Description:
This page allows administrators to log in using their email and password to access the admin dashboard. If the login details are incorrect, an error message will prompt the admin to retry.

### Output (Screenshot):
![Admin Login Screenshot](path_to_admin_login_screenshot.png)

---

## 4. User Dashboard Page
### Description:
The user dashboard displays the student's profile, including their name, email, and enrolled course. It also shows recent notifications relevant to the student. The student can update their name and email through this page. After making changes, the student is redirected to the same page with updated details.

### Output (Screenshot):
![User Dashboard Screenshot](path_to_user_dashboard_screenshot.png)

---

## 5. Admin Dashboard Page
### Description:
The admin dashboard allows the administrator to manage the data on the site. Admins can add new courses, students, and send notifications. They can also delete students, courses, and notifications. This page provides an overview of the courses, students, enrollments, and recent notifications.

### Output (Screenshot):
![Admin Dashboard Screenshot](path_to_admin_dashboard_screenshot.png)

---

## 6. Logout Page
### Description:
The logout page logs the user (either a student or admin) out of the application, ending the session and redirecting the user back to the home page.

### Output (Screenshot):
![Logout Screenshot](path_to_logout_screenshot.png)

