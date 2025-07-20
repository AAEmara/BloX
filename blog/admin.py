from django.contrib import admin
from .models import Post, Category, PostReaction, Tag

class PostReactionInline(admin.TabularInline):
    model = PostReaction
    extra = 0
    readonly_fields = ('user','is_like')
    can_delete = True

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date', 'category', 'likes')
    search_fields = ('title', 'content')
    list_filter = ('category', 'publish_date')
    ordering = ('-publish_date',)
    inlines = [PostReactionInline]
    
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Image'
    
    
admin.site.register(Category)
admin.site.register(Tag)