from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Product


class CreateProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

    class Meta:
        model = Product
        exclude = ('user', )

    def save(self, commit=True):
        post = super().save(commit=False)
        post.user = self.request.user
        post.save()
        return post


class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('user', )


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'name': 'username',
            'type': 'text',
            'class': 'register__input',
            'placeholder': 'Username'
        })
        self.fields["email"].widget.attrs.update({
            'name': 'email',
            'type': 'email',
            'class': 'register__input',
            'placeholder': 'Email'
        })
        self.fields["password1"].widget.attrs.update({
            'name': 'email',
            'type': 'password',
            'class': 'register__input',
            'placeholder': 'Password'
        })
        self.fields["password2"].widget.attrs.update({
            'name': 'email',
            'type': 'password',
            'class': 'register__input',
            'placeholder': 'Password confirm'
        })

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

