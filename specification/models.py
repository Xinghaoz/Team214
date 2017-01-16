from django.db import models
from django.utils import timezone


# User class for built-in authentication module
from django.contrib.auth.models import User

class MyProperty(models.Model):
    owner = models.OneToOneField(User)
    current_role = models.ForeignKey(PlayRole)
    acc_wealth = models.IntegerField(default=200)
    acc_gpa = models.FloatField(default=3.5)
    acc_strength = models.IntegerField(default=20)
    acc_experience = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    def __str__(self):
        return self.owner+ " MyProperty " + self.current_role
    @staticmethod
    def get_myproperty(owner):
        return MyProperty.objects.filter(owner=owner)

class PlayRole(models.Model):
    role_name = models.CharField(default="unknown role")
    init_wealth = models.IntegerField(default=0)
    init_gpa = models.FloatField(default=0)
    init_strength = models.IntegerField(default=0)
    lucky = models.IntegerField(default=999)
    def __str__(self):
        return self.role_name

class PlayMap(models.Model):
    map_name = models.CharField(default="unknown map")
    map_picture = models.ImageField(upload_to="lovelive-map")
    def __str__(self):
        return self.map_name

class Event(models.Model):
    event_map = models.ManytoManyField(PlayMap)
    event_name = models.CharField(default="unknown event")
    event_message = event_name = models.CharField(default="???")
    delta_wealth = models.IntegerField(default=0)
    delta_gpa = models.FloatField(default=0)
    delta_strength = models.IntegerField(default=0)
    def __str__(self):
        return self.event_name

class ChatMessage(models.Model):
    chat_message_text = models.CharField(max_length=42)
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField(default=timezone.now())
    def __str__(self):
        return self.message_text
