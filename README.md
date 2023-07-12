# Django Jeonse Calculator
Source code for Pycon Korea 2023 Tutorial

## Aim of this project
In this comprehensive tutorial, we will explore how to build a modern, feature-rich rental listing website using Django, a popular Python web framework, and several community packages. By harnessing the power of packages such as django-allauth, django-tables2, django-htmx, and django-filter, we will create a dynamic and efficient website that offers enhanced functionality and user experience.

Throughout the tutorial, we will guide you through the process of setting up the Django project and integrating these community packages seamlessly. We will demonstrate how django-allauth simplifies user authentication, registration, allowing users to easily sign up, log in, and manage their rental listings.

We will leverage the power of django-tables2 to generate interactive and customizable tables for displaying rental listings, complete with sorting, pagination, and filtering capabilities. By integrating django-htmx, we will implement seamless and efficient user interactions, such as updating listing details, filtering results, and dynamically loading content without full page refreshes, resulting in a smooth and responsive user interface.

To enhance the search functionality, we will utilize django-filter to create advanced filtering options, enabling users to refine their search results based on criteria such as location, price range, amenities, and more.

Throughout the tutorial, we will provide clear and concise instructions, accompanied by code examples and demonstrations of each package's usage. By the end of the tutorial, you will have a fully functional rental listing website that showcases the power of Django and its community packages in creating modern, fast, and feature-rich web applications.

## Tutorial outline:
1. Introduction
    * Overview of the tutorial
    * Explanation of the application's purpose and functionality
2. Prerequisites
    * Django installation
    * Basic understanding of Django and Python
3. Setting up the Project
    * Creating a new Django project
    * Creating a new Django app for rental listings
4. Defining the Models
    * Creating the Listing model
    * Adding fields for title, description, price, location, amenities, etc.
    * Defining the relationships between models (if needed)
1. Database Configuration
    * Configuring the database settings in Django
    * Applying migrations to create the necessary database tables
1. Creating Views and Templates
    * Listing List View: Displaying a list of all rental listings
    * Listing Detail View: Displaying detailed information about a specific rental listing
    * Listing Create View: Allowing users to create new rental listings
    * Listing Update View: Allowing users to modify existing rental listings
1. Building Forms
    * Creating a ListingForm for creating and updating rental listings
    * Implementing form validation and handling form submissions
1. Routing URLs
    * Configuring URL patterns for different views
    * Mapping URLs to appropriate view functions
1. User Authentication and Permissions
    * Implementing user registration and login functionality
    * Restricting certain views or actions to authenticated users
    * Implementing authorization and permissions as required
1. Styling with CSS
    * Adding CSS stylesheets to enhance the application's appearance
    * Applying responsive design principles for better user experience
1. Testing the Application
    * Writing unit tests for models, views, and forms
    * Running tests to ensure the application functions correctly
1. Deployment
    * Preparing the application for deployment
    * Deploying the Django application to a web server or hosting platform (optional)
1. Conclusion
    * Recap of what was covered in the tutorial
    * Encouraging further exploration and enhancements to the application

### 1. Introduction
In this tutorial, we will build a rental listing website using Django, a popular Python web framework. The application will allow users to create and manage rental listings, as well as search for listings based on various criteria.
### 2. Prerequisites

* Python 3.8+ ([Python](https://www.python.org/downloads/))
* Django 4.2+ ([Django](https://pypi.org/project/Django/))
* Pipenv (or any other virtual environment manager)
* Shell (Terminal, Command Prompt, etc.)
* Text Editor ([VS Code](https://code.visualstudio.com/))

### 3. Setting up the Project
1. **Install Python 3.8+ and Django 4.2+**

    * Install python: https://www.python.org/downloads/
    * Make a directory for the project: `mkdir django-jeonse`
    * Change directory to the project: `cd django-jeonse`
    * Install pipenv (we will use it for virtual environment): `pip install pipenv`
    * Install Django: `pipenv install django==4.2.3`
    * Create virtual environment: `pipenv shell`

2. **Create Django project**

    * Create Django project: `django-admin startproject settings .`
    * Create Django app: `python manage.py startapp jeonse`
    * Add `jeonse` to `INSTALLED_APPS` in `settings.py`:
        ```python
        # settings.py

        INSTALLED_APPS = [
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.messages",
            "django.contrib.staticfiles",
            "jeonse"                        # <-- Add this line
        ]
        ```
    * Run server: `python manage.py runserver`
    * Open browser and go to `http://localhost:8000`: `open http://localhost:8000`

3. **Custom user model**
    * Open `jeonse/models.py` and add `CustomUser` model:
        ```python
        from django.contrib.auth.models import AbstractUser
        from django.db import models

        class CustomUser(AbstractUser):
            pass
        ```
    * Add `AUTH_USER_MODEL = 'jeonse.CustomUser'` to `settings.py`
        ```python
        # settings.py

        AUTH_USER_MODEL = 'jeonse.CustomUser'
        ```
    * Run makemigrations: `python manage.py makemigrations`
    * Run migrate: `python manage.py migrate`
    * Run server: `python manage.py runserver`
