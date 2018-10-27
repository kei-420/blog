from django import forms
from .models import UserManager
from django.core.exceptions import ValidationError


class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserManager
        fields = ('username', 'email', 'password', )
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'パスワード'}),
        }

    confirm_password = forms.CharField(
        label='確認用パスワード',
        required=True,
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': '確認用パスワード'}),
    )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {'placeholder': 'username'}
        self.fields['email'].required = True
        self.fields['email'].widget.attrs = {'placeholder': 'email'}
        # self.fields['password'].widget.attrs = {'placeholder': 'password'}

    def clean_username(self):
        """usernameのバリデーション"""
        username = self.cleaned_data['username']
        # usernameは3文字以上にならねばエラー表示。
        if len(username) < 3:
            raise forms.ValidationError('Username must be longer than 3')
        # usernameはアルファベットのみ/アルファベット＆数字でなければエラー表示。
        if not username.isalpha() or username.isalnum():
            raise forms.ValidationError('Username must contain only alphabets and numbers ')
        # usernameは数字のみではならない。
        if username.isnumeric():
            raise forms.ValidationError('Username cannot contain only numbers')
        return username

    def clean(self):
        """passwordとconfirm_passwordのバリデーション"""
        super(SignUpForm, self).clean()
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirmed_password')
        # password と confirm_passwordが一致していなければエラー表示
        if password != confirm_password:
            raise forms.ValidationError("password and confirmed_password don't match")

    def save(self, commit=True):
        """passwordをハッシュ化してからユーザー情報の保存"""
        user_info = super(SignUpForm, self).save(commit=False)
        user_info.set_password(self.cleaned_data["password"])
        if commit:
            user_info.save()

        return user_info

