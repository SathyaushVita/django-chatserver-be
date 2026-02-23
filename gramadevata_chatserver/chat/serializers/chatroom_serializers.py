from rest_framework import serializers
from ..models import *
from django.conf import settings



class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChatRoom
        fields = ['_id', 'user', 'village', 'message','temple']



class MessageSerializer1(serializers.ModelSerializer):
    image = serializers.ListField(child=serializers.CharField(), required=False, allow_null=True)
    video = serializers.ListField(child=serializers.CharField(), required=False, allow_null=True)

    class Meta:
        model = ChatRoom
        fields = '__all__'








# class MessageSerializer2(serializers.ModelSerializer):
#     user = serializers.SerializerMethodField(read_only=True)

#     def get_user(self, instance):
#         """Fetches the user details including full name and complete profile picture URL"""
#         user = instance.user if isinstance(instance.user, Register) else Register.objects.filter(id=instance.user).first()
        
#         if user:
#             profile_pic = user.profile_pic
#             if profile_pic and not profile_pic.startswith("http"):
#                 profile_pic = f"{settings.FILE_URL}{profile_pic}"

#             return {
#                 "_id": str(user.id),
#                 "name": user.full_name,
#                 "profile_pic": profile_pic
#             }
#         return None  # Return None if user not found

#     class Meta:
#         model = ChatRoom
#         fields = ['_id', 'user', 'village', 'message', 'temple']





from django.utils.timesince import timesince
from django.utils.timezone import now


# class MessageSerializer2(serializers.ModelSerializer):
#     user = serializers.SerializerMethodField(read_only=True)
#     posted_time_ago = serializers.SerializerMethodField()
#     image = serializers.SerializerMethodField()
#     video = serializers.SerializerMethodField()

#     def get_user(self, instance):
#         """Safely fetches the user details without triggering DoesNotExist error"""
#         if not instance.user_id:  # If user_id is null, return None
#             return None

#         user = Register.objects.filter(id=instance.user_id).first()  # Avoids DoesNotExist error
#         if user:
#             profile_pic = user.profile_pic
#             if profile_pic and not profile_pic.startswith("http"):
#                 profile_pic = f"{settings.FILE_URL}{profile_pic}"

#             return {
#                 "_id": str(user.id),
#                 "name": user.full_name,
#                 "profile_pic": profile_pic
#             }
#         return None  # Return None if user is not found

#     def get_posted_time_ago(self, instance):
#         """Returns time elapsed since the message was created"""
#         return timesince(instance.created_at, now()) + " ago"

#     def get_image(self, instance):
#         """Formats image URLs properly"""
#         if instance.image:
#             return [f"{settings.FILE_URL}{img}" if not img.startswith("http") else img for img in instance.image]
#         return []

#     def get_video(self, instance):
#         """Formats video URLs properly"""
#         if instance.video:
#             return [f"{settings.FILE_URL}{vid}" if not vid.startswith("http") else vid for vid in instance.video]
#         return []

#     class Meta:
#         model = ChatRoom
#         fields = ['_id', 'user', 'village', 'message', 'temple', 'posted_time_ago', 'image', 'video']







from rest_framework import serializers
from django.conf import settings
from django.utils.timesince import timesince
from django.utils.timezone import now
from ..models import ChatRoom, Register


class MessageSerializer2(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    posted_time_ago = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    video = serializers.SerializerMethodField()

    class Meta:
        model = ChatRoom
        fields = ['_id', 'user', 'village', 'message', 'temple', 'posted_time_ago', 'image', 'video']

    def get_user(self, instance):
        if not instance.user_id:
            return None

        user = Register.objects.filter(id=instance.user_id).first()
        if user:
            profile_pic = user.profile_pic or ""

            if profile_pic.startswith("None"):
                profile_pic = profile_pic.replace("None", "", 1)

            if profile_pic and not profile_pic.startswith("http"):
                profile_pic = f"{settings.FILE_URL}{profile_pic}"

            return {
                "_id": str(user.id),
                "name": user.full_name,
                "profile_pic": profile_pic
            }
        return None

    def get_posted_time_ago(self, instance):
        return timesince(instance.created_at, now()) + " ago"

    def get_image(self, instance):
        images = instance.image or []
        return [
            f"{settings.FILE_URL}{img}" if img and not img.startswith("http") else img
            for img in images
        ]

    def get_video(self, instance):
        videos = instance.video or []
        return [
            f"{settings.FILE_URL}{vid}" if vid and not vid.startswith("http") else vid
            for vid in videos
        ]
