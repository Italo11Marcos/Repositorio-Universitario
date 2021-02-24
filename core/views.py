from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, ListView, View
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.
# Site Views
def SiteView(request):

    documentos = 0
    
    if request.method == 'POST':
        titulo = request.POST.get('titulo', False)
        autor = request.POST.get('autor', False)
        programa = request.POST.get('programa', False)
        orientador = request.POST.get('orientador', False)
        tipo = request.POST.get('tipo', False)
        ano = request.POST.get('ano', False)
        keys = request.POST.get('keys', False)

        filters = {
            key: value
            for key, value in request.POST.items()
            if key in ['programa', 'tipo', 'ano', 'keys']
        }

        #print('{} \n {} \n {} \n {} \n {} \n {} \n {}'.format(titulo, autor, programa, orientador, tipo, ano, keys))
        #documentos = Documento.objects.filter(titulo__contains=titulo).filter(programa=programa).filter(tipo=tipo).filter(ano=ano).filter(keys=keys)
        documentos = Documento.objects.filter(titulo__contains=titulo).filter(**filters)

    context = {
        'autors' : Autor.objects.order_by('?').all(),
        'programas' : Programa.objects.order_by('?').all(),
        'orientadors' : Orientador.objects.order_by('?').all(),
        'tipos' : TipoDocumento.objects.order_by('?').all(),
        'anos' : AnoPublicacao.objects.order_by('?').all(),
        'keys' : PalavrasChave.objects.order_by('?').all(),
        'documentos': documentos
    }

    return render(request, 'site/index.html', context)

# Panel View
class PanelView(UserPassesTestMixin, TemplateView):
    login_url = 'login'
    template_name = 'panel/panel/index.html'

    def test_func(self):
        if self.request.user.is_staff:
            return True
        else:
            raise Http404('Você não tem permissão')

# Cursos Views
class ListCursoView(ListView):
    model = Curso
    template_name = 'panel/cursos/index.html'

    def test_func(self):
        if self.request.user.is_staff:
            return True
        else:
            raise Http404('Você não tem permissão')

    def get_context_data(self, **kwargs):
        context = super(ListCursoView, self).get_context_data(**kwargs)
        context['cursos'] = Curso.objects.order_by('?').all()
        return context

class CreateCursoView(CreateView):
    form_class = CursoForm
    success_url = reverse_lazy('curso-index')

    def form_valid(self, form, *args, **kwargs):
        messages.success(self.request, 'Curso Cadastrado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Tivemos algum problema')
        return super().form_valid(form)

class DetailCursoView(DetailView):
    model = Curso
    template_name = 'panel/cursos/detail.html'
    context_object_name = 'curso'

class UpdateCursoView(UpdateView):
    model = Curso
    fields = ['nome']
    success_url = reverse_lazy('curso-index')

    def form_valid(self, form, *args, **kwargs):
        messages.success(self.request, 'Curso editado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Tivemos algum problema')
        return super().form_valid(form)

class DeleteCursoView(DeleteView):
    model = Curso
    success_url = reverse_lazy('curso-index')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(self.request, 'Curso excluído com sucesso!')
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)

#Programas Views
class ListProgramaView(ListView):
    model = Programa
    template_name = 'panel/programas/index.html'

    def get_context_data(self, **kwargs):
        context = super(ListProgramaView, self).get_context_data(**kwargs)
        context['programas'] = Programa.objects.order_by('?').all()
        return context

class CreateProgramaView(CreateView):
    form_class = ProgramaForm
    success_url = reverse_lazy('programa-index')

    def form_valid(self, form, *args, **kwargs):
        messages.success(self.request, 'Programa Cadastrado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Tivemos algum problema')
        return super().form_valid(form)

class DetailProgramaView(DetailView):
    model = Programa
    template_name = 'panel/programas/detail.html'
    context_object_name = 'programa'

class UpdateProgramaView(UpdateView):
    model = Programa
    fields = ['nome']
    success_url = reverse_lazy('programa-index')

    def form_valid(self, form, *args, **kwargs):
        messages.success(self.request, 'Programa editado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Tivemos algum problema')
        return super().form_valid(form)

class DeleteProgramaView(DeleteView):
    model = Programa
    success_url = reverse_lazy('programa-index')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(self.request, 'Programa excluído com sucesso!')
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)

