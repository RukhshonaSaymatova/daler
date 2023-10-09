from django.contrib import admin
from .models import Participation
# Register your models here.


@admin.register(Participation)

class ParticipationAdmin(admin.ModelAdmin):
    list_display = ("user",  "project", "dt_of_joining", "dt_of_departure")
    date_hierarchy = "dt_of_joining"
