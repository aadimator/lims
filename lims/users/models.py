from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for LIMS.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore[assignment]
    last_name = None  # type: ignore[assignment]

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class Analyst(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="analyst")
    first_name = models.CharField(max_length=100, blank=True, default="")
    last_name = models.CharField(max_length=100, blank=True, default="")
    dob = models.DateField(blank=True, null=True)
    role = models.ForeignKey("Role", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        analyst_group, created = Group.objects.get_or_create(name="Analyst")
        analyst_role = Role.objects.get(
            group=analyst_group,
        )  # Get the 'Analyst' Role object
        if self.role == analyst_role:
            self.user.groups.add(analyst_group)
        else:
            self.user.groups.remove(analyst_group)

    def delete(self, *args, **kwargs):
        analyst_group = Group.objects.get(name="Analyst")
        self.user.groups.remove(analyst_group)
        super().delete(*args, **kwargs)


class Role(models.Model):
    group = models.OneToOneField(
        Group,
        on_delete=models.CASCADE,
        related_name="role",
        null=True,
    )
    role_description = models.TextField()

    def __str__(self):
        return self.group.name
