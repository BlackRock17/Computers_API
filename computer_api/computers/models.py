from django.db import models


class Computer(models.Model):
    MAX_LENGTH = 200

    computer_name = models.CharField(
        max_length=MAX_LENGTH,
        null=True
    )

    processor = models.CharField(
        max_length=MAX_LENGTH,
        null=True
    )

    gpu = models.CharField(
        max_length=MAX_LENGTH,
        null=True
    )

    motherboard = models.CharField(
        max_length=MAX_LENGTH,
        null=True
    )

    ram = models.CharField(
        max_length=MAX_LENGTH,
        null=True
    )

    class Meta:
        unique_together = ('computer_name', 'processor', 'gpu', 'motherboard', 'ram')
        db_table = 'computers'

