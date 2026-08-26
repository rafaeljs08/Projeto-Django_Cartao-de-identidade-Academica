from django.contrib import admin
from django.utils.html import format_html

from .models import Aluno


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('avatar_display', 'nome', 'curso_badge', 'bio_resumo', 'criado_em')
    search_fields = ('nome', 'curso', 'bio')
    list_filter = ('curso',)
    readonly_fields = ('criado_em',)
    ordering = ('-criado_em',)

    fieldsets = (
        ('Identificação', {
            'fields': ('nome',),
        }),
        ('Perfil acadêmico', {
            'fields': ('curso', 'bio'),
        }),
        ('Registro', {
            'fields': ('criado_em',),
            'classes': ('collapse',),
        }),
    )

    @admin.display(description='')
    def avatar_display(self, obj):
        initial = obj.nome[0].upper() if obj.nome else '?'
        return format_html('<span class="fepi-admin-avatar">{}</span>', initial)

    @admin.display(description='Curso', ordering='curso')
    def curso_badge(self, obj):
        return format_html('<span class="fepi-admin-badge">{}</span>', obj.curso)

    @admin.display(description='Bio')
    def bio_resumo(self, obj):
        if len(obj.bio) <= 60:
            return obj.bio
        return f'{obj.bio[:57]}...'
