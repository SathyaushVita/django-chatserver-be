import uuid
from django.db import models


class Village(models.Model):
    _id = models.CharField(db_column='_id', primary_key=True, max_length=45, default=uuid.uuid1, unique=True, editable=False)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "village"
