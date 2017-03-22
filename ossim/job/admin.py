from django.contrib import admin

# Register your models here.
from .models import JobSchedAlg, Adv

class AdvInline(admin.TabularInline):
    model = Adv
    extra = 3

class JobSchedAlgAdmin(admin.ModelAdmin):

    inlines = [AdvInline]

admin.site.register(JobSchedAlg, JobSchedAlgAdmin)
