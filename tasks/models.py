from django.db import models


class Task(models.Model):
    PRIORITY_CHOICES = [
        (1, 'HIGH'),
        (2, 'MEDIUM'),
        (3, 'LOW')
    ]
    STATUS_CHOICES = [
        (1, 'IN-PROGRESS'),
        (2, 'COMPLETED')
    ]

    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    priority = models.PositiveSmallIntegerField(choices=PRIORITY_CHOICES)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=1)
    is_deleted = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
