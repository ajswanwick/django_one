from django.contrib import admin
from.models import Goal_Profile, Post, Comment, Connection, LikesDislike, Notification, League, Team


# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'league')
    ordering = ('name',)  # Sort teams alphabetically by name
    list_filter = ('league',)  # Add a league filter in the admin panel
    list_filter = ('league',)  # Add a league filter in the admin panel
    search_fields = ('name',)  # Optional: Add search functionality for teams

class LeagueAdmin(admin.ModelAdmin):
      list_display = ('name', 'country')
      ordering = ('name',)  # Sort teams alphabetically by name
      list_filter = ('country',)  # Add a league filter in the admin panel
      search_fields = ('name',)  # Optional: Add search functionality for teams




admin.site.register(Goal_Profile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Connection)
admin.site.register(LikesDislike)
admin.site.register(Notification)
admin.site.register(League, LeagueAdmin)
admin.site.register(Team, TeamAdmin)



