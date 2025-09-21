# environmental/models.py
from django.db import models

class WeatherData(models.Model):
    location = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField(null=True, blank=True)
    visibility = models.FloatField(null=True, blank=True)
    wind_speed = models.FloatField(null=True, blank=True)
    wind_direction = models.IntegerField(null=True, blank=True)
    
    weather_condition = models.CharField(max_length=50)
    weather_description = models.CharField(max_length=100)
    cloud_coverage = models.IntegerField(null=True, blank=True)
    
    recorded_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-recorded_at']
        
    def __str__(self):
        return f"{self.location} - {self.recorded_at}"

class AirQualityData(models.Model):
    location = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    
    # Air quality measurements
    pm25 = models.FloatField(null=True, blank=True)  # PM2.5
    pm10 = models.FloatField(null=True, blank=True)  # PM10
    no2 = models.FloatField(null=True, blank=True)   # Nitrogen Dioxide
    co = models.FloatField(null=True, blank=True)    # Carbon Monoxide
    so2 = models.FloatField(null=True, blank=True)   # Sulfur Dioxide
    o3 = models.FloatField(null=True, blank=True)    # Ozone
    
    # Overall air quality index
    aqi = models.IntegerField()
    aqi_category = models.CharField(max_length=20, choices=[
        ('good', 'Good'),
        ('moderate', 'Moderate'),
        ('unhealthy_sensitive', 'Unhealthy for Sensitive Groups'),
        ('unhealthy', 'Unhealthy'),
        ('very_unhealthy', 'Very Unhealthy'),
        ('hazardous', 'Hazardous'),
    ])
    
    recorded_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-recorded_at']
        
    def __str__(self):
        return f"AQI {self.aqi} - {self.location} - {self.recorded_at}"

class ComplianceStandard(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    # Emission thresholds
    max_smoke_opacity = models.FloatField(help_text="Maximum allowed smoke opacity percentage")
    max_pm25 = models.FloatField(null=True, blank=True)
    max_pm10 = models.FloatField(null=True, blank=True)
    max_no2 = models.FloatField(null=True, blank=True)
    max_co = models.FloatField(null=True, blank=True)
    
    # Applicable regions/vehicle types
    vehicle_types = models.JSONField(default=list, blank=True)
    applicable_regions = models.JSONField(default=list, blank=True)
    
    is_active = models.BooleanField(default=True)
    effective_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class EnvironmentalImpact(models.Model):
    location = models.CharField(max_length=100)
    measurement_date = models.DateField()
    
    # Pollution metrics
    total_violations = models.IntegerField(default=0)
    average_aqi = models.FloatField(null=True, blank=True)
    pollution_reduction_percentage = models.FloatField(null=True, blank=True)
    
    # Vehicle compliance metrics
    total_vehicles_detected = models.IntegerField(default=0)
    compliant_vehicles = models.IntegerField(default=0)
    violation_rate = models.FloatField(default=0.0)
    
    # Environmental improvement indicators
    air_quality_trend = models.CharField(max_length=20, choices=[
        ('improving', 'Improving'),
        ('stable', 'Stable'),
        ('declining', 'Declining'),
    ], null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-measurement_date']
        unique_together = ['location', 'measurement_date']
        
    def __str__(self):
        return f"Environmental Impact - {self.location} - {self.measurement_date}"