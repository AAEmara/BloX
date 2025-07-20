from django.contrib import admin
from .models import Post, Category, Tag
from blog_auth.models import CustomUser
from django.http import HttpResponseRedirect
from django.urls import reverse

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date', 'category', 'likes')
    search_fields = ('title', 'content')
    list_filter = ('category', 'publish_date')
    ordering = ('-publish_date',)
    
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Image'
    
    
admin.site.register(Category)
admin.site.register(Tag)



class UserRedirectAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        return HttpResponseRedirect(reverse('admin_panel:user_list')
)



admin.site.register(CustomUser, UserRedirectAdmin)
