from django.contrib import admin
from genres.models import Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ()

    def __str__(self):
        return self.name
