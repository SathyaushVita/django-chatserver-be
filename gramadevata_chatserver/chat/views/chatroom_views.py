
import uuid
from rest_framework import generics
from ..models import ChatRoom
from ..serializers import MessageSerializer,MessageSerializer1,MessageSerializer2
from rest_framework.views import *
from ..utils import save_image_to_azure,save_video_to_azure
# View to list all chat messages or create a new chat message
class ChatRoomListCreateView(generics.ListCreateAPIView):
    queryset = ChatRoom.objects.all().order_by('created_at')
    serializer_class = MessageSerializer1

    def create(self, request, *args, **kwargs):
            data = request.data.copy()

            # Ensure `_id` is set before saving images/videos
            _id = data.get('_id')
            if not _id:
                _id = str(uuid.uuid4())  # Generate a new UUID if not provided
                data['_id'] = _id

            # Process images
            if 'image' in data and isinstance(data['image'], list):
                image_urls = []
                for image_data in data['image']:
                    image_url = save_image_to_azure(image_data, _id, 'chat_image', 'chatroom')
                    if image_url:
                        image_urls.append(image_url)
                data['image'] = image_urls  

            # Process videos
            if 'video' in data and isinstance(data['video'], list):
                video_urls = []
                for video_data in data['video']:
                    video_url = save_video_to_azure(video_data, _id, 'chat_video', 'chatroom')
                    if video_url:
                        video_urls.append(video_url)
                data['video'] = video_urls  

            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data)
    





class village_GetItemByfield_InputView(APIView):
    serializer_class = MessageSerializer2

    def get(self, request, input_value, field_name):
        try:
           
            field_names = [field.name for field in ChatRoom._meta.get_fields()]

            
            if field_name in field_names:
               
                filter_kwargs = {field_name: input_value}
                newsdata = ChatRoom.objects.filter(**filter_kwargs).order_by('created_at')
               
                serialized_data = MessageSerializer2(newsdata, many=True)

                return Response({
                    "message":200,
                     "data": serialized_data.data
                     })
            
                
              
            else:
                return Response({
                    'message': 'Invalid field name',
                    'status': 400
                })

        except ChatRoom.DoesNotExist:
            return Response({
                'message': 'Object not found',
                'status': 404
            })


