from django.urls import path,include
from .views import ChatRoomListCreateView,village_GetItemByfield_InputView
# from rest_framework.routers import DefaultRouter


# router = DefaultRouter()




urlpatterns = [
    # path('', include(router.urls)),

    path('api/chatrooms/', ChatRoomListCreateView.as_view(), name='chatroom-list-create'),
    path('village_GetItemByfield_InputView/<str:field_name>/<str:input_value>/', village_GetItemByfield_InputView.as_view(), name='village_GetItemByfield_InputView'),
    # path('api/chatrooms/village/<str:village_id>/', ChatRoomByVillageView.as_view(), name='chatroom-by-village'),
    # path('api/chatrooms/user/<str:user_id>/', ChatRoomByUserView.as_view(), name='chatroom-by-user'),
    # path('api/chatrooms/user/<str:user_id>/village/<str:village_id>/', ChatRoomByUserAndVillageView.as_view(), name='chatroom-by-user-village'),


]
