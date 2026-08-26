from django.contrib import admin
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import path, include

from aluno.models import Aluno
from core.views import home

admin.site.site_header = 'FEPI — Administração Acadêmica'
admin.site.site_title = 'FEPI Admin'
admin.site.index_title = 'Cartão de Identidade Acadêmica'
admin.site.site_url = '/'


def fepi_admin_has_permission(request):
    return True


def fepi_admin_login(request, extra_context=None):
    return redirect('home')


def _patch_admin_permissions():
    def allow(_request, _obj=None):
        return True

    for model_admin in admin.site._registry.values():
        model_admin.has_module_permission = allow
        model_admin.has_view_permission = allow
        model_admin.has_add_permission = allow
        model_admin.has_change_permission = allow
        model_admin.has_delete_permission = allow


_admin_index = admin.site.index


def fepi_admin_index(request, extra_context=None):
    extra_context = extra_context or {}
    alunos = Aluno.objects.all()
    extra_context.update({
        'fepi_total_alunos': alunos.count(),
        'fepi_total_usuarios': get_user_model().objects.count(),
        'fepi_total_cursos': alunos.values('curso').distinct().count(),
        'fepi_alunos_recentes': alunos[:8],
    })
    return _admin_index(request, extra_context)


admin.site.has_permission = fepi_admin_has_permission
admin.site.login = fepi_admin_login
admin.site.index = fepi_admin_index
_patch_admin_permissions()

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('aluno/', include('aluno.urls')),
]
