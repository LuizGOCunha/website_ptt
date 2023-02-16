from django import forms

class SignupForm(forms.Form):
    name = forms.CharField(max_length=150, required=True)
    pis = forms.CharField(max_length=11, required=True)
    cpf = forms.CharField(max_length=11, required=True)

    country = forms.CharField(max_length=150, required=True)
    state = forms.CharField(max_length=150, required=True)
    city = forms.CharField(max_length=150, required=True)
    street = forms.CharField(max_length=150, required=True)
    number = forms.IntegerField(required=True)
    zipcode = forms.CharField(max_length=50, required=True)
    complement = forms.CharField(max_length=150)

    email = forms.EmailField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    password_conf = forms.CharField(widget=forms.PasswordInput)

class SigninForm(forms.Form):
    email = forms.EmailField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


    
