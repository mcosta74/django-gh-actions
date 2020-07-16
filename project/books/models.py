from django.db import models

from django.contrib.postgres.fields.citext import CITextField


# Create your models here.

class Author(models.Model):
    first_name = CITextField()
    last_name = CITextField()
    date_of_birth = models.DateField(null=True)


class Book(models.Model):
    title = CITextField(null=False)
    author = models.ForeignKey(
        Author,
        models.CASCADE,
        related_name='books'
    )
    copies_sold = models.PositiveIntegerField(
        default=0,
    )
