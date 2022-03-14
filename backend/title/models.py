from django.conf import settings
from django.db import models


class REview(models.Model):
    "Generated Model"
    title = models.CharField(
        max_length=256,
    )
    rating = models.FloatField()
    description = models.CharField(
        max_length=256,
    )
    revieweer = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="review_revieweer",
    )
    seller = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="review_seller",
    )


# Create your models here.
