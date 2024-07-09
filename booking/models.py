from django.db import models

# Create your models here.

class Room(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField()

    def __str__(self):
        return f"{self.number} - {self.status}"

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
        ordering = ["number"]

class User(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField()
    phone_number = models.CharField(max_length=256)
    date_of_birth = models.DateField()
    role = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.phone_number}"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["first_name"]

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="rooms_booking")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users_booking")
    booking_date = models.DateTimeField(auto_now_add=True)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.booking_date} - {self.total_price}"

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ["booking_date"]

class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name="bookings_payment")
    payment_date = models.DateTimeField(auto_now_add=True)
    full_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.payment_date} - {self.payment_method}"

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
        ordering = ["payment_date"]

class Employe(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    position = models.CharField(max_length=256)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"

    class Meta:
        verbose_name = "Employe"
        verbose_name_plural = "Employes"
        ordering = ["first_name"]

class Service(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.employe} - {self.name}"

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ["name"]

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="uses_review")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="rooms_review")
    review_date = models.DateField(auto_now_add=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    comment = models.TextField()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.review_date}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ["rating"]












