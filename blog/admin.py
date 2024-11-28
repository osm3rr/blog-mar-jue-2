from django.contrib import admin
from .models import Publication

# Register your models here.
class PublicationAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
    )

admin.site.register(Publication, PublicationAdmin)