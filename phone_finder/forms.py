from django import forms
from django.core.validators import RegexValidator, MinLengthValidator


class CheckPhoneForm(forms.Form):
    phone_validator = RegexValidator(
        regex=r'^\+?1?\d{11,11}$',
        message="Телефон должен быть в формате: '79999999999'."
    )
    phone_number = forms.CharField(
        max_length=11,
        validators=[phone_validator, ]
    )
