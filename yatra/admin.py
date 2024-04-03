from django.contrib import admin
from .models import PersonalP
# Register your models here.

class PersonalPAdmin(admin.ModelAdmin):
    list_display = ("name","Address","Phone","Mobile","E_mail","Aadhar_card")

admin.site.register(PersonalP,PersonalPAdmin)