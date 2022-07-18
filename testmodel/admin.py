from django.contrib import admin
from .models import Testmodel1, Testmodel2


@admin.register(Testmodel2)
class Testmodel2Admin(admin.ModelAdmin):
    list_display = ['name', 'age']