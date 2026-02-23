from django.db import models
import uuid
from ..models import Register,Village,Temple



class ChatRoom(models.Model):
    _id = models.CharField(db_column='_id', primary_key=True, max_length=45, default=uuid.uuid4, unique=True, editable=False)
    
    user = models.ForeignKey(Register, on_delete=models.CASCADE, related_name='chats', db_constraint=False,db_column='user')
    village = models.ForeignKey(Village, on_delete=models.CASCADE, related_name='chats', null=True, blank=True, db_constraint=False,db_column='village')
    temple = models.ForeignKey(Temple, on_delete=models.CASCADE, related_name='chats', null=True, blank=True, db_constraint=False,db_column='temple')
    image = models.JSONField(db_column='image', blank=True, null=True,default=list)
    video = models.JSONField(db_column='video', null=True, blank=True, default=list) 
    message = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "chatroom"
        ordering = ['created_at'] 

    def __str__(self):
        return f"{self.user.full_name}: {self.message[:200]}"
