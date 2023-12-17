from django.contrib import admin
from .models import Game
from .models import CustomUser
from .models import Review
from .models import GameList


# Register your models here.




admin.site.register(Game)
admin.site.register(Review)

admin.site.register(CustomUser)
admin.site.register(GameList)