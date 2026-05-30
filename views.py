from django.shortcuts import render,redirect
from .models import Room,Message

def indexView(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        room = request.POST.get('room')

        try:
            get_room = Room.objects.get(room_name=room)
            return redirect('room', room_name=room, username=username)
        except Room.DoesNotExist:
            r=Room.objects.create(room_name=room)
            
            return redirect('room', room_name=room, username=username)

    return render(request, 'index.html')
        


def roomView(request, room_name, username):
    
    get_room = Room.objects.get(room_name=room_name)
    get_messages = Message.objects.filter(room=get_room)
    
    context = {
        "messages": get_messages,
        "username": username,
        "room_name": room_name,
    }
    
    return render(request, 'room.html', context)
