import uuid
from datetime import date
from django.db import models

class StockReadingManager(models.Manager):
    def filter_current(self, **kwargs):
        kwargs["expiry_date__gte"] = date.today()
        return self.filter(**kwargs)

    def filter_historic(self, **kwargs):
        kwargs["expiry_date__lt"] = date.today()
        return self.filter(**kwargs)


class StockReading(models.Model):
    class Meta:
        unique_together = (
            'reference_id', 'expiry_date'
        )

    objects = StockReadingManager()

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    reference_id = models.CharField(
        max_length=13,
        blank=False,
        null=False,
        db_index=True,
        help_text="13 digit code"
    )
    expiry_date = models.DateField(
        blank=False,
        null=False,
        db_index=True,
        help_text="Expiry date of your reference"
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        help_text="Created on"
    )

    def __str__(self):
        return f"<{self.id}> {self.reference_id} : {self.expiry_date.isoformat()}"

