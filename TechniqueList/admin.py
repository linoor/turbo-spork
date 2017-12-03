from django.contrib import admin

# Register your models here.
from TechniqueList.models import Position, Technique, Group

admin.site.register(Position)
admin.site.register(Group)
admin.site.register(Technique)
