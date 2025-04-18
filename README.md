 # DJANGO-BLOG

# My Awesome Django Web Application

Welcome to my Django web application! This project is designed to provide users with a platform to create blog posts, announce announcements, view a calendar, and check the weather forecast for various locations.

## Features

### Blog App
- Users can register an account to create and manage their own blog posts.
- Announcements can be made and managed by authorized users.
- Protected login/logout system ensures security for user accounts.

### Calendar App
- Accessible calendar feature for users to view events and important dates.

### Weather App
- Provides users with the current weather forecast for specific locations.
- Users can search for weather information for any location.

## Technology Stack

- **Framework**: Django
- **Hosting**: Render
- **Database**: PostgreSQL
- **Static Files**: Amazon S3 bucket

## Setup Instructions

1. Clone the repository from GitHub.
2. Install the required dependencies listed in `requirements.txt`.
3. Set up PostgreSQL and configure the database settings in `settings.py`.
4. Set up an S3 bucket on Amazon Web Services for hosting static files.
5. Configure Django settings to use the S3 bucket for static files.
6. Run migrations to create database tables.
7. Start the Django development server.

<!--
 ```bash
python manage.py migrate
python manage.py runserver
-->

## Usage
1. Register for an account or log in if you already have one.
2. Explore the blog app to create, view, update, or delete posts.
3. Check out the announcements section for important updates.
4. Navigate to the calendar to view upcoming events.
5. Use the weather app to check the weather forecast for desired locations.

# Contributions
- Contributions are welcome! If you'd like to contribute to the project    - then feel free to submit a pull request.


