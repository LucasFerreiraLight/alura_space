from django.shortcuts import render, redirect

from usuarios.forms import LoginForms, CadastroForms

from django.contrib.auth.models import User

from django.contrib import auth

from django.contrib import messages

def login(request):
        form = LoginForms()

        if request.method == 'POST':
                form = LoginForms(request.POST)

                if form.is_valid():
                        nome = form['nome_login'].value()
                        senha = form['senha'].value()

                usuario = auth.authenticate(
                        request,
                        username = nome,
                        password = senha
                )
                if usuario is not None:
                        auth.login(request, usuario)
                        messages.success(request, f"Usuário ({nome}) Logado com Sucesso!")
                        return redirect('index')
                else:
                        messages.error(request, f"Erro ao efetuar Login.")
                        return redirect('login') 






        return render(request, "usuarios/login.html", {"form": form})




def cadastro(request):
        form = CadastroForms()

        if request.method == 'POST':
                form = CadastroForms(request.POST)

                if form.is_valid():

                        # a informacao está no forms, ou seja caso eu coloque
                        # nome_cadastro no forms, tenho que colocar aqui também
                        nome=form['nome_cadastro'].value()
                        email=form['email'].value()
                        senha=form['senha_1'].value()

                        if User.objects.filter(username=nome).exists():
                                messages.error(request, "Não foi possivel efetuar o cadastro, usuario já existente!")
                                return redirect('cadastro')
                        
                        usuario = User.objects.create_user(
                                username=nome,
                                email=email,
                                password=senha
                                )
                        usuario.save()
                        messages.success(request, f"Usuário {nome} cadastrado com sucesso!")
                        return redirect('login')
                
                        


        return render(request, 'usuarios/cadastro.html', {"form": form})


def logout(request):
        auth.logout(request)
        messages.success(request, "Logout efetuado com sucesso!")
        return redirect('login')




