from django.db import models

class People(models.Model):
    name = models.CharField(
        max_length=100,
        blank=True,
        default='Меня заполнить забыли?'
    )
    experience_in_years = models.CharField(
        max_length=100,
        blank=True,
        default='Меня заполнить забыли?'
    )
    skills = models.CharField(
        max_length=100,
        blank=True,
        default='Меня заполнить забыли?'
    )
    created_at = models.DateTimeField(
        auto_now=True
    )
    salary_three_years = models.CharField(
        max_length=100,
        blank=True,
        default='Меня заполнить забыли?'
    )
    salary_five_years = models.CharField(
        max_length=100,
        blank=True,
        default='Меня заполнить забыли?'
    )
