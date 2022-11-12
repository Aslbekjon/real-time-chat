from django.urls import path
from .views import home, room_view, checkview, send, getMessages

urlpatterns = [
    path('', home, name="home"),
    path('<str:room>/', room_view, name="room"),
    path('checkview', checkview, name="checkview"),
    path('send', send, name="send"),
    path('getMessages/<str:room>/', getMessages, name="getMessages"),


]