from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from ferry.accounts.models import APIToken, User


class InlineAPITokenAdmin(admin.TabularInline):
    model = APIToken
    readonly_fields = ("token", "created_at", "updated_at")
    extra = 0


class FerryUserAdmin(UserAdmin):
    inlines = [InlineAPITokenAdmin]

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


admin.site.register(User, FerryUserAdmin)
admin.site.unregister(Group)
