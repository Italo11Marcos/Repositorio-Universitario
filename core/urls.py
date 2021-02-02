from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', SiteView.as_view(), name='site'),
    path('admin/panel', PanelView.as_view(), name='panel'),
    #URLs Auth
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    #path('registrar/', CreateUserView.as_view(), name='registrar'),
    # path('registrar/', cadastro, name='registrar'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #URLs Cursos
    path('admin/panel/cursos/', ListCursoView.as_view(), name='curso-index'),
    path('admin/panel/cursos/cadastrar', CreateCursoView.as_view(), name='curso-create'),
    path('admin/panel/cursos/<uuid:pk>', DetailCursoView.as_view(), name='curso-detail'),
    path('admin/panel/cursos/atualizar/<uuid:pk>', UpdateCursoView.as_view(), name='curso-update'),
    path('admin/panel/cursos/deletar/<uuid:pk>', DeleteCursoView.as_view(), name='curso-delete'),
    #URLs Programas
    path('admin/panel/programas/', ListProgramaView.as_view(), name='programa-index'),
    path('admin/panel/programas/cadastrar', CreateProgramaView.as_view(), name='programa-create'),
    path('admin/panel/programas/<uuid:pk>', DetailProgramaView.as_view(), name='programa-detail'),
    path('admin/panel/programas/atualizar/<uuid:pk>', UpdateProgramaView.as_view(), name='programa-update'),
    path('admin/panel/programas/deletar/<uuid:pk>', DeleteProgramaView.as_view(), name='programa-delete'),
    #URLs Palavras Chave
    path('admin/panel/keys/', ListKeyView.as_view(), name='key-index'),
    path('admin/panel/keys/cadastrar', CreateKeyView.as_view(), name='key-create'),
    path('admin/panel/keys/<int:pk>', DetailKeyView.as_view(), name='key-detail'),
    path('admin/panel/keys/atualizar/<int:pk>', UpdateKeyView.as_view(), name='key-update'),
    path('admin/panel/keys/deletar/<int:pk>', DeleteKeyView.as_view(), name='key-delete'),
    #URLs Tipo Documentos
    path('admin/panel/tipos/', ListTipoDocumentoView.as_view(), name='tipo-index'),
    path('admin/panel/tipos/cadastrar', CreateTipoDocumentoView.as_view(), name='tipo-create'),
    path('admin/panel/tipos/<uuid:pk>', DetailTipoDocumentoView.as_view(), name='tipo-detail'),
    path('admin/panel/tipos/atualizar/<uuid:pk>', UpdateTipoDocumentoView.as_view(), name='tipo-update'),
    path('admin/panel/tipos/deletar/<uuid:pk>', DeleteTipoDocumentoView.as_view(), name='tipo-delete'),
    #URLs Ano Publicação
    path('admin/panel/ano-publicacao/', ListAnoPublicacaoView.as_view(), name='publicacao-index'),
    path('admin/panel/ano-publicacao/cadastrar', CreateAnoPublicacaoView.as_view(), name='publicacao-create'),
    path('admin/panel/ano-publicacao/<uuid:pk>', DetailAnoPublicacaoView.as_view(), name='publicacao-detail'),
    path('admin/panel/ano-publicacao/atualizar/<uuid:pk>', UpdateAnoPublicacaoView.as_view(), name='publicacao-update'),
    path('admin/panel/ano-publicacao/deletar/<uuid:pk>', DeleteAnoPublicacaoView.as_view(), name='publicacao-delete'),
    #URLs Orientador
    path('admin/panel/orientador/', ListOrientadorView.as_view(), name='orientador-index'),
    path('admin/panel/orientador/cadastrar', CreateOrientadorView.as_view(), name='orientador-create'),
    path('admin/panel/orientador/<int:pk>', DetailOrientadorView.as_view(), name='orientador-detail'),
    path('admin/panel/orientador/atualizar/<int:pk>', UpdateOrientadorView.as_view(), name='orientador-update'),
    path('admin/panel/orientador/deletar/<int:pk>', DeleteOrientadorView.as_view(), name='orientador-delete'),
    #URLs Autor
    path('admin/panel/autor/', ListAutorView.as_view(), name='autor-index'),
    path('admin/panel/autor/cadastrar', CreateAutorView.as_view(), name='autor-create'),
    path('admin/panel/autor/<int:pk>', DetailAutorView.as_view(), name='autor-detail'),
    path('admin/panel/autor/atualizar/<int:pk>', UpdateAutorView.as_view(), name='autor-update'),
    path('admin/panel/autor/deletar/<int:pk>', DeleteAutorView.as_view(), name='autor-delete'),
    #URLs Documento
    path('admin/panel/documentos/', ListDocumentoView.as_view(), name='documento-index'),
    path('admin/panel/documentos/cadastrar', CreateDocumentoView.as_view(), name='documento-create'),
    path('admin/panel/documentos/<uuid:pk>', DetailDocumentoView.as_view(), name='documento-detail'),
    path('admin/panel/documentos/atualizar/<uuid:pk>', UpdateDocumentoView.as_view(), name='documento-update'),
    path('admin/panel/documentos/deletar/<uuid:pk>', DeleteDocumentoView.as_view(), name='documento-delete'),
]

