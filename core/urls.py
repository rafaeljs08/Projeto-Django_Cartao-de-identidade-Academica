from django.contrib import admin
from django.urls import path, include

from core.views import home

admin.site.site_header = 'FEPI — Administração Acadêmica'
admin.site.site_title = 'FEPI Admin'
admin.site.index_title = 'Cartão de Identidade Acadêmica'
admin.site.site_url = '/'

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('aluno/', include('aluno.urls')),
]
