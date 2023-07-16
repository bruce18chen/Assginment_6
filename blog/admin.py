from django.contrib import admin
from .models import Topic, Post
from .models import ContestEntry

class ContestEntryAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('last_name', 'email')

admin.site.register(ContestEntry, ContestEntryAdmin)

admin.site.register(Topic)
admin.site.register(Post)