#Palavras Chave Views
class ListKeyView(ListView):
    model = PalavrasChave
    template_name = 'panel/wordkeys/index.html'

    def get_context_data(self, **kwargs):
        context = super(ListKeyView, self).get_context_data(**kwargs)
        context['keys'] = PalavrasChave.objects.order_by('?').all()
        return context

class CreateKeyView(CreateView):
    form_class = KeyForm
    success_url = reverse_lazy('key-index')

    def form_valid(self, form, *args, **kwargs):
        messages.success(self.request, 'Palavra Chave Cadastrado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Tivemos algum problema')
        return super().form_valid(form)

class DetailKeyView(DetailView):
    model = PalavrasChave
    template_name = 'panel/wordkeys/detail.html'
    context_object_name = 'key'

class UpdateKeyView(UpdateView):
    model = PalavrasChave
    fields = ['nome']
    success_url = reverse_lazy('key-index')

    def form_valid(self, form, *args, **kwargs):
        messages.success(self.request, 'Palavra Chave editado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Tivemos algum problema')
        return super().form_valid(form)

class DeleteKeyView(DeleteView):
    model = PalavrasChave
    success_url = reverse_lazy('key-index')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(self.request, 'Palavra Chave excluída com sucesso!')
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)

#Tipos de Documonto Views
class ListTipoDocumentoView(ListView):
    model = TipoDocumento
    template_name = 'panel/tipodocumentos/index.html'

    def get_context_data(self, **kwargs):
        context = super(ListTipoDocumentoView, self).get_context_data(**kwargs)
        context['tipos'] = TipoDocumento.objects.order_by('?').all()
        return context

class CreateTipoDocumentoView(CreateView):
    form_class = TipoDocumentoForm
    success_url = reverse_lazy('tipo-index')

    def form_valid(self, form, *args, **kwargs):
        messages.success(self.request, 'Tipo de Documento Cadastrado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Tivemos algum problema')
        return super().form_valid(form)

class DetailTipoDocumentoView(DetailView):
    model = TipoDocumento
    template_name = 'panel/tipodocumentos/detail.html'
    context_object_name = 'tipo'

class UpdateTipoDocumentoView(UpdateView):
    model = TipoDocumento
    fields = ['nome']
    success_url = reverse_lazy('tipo-index')

    def form_valid(self, form, *args, **kwargs):
        messages.success(self.request, 'Tipo de Documento editado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Tivemos algum problema')
        return super().form_valid(form)

class DeleteTipoDocumentoView(DeleteView):
    model = TipoDocumento
    success_url = reverse_lazy('tipo-index')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(self.request, 'Tipo de Documento excluída com sucesso!')
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)

#Ano Publicação Views
class ListAnoPublicacaoView(ListView):
    model = AnoPublicacao
    template_name = 'panel/anopublicacao/index.html'

    def get_context_data(self, **kwargs):
        context = super(ListAnoPublicacaoView, self).get_context_data(**kwargs)
        context['publicacao'] = AnoPublicacao.objects.order_by('?').all()
        return context

class CreateAnoPublicacaoView(CreateView):
    form_class = AnoPublicacaoForm
    success_url = reverse_lazy('publicacao-index')

    def form_valid(self, form, *args, **kwargs):
        messages.success(self.request, 'Ano Publicação Cadastrado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Tivemos algum problema')
        return super().form_valid(form)

class DetailAnoPublicacaoView(DetailView):
    model = AnoPublicacao
    template_name = 'panel/anopublicacao/detail.html'
    context_object_name = 'publicacao'

class UpdateAnoPublicacaoView(UpdateView):
    model = AnoPublicacao
    fields = ['ano']
    success_url = reverse_lazy('publicacao-index')

    def form_valid(self, form, *args, **kwargs):
        messages.success(self.request, 'Ano Publicação editado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Tivemos algum problema')
        return super().form_valid(form)

class DeleteAnoPublicacaoView(DeleteView):
    model = AnoPublicacao
    success_url = reverse_lazy('publicacao-index')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(self.request, 'Ano Publicação excluída com sucesso!')
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)

#Orientador Views
class ListOrientadorView(ListView):
    model = Orientador
    template_name = 'panel/orientador/index.html'

    def get_context_data(self, **kwargs):
        context = super(ListOrientadorView, self).get_context_data(**kwargs)
        context['orientador'] = Orientador.objects.order_by('?').all()
        return context

