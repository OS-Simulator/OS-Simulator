from django.contrib import admin

# Register your models here.
from .models import MemSchedAlg, Adv

class AdvInline(admin.TabularInline):
    model = Adv
    extra = 3

class MemSchedAlgAdmin(admin.ModelAdmin):

    inlines = [AdvInline]

admin.site.register(MemSchedAlg, MemSchedAlgAdmin)
