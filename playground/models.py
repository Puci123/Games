from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # Add your custom fields here
    # For example:
    # profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    # additional_field = models.CharField(max_length=255, null=True, blank=True)
    
    use_decryption = models.TextField(default='Your default value here')
    profile_pics = models.ImageField(default=None, blank=True, null=True)

    def __str__(self):
        return self.username


class Game(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title =  models.CharField(max_length = 50)
    genera = models.CharField(max_length = 50)
    decryption = models.TextField()
    image =  models.ImageField(default=None, blank=True, null=True)
    rales = models.DateField()


    def __str__(self) -> str:
        return(f"{self.title}")
    

class Review(models.Model):
    body = models.TextField(default = '')
    score = models.IntegerField()
    likes = models.IntegerField(default = 0)
    dislikes = models.IntegerField(default = 0) 
    created_at = models.DateTimeField(auto_now_add=True)

    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    

class GameList(models.Model):
    title = models.CharField(max_length = 50)
    body = models.TextField(default=None, blank=True, null=True)

    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    games = models.ManyToManyField(Game, default=None, blank=True, null=True)

    def __str__(self) -> str:
        return(f"{self.title}")