# Django Jeonse Calculator
Source code for Pycon Korea 2023 Tutorial

## Aim of this project
In this comprehensive tutorial, we will explore how to build a modern, feature-rich rental listing website using Django, a popular Python web framework, and several community packages. By harnessing the power of packages such as django-allauth, django-tables2, django-htmx, and django-filter, we will create a dynamic and efficient website that offers enhanced functionality and user experience.

Throughout the tutorial, we will guide you through the process of setting up the Django project and integrating these community packages seamlessly. We will demonstrate how django-allauth simplifies user authentication, registration, allowing users to easily sign up, log in, and manage their rental listings.

We will leverage the power of django-tables2 to generate interactive and customizable tables for displaying rental listings, complete with sorting, pagination, and filtering capabilities. By integrating django-htmx, we will implement seamless and efficient user interactions, such as updating listing details, filtering results, and dynamically loading content without full page refreshes, resulting in a smooth and responsive user interface.

To enhance the search functionality, we will utilize django-filter to create advanced filtering options, enabling users to refine their search results based on criteria such as location, price range, amenities, and more.

Throughout the tutorial, we will provide clear and concise instructions, accompanied by code examples and demonstrations of each package's usage. By the end of the tutorial, you will have a fully functional rental listing website that showcases the power of Django and its community packages in creating modern, fast, and feature-rich web applications.


