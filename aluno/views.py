from django.shortcuts import get_object_or_404, redirect, render

from .models import Aluno


def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'aluno/aluno.html', {'alunos': alunos})


def criar_aluno(request):
    if request.method == 'POST':
        Aluno.objects.create(
            nome=request.POST['nome'],
            curso=request.POST['curso'],
            bio=request.POST.get('bio', ''),
        )
        return redirect('listar_alunos')

    return render(request, 'aluno/form_aluno.html', {'titulo': 'Novo Aluno'})


def editar_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)

    if request.method == 'POST':
        aluno.nome = request.POST['nome']
        aluno.curso = request.POST['curso']
        aluno.bio = request.POST.get('bio', '')
        aluno.save()
        return redirect('listar_alunos')

    return render(request, 'aluno/form_aluno.html', {
        'titulo': 'Editar Aluno',
        'aluno': aluno,
    })


def excluir_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)

    if request.method == 'POST':
        aluno.delete()
        return redirect('listar_alunos')

    return render(request, 'aluno/confirmar_exclusao.html', {'aluno': aluno})
