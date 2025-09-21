# detection/models.py
from django.db import models
from django.contrib.auth.models import User
import uuid

class Vehicle(models.Model):
    license_plate = models.CharField(max_length=20, unique=True)
    vehicle_type = models.CharField(max_length=50, choices=[
        ('car', 'Car'),
        ('truck', 'Truck'),
        ('bus', 'Bus'),
        ('motorcycle', 'Motorcycle'),
        ('other', 'Other'),
    ])
    owner_name = models.CharField(max_length=100, blank=True)
    owner_phone = models.CharField(max_length=15, blank=True)
    owner_email = models.EmailField(blank=True)
    registration_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.license_plate} ({self.vehicle_type})"

class Camera(models.Model):
    camera_id = models.CharField(max_length=50, unique=True)
    location = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    installation_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"Camera {self.camera_id} - {self.location}"

class DetectionRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True, blank=True)
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='detections/')
    
    # Detection results
    smoke_detected = models.BooleanField(default=False)
    confidence_score = models.FloatField(default=0.0)
    vehicle_detected = models.BooleanField(default=False)
    license_plate_detected = models.CharField(max_length=20, blank=True)
    
    # Environmental context
    weather_condition = models.CharField(max_length=50, blank=True)
    temperature = models.FloatField(null=True, blank=True)
    humidity = models.FloatField(null=True, blank=True)
    air_quality_index = models.IntegerField(null=True, blank=True)
    
    # Timestamps
    detected_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(null=True, blank=True)
    
    # Status
    is_violation = models.BooleanField(default=False)
    reviewed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    review_status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('false_positive', 'False Positive'),
        ('disputed', 'Disputed'),
    ], default='pending')
    
    class Meta:
        ordering = ['-detected_at']
    
    def __str__(self):
        return f"Detection {self.id} - {self.detected_at}"

class ViolationRecord(models.Model):
    detection = models.OneToOneField(DetectionRecord, on_delete=models.CASCADE)
    violation_type = models.CharField(max_length=50, default='emission_violation')
    severity = models.CharField(max_length=20, choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ])
    fine_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    # Notification status
    authority_notified = models.BooleanField(default=False)
    owner_notified = models.BooleanField(default=False)
    authority_notified_at = models.DateTimeField(null=True, blank=True)
    owner_notified_at = models.DateTimeField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Violation {self.detection.id} - {self.severity}"