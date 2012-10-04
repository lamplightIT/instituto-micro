#coding:utf-8
from django import forms
from django.contrib.auth.models import User

class SubscriptionForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    email2 = forms.EmailField()

    def clean(self):
				cleaned_data = super(SubscriptionForm, self).clean()

				username = cleaned_data.get("username")
				password = cleaned_data.get("password")
				password2 = cleaned_data.get("password2")

				email = cleaned_data.get("email")
				email2 = cleaned_data.get("email2")

				msg = u"Error"

				if password != password2:
						self._errors["password"] = self.error_class([msg])
						self._errors["password2"] = self.error_class([msg])
						raise forms.ValidationError("Por favor, confirme sua senha novamente.")
				if email != email2:
						self._errors["email"] = self.error_class([msg])
						self._errors["email2"] = self.error_class([msg])
						raise forms.ValidationError("Por favor, confirme seu e-mail novamente.")
				if email:
						try:
								user_email = User.objects.filter(email=email)
						except User.DoesNotExist:
								user_email = None
						if user_email:
								self._errors["email"] = self.error_class([msg])
								self._errors["email2"] = self.error_class([msg])
								raise forms.ValidationError("Este e-mail já está cadastrado no nosso sistema.")
				if username:
						try:
								user_username  = User.objects.get(username=username)
						except User.DoesNotExist:
								user_username = None
						if user_username:
								self._errors["username"] = self.error_class([msg])
								raise forms.ValidationError("Este nome de usuário já está cadastrado no nosso sistema.")
				return cleaned_data

class ContactForm(forms.Form):
		full_name = forms.CharField(max_length=250)
		email = forms.EmailField()
		subject = forms.CharField(max_length=250)
		msg = forms.CharField(widget=forms.Textarea)

		def clean(self):
				cleaned_data = super(ContactForm, self).clean()