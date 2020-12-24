from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post #Comment, Reply

'''
class ReplyInline(admin.StackedInline):
    model = Reply
    extra = 5


class CommentAdmin(admin.ModelAdmin):
    inlines = [ReplyInline]
'''

class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'text')
    list_display = ['title', 'is_public', 'updated_at', 'created_at', 'title_len']
    list_filter = ['is_public']
    ordering = ('-updated_at',)

    def title_len(self, obj):
        return len(obj.title)

    title_len.short_description = 'タイトルの文字数'

#Admin page with markdown editor
admin.site.register(Post, MarkdownxModelAdmin)