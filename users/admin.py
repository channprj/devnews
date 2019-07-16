# django
from django.contrib import admin

# apps
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('css/admin/base.css',),
        }

    items = [
        'user',
        'display_name',
        'bio',
        'karma',
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
        'display_name',
        'bio',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
    )
    ordering = ('-created_at',)
