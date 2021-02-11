from django.db import models
from django.core.validators import *

# Unused imports from webserver lab...
# from __future__ import unicode_literals
# from django.contrib.auth.models import User, Group
# from django.contrib import admin
# import base64

# Breed Model - added from work done in webserver....


class Breed(models.Model):
    TINY = 'tiny'
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'
    BREED_SIZE_CHOICES = [
        (TINY, 'tiny'),
        (SMALL, 'small'),
        (MEDIUM, 'medium'),
        (LARGE, 'large'),
    ]
    size = models.CharField(
        max_length=6,
        choices=BREED_SIZE_CHOICES,
        default=TINY,
    )

    name = models.CharField(max_length=50, blank=False)
    # (a character string) [should accept Tiny, Small, Medium, Large]
    friendliness = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)])
    # (an integer field) [should accept values from 1-5]
    trainability = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)])
    # (an integer field) [should accept values from 1-5]
    sheddingamount = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)])
    # (an integer field) [should accept values from 1-5]
    exerciseneeds = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)])
    # (an integer field) [should accept values from 1-5]

    def __str__(self):
        return str(self.name)

# Dog model


class Dog(models.Model):
    name = models.CharField(max_length=50, blank=False)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=20, blank=False)
    color = models.CharField(max_length=30, blank=False)
    favoriteFood = models.CharField(max_length=50, blank=False)
    favoriteToy = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return str(self.name)
