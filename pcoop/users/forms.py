from django.contrib.auth import get_user_model, forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class UserChangeForm(forms.UserChangeForm):

    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(forms.UserCreationForm):

    # error_message = forms.UserCreationForm.error_messages.update(
    #     {"duplicate_username": _("This username has already been taken.")}
    # )

    class Meta(forms.UserCreationForm.Meta):
        model = User

    # def clean_username(self):
    #     username = self.cleaned_data["username"]
    #
    #     try:
    #         User.objects.get(username=username)
    #     except User.DoesNotExist:
    #         return username
    #
    #     raise ValidationError(self.error_messages["duplicate_username"])

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False
        # If one field gets autocompleted but not the other, our 'neither
        # password or both password' validation will be triggered.
        self.fields['password1'].widget.attrs['autocomplete'] = 'off'
        self.fields['password2'].widget.attrs['autocomplete'] = 'off'

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = super(UserCreationForm, self).clean_password2()
        if bool(password1) ^ bool(password2):
            raise forms.ValidationError("Fill out both fields")
        return password2
