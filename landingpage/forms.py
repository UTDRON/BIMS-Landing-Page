from django import forms
from django.forms import Textarea
from django.db.models import fields
from .models import Contact,ContactAndOTP
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

# from .views import var_global

class ContactForm(forms.ModelForm):
    class Meta:
        model       = Contact
        fields      = '__all__'

    def clean_otp(self):
        data = self.cleaned_data['otp']
        if data!=str(ContactAndOTP.objects.last().otp):
            raise ValidationError("The OTP didn't match")
        return data
        