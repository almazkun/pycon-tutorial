from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse_lazy


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

    def get_absolute_url(self):
        return reverse_lazy("listing_detail", kwargs={"pk": self.pk})
