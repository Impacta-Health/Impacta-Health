from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models.user_model import (
    AdminUserProfile,
    DoctorUserProfile,
    PatientUserProfile,
    User,
)


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = (
        "email",
        "username",
        "first_name",
    )
    list_filter = ("email", "username", "first_name", "is_active", "is_staff")
    ordering = ("-date_joined",)
    list_display = ("id", "username", "first_name", "last_name", "email", "is_active", "is_staff")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "username",
                    "first_name",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "first_name", "password1", "password2", "is_active", "is_staff"),
            },
        ),
    )


class AdminUserProfileAdmin(admin.ModelAdmin):
    model = AdminUserProfile
    search_fields = (
        "user__email",
        "user__username",
        "user__first_name",
    )
    list_filter = (
        "user",
        "user__username",
        "user__first_name",
        "user__email",
    )
    ordering = ("-updated_at",)
    list_display = (
        "id",
        "user",
        "cpf",
        "avatar",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "user",
                    "cpf",
                    "avatar",
                )
            },
        ),
    )


admin.site.register(User, UserAdminConfig)
admin.site.register(AdminUserProfile, AdminUserProfileAdmin)
