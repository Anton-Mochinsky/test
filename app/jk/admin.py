from django.contrib import admin
from jk.models import User

admin.site.register(User)

# from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser, TwoFactorAuth, MeterReading
#
#
# class CustomUserAdmin(UserAdmin):
#     # Отображение следующих полей в списке пользователей
#     list_display = ("email", "full_name", "phone_number", "apartment_number", "is_staff")
#
#     # Поля, которые будут использоваться при поиске пользователя
#     search_fields = ("email", "full_name")
#
#     # Поля, отображаемые и редактируемые при просмотре/редактировании отдельного пользователя
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal info', {'fields': ('full_name', 'phone_number', 'apartment_number')}),
#         ('Permissions', {
#             'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
#         }),
#         ('Important dates', {'fields': ('last_login',)}),
#     )
#
#     # Поля, отображаемые при создании нового пользователя
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2', 'full_name', 'phone_number', 'apartment_number')}
#          ),
#     )
#     ordering = ('email',)
#
#
# admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(TwoFactorAuth)
# admin.site.register(MeterReading)