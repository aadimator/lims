from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView

from lims.users.forms import AnalystForm
from lims.users.models import Analyst
from lims.users.models import User


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        # for mypy to know that the user is authenticated
        assert self.request.user.is_authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["analyst_group"] = Group.objects.get(name="Analyst")
        if self.request.user.groups.filter(name="Analyst").exists():
            context["analyst_form"] = AnalystForm(instance=self.get_analyst_instance())
        return context

    def get_analyst_instance(self):
        try:
            return Analyst.objects.get(user=self.request.user)
        except Analyst.DoesNotExist:
            return None

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.user.groups.filter(name="Analyst").exists():
            analyst_form = AnalystForm(
                self.request.POST,
                instance=self.get_analyst_instance(),
            )
            if analyst_form.is_valid():
                analyst_form.save()
        return response


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()
