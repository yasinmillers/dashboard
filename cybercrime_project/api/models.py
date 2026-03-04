from django.db import models
class Complaint(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Investigating', 'Investigating'),
        ('Resolved', 'Resolved'),
        ('Rejected', 'Rejected'),
    ]

    complaint_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    crime_type = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.email

class Complaint(models.Model):
    complaint_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    crime_type = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=30, default="Pending")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="complaints")

    def __str__(self):
        return f"{self.crime_type} - {self.user.email}"