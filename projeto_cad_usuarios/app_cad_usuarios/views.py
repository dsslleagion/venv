from django.shortcuts import render, redirect
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    if request.method == 'POST':
        # salvar os dados da tela para o banco
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.idade = request.POST.get('idade')
        novo_usuario.save()
        # redirecionar após o salvamento
        return redirect('listagem_usuarios')

    # exibir todos os usuários já cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    # retornar os dados para a página de listagem de usuários
    return render(request, 'usuarios/usuarios.html', usuarios)

def editar_usuario(request, id):
    usuario = Usuario.objects.get(pk=id)
    if request.method == 'POST':
        usuario.nome = request.POST.get('nome')
        usuario.idade = request.POST.get('idade')
        usuario.save()
        return redirect('listagem_usuarios')
    return render(request, 'usuarios/editar_usuario.html', {'usuario': usuario})

def excluir_usuario(request, id):
    usuario = Usuario.objects.get(pk=id)
    usuario.delete()
    return redirect('listagem_usuarios')
