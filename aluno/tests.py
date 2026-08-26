from django.test import Client, TestCase
from django.urls import reverse

from .models import Aluno


class AlunoCRUDTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.aluno = Aluno.objects.create(
            nome='Ana Silva',
            curso='ADS',
            bio='Apaixonada por desenvolvimento web.',
        )

    def test_listar_alunos(self):
        response = self.client.get(reverse('listar_alunos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'aluno/aluno.html')
        self.assertContains(response, 'Ana Silva')

    def test_criar_aluno_get(self):
        response = self.client.get(reverse('criar_aluno'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'aluno/form_aluno.html')
        self.assertContains(response, 'Novo Aluno')

    def test_criar_aluno_post(self):
        response = self.client.post(reverse('criar_aluno'), {
            'nome': 'Carlos Mendes',
            'curso': 'SI',
            'bio': 'Foco em segurança da informação.',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('listar_alunos'))
        self.assertTrue(Aluno.objects.filter(nome='Carlos Mendes').exists())

    def test_editar_aluno_get(self):
        response = self.client.get(reverse('editar_aluno', args=[self.aluno.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'aluno/form_aluno.html')
        self.assertContains(response, 'Ana Silva')
        self.assertContains(response, 'ADS')

    def test_editar_aluno_post(self):
        response = self.client.post(reverse('editar_aluno', args=[self.aluno.pk]), {
            'nome': 'Ana Silva Atualizada',
            'curso': 'Engenharia de Software',
            'bio': 'Nova bio.',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('listar_alunos'))
        self.aluno.refresh_from_db()
        self.assertEqual(self.aluno.nome, 'Ana Silva Atualizada')
        self.assertEqual(self.aluno.curso, 'Engenharia de Software')

    def test_excluir_aluno_get(self):
        response = self.client.get(reverse('excluir_aluno', args=[self.aluno.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'aluno/confirmar_exclusao.html')
        self.assertContains(response, 'Ana Silva')

    def test_excluir_aluno_post(self):
        pk = self.aluno.pk
        response = self.client.post(reverse('excluir_aluno', args=[pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('listar_alunos'))
        self.assertFalse(Aluno.objects.filter(pk=pk).exists())
