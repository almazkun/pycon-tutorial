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
1. Prerequisites
    * Django installation
    * Basic understanding of Django and Python
1. Setting up the Project
    * Creating a new Django project
    * Creating a new Django app for rental listings
1. Setting up the Project
    * Install Python 3.8+ and Django 4.2
    * Create Django project
    * Custom user model
    * Create User Signup and Signin Views
    * Create Listing Model and Views
    * Configuring URL patterns for different views
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

1. Python 3.8+ ([Python](https://www.python.org/downloads/))
1. Django 4.2+ ([Django](https://pypi.org/project/Django/))
1. Pipenv ([Pipenv](https://pypi.org/project/pipenv/), or any other virtual environment manager)
1. Shell (Terminal, Command Prompt, PowerShell, etc.)
1. Text Editor ([VS Code](https://code.visualstudio.com/) or any other editor of your choice)

### 3. Setting up the Project
1. **Install Python 3.8+ and Django 4.2+**

    1. Install python: https://www.python.org/downloads/
    1. Make a directory for the project: `mkdir django-jeonse`
    1. Change directory to the project: `cd django-jeonse`
    1. Install pipenv (we will use it for virtual environment): `pip install pipenv`
    1. Install Django: `pipenv install django==4.2.3`
    1. Create virtual environment: `pipenv shell`
    1. Open this project in VS Code: `code .`

2. **Create Django project**

    1. Create Django project: `django-admin startproject settings .`
    1. Create Django app: `python manage.py startapp jeonse`
    1. Add `jeonse` to `INSTALLED_APPS` in `settings.py`:
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
    1. Run server: `python manage.py runserver`
    1. Open browser and go to `http://localhost:8000`: `open http://localhost:8000`

3. **Custom user model**
    1. Open `jeonse/models.py` and add `CustomUser` model:
        ```python
        from django.contrib.auth.models import AbstractUser
        from django.db import models

        class CustomUser(AbstractUser):
            pass
        ```
    1. Add `AUTH_USER_MODEL = 'jeonse.CustomUser'` to `settings.py`
        ```python
        # settings.py

        AUTH_USER_MODEL = 'jeonse.CustomUser'
        ```
    1. Run makemigrations: `python manage.py makemigrations`
    1. Run migrate: `python manage.py migrate`
    1. Run server: `python manage.py runserver`

4. **Create User Signup and Signin Views**
    1. Install django-allauth: `pipenv install django-allauth==0.54.0`
    1. Add `allauth` to `INSTALLED_APPS` in `settings.py`:
        ```python
        # settings.py

        INSTALLED_APPS = [
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.messages",
            "django.contrib.staticfiles",
            "jeonse",
            "allauth",                          # <-- Add this line
            "allauth.account",                  # <-- Add this line
        ]
        ```
    1. Add `'django.template.context_processors.request'` to `TEMPLATES`
    1. Add `AUTHENTICATION_BACKENDS` in `settings.py`:
        ```python
        # settings.py

        # django-allauth settings
        # https://django-allauth.readthedocs.io/en/latest/installation.html
        AUTHENTICATION_BACKENDS = [
            'django.contrib.auth.backends.ModelBackend',
            'allauth.account.auth_backends.AuthenticationBackend',
        ]
        ```
    1. Configure Allauth settings in `settings.py`:
        ```python
        # settings.py

        # https://django-allauth.readthedocs.io/en/latest/configuration.html
        ACCOUNT_USERNAME_REQUIRED = False
        ACCOUNT_AUTHENTICATION_METHOD = "email"
        ACCOUNT_EMAIL_REQUIRED = True
        ACCOUNT_UNIQUE_EMAIL = True
        ACCOUNT_EMAIL_VERIFICATION = "none"
        ```
    1. Create `urls.py` in `jeonse` app: `touch jeonse/urls.py`
    1. Create `account_login`, `account_logout`, and `account_signup` URLs in `jeonse/urls.py`:
        ```python
        # jeonse/urls.py

        from django.urls import path
        from allauth.account import views as allauth_views

        urlpatterns = [
            path('accounts/login/', allauth_views.LoginView.as_view(), name='account_login'),
            path('accounts/logout/', allauth_views.LogoutView.as_view(), name='account_logout'),
            path('accounts/signup/', allauth_views.SignupView.as_view(), name='account_signup'),
        ]
        ```
    1. Create templated:
        ```
        mkdir jeonse/templates
        mkdir jeonse/templates/account
        touch jeonse/templates/account/login.html
        touch jeonse/templates/account/logout.html
        touch jeonse/templates/account/signup.html
        ```    
    1. Modify templates:
        ```html
        <!-- jeonse/templates/account/login.html -->
        
        <form method="POST">{% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Login</button>
        </form>
        ```
        ```html
        <!-- jeonse/templates/account/logout.html -->

        <form method="POST">{% csrf_token %}
            <button type="submit">Logout</button>
        </form>
        ```
        ```html
        <!-- jeonse/templates/account/signup.html -->

        <form method="POST">{% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Signup</button>
        </form>
        ```
        
    1. Include `jeonse.urls` in `settings/urls.py`:
        ```python
        # settings/urls.py

        from django.contrib import admin
        from django.urls import path, include # <-- Add this line

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include('jeonse.urls')), # <-- Add this line
        ]
        ```
    1. Run makemigrations: `python manage.py makemigrations`
    1. Run migrate: `python manage.py migrate`
    1. Run server: `python manage.py runserver`
    1. Open browser and go to `http://localhost:8000/accounts/signup/`: `open http://localhost:8000/accounts/signup/`
    1. Create a new user and login
    1. Open browser and go to `http://localhost:8000/accounts/logout/`: `open http://localhost:8000/accounts/logout/`
    1. Logout and login again

5. **Create Listing Model and Views**
    1. Create `Listing model`:
        ```python
        # jeonse/models.py
        from django.db import models

        class Listing(models.Model):
            creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="creator")
            jeonse_deposit_amount = models.BigIntegerField("전세금", default=0)
            wolse_deposit_amount = models.BigIntegerField("월세금", default=0)
            wolse_monthly_amount = models.IntegerField("월세", default=0)
            gwanlibi_monthly_amount = models.IntegerField("월관리비", default=0)

            loan_amount = models.BigIntegerField("대출금", default=0)
            loan_interest_rate = models.FloatField("대출금리", default=0.0)
            
            total_monthly_payment = models.IntegerField("월납부금", default=0)
            
            total_area = models.FloatField("전용면적", default=0.0)
            number_of_rooms = models.IntegerField("방개수", default=0)
            number_of_bathrooms = models.IntegerField("욕실개수", default=0)
            
            comment = models.TextField("코멘트", default="")
        ```
    
    1. Create `ListingForm`:
        ```bash
        mkdir jeonse/forms
        ```
        ```python
        # jeonse/forms.py
        from django import forms
        from jeonse.models import Listing

        class ListingForm(forms.ModelForm):
            class Meta:
                model = Listing
                fields = "__all__"
        ```

    1. Create `ListingListView`, `ListingDetailView`, and `ListingCreateView`:
        ```python
        # jeonse/views.py

        from django.views.generic import ListView, DetailView, CreateView
        from django.urls import reverse_lazy
        from jeonse.forms import ListingForm
        from jeonse.models import Listing


        class ListingListView(ListView):
            model = Listing
            template_name = "listing_list.html"


        class ListingDetailView(DetailView):
            model = Listing
            template_name = "listing_detail.html"

        
        class ListingCreateView(CreateView):
            model = Listing
            form_class = ListingForm
            template_name = "listing_create.html"
            success_url = reverse_lazy("listing_list")
        ```
    
    1. Create `listing_list.html`, `listing_detail.html`, and `listing_create.html`:
        ```bash
        touch jeonse/templates/listing_list.html
        touch jeonse/templates/listing_detail.html
        touch jeonse/templates/listing_create.html
        ```

    1. Modify templates:
        ```html
        <!-- jeonse/templates/listing_list.html -->

        <h1>Listing List</h1>
        <ul>
            {% for listing in object_list %}
                <li><a href="{% url 'listing_detail' listing.pk %}">{{ listing }}</a></li>
            {% endfor %}
        </ul>
        ```
        ```html
        <!-- jeonse/templates/listing_detail.html -->

        <h1>Listing Detail</h1>
        <p>{{ object }}</p>
        ```
        ```html
        <!-- jeonse/templates/listing_create.html -->

        <h1>Listing Create</h1>
        <form method="POST">{% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Create</button>
        </form>
        ```
    
    1. Add urls to `jeonse/urls.py`:
        ```python
        # jeonse/urls.py

        from jeonse.views import ListingListView, ListingDetailView, ListingCreateView

        urlpatterns = [
            ...
            path('', ListingListView.as_view(), name="listing_list"),
            path('<int:pk>/', ListingDetailView.as_view(), name="listing_detail"),
            path('create/', ListingCreateView.as_view(), name="listing_create"),
        ]
        ```
    
    1. Run makemigrations: `python manage.py makemigrations`
    1. Run migrate: `python manage.py migrate`
    1. Run server: `python manage.py runserver`
    1. Open browser and go to `http://localhost:8000/`: `open http://localhost:8000/`
    1. Create a new listing: `open http://localhost:8000/create/`
    1. View the listing: `open http://localhost:8000/1/`