class CreateOrientadorView(CreateView):
    form_class = OrientadorForm
    success_url = reverse_lazy('orientador-index')

    def form_valid(self, form, *args, **kwargs):
        messages.success(self.request, 'Ano Publicação Cadastrado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Tivemos algum problema')
        return super().form_valid(form)

class DetailOrientadorView(DetailView):
    model = Orientador
    template_name = 'panel/orientador/detail.html'
    context_object_name = 'orientador'

class UpdateOrientadorView(UpdateView):
    model = Orientador
    fields = ['matricula', 'nome']
    success_url = reverse_lazy('orientador-index')

    def form_valid(self, form, *args, **kwargs):
        messages.success(self.request, 'Orientador(a) editado(a) com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Tivemos algum problema')
        return super().form_valid(form)

class DeleteOrientadorView(DeleteView):
    model = Orientador
    success_url = reverse_lazy('orientador-index')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(self.request, 'Orientador(a) excluído(a) com sucesso!')
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)

#Autor Views
class ListAutorView(ListView):
    model = Autor
    template_name = 'panel/autor/index.html'

    def get_context_data(self, **kwargs):
        context = super(ListAutorView, self).get_context_data(**kwargs)
        context['autor'] = Autor.objects.order_by('?').all()
        return context

class CreateAutorView(CreateView):
    form_class = AutorForm
    success_url = reverse_lazy('autor-index')

    def form_valid(self, form, *args, **kwargs):
        messages.success(self.request, 'Autor Cadastrado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Tivemos algum problema')
        return super().form_valid(form)

class DetailAutorView(DetailView):
    model = Autor
    template_name = 'panel/autor/detail.html'
    context_object_name = 'autor'

class UpdateAutorView(UpdateView):
    model = Autor
    fields = ['matricula', 'nome']
    success_url = reverse_lazy('autor-index')

    def form_valid(self, form, *args, **kwargs):
        messages.success(self.request, 'Autor(a) editado(a) com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Tivemos algum problema')
        return super().form_valid(form)

class DeleteAutorView(DeleteView):
    model = Autor
    success_url = reverse_lazy('autor-index')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(self.request, 'Autor(a) excluído(a) com sucesso!')
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)

#Documento Views
class ListDocumentoView(ListView):
    model = Documento
    template_name = 'panel/documento/index.html'

    def get_context_data(self, **kwargs):
        context = super(ListDocumentoView, self).get_context_data(**kwargs)
        context['documentos'] = Documento.objects.order_by('?').all()
        context['autors'] = Autor.objects.order_by('?').all()
        context['programas'] = Programa.objects.order_by('?').all()
        context['orientadors'] = Orientador.objects.order_by('?').all()
        context['tipos'] = TipoDocumento.objects.order_by('?').all()
        context['anos'] = AnoPublicacao.objects.order_by('?').all()
        context['keys'] = PalavrasChave.objects.order_by('?').all()
        return context

class CreateDocumentoView(CreateView):
    model = Documento
    form_class = DocumentoForm
    success_url = reverse_lazy('documento-index')

    def form_valid(self, form, *args, **kwargs):
        messages.success(self.request, 'Documento Cadastrado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Tivemos algum problema')
        return super().form_valid(form)

class DetailDocumentoView(DetailView):
    model = Documento
    template_name = 'panel/documento/detail.html'
    context_object_name = 'documento'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['autors'] = Autor.objects.order_by('?').all()
        context['programas'] = Programa.objects.order_by('?').all()
        context['orientadors'] = Orientador.objects.order_by('?').all()
        context['tipos'] = TipoDocumento.objects.order_by('?').all()
        context['anos'] = AnoPublicacao.objects.order_by('?').all()
        context['keys'] = PalavrasChave.objects.order_by('?').all()
        return context

class UpdateDocumentoView(UpdateView):
    model = Documento
    fields = ['titulo', 'file', 'autor', 'programa', 'orientador', 'keys', 'ano', 'tipo']
    success_url = reverse_lazy('documento-index')

    def form_valid(self, form, *args, **kwargs):
        messages.success(self.request, 'Documento(a) editado(a) com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Tivemos algum problema')
        return super().form_valid(form)

class DeleteDocumentoView(DeleteView):
    model = Documento
    success_url = reverse_lazy('documento-index')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(self.request, 'Documento(a) excluído(a) com sucesso!')
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)

