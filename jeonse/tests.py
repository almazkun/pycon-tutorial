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

    def test_account_logout(self):
        user = get_user_model().objects.create_user(**self.user_kwargs)

        endpoint = reverse("account_logout")
        response = self.client.post(endpoint)
        self.assertFalse(response.context)

        self.client.force_login(user)
        response = self.client.post(endpoint)
        self.assertTrue(response.context["user"].is_authenticated)

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
