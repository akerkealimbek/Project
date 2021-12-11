from django.contrib import admin

from .models import Cinema, Banner, CinemaComment, Film, FilmComment, Session

admin.site.register(Cinema)
admin.site.register(Banner)
admin.site.register(Film)
admin.site.register(Session)
admin.site.register(FilmComment)
admin.site.register(CinemaComment)
