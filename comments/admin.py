from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','post','content','parent','created_at')
    list_filter = ('created_at','post','user')
    search_fields = ('content','user__username','post__title')
    raw_id_fields = ('post','user','parent')

admin.site.register(Comment,CommentAdmin)