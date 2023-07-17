from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass

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
