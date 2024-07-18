from django.urls import path
import booking.views as b_views

urlpatterns = [
    path("", b_views.get_rooms, name="rooms"),
    path("<int:room_id>/", b_views.room_details, name="room-details"),
]
