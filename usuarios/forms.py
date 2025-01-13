from django import forms

# LOGIN FORMS
class LoginForms(forms.Form):
        nome_login=forms.CharField(
                label='Nome de Login', 
                required=True, 
                max_length=100,
                widget=forms.TextInput(
                        attrs={
                                "class": "form-control",
                                "placeholder":"Ex.: João Silva"

                        }
                )
        )
        senha=forms.CharField(
                label='Senha', 
                required=True, 
                max_length=70,
                widget=forms.PasswordInput(
                        attrs={
                                "class": "form-control",
                                "placeholder":"Digite sua Senha: "
                        }
                )

    )


# CADASTRO FORMS
class CadastroForms(forms.Form):
        
        nome_cadastro=forms.CharField(
                label='Nome de Cadastro',
                required=True,
                max_length=100,
                widget=forms.TextInput(
                        attrs={
                                "class": "form-control",
                                "placeholder":"Ex.: João Silva de Oliveira"
                        }
                )
        )
        # EMAIL
        email=forms.EmailField(
                label='Email',
                required=True,
                max_length=100,
                widget=forms.EmailInput(
                        attrs={
                                "class": "form-control",
                                "placeholder":"Ex.: joaosilva450@gmail.com"
                        }
                )
        )
        # PASSWORD
        senha_1=forms.CharField(
                label='Senha', 
                required=True, 
                max_length=70,
                widget=forms.PasswordInput(
                        attrs={
                                "class": "form-control",
                                "placeholder":"Digite sua senha "
                        }
                )
        )
        senha_2=forms.CharField(
                label='Confirmação de Senha', 
                required=True, 
                max_length=70,
                widget=forms.PasswordInput(
                        attrs={
                                "class": "form-control",
                                "placeholder":"Digite sua senha novamente "
                        }
                )
        )



