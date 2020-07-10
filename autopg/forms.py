from string import ascii_letters, digits

from django import forms

from .models import Database


VALID_ALPHABET = ascii_letters + digits


class DatabaseCreateForm(forms.ModelForm):
    class Meta:
        model = Database
        exclude = 'username',

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        name = self.cleaned_data.get('name')
        valid = all((ch in VALID_ALPHABET for ch in name)) and name[0] not in digits
        if not valid:
            raise forms.ValidationError('Название БД может содержать только латинские буквы и цифры,'
                                        ' причем первый символ должен быть буквой')
        return name

    def clean_password(self):
        password = self.cleaned_data.get('password')
        valid = all((ch in VALID_ALPHABET for ch in password))
        if not valid:
            raise forms.ValidationError('Пароль может содержать только латинские буквы и цифры')
        return password
