from django.conf import settings
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from .forms import AnalystForm
from .forms import UserAdminChangeForm
from .forms import UserAdminCreationForm
from .models import Analyst
from .models import Role
from .models import User

if settings.DJANGO_ADMIN_FORCE_ALLAUTH:
    # Force the `admin` sign in process to go through the `django-allauth` workflow:
    # https://docs.allauth.org/en/latest/common/admin.html#admin
    admin.site.login = login_required(admin.site.login)  # type: ignore[method-assign]


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    analyst_form = AnalystForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "email")}),
        (_("Analyst info"), {"fields": ("analyst",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "name", "is_superuser", "analyst"]
    search_fields = ["name"]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if "analyst" in form.cleaned_data:
            # If there's analyst data, update or create the analyst.
            analyst_data = form.cleaned_data["analyst"]
            Analyst.objects.update_or_create(user=obj, defaults=analyst_data)


@admin.register(Analyst)
class AnalystAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "dob", "role")


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("group", "role_description")


# Now, register each model with the associated admin class.


# Register the built-in Group model with the built-in GroupAdmin interface
admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)
