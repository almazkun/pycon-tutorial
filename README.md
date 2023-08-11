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
    * Restricting views and actions to authenticated users and listing creator's objects
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
1. [Deployment](#9-deployment)
    * Create ngrok account and download ngrok.
    * Run ngrok to expose local server to the internet
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
    1. Make a directory for the project: 
        ```bash
        mkdir django-jeonse
        ```
    1. Change directory to the project: 
        ```bash
        cd django-jeonse
        ```
    1. Install pipenv (we will use it for virtual environment): 
        ```bash
        pip3 install pipenv
        ```
    1. Install Django: 
        ```bash
        pipenv install django==4.2.4
        ```
    1. Activate virtual environment: 
        ```bash
        pipenv shell
        ```
    1. Open this project in VS Code: 
        ```bash 
        code .
        ```

1. **Create Django project**

    1. Create Django project: 
        ```bash
        django-admin startproject settings .
        ```
    1. Create Django app: 
        ```bash
        python3 manage.py startapp jeonse
        ```
    1. Add `jeonse` to `INSTALLED_APPS` in `settings/settings.py`:
        ```python
        # settings/settings.py

        INSTALLED_APPS = [
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.messages",
            "django.contrib.staticfiles",
            "jeonse",                                       # <-- Add this line
        ]
        ```
    1. Run server:  
        ```bash
        python3 manage.py runserver
        ```
    1. Open browser and go to http://localhost:8000.

1. **Custom user model**
    1. Open `jeonse/models.py` and add `CustomUser` model:
        ```python
        from django.contrib.auth.models import AbstractUser
        from django.db import models

        class CustomUser(AbstractUser):
            pass
        ```
    1. Add `AUTH_USER_MODEL = 'jeonse.CustomUser'` to `settings/settings.py`
        ```python
        # settings/settings.py

        AUTH_USER_MODEL = 'jeonse.CustomUser'
        ```
    1. Run makemigrations: 
        ```bash
        python3 manage.py makemigrations
        ```
    1. Run migrate: 
        ```bash
        python3 manage.py migrate
        ```
    1. Run server: 
        ```bash
        python3 manage.py runserver
        ```

1. **Create User Signup and Signin Views**
    1. Install django-allauth:  
        ```bash
        pipenv install django-allauth==0.54.0
        ```
    1. Add `allauth` and `allauth.account` to `INSTALLED_APPS` in `settings/settings.py`:
        ```python
        # settings/settings.py

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
    1. Add `AUTHENTICATION_BACKENDS` in `settings/settings.py`:
        ```python
        # settings/settings.py

        # django-allauth settings
        # https://django-allauth.readthedocs.io/en/latest/installation.html
        AUTHENTICATION_BACKENDS = [
            "django.contrib.auth.backends.ModelBackend",
            "allauth.account.auth_backends.AuthenticationBackend",
        ]
        ```
    1. Configure `Allauth` settings in `settings/settings.py`:
        ```python
        # settings/settings.py

        # https://django-allauth.readthedocs.io/en/latest/configuration.html
        ACCOUNT_USERNAME_REQUIRED = False
        ACCOUNT_AUTHENTICATION_METHOD = "email"
        ACCOUNT_EMAIL_REQUIRED = True
        ACCOUNT_UNIQUE_EMAIL = True
        ACCOUNT_EMAIL_VERIFICATION = "none"
        LOGIN_REDIRECT_URL = "/"
        ```
    1. Create `jeonse/urls.py`:
        ```bash
        touch jeonse/urls.py
        ```
    1. Create `account_login`, `account_logout`, and `account_signup` URLs in `jeonse/urls.py`:
        ```python
        # jeonse/urls.py

        from allauth.account import views as allauth_views
        from django.urls import path

        urlpatterns = [
            path("accounts/login/", allauth_views.LoginView.as_view(), name="account_login"),
            path("accounts/logout/", allauth_views.LogoutView.as_view(), name="account_logout"),
            path("accounts/signup/", allauth_views.SignupView.as_view(), name="account_signup"),
        ]

        ```
    1. Create templates directory and login, logout, and signup templates in `jeonse/templates/account`:
        ```
        mkdir jeonse/templates
        mkdir jeonse/templates/account
        touch jeonse/templates/account/login.html
        touch jeonse/templates/account/logout.html
        touch jeonse/templates/account/signup.html
        ```    
    1. Modify `jeonse/templates/account/login.html` template:
        ```html
        <!-- jeonse/templates/account/login.html -->
                
        <form method="POST">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Login</button>
        </form>
        ```
    1. Modify `jeonse/templates/account/logout.html` template:
        ```html
        <!-- jeonse/templates/account/logout.html -->

        <form method="POST">
            {% csrf_token %}
            <button type="submit">Logout</button>
        </form>
        ```
    1. Modify `jeonse/templates/account/signup.html` template:
        ```html
        <!-- jeonse/templates/account/signup.html -->

        <form method="POST">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Signup</button>
        </form>
        ```
    1. Include `jeonse.urls` in `settings/urls.py`:
        ```python
        # settings/urls.py

        from django.contrib import admin
        from django.urls import path, include  # <-- Add this line  

        urlpatterns = [
            path("admin/", admin.site.urls),
            path("", include("jeonse.urls")),  # <-- Add this line
        ]
        ```
    1. Run makemigrations: 
        ```bash
        python3 manage.py makemigrations
        ```
    1. Run migrate:
        ```bash
        python3 manage.py migrate
        ```
    1. Run server: 
        ```bash
        python3 manage.py runserver
        ```
    1. Create a new user and login: http://localhost:8000/accounts/signup/
    1. Logout: http://localhost:8000/accounts/logout/
    1. Login again: http://localhost:8000/accounts/login/

1. **Create Listing Model and Views**
    1. Create `Listing model` in `jeonse/models.py`:
        ```python
        # jeonse/models.py

        from django.contrib.auth.models import AbstractUser
        from django.db import models


        def monthly_interest_payment(loan_amount: int, annual_interest_rate: float):
            return round(loan_amount * (annual_interest_rate / 12 / 100))


        class CustomUser(AbstractUser):
            pass


        class Listing(models.Model):
            creator = models.ForeignKey(
                CustomUser, on_delete=models.CASCADE, related_name="listings"
            )

            jeonse_deposit_amount = models.BigIntegerField("전세금", default=0)
            wolse_deposit_amount = models.BigIntegerField("월세금", default=0)
            wolse_monthly_payment = models.IntegerField("월세", default=0)
            gwanlibi_monthly_payment = models.IntegerField("월관리비", default=0)

            total_monthly_payment = models.IntegerField("총 월세", default=0)

            annual_interest_rate = models.FloatField("대출 이자율", default=0.0)

            total_area = models.FloatField("전용면적", default=0.0)
            number_of_rooms = models.IntegerField("방개수", default=0)
            number_of_bathrooms = models.IntegerField("욕실개수", default=0)

            comment = models.TextField("코멘트", blank=True, null=True)

            def _total_monthly_payment(self):
                interest_payment = monthly_interest_payment(
                    self.jeonse_deposit_amount + self.wolse_deposit_amount,
                    self.annual_interest_rate,
                )

                return sum(
                    [
                        interest_payment,
                        self.wolse_monthly_payment,
                        self.gwanlibi_monthly_payment,
                    ]
                )

            def save(self, *args, **kwargs):
                self.total_monthly_payment = self._total_monthly_payment()
                super().save(*args, **kwargs)
        ```
    1. Create `jeonse/forms.py`:
        ```bash
        touch jeonse/forms.py
        ```
    1. Create `ListingForm` in `jeonse/forms.py`:
        ```python
        # jeonse/forms.py

        from django import forms

        from jeonse.models import Listing


        class ListingForm(forms.ModelForm):
            class Meta:
                model = Listing
                fields = [
                    "creator",
                    "jeonse_deposit_amount",
                    "wolse_deposit_amount",
                    "wolse_monthly_payment",
                    "gwanlibi_monthly_payment",
                    "annual_interest_rate",
                    "total_area",
                    "number_of_rooms",
                    "number_of_bathrooms",
                    "comment",
                ]
        ```
    1. Create `ListingListView`, `ListingDetailView`, and `ListingCreateView` in `jeonse/views.py`:
        ```python
        # jeonse/views.py

        from django.urls import reverse_lazy
        from django.views.generic import CreateView, DetailView, ListView

        from jeonse.forms import ListingForm
        from jeonse.models import Listing


        class ListingListView(ListView):
            model = Listing
            template_name = "jeonse/listing_list.html"


        class ListingDetailView(DetailView):
            model = Listing
            template_name = "jeonse/listing_detail.html"


        class ListingCreateView(CreateView):
            model = Listing
            form_class = ListingForm
            template_name = "jeonse/listing_create.html"
            success_url = reverse_lazy("listing_list")

        ```
    
    1. Create `listing_list.html`, `listing_detail.html`, and `listing_create.html` in `jeonse/templates/jeonse/`:
        ```bash
        mkdir jeonse/templates/jeonse
        touch jeonse/templates/jeonse/listing_create.html
        touch jeonse/templates/jeonse/listing_detail.html
        touch jeonse/templates/jeonse/listing_list.html
        ```

    1. Modify `jeonse/templates/jeonse/listing_create.html`:
        ```html
        <!-- jeonse/templates/listing_create.html -->

        <h1>Listing Create</h1>
        <form method="POST">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Create</button>
        </form>
        ```
    1. Modify `jeonse/templates/jeonse/listing_detail.html`:
        ```html
        <!-- jeonse/templates/listing_detail.html -->

        <h1>Listing Detail</h1>
        <p>전세금: {{ object.jeonse_deposit_amount }}</p>
        <p>월세금: {{ object.wolse_deposit_amount }}</p>
        <p>월세: {{ object.wolse_monthly_payment }}</p>
        <p>월관리비: {{ object.gwanlibi_monthly_payment }}</p>
        <p>총 월세: {{ object.total_monthly_payment }}</p>
        <p>대출 이자율: {{ object.annual_interest_rate }}</p>
        <p>전용면적: {{ object.total_area }}</p>
        <p>방개수: {{ object.number_of_rooms }}</p>
        <p>욕실개수: {{ object.number_of_bathrooms }}</p>
        <p>코멘트: {{ object.comment }}</p>
        ```
    1. Modify `jeonse/templates/jeonse/listing_list.html`:
        ```html
        <!-- jeonse/templates/listing_list.html -->

        <h1>Listing List</h1>
        <ul>
            {% for listing in object_list %}
                <li>
                    <a href="{% url 'listing_detail' listing.pk %}">{{ listing }}</a>
                </li>
            {% endfor %}
        </ul>
        ```
    1. Modify `jeonse/urls.py`:
        ```python
        # jeonse/urls.py

        from allauth.account import views as allauth_views
        from django.urls import path

        from jeonse.views import ListingCreateView, ListingDetailView, ListingListView

        urlpatterns = [
            path("accounts/login/", allauth_views.LoginView.as_view(), name="account_login"),
            path("accounts/logout/", allauth_views.LogoutView.as_view(), name="account_logout"),
            path("accounts/signup/", allauth_views.SignupView.as_view(), name="account_signup"),
            path("", ListingListView.as_view(), name="listing_list"),
            path("<int:pk>/", ListingDetailView.as_view(), name="listing_detail"),
            path("create/", ListingCreateView.as_view(), name="listing_create"),
        ]
        ```
    1. Run makemigrations:
        ```bash
        python3 manage.py makemigrations
        ```
    1. Run migrate:
        ```bash
        python3 manage.py migrate
        ```
    1. Run server:
        ```bash
        python3 manage.py runserver
        ```
    1. Create a new listing: http://localhost:8000/create/
    1. Create a second listing: http://localhost:8000/create/
    1. View the listing list: http://localhost:8000/
    1. View the first listing: http://localhost:8000/1/

### 4. User Authentication and Permissions

1. **Restricting views and actions to authenticated users and listing creator's objects**

    1. Create `mixins.py`:
        ```bash
        touch jeonse/mixins.py
        ```
    1. Add `CreatorRequiredMixin` to `jeonse/mixins.py`:
        ```python
        # jeonse/mixins.py

        from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


        class UserIsAuthenticatedMixin(LoginRequiredMixin):
            pass


        class UserIsCreatorMixin(UserPassesTestMixin):
            def test_func(self):
                return self.request.user == self.get_object().creator
        ```
    1. Modify `jeonse/views.py`:
        ```python
        # jeonse/views.py

        from django.urls import reverse_lazy
        from django.views.generic import CreateView, DetailView, ListView

        from jeonse.forms import ListingForm
        from jeonse.mixins import UserIsAuthenticatedMixin, UserIsCreatorMixin
        from jeonse.models import Listing


        class ListingListView(UserIsAuthenticatedMixin, ListView):
            model = Listing
            template_name = "jeonse/listing_list.html"

            def get_queryset(self):
                return self.request.user.listings.all()


        class ListingDetailView(UserIsAuthenticatedMixin, UserIsCreatorMixin, DetailView):
            model = Listing
            template_name = "jeonse/listing_detail.html"


        class ListingCreateView(UserIsAuthenticatedMixin, CreateView):
            model = Listing
            form_class = ListingForm
            template_name = "jeonse/listing_create.html"
            success_url = reverse_lazy("listing_list")

            def form_valid(self, form):
                form.instance.creator = self.request.user
                return super().form_valid(form)

        ``` 
    1. Remove `creator` from fields in `jeonse/forms.py`:
        ```python
        # jeonse/forms.py

        from django import forms

        from jeonse.models import Listing


        class ListingForm(forms.ModelForm):
            class Meta:
                model = Listing
                fields = [
                    "jeonse_deposit_amount",
                    "wolse_deposit_amount",
                    "wolse_monthly_payment",
                    "gwanlibi_monthly_payment",
                    "annual_interest_rate",
                    "total_area",
                    "number_of_rooms",
                    "number_of_bathrooms",
                    "comment",
                ]
        ```
    1. Run server: 
        ```bash
        python3 manage.py runserver
        ```
    1. Logout: http://localhost:8000/accounts/logout/
    1. Create a new user: http://localhost:8000/accounts/signup/
    1. Create a new listing: http://localhost:8000/create/
    1. View the listing list: http://localhost:8000/
    1. View the listing: http://localhost:8000/3/
    1. Try to view the listing of other user: http://localhost:8000/1/

### 5. Styling and Appearance

1. **Adding Bootstrap**

    1. Create `_base.html` in `jeonse/templates/`:
        ```bash
        touch jeonse/templates/_base.html
        ```
    1. Create `includes` directory in `jeonse/templates/`:
        ```bash
        mkdir jeonse/templates/includes
        ```
    1. Create `head.html`, `navbar.html`, `footer.html`, and `scripts.html` in `jeonse/templates/includes/`:
        ```bash
        touch jeonse/templates/includes/head.html
        touch jeonse/templates/includes/navbar.html
        touch jeonse/templates/includes/footer.html
        touch jeonse/templates/includes/scripts.html
        ```
    1. Modify `jeonse/templates/_base.html`:
        ```html
        <!-- jeonse/templates/_base.html -->

        <!DOCTYPE html>
        <html lang="en" class="h-100">
            <head>
                {% block head %}
                    {% include "includes/head.html" %}
                {% endblock %}
            </head>
            <body class="d-flex flex-column h-100">
                {% block navbar %}
                    {% include "includes/navbar.html" %}
                {% endblock %}
                <main class="container flex-shrink-0 py-3">
                    {% block content %}{% endblock %}
                </main>
                {% block footer %}
                    {% include "includes/footer.html" %}
                {% endblock %}
            </body>
            {% block scripts %}
                {% include "includes/scripts.html" %}
            {% endblock %}
        </html>
        ```
    1. Got to the https://getbootstrap.com/docs/5.3/getting-started/download/#cdn-via-jsdelivr website and copy the CDN links:
        ```html
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
        ```
        ```html
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
        ```
    1. Modify `jeonse/templates/includes/head.html`:
        ```html
        <!-- jeonse/templates/includes/head.html -->

        <meta charset="UTF-8"/>
        <meta name="viewport"
            content="width=device-width,minimum-scale=1,initial-scale=1"/>
        <title>Jeonse</title>
        <meta name="author" content="Your name"/>
        <meta name="description" content="Compare rental listings"/>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css"
            rel="stylesheet"
            integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9"
            crossorigin="anonymous">
        ```
    1. Modify `jeonse/templates/includes/navbar.html`:
        ```html
        <!-- jeonse/templates/includes/navbar.html -->

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
    1. Modify `jeonse/templates/includes/footer.html`:
        ```html
        <!-- jeonse/templates/includes/footer.html -->

        <nav class="navbar navbar-dark bg-dark text-light small mt-auto">
            <div class="container">
                <div>{% now 'Y' %} © Your Name. All rights reserved.</div>
            </div>
        </nav>
        ```
    1. Modify `jeonse/templates/includes/scripts.html`:
        ```html
        <!-- jeonse/templates/scripts.html -->

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js"
                integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm"
                crossorigin="anonymous"></script>
        ```
    1. Modify `jeonse/templates/account/login.html`:
        ```html
        <!-- jeonse/templates/account/login.html -->

        {% extends "_base.html" %}
        {% block content %}
            <form method="POST">
                {% csrf_token %}
                {{ form.as_p }}
                <button class="btn btn-warning" type="submit">Login</button>
            </form>
        {% endblock %}
        ```
    1. Modify `jeonse/templates/account/logout.html`:
        ```html
        <!-- jeonse/templates/account/logout.html -->

        {% extends "_base.html" %}
        {% block content %}
            <form method="POST">
                {% csrf_token %}
                <button class="btn btn-danger" type="submit">Logout</button>
            </form>
        {% endblock %}
        ```
    1. Modify `jeonse/templates/account/signup.html`:
        ```html
        <!-- jeonse/templates/account/signup.html -->

        {% extends "_base.html" %}
        {% block content %}
            <form method="POST">
                {% csrf_token %}
                {{ form.as_p }}
                <button class="btn btn-warning" type="submit">Signup</button>
            </form>
        {% endblock %}
        ```
    1. Modify `jeonse/templates/jeonse/listing_create.html`:
        ```html
        <!-- jeonse/templates/jeonse/listing_create.html -->

        {% extends "_base.html" %}
        {% block content %}
            <h1>Listing Create</h1>
            <form method="POST">
                {% csrf_token %}
                {{ form.as_p }}
                <button type="submit" class="btn btn-warning">Create</button>
            </form>
        {% endblock %}
        ```
    1. Modify `jeonse/templates/jeonse/listing_detail.html`:
        ```html
        <!-- jeonse/templates/jeonse/listing_detail.html -->

        {% extends "_base.html" %}
        {% block content %}
            <h1>Listing {{ object.pk }}</h1>
            <p>전세금: {{ object.jeonse_deposit_amount }}</p>
            <p>월세금: {{ object.wolse_deposit_amount }}</p>
            <p>월세: {{ object.wolse_monthly_payment }}</p>
            <p>월관리비: {{ object.gwanlibi_monthly_payment }}</p>
            <p>총 월세: {{ object.total_monthly_payment }}</p>
            <p>대출 이자율: {{ object.annual_interest_rate }}</p>
            <p>전용면적: {{ object.total_area }}</p>
            <p>방개수: {{ object.number_of_rooms }}</p>
            <p>욕실개수: {{ object.number_of_bathrooms }}</p>
            <p>코멘트: {{ object.comment }}</p>
        {% endblock %}
        ```
    1. Modify `jeonse/templates/jeonse/listing_list.html`:
        ```html
        <!-- jeonse/templates/jeonse/listing_list.html -->

        {% extends "_base.html" %}
        {% block content %}
            <h1>Listing List</h1>
            <ul>
                {% for listing in object_list %}
                    <li>
                        <a href="{% url 'listing_detail' listing.pk %}">{{ listing }}</a>
                    </li>
                {% endfor %}
            </ul>
        {% endblock %}
        ```
    1. Modify `jeonse/forms.py`:
        ```python
        # jeonse/forms.py

        from django import forms

        from jeonse.models import Listing


        class ListingForm(forms.ModelForm):
            class Meta:
                model = Listing
                fields = [
                    "jeonse_deposit_amount",
                    "wolse_deposit_amount",
                    "wolse_monthly_payment",
                    "gwanlibi_monthly_payment",
                    "annual_interest_rate",
                    "total_area",
                    "number_of_rooms",
                    "number_of_bathrooms",
                    "comment",
                ]
            
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                for _, field in self.fields.items():
                    field.widget.attrs.update({"class": "form-control"})
        ```
    1. Run server: 
        ```bash
        python3 manage.py runserver
        ```
    1. Open browser and go to: http://localhost:8000/

1. **Adding django-tables2**

    1. Install [django-tables2](https://pypi.org/project/django-tables2/): 
        ```bash
        pipenv install django-tables2==2.6.0
        ```
    1. Add `django_tables2` to `INSTALLED_APPS` in `settings/settings.py`:
        ```python
        # settings/settings.py

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
    1. Create `jeonse/tables.py`:
        ```bash
        touch jeonse/tables.py
        ```
    1. Add `ListingTable` to `jeonse/tables.py`:
        ```python
        # jeonse/tables.py

        import django_tables2 as tables

        from jeonse.models import Listing


        class ListingTable(tables.Table):
            get_absolute_url = tables.Column(
                verbose_name="Detail", linkify=True, orderable=False
            )

            class Meta:
                model = Listing
                template_name = "django_tables2/bootstrap5.html"
                attrs = {"class": "table table-striped table-bordered table-hover"}

            def render_get_absolute_url(self, value):
                return "Detail"
        ```
    1. Modify `jeonse/views.py`:
        ```python
        # jeonse/views.py

        from django.urls import reverse_lazy
        from django.views.generic import CreateView, DetailView
        from django_tables2 import SingleTableView                  # <-- Add this line

        from jeonse.forms import ListingForm
        from jeonse.mixins import UserIsAuthenticatedMixin, UserIsCreatorMixin
        from jeonse.models import Listing
        from jeonse.tables import ListingTable                      # <-- Add this line


        class ListingListView(UserIsAuthenticatedMixin, SingleTableView): # <-- Modify this line
            model = Listing
            template_name = "jeonse/listing_list.html"
            table_class = ListingTable                                # <-- Add this line

            def get_queryset(self):
                return self.request.user.listings.all()


        class ListingDetailView(UserIsAuthenticatedMixin, UserIsCreatorMixin, DetailView):
            model = Listing
            template_name = "jeonse/listing_detail.html"


        class ListingCreateView(UserIsAuthenticatedMixin, CreateView):
            model = Listing
            form_class = ListingForm
            template_name = "jeonse/listing_create.html"
            success_url = reverse_lazy("listing_list")

            def form_valid(self, form):
                form.instance.creator = self.request.user
                return super().form_valid(form)
        ```
    1. Modify `jeonse/models.py`:
        ```python
        # jeonse/models.py

        from django.contrib.auth.models import AbstractUser
        from django.db import models
        from django.urls import reverse_lazy                                      # <-- Add this line


        def monthly_interest_payment(loan_amount: int, annual_interest_rate: float):
            return round(loan_amount * (annual_interest_rate / 12 / 100))


        class CustomUser(AbstractUser):
            pass


        class Listing(models.Model):
            creator = models.ForeignKey(
                CustomUser, on_delete=models.CASCADE, related_name="listings"
            )

            jeonse_deposit_amount = models.BigIntegerField("전세금", default=0)
            wolse_deposit_amount = models.BigIntegerField("월세금", default=0)
            wolse_monthly_payment = models.IntegerField("월세", default=0)
            gwanlibi_monthly_payment = models.IntegerField("월관리비", default=0)

            total_monthly_payment = models.IntegerField("총 월세", default=0)

            annual_interest_rate = models.FloatField("대출 이자율", default=0.0)

            total_area = models.FloatField("전용면적", default=0.0)
            number_of_rooms = models.IntegerField("방개수", default=0)
            number_of_bathrooms = models.IntegerField("욕실개수", default=0)

            comment = models.TextField("코멘트", blank=True, null=True)

            def _total_monthly_payment(self):
                interest_payment = monthly_interest_payment(
                    self.jeonse_deposit_amount + self.wolse_deposit_amount,
                    self.annual_interest_rate,
                )

                return sum(
                    [
                        interest_payment,
                        self.wolse_monthly_payment,
                        self.gwanlibi_monthly_payment,
                    ]
                )

            def save(self, *args, **kwargs):
                self.total_monthly_payment = self._total_monthly_payment()
                super().save(*args, **kwargs)

            def get_absolute_url(self):                                         # <-- Add this line
                return reverse_lazy("listing_detail", kwargs={"pk": self.pk})   # <-- Add this line
        ```
    1. Modify `jeonse/templates/jeonse/listing_list.html`:
        ```html
        <!-- jeonse/templates/jeonse/listing_list.html -->

        {% extends "_base.html" %}
        {% load render_table from django_tables2 %}
        {% block content %}
            <h1>Listing List</h1>
            <div class="overflow-auto">{% render_table table %}</div>
        {% endblock %}
        ```
    1. Run server: 
        ```bash
        python3 manage.py runserver
        ```
    1. Open browser and go to http://localhost:8000/

### 6. Search and Filtering

1. **Adding django-filter to enable advanced search and filtering**

    1. Install [django-filter](https://pypi.org/project/django-filter/): 
        ```bash
        pipenv install django-filter==23.2
        ```
    1. Add `django_filters` to `INSTALLED_APPS` in `settings/settings.py`:
        ```python
        # settings/settings.py

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
        from django import forms

        from jeonse.models import Listing


        class ListingFilter(django_filters.FilterSet):
            total_monthly_payment = django_filters.NumberFilter(
                field_name="total_monthly_payment",
                lookup_expr="lte",
                widget=forms.widgets.TextInput(attrs={"class": "form-control form-control-sm"}),
            )

            class Meta:
                model = Listing
                fields = ["total_monthly_payment"]
        ```
    1. Modify `jeonse/views.py`:
        ```python
        # jeonse/views.py

        from django.urls import reverse_lazy
        from django.views.generic import CreateView, DetailView
        from django_filters.views import FilterView                         # <-- Add this line
        from django_tables2 import SingleTableView

        from jeonse.filters import ListingFilter                            # <-- Add this line
        from jeonse.forms import ListingForm
        from jeonse.mixins import UserIsAuthenticatedMixin, UserIsCreatorMixin
        from jeonse.models import Listing
        from jeonse.tables import ListingTable


        class ListingListView(UserIsAuthenticatedMixin, FilterView, SingleTableView):  # <-- Modify this line
            model = Listing
            template_name = "jeonse/listing_list.html"
            table_class = ListingTable
            filterset_class = ListingFilter                                    # <-- Add this line

            def get_queryset(self):
                return self.request.user.listings.all()


        class ListingDetailView(UserIsAuthenticatedMixin, UserIsCreatorMixin, DetailView):
            model = Listing
            template_name = "jeonse/listing_detail.html"


        class ListingCreateView(UserIsAuthenticatedMixin, CreateView):
            model = Listing
            form_class = ListingForm
            template_name = "jeonse/listing_create.html"
            success_url = reverse_lazy("listing_list")

            def form_valid(self, form):
                form.instance.creator = self.request.user
                return super().form_valid(form)

        ```
    1. Modify `jeonse/templates/jeonse/listing_list.html`:
        ```html
        <!-- jeonse/templates/jeonse/listing_list.html -->

        {% extends "_base.html" %}
        {% load render_table from django_tables2 %}
        {% block content %}
            <h1>Listing List</h1>
            <form method="GET">
                <div class="input-group my-2">
                    {{ filter.form }}
                    <button type="submit" class="btn btn-sm btn-outline-warning">Search</button>
                </div>
            </form>
            <div class="overflow-auto">{% render_table table %}</div>
        {% endblock %}
        ```
    1. Run server: 
        ```bash
        python3 manage.py runserver
        ```
    1. Open browser and go to: http://localhost:8000/

### 7. Request optimization

1. **Adding django-htmx to optimize user interactions**

    1. Install [django-htmx](https://pypi.org/project/django-htmx/): 
        ```bash
        pipenv install django-htmx==1.16.0
        ```
    1. Add `django_htmx` to `INSTALLED_APPS` in `settings/settings.py`:
        ```python
        # settings/settings.py

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
            "django_filters",
            "django_htmx",                              # <-- Add this line
        ]
        ```
    1. Add `django_htmx.middleware.HtmxMiddleware` middleware:
        ```python
        # settings/settings.py
                
        MIDDLEWARE = [
            "django.middleware.security.SecurityMiddleware",
            "django.contrib.sessions.middleware.SessionMiddleware",
            "django.middleware.common.CommonMiddleware",
            "django.middleware.csrf.CsrfViewMiddleware",
            "django.contrib.auth.middleware.AuthenticationMiddleware",
            "django.contrib.messages.middleware.MessageMiddleware",
            "django.middleware.clickjacking.XFrameOptionsMiddleware",
            "django_htmx.middleware.HtmxMiddleware",    # <-- Add this line
        ]
        ```
    1. Get the HTMX script from https://htmx.org/docs/#via-a-cdn-e-g-unpkg-com:
        ```html
        <script src="https://unpkg.com/htmx.org@1.9.4" integrity="sha384-zUfuhFKKZCbHTY6aRR46gxiqszMk5tcHjsVFxnUo8VMus4kHGVdIYVbOYYNlKmHV" crossorigin="anonymous"></script>
        ```
    1. Add HTMX script to `jeonse/templates/includes/scripts/`
        ```html
        <!-- jeonse/templates/includes/scripts/htmx.html -->

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm"
        crossorigin="anonymous"></script>

        <script src="https://unpkg.com/htmx.org@1.9.4"
                integrity="sha384-zUfuhFKKZCbHTY6aRR46gxiqszMk5tcHjsVFxnUo8VMus4kHGVdIYVbOYYNlKmHV"
                crossorigin="anonymous"></script>
        ```
    1. Create directory for `htmx` templates:
        ```bash
        mkdir jeonse/templates/htmx
        ```
    1. Create `htmx/listing_list.html`:
        ```bash
        touch jeonse/templates/htmx/listing_list.html
        ```
    1. Modify `jeonse/templates/jeonse/listing_list.html`:
        ```html
        <!-- jeonse/templates/jeonse/listing_list.html -->

        {% extends "_base.html" %}
        {% block content %}
            <h1>Listing List</h1>
            <form hx-get="" hx-target="#table">
                <div class="input-group my-2">
                    {{ filter.form }}
                    <button type="submit" class="btn btn-sm btn-outline-warning">Search</button>
                </div>
            </form>
            {% include "htmx/listing_list.html" %}
        {% endblock %}
        ```


    1. Modify `jeonse/templates/htmx/listing_list.html`:
        ```html
        <!-- jeonse/templates/htmx/listing_list.html -->

        {% load render_table from django_tables2 %}
        <div id="table" class="overflow-auto">{% render_table table %}</div>
        ```

    1. Modify `ListingListView` in `jeonse/views.py`:
        ```python
        # jeonse/views.py

        from django.urls import reverse_lazy
        from django.views.generic import CreateView, DetailView
        from django_filters.views import FilterView
        from django_tables2 import SingleTableView

        from jeonse.filters import ListingFilter
        from jeonse.forms import ListingForm
        from jeonse.mixins import UserIsAuthenticatedMixin, UserIsCreatorMixin
        from jeonse.models import Listing
        from jeonse.tables import ListingTable


        class ListingListView(UserIsAuthenticatedMixin, FilterView, SingleTableView):
            model = Listing
            template_name = "jeonse/listing_list.html"
            table_class = ListingTable
            filterset_class = ListingFilter

            def get_queryset(self):
                return self.request.user.listings.all()

            def get_template_names(self):                           # <-- Add this method
                if self.request.htmx:                               # <-- Add this line    
                    return ["htmx/listing_list.html"]               # <-- Add this line
                return super().get_template_names()                 # <-- Add this line


        class ListingDetailView(UserIsAuthenticatedMixin, UserIsCreatorMixin, DetailView):
            model = Listing
            template_name = "jeonse/listing_detail.html"


        class ListingCreateView(UserIsAuthenticatedMixin, CreateView):
            model = Listing
            form_class = ListingForm
            template_name = "jeonse/listing_create.html"
            success_url = reverse_lazy("listing_list")

            def form_valid(self, form):
                form.instance.creator = self.request.user
                return super().form_valid(form)

        ```
    1. Run server: 
        ```bash
        python3 manage.py runserver
        ```
    1. Open browser and go to: http://localhost:8000/

### 8. Testing the Application

1. Add `django.test.TestCase` to `jeonse/tests.py`:
    ```python
    # jeonse/tests.py

    from django.contrib.auth import get_user_model
    from django.test import TestCase
    from django.urls import reverse

    from jeonse.models import Listing


    class TestViews(TestCase):
        def setUp(self):
            self.user_kwargs = {
                "username": "testuser",
                "email": "testuser@gmail.com",
                "password": "testpassword",
            }

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

    def test_account_login(self):
        post_data = {
            "login": self.user_kwargs["email"],
            "password": self.user_kwargs["password"],
        }
        endpoint = reverse("account_login")
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/login.html")

        response = self.client.post(endpoint, post_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/login.html")
        self.assertTrue(response.context["form"].errors)

        get_user_model().objects.create_user(**self.user_kwargs)
        response = self.client.post(endpoint, post_data)
        self.assertRedirects(response, reverse("listing_list"))
    ```
1. Add `test_account_logout` to `jeonse/tests.py`:
    ```python
    # jeonse/tests.py

    def test_account_logout(self):
        user = get_user_model().objects.create_user(**self.user_kwargs)

        endpoint = reverse("account_logout")
        response = self.client.post(endpoint)
        self.assertFalse(response.context)

        self.client.force_login(user)
        response = self.client.post(endpoint)
        self.assertTrue(response.context["user"].is_authenticated)
    ```
1. Add `test_account_signup` to `jeonse/tests.py`:
    ```python
    # jeonse/tests.py

    def test_account_signup(self):
        post_data = {
            "email": self.user_kwargs["email"],
            "password1": self.user_kwargs["password"],
            "password2": self.user_kwargs["password"],
        }
        endpoint = reverse("account_signup")
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/signup.html")

        endpoint = reverse("account_signup")
        response = self.client.post(endpoint, post_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.context["user"].is_authenticated)

        user = get_user_model().objects.get(email=self.user_kwargs["email"])
        self.assertTrue(user.is_active)
        self.assertEqual(user.email, self.user_kwargs["email"])
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
                wolse_monthly_payment=i,
                gwanlibi_monthly_payment=i,
                total_monthly_payment=i,
                annual_interest_rate=i,
                total_area=i,
                number_of_rooms=i,
                number_of_bathrooms=i,
                comment=f"comment{i}",
            )
        endpoint = reverse("listing_list")
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("account_login") + f"?next={endpoint}")

        self.client.force_login(user)
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "jeonse/listing_list.html")
        self.assertEqual(len(response.context["object_list"]), 10)
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
            wolse_monthly_payment=1,
            gwanlibi_monthly_payment=1,
            total_monthly_payment=1,
            annual_interest_rate=1,
            total_area=1,
            number_of_rooms=1,
            number_of_bathrooms=1,
            comment="comment",
        )
        endpoint = reverse("listing_detail", kwargs={"pk": listing.pk})
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("account_login") + f"?next={endpoint}")

        self.client.force_login(user)
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "jeonse/listing_detail.html")
        self.assertEqual(response.context["object"], listing)
    ```
1. Add `test_listing_create` to `jeonse/tests.py`:
    ```python
    # jeonse/tests.py

    def test_listing_create(self):
        user = get_user_model().objects.create_user(**self.user_kwargs)
        endpoint = reverse("listing_create")
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("account_login") + f"?next={endpoint}")

        self.client.force_login(user)
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "jeonse/listing_create.html")

        post_data = {
            "jeonse_deposit_amount": 1,
            "wolse_deposit_amount": 1,
            "wolse_monthly_payment": 1,
            "gwanlibi_monthly_payment": 1,
            "annual_interest_rate": 1,
            "total_area": 1,
            "number_of_rooms": 1,
            "number_of_bathrooms": 1,
            "comment": "comment",
        }
        response = self.client.post(endpoint, post_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("listing_list"))
        self.assertEqual(Listing.objects.count(), 1)

        listing = Listing.objects.first()
        self.assertEqual(listing.creator, user)
        self.assertEqual(
            listing.jeonse_deposit_amount, post_data["jeonse_deposit_amount"]
        )
        self.assertEqual(
            listing.wolse_deposit_amount, post_data["wolse_deposit_amount"]
        )
        self.assertEqual(
            listing.wolse_monthly_payment, post_data["wolse_monthly_payment"]
        )
        self.assertEqual(
            listing.gwanlibi_monthly_payment, post_data["gwanlibi_monthly_payment"]
        )
        self.assertEqual(
            listing.annual_interest_rate, post_data["annual_interest_rate"]
        )
        self.assertEqual(listing.total_area, post_data["total_area"])
        self.assertEqual(listing.number_of_rooms, post_data["number_of_rooms"])
        self.assertEqual(listing.number_of_bathrooms, post_data["number_of_bathrooms"])
        self.assertEqual(listing.comment, post_data["comment"])

        monthly_payment = (
            (post_data["jeonse_deposit_amount"] + post_data["wolse_deposit_amount"])
            * post_data["annual_interest_rate"]
            / 100
            / 12
        )
        self.assertEqual(
            listing.total_monthly_payment,
            round(
                sum(
                    [
                        monthly_payment,
                        post_data["wolse_monthly_payment"],
                        post_data["gwanlibi_monthly_payment"],
                    ]
                )
            ),
        )
    ```
1. Run tests: 
    ```bash
    python3 manage.py test
    ```

### 9. Deployment

1. Go to https://ngrok.com and create account.
1. Verify your email address.
1. Download [ngrok](https://ngrok.com/download) 
1. Open https://dashboard.ngrok.com/get-started/setup and copy the authtoken:
    ```bash
    path/to/ngrok config add-authtoken SomeRand0mStr1ng
    ```
1. Run `ngrok`:
    ```bash
    path/to/ngrok http 8000
    ```
1. Copy the forwarding link to `ALLOWED_HOSTS` in `settings/settings.py`:
    ```python
    # settings/settings.py

    ALLOWED_HOSTS = ["localhost", "25ba-14-52-118-121.ngrok-free.app"]
    ```
1. Copy thy forwarding link to `CSRF_TRUSTED_ORIGINS` in `settings/settings.py`:
    ```python
    # settings/settings.py

    CSRF_TRUSTED_ORIGINS = ["localhost", "https://25ba-14-52-118-121.ngrok-free.app"]
    ```
1. Run server: 
    ```bash
    python3 manage.py runserver
    ```
1. Open browser and go to https://25ba-14-52-118-121.ngrok-free.app/
