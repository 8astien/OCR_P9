from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields["username"].label = "Nom d'utilisateur :"
        self.fields["password"].label = "Mot de passe :"


class SignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields["username"].label = "Nom d'utilisateur :"
        self.fields["email"].label = "Email :"
        self.fields["password1"].label = "Mot de passe :"
        self.fields["password2"].label = "Confirmation mot de passe :"
        for fieldname in ["username", "email", "password1", "password2"]:
            self.fields[fieldname].help_text = None
