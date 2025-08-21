# Online Learning Platform – Django ORM Project

## Overview
This project implements the backend of an **online learning platform** using **Django ORM** and **PostgreSQL**.  
It was developed as part of an IBM course to practice real-world database modeling, object-relational mapping, and querying with Django.

The system models **Learners, Courses, Instructors, Lessons, and Enrollments**, allowing us to simulate how students interact with online courses and how instructors manage their classes.

---

## Features
- **User Management**
  - `Learner` model extending Django’s built-in `User`
  - Support for different occupations (Student, Developer, Data Scientist, DBA)
- **Course Management**
  - Courses with descriptions and multiple instructors
  - Lessons tied to courses with detailed content
- **Relationships**
  - One-to-Many: `Course` → `Lesson`
  - Many-to-Many: `Course` ↔ `Instructor`, `Course` ↔ `Learner`
  - Many-to-Many with a custom join table: `Enrollment`
- **Enrollment Tracking**
  - Learners can enroll in multiple courses
  - Enrollment records store date and learning mode (Audit or Honor)
- **CRUD Operations**
  - Create, update, and delete records for all models
  - Query learners by occupation, instructors by course, and more

---

## Tech Stack
- **Python 3.11**
- **Django 4.x**
- **PostgreSQL**
- **psycopg2** (PostgreSQL adapter for Python)

---
