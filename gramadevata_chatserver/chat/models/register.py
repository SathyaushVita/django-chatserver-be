import uuid
from django.db import models

class Register(models.Model):
    id = models.CharField(db_column='id', primary_key=True, max_length=45, default=uuid.uuid1, unique=True, editable=False)
    full_name = models.CharField(db_column='full_name', max_length=200, blank=True, null=True)
    profile_pic=models.TextField()
    


    



    class Meta:
        db_table = "user"
