# django
from django.contrib import admin

# apps
from .models import Link
from .models import Comment
from .models import Vote


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('css/admin/base.css',),
        }

    items = [
        'user',
        'url',
        'root_url',
        'title',
        'content',
        'tag_list', # tags
        'created_at',
        'updated_at',
    ]
    editable_items = (
    )
    list_display = items
    list_editable = editable_items
    list_filter = (
        'created_at',
    )
    csv_fields = items
    search_fields = (
        'url',
        'root_url',
        'title',
        'content',
        'tags',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
    )
    ordering = ('-updated_at', '-created_at',)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('css/admin/base.css',),
        }

    items = [
        'parent',
        'user',
        'content',
        'created_at',
        'updated_at',
    ]
    editable_items = (
    )
    list_display = items
    list_editable = editable_items
    list_filter = (
        'created_at',
    )
    csv_fields = items
    search_fields = (
        'user',
        'content',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
    )
    ordering = ('-updated_at', '-created_at',)


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('css/admin/base.css',),
        }

    items = [
        'link',
        'user',
        'action',
        'created_at',
    ]
    editable_items = (
    )
    list_display = items
    list_editable = editable_items
    list_filter = (
    )
    csv_fields = items
    search_fields = (
        'link',
        'user',
    )
    readonly_fields = (
        'created_at',
    )
    ordering = ('-created_at',)
