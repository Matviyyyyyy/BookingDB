from django.shortcuts import render
from booking.models import User, Service, Room, Review, Employe, Payment, Booking
# Create your views here.

def get_rooms(request):
    rooms = Room.objects.all()
    context = {
        "rooms": rooms,
    }
    return render(
        request,
        template_name="booking/rooms.html",
        context=context,
    )
def room_details(request, room_id):
    room = Room.objects.get(id = room_id)
    context = {
        "room": room,
    }
    return render(
        request,
        template_name="booking/room_details.html",
        context=context,
    )
