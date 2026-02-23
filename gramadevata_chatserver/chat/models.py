# # from django.db import models


# # class Room(models.Model):
# #     room_name = models.CharField(max_length=50)

# #     def __str__(self):
# #         return self.room_name


# # class Message(models.Model):
# #     room = models.ForeignKey(Room, on_delete=models.CASCADE)
# #     sender = models.CharField(max_length=50)
# #     message = models.TextField()

# #     def __str__(self):
# #         return f"{str(self.room)} - {self.sender}"

# from django.db import models
# import uuid



# class ChatRoom(models.Model):
#     _id = models.CharField(db_column='_id', primary_key=True, max_length=45 ,default=uuid.uuid1, unique=True ,editable=False)
#     user = models.CharField(db_column='user',max_length=45, null=True, blank=True)
#     village = models.CharField(db_column='village',max_length=45)
#     message = models.TextField(db_column='message')
#     created_at = models.DateTimeField(db_column='created_at',auto_now_add=True)

#     def __str__(self):
#         return f"{str(self.village)} - {self.user}"

#     class Meta:
#         managed = True
#         db_table = 'chatroom'