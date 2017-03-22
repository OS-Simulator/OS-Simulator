from django.contrib import admin

# Register your models here.
from .models import DiskSchedAlg, Adv

class AdvInline(admin.TabularInline):
    model = Adv
    extra = 3

class DiskSchedAlgAdmin(admin.ModelAdmin):

    inlines = [AdvInline]

admin.site.register(DiskSchedAlg, DiskSchedAlgAdmin)
