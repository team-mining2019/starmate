from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    link_from = models.CharField(
        max_length=50,
        null=True,
        default=None,
    )

    done = models.BooleanField(
        default=False,
    )

    question_01 = models.IntegerField(
        default=0,
    )

    question_02 = models.IntegerField(
        default=0,
    )

    question_03 = models.IntegerField(
        default=0,
    )

    question_04 = models.IntegerField(
        default=0,
    )

    question_05 = models.IntegerField(
        default=0,
    )

    question_06 = models.IntegerField(
        default=0,
    )

    question_07 = models.IntegerField(
        default=0,
    )

    question_08 = models.IntegerField(
        default=0,
    )

    question_09 = models.IntegerField(
        default=0,
    )

    question_10 = models.IntegerField(
        default=0,
    )

    question_11 = models.IntegerField(
        default=0,
    )

    question_12 = models.IntegerField(
        default=0,
    )

    question_13 = models.IntegerField(
        default=0,
    )

    question_14 = models.IntegerField(
        default=0,
    )

    question_15 = models.IntegerField(
        default=0,
    )

    def __str__(self):
        return self.user.username

    