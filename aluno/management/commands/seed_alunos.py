from django.core.management.base import BaseCommand

from aluno.models import Aluno

ALUNOS_DEMO = [
    {
        'nome': 'Ana Silva',
        'curso': 'Análise e Desenvolvimento de Sistemas',
        'bio': 'Desenvolvedora full stack apaixonada por Python e interfaces modernas.',
    },
    {
        'nome': 'Carlos Mendes',
        'curso': 'Engenharia de Software',
        'bio': 'Foco em arquitetura de sistemas e qualidade de código.',
    },
    {
        'nome': 'Marina Costa',
        'curso': 'Direito',
        'bio': 'Interesse em direito civil e mediação de conflitos.',
    },
    {
        'nome': 'Lucas Ferreira',
        'curso': 'Biomedicina',
        'bio': 'Pesquisa em diagnóstico molecular e análises clínicas.',
    },
    {
        'nome': 'Beatriz Almeida',
        'curso': 'Engenharia Civil',
        'bio': 'Projetos de estruturas e infraestrutura urbana sustentável.',
    },
    {
        'nome': 'Rafael Souza',
        'curso': 'Engenharia Mecânica',
        'bio': 'Projetos automotivos e manufatura avançada.',
    },
    {
        'nome': 'Juliana Rocha',
        'curso': 'Psicologia',
        'bio': 'Atuação clínica com enfoque em saúde mental comunitária.',
    },
    {
        'nome': 'Pedro Nunes',
        'curso': 'Administração',
        'bio': 'Empreendedorismo, gestão de equipes e inovação.',
    },
    {
        'nome': 'Camila Dias',
        'curso': 'Enfermagem',
        'bio': 'Cuidado humanizado e atenção primária à saúde.',
    },
    {
        'nome': 'Thiago Martins',
        'curso': 'Sistemas de Informação',
        'bio': 'Segurança da informação e governança de dados.',
    },
]


class Command(BaseCommand):
    help = 'Popula o banco com alunos de demonstração de diversos cursos.'

    def handle(self, *args, **options):
        criados = 0
        existentes = 0

        for dados in ALUNOS_DEMO:
            _, created = Aluno.objects.get_or_create(
                nome=dados['nome'],
                defaults={
                    'curso': dados['curso'],
                    'bio': dados['bio'],
                },
            )
            if created:
                criados += 1
            else:
                existentes += 1

        self.stdout.write(
            self.style.SUCCESS(
                f'Seed concluído: {criados} aluno(s) criado(s), {existentes} já existente(s).'
            )
        )