## Tutorial outline:
1. [Introduction](#1-introduction)
    * Overview of the tutorial
    * Explanation of the application's purpose and functionality
1. [Prerequisites](#2-prerequisites)
    * Django installation
    * Basic understanding of Django and Python
1. [Setting up the Project](#3-setting-up-the-project)
    * Creating a new Django project
    * Creating a new Django app for rental listings
    * Install Python 3.8+ and Django 4.2
    * Create Django project
    * Custom user model
    * Create User Signup and Signin Views
    * Create Listing Model and Views
    * Configuring URL patterns for different views
1. [User Authentication and Permissions](#4-user-authentication-and-permissions)
    * Restricting views and actions to authenticated users
    * Restricting views and actions to listing owners
1. [Styling and Appearance](#5-styling-and-appearance)
    * Adding CSS stylesheets to enhance the application's appearance
    * Adding django-tables2 to display rental listings in a table
1. [Search and Filtering](#6-search-and-filtering)
    * Adding django-filter to enable advanced search and filtering
1. [Request optimization](#7-request-optimization)
    * Adding django-htmx to optimize user interactions
1. [Testing the Application](#8-testing-the-application)
    * Writing unit tests for models, views, and forms
    * Running tests to ensure the application functions correctly
1. Deployment
    * Preparing the application for deployment
    * Deploying the Django application to a web server or hosting platform (optional)
1. Conclusion
    * Recap of what was covered in the tutorial
    * Encouraging further exploration and enhancements to the application


## Tutorial Presentation:
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
    1. Install pipenv (we will use it for virtual environment): `pip3 install pipenv`
    1. Install Django: `pipenv install django==4.2.3`
    1. Create virtual environment: `pipenv shell`
    1. Open this project in VS Code: `code .`

1. **Create Django project**

    1. Create Django project: `django-admin startproject settings .`
    1. Create Django app: `python3 manage.py startapp jeonse`
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

1. **Custom user model**
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

1. **Create User Signup and Signin Views**
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

1. **Create Listing Model and Views**
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

### 4. User Authentication and Permissions

1. **Restricting views and actions to creators**

    1. Create `mixins.py`:
        ```bash
        touch jeonse/mixins.py
        ```
    1. Add `CreatorRequiredMixin` to `jeonse/mixins.py`:
        ```python
        # jeonse/mixins.py

        from django.contrib.auth.mixins import UserPassesTestMixin

        class UserIsCreatorMixin(UserPassesTestMixin):
            def test_func(self):
                return self.request.user == self.get_object().creator
        ```
    1. Modify `jeonse/views.py`:
        ```python
        # jeonse/views.py

        from django.views.generic import ListView, DetailView, CreateView
        from django.urls import reverse_lazy
        from jeonse.forms import ListingForm
        from jeonse.models import Listing
        from django.contrib.auth.mixins import LoginRequiredMixin
        from jeonse.mixins import UserIsCreatorMixin


        class ListingListView(LoginRequiredMixin, ListView):
            model = Listing
            template_name = "listing_list.html"

            def get_queryset(self):
                return Listing.objects.filter(creator=self.request.user)


        class ListingDetailView(LoginRequiredMixin, UserIsCreatorMixin, DetailView):
            model = Listing
            template_name = "listing_detail.html"


        class ListingCreateView(LoginRequiredMixin, CreateView):
            model = Listing
            form_class = ListingForm
            template_name = "listing_create.html"
            success_url = reverse_lazy("listing_list")

            def form_valid(self, form):
                form.instance.creator = self.request.user
                return super().form_valid(form)
        ``` 
    1. Modify `jeonse/forms.py`:
        ```python
        from django import forms
        from jeonse.models import Listing

        class ListingForm(forms.ModelForm):
            class Meta:
                model = Listing
                fields = "__all__"
                exclude = ["creator"]  # <-- Add this line
        ```
    1. Run server: `python manage.py runserver`
    1. Open browser and go to `http://localhost:8000/signin/`: `open http://localhost:8000/signin/`
    1. Create a new user and create a new listing: `open http://localhost:8000/create/`

### 5. Styling and Appearance

1. **Adding Bootstrap**

    1. Got to the https://getbootstrap.com/docs/5.3/getting-started/download/ website and copy the CDN links:
        ```html
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>
        ```
    1. Create `base.html`, `navbar.html`, and `footer.html`:
        ```bash
        touch jeonse/templates/base.html jeonse/templates/navbar.html jeonse/templates/footer.html
        ```
        ```
    1. Modify `base.html`:
        ```html
        <!-- jeonse/templates/base.html -->

        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{% block title %}Jeonse{% endblock %}</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
        </head>

        <body>
            {% block navbar %}
                {% include "navbar.html" %}
            {% endblock %}
            
            {% block content %}
            {% endblock %}

            {% block footer %}
                {% include "footer.html" %}
            {% endblock %}
        </body>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>
        </html>
        ```
    1. Modify `navbar.html`:
        ```html
        <!-- jeonse/templates/navbar.html -->

        <nav class="navbar bg-light">
            <div class="container">
                <a class="navbar-brand" href="{% url 'listing_list' %}">Jeonse</a>
                <a class="nav-item" href="{% url 'listing_create' %}">Create Listing</a>
                {% if user.is_authenticated %}
                    <a class="nav-item" href="{% url 'account_logout' %}">Logout</a>
                {% else %}
                    <a class="nav-item" href="{% url 'account_login' %}">Login</a>
                    <a class="nav-item" href="{% url 'account_signup' %}">Signup</a>
                {% endif %}
            </div>
        </nav>
        ```
    1. Modify `footer.html`:
        ```html
        <!-- jeonse/templates/footer.html -->

        <footer class="navbar bg-dark fixed-bottom">
            <div class="container">
                <a class="navbar-brand text-white" href="{% url 'listing_list' %}">Jeonse</a>
            </div>
        </footer>
        ```
    1. Modify `account\login.html`:
        ```html
        <!-- jeonse/templates/account/login.html -->

        {% extends "base.html" %}

        {% block title %}Login{% endblock %}

        {% block content %}
        <form method="POST">{% csrf_token %}
            {{ form.as_p }}
            <button class="btn btn-primary" type="submit">Login</button>
        </form>
        {% endblock %}
        ```
    1. Modify `account\logout.html`:
        ```html
        <!-- jeonse/templates/account/logout.html -->

        {% extends "base.html" %}

        {% block title %}Logout{% endblock %}

        {% block content %}
        <form method="POST">{% csrf_token %}
            <button class="btn btn-primary" type="submit">Logout</button>
        </form>
        {% endblock %}
        ```
    1. Modify `account\signup.html`:
        ```html
        <!-- jeonse/templates/account/signup.html -->

        {% extends "base.html" %}

        {% block title %}Signup{% endblock %}

        {% block content %}
        <form method="POST">{% csrf_token %}
            {{ form.as_p }}
            <button class="btn btn-primary" class="btn" type="submit">Signup</button>
        </form>
        {% endblock %}
        ```
    1. Modify `listing_create.html`:
        ```html
        <!-- jeonse/templates/listing_create.html -->

        {% extends "base.html" %}

        {% block title %}Listing Create{% endblock %}

        {% block content %}
        <h1>Listing Create</h1>
        <form method="POST">{% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Create</button>
        </form>
        {% endblock %}
        ```
    1. Modify `listing_detail.html`:
        ```html
        <!-- jeonse/templates/listing_detail.html -->

        {% extends "base.html" %}

        {% block title %}Listing Detail{% endblock %}

        {% block content %}
        <h1>Listing Detail</h1>
        <p>{{ object.creator }}</p>
        <p>{{ object.jeonse_deposit_amount }}</p>
        {% endblock %}
        ```
    1. Modify `listing_list.html`:
        ```html
        <!-- jeonse/templates/listing_list.html -->

        {% extends "base.html" %}

        {% block title %}Listing List{% endblock %}

        {% block content %}
            <h1>Listing List</h1>
            <ul>
                {% for listing in object_list %}
                    <li><a href="{% url 'listing_detail' listing.pk %}">{{ listing }}</a></li>
                {% endfor %}
            </ul>
        {% endblock %}
        ```
    1. Run server: `python manage.py runserver`
    1. Open browser and go to `http://localhost:8000/`: `open http://localhost:8000/`

1. **Adding django-tables2**

    1. Install django-tables2: `pipenv install django-tables2==2.6.0`
    1. Add `django_tables2` to `INSTALLED_APPS` in `settings.py`:
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
            "allauth",
            "allauth.account",
            "django_tables2",                   # <-- Add this line
        ]
        ```
    1. Create `tables.py`:
        ```bash
        touch jeonse/tables.py
        ```
    1. Add `ListingTable` to `jeonse/tables.py`:
        ```python
        # jeonse/tables.py

        import django_tables2 as tables

        from jeonse.models import Listing

        class ListingTable(tables.Table):
            class Meta:
                model = Listing
                template_name = "django_tables2/bootstrap5.html"
                attrs = {"class": "table table-striped table-bordered table-hover"}
        ```
    1. Modify `jeonse/views.py`:
        ```python
        # jeonse/views.py

        from django_tables2 import SingleTableView

        from django.contrib.auth.mixins import LoginRequiredMixin
        from django.urls import reverse_lazy
        from django.views.generic import DetailView, CreateView

        from jeonse.forms import ListingForm
        from jeonse.mixins import UserIsCreatorMixin
        from jeonse.models import Listing
        from jeonse.tables import ListingTable


        class ListingListView(LoginRequiredMixin, SingleTableView):
            model = Listing
            template_name = "listing_list.html"
            table_class = ListingTable

            def get_queryset(self):
                return Listing.objects.filter(creator=self.request.user)
        ...
        ```
    1. Modify `listing_list.html`:
        ```html
        <!-- jeonse/templates/listing_list.html -->

        {% extends "base.html" %}
        {% load render_table from django_tables2 %}

        {% block title %}Listing List{% endblock %}

        {% block content %}
            <h1>Listing List</h1>
            <div class="overflow-auto">
                {% render_table table %}
            </div>
        {% endblock %}
        ```
    1. Run server: `python manage.py runserver`
    1. Open browser and go to `http://localhost:8000/`: `open http://localhost:8000/`

### 6. Search and Filtering

1. **Adding django-filter to enable advanced search and filtering**

    1. Install django-filter: `pipenv install django-filter==23.2`
    1. Add `django_filters` to `INSTALLED_APPS` in `settings.py`:
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
            "allauth",
            "allauth.account",
            "django_tables2",
            "django_filters",                   # <-- Add this line
        ]
        ```
    1. Create `jeonse/filters.py`:
        ```bash
        touch jeonse/filters.py
        ```
    1. Add `ListingFilter` to `jeonse/filters.py`:
        ```python
        # jeonse/filters.py

        import django_filters

        from jeonse.models import Listing


        class ListingFilter(django_filters.FilterSet):
            
            class Meta:
                model = Listing
                fields = {
                    "jeonse_deposit_amount": ["lte",],
                    "wolse_deposit_amount": ["lte",],
                    "total_monthly_payment": ["lte",],
                }
        ```
    1. Modify `jeonse/views.py`:
        ```python
        # jeonse/views.py

        ...
        from django_filters.views import FilterView
        from jeonse.filters import ListingFilter
        ...
        
        class ListingListView(LoginRequiredMixin, FilterView, SingleTableView):
            model = Listing
            template_name = "listing_list.html"
            table_class = ListingTable
            filterset_class = ListingFilter

            def get_queryset(self):
                return Listing.objects.filter(creator=self.request.user)
        ...
        ```
    1. Modify `listing_list.html`:
        ```html
        <!-- jeonse/templates/listing_list.html -->

        {% extends "base.html" %}
        {% load render_table from django_tables2 %}

        {% block title %}Listing List{% endblock %}

        {% block content %}
            <h1>Listing List</h1>
            <form method="GET">
                {{ filter.form.as_p }}
                <button type="submit">Search</button>
            </form>
            {% render_table table %}
        {% endblock %}
        ```
    1. Run server: `python manage.py runserver`
    1. Open browser and go to `http://localhost:8000/`: `open http://localhost:8000/`

### 7. Request optimization

1. **Adding django-htmx to optimize user interactions**

    1. Install `django-htmx`: `pipenv install django-htmx==1.16.0`
    1. Add `django_htmx` to `INSTALLED_APPS` in `settings.py`:
        ```python
        # settings.py

        INSTALLED_APPS = [
            ...
            "django_htmx",                         # <-- Add this line
        ]
        ```
    1. Add `django_htmx.middleware.HtmxMiddleware` middleware:
        ```python
        # settings.py
        
        MIDDLEWARE = [
            ...
            "django_htmx.middleware.HtmxMiddleware", # <-- Add this line
        ]
        ```
    1. Add `id="content"` to `base.html`:
        ```html
        <!-- jeonse/templates/base.html -->

        <div id="content" class="container">
            {% block content %}
            {% endblock %}
        </div>
        ```
    1. Add `<script src="https://unpkg.com/htmx.org@1.9.3" integrity="sha384-lVb3Rd/Ca0AxaoZg5sACe8FJKF0tnUgR2Kd7ehUOG5GCcROv5uBIZsOqovBAcWua" crossorigin="anonymous"></script>` to `base.html` as the last line:
        ```html
        <!-- jeonse/templates/base.html -->
        <div id="content" class="container">
            {% block content %}
            {% endblock %}
        </div>
        ...
        <script src="https://unpkg.com/htmx.org@1.9.3" integrity="sha384-lVb3Rd/Ca0AxaoZg5sACe8FJKF0tnUgR2Kd7ehUOG5GCcROv5uBIZsOqovBAcWua" crossorigin="anonymous"></script>
        </html>
        ```
    1. Create directory for `htmx` templates:
        ```bash
        mkdir jeonse/templates/htmx
        ```
    1. Create `htmx/listing_list.html`:
        ```bash
        touch jeonse/templates/htmx/listing_list.html
        ```
    1. Modify `htmx/listing_list.html`:
        ```html
        <!-- jeonse/templates/htmx/listing_list.html -->

        {% load render_table from django_tables2 %}

        <h1>Listing List</h1>
        <form hx-get="" hx-target="#content">
            {{ filter.form.as_p }}
            <button type="submit">Search</button>
        </form>
        {% render_table table %}
        ```
    1. Modify `templates/listing_list.html`:
        ```html
        <!-- jeonse/templates/listing_list.html -->

        {% extends "base.html" %}

        {% block title %}Listing List{% endblock %}

        {% block content %}
            {% include "htmx/listing_list.html" %}
        {% endblock %}
        ```
    1. Modify `ListingListView` in `jeonse/views.py`:
        ```python
        # jeonse/views.py

        ...
        class ListingListView(LoginRequiredMixin, FilterView, SingleTableView):
            ...

            def get_template_names(self) -> List[str]:
                if self.request.htmx:
                    return ["htmx/listing_list.html"]
                return super().get_template_names()
        ...
        ```
    1. Run server: `python manage.py runserver`
    1. Open browser and go to `http://localhost:8000/`: `open http://localhost:8000/`

### 8. Testing the Application

1. Add `django.test.TestCase` to `jeonse/tests.py`:
    ```python
    # jeonse/tests.py

    from django.test import TestCase

    class TestViews(TestCase):
        def setUp(self):
            pass

        def test_account_login(self):
            pass

        def test_account_logout(self):
            pass
        
        def test_account_signup(self):
            pass

        def test_listing_list(self):
            pass

        def test_listing_detail(self):
            pass

        def test_listing_create(self):
            pass
    ```
1. Add `test_account_login` to `jeonse/tests.py`:
    ```python
    # jeonse/tests.py

    def setUp(self):    
        self.user_kwargs = {
            'username': 'testuser',
            'email': 'testuser@gmail.com',
            'password': 'testpassword',
        }

    def test_account_login(self):
        post_data = {
            'login': self.user_kwargs['email'],
            'password': self.user_kwargs['password'],
        }
        endpoint = reverse('account_login')
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

        response = self.client.post(endpoint, post_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')
        self.assertTrue(response.context['form'].errors)

        get_user_model().objects.create_user(**self.user_kwargs)
        response = self.client.post(endpoint, post_data)
        self.assertRedirects(response, reverse('listing_list'))
    ```
1. Add `test_account_logout` to `jeonse/tests.py`:
    ```python
    # jeonse/tests.py

    def test_account_logout(self):
        user = get_user_model().objects.create_user(**self.user_kwargs)

        endpoint = reverse('account_logout')
        response = self.client.post(endpoint)
        self.assertFalse(response.context)

        self.client.force_login(user)
        response = self.client.post(endpoint)
        self.assertTrue(response.context['user'].is_authenticated)
    ```

1. Add `test_account_signup` to `jeonse/tests.py`:
    ```python
    # jeonse/tests.py

    def test_account_signup(self):
        post_data = {
            'email': self.user_kwargs['email'],
            'password1': self.user_kwargs['password'],
            'password2': self.user_kwargs['password'],
        }
        endpoint = reverse('account_signup')
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/signup.html')

        endpoint = reverse('account_signup')
        response = self.client.post(endpoint, post_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.context['user'].is_authenticated)

        user = get_user_model().objects.get(email=self.user_kwargs['email'])
        self.assertTrue(user.is_active)
        self.assertEqual(user.email, self.user_kwargs['email'])
    ```

1. Add `test_listing_list` to `jeonse/tests.py`:
    ```python
    # jeonse/tests.py

    def test_listing_list(self):
        user = get_user_model().objects.create_user(**self.user_kwargs)
        for i in range(10):
            Listing.objects.create(
                creator=user,
                jeonse_deposit_amount=i,
                wolse_deposit_amount=i,
                wolse_monthly_amount=i,
                gwanlibi_monthly_amount=i,
                loan_amount=i,
                loan_interest_rate=i,
                total_monthly_payment=i,
                total_area=i,
                number_of_rooms=i,
                number_of_bathrooms=i,
                comment=f"comment{i}",
            )
        endpoint = reverse('listing_list')
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('account_login') + f'?next={endpoint}')

        self.client.force_login(user)
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listing_list.html')
        self.assertEqual(len(response.context['object_list']), 10)
    ```

1. Add `test_listing_detail` to `jeonse/tests.py`:
    ```python
    # jeonse/tests.py

    def test_listing_detail(self):
        user = get_user_model().objects.create_user(**self.user_kwargs)
        listing = Listing.objects.create(
            creator=user,
            jeonse_deposit_amount=1,
            wolse_deposit_amount=1,
            wolse_monthly_amount=1,
            gwanlibi_monthly_amount=1,
            loan_amount=1,
            loan_interest_rate=1,
            total_monthly_payment=1,
            total_area=1,
            number_of_rooms=1,
            number_of_bathrooms=1,
            comment="comment",
        )
        endpoint = reverse('listing_detail', kwargs={'pk': listing.pk})
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('account_login') + f'?next={endpoint}')

        self.client.force_login(user)
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listing_detail.html')
        self.assertEqual(response.context['object'], listing)
    ```

1. Add `test_listing_create` to `jeonse/tests.py`:
    ```python
    # jeonse/tests.py

    def test_listing_create(self):
        user = get_user_model().objects.create_user(**self.user_kwargs)
        endpoint = reverse('listing_create')
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('account_login') + f'?next={endpoint}')

        self.client.force_login(user)
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listing_create.html')

        post_data = {
            'jeonse_deposit_amount': 1,
            'wolse_deposit_amount': 1,
            'wolse_monthly_amount': 1,
            'gwanlibi_monthly_amount': 1,
            'loan_amount': 1,
            'loan_interest_rate': 1,
            'total_monthly_payment': 1,
            'total_area': 1,
            'number_of_rooms': 1,
            'number_of_bathrooms': 1,
            'comment': "comment",
        }
        response = self.client.post(endpoint, post_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listing_list'))
        self.assertEqual(Listing.objects.count(), 1)
    ```

1. Run tests: `python manage.py test`
    