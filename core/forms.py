from django import forms
from .models import UrlModel
from django.utils.translation import gettext_lazy as _


class UrlCreationForm(forms.ModelForm):
    class Meta:
        model = UrlModel
        fields = (
            "url_name",
        )
        label = {
            "url_name": _("URL"),
        }

