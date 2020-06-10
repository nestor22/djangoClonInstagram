"""user admin classes"""
from django.contrib import admin

# models
from users.models import Profile

"""
registro bagre
admin.site.register(Profile)


abajo se usa el decorador para registrarlo en una linea
"""
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """profile admin """
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk','user', 'phone_number')
    list_editable = ('website', 'picture')
    search_fields = ('user__email', 'user_first_name', 'user__last_name', 'phone_number')
    list_filter = ('create', 'modified', 'user__is_active','user__is_staff')
