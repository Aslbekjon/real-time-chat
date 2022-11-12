from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .models import Room, Message

# Create your views here.

def home(request):
    return render(request, "home.html")

def room_view(request, room):
    username = request.GET.get('username')
    print('hello')
    room_details = Room.objects.get(name=room)
    context = {
        'username': username,
        'room':room,
        'room_details': room_details
    }
    return render(request, "room.html", context)

def checkview(request):
    room = request.POST.get('room_name')
    username = request.POST.get('username')

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room(name=room)
        new_room.save()   
        return redirect('/'+room+'/?username='+username)

def send(request):
    username = request.POST['username']
    room_id = request.POST['room_id']
    message = request.POST['message']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    return HttpResponse('Message sent successfully')


def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)

    return JsonResponse({"messages":list(messages.values())})