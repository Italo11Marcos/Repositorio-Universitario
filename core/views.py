from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, ListView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.
class PanelView(TemplateView):
    template_name = 'panel/panel/index.html'

# Cursos Views
class ListCursoView(ListView):
    model = Curso
    template_name = 'panel/cursos/index.html'

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
        context['documentos'] = TipoDocumento.objects.order_by('?').all()
        return context

class CreateTipoDocumentoView(CreateView):
    form_class = TipoDocumentoForm
    success_url = reverse_lazy('documento-index')

    def form_valid(self, form, *args, **kwargs):
        messages.success(self.request, 'Tipo de Documento Cadastrado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Tivemos algum problema')
        return super().form_valid(form)

class DetailTipoDocumentoView(DetailView):
    model = TipoDocumento
    template_name = 'panel/tipodocumentos/detail.html'
    context_object_name = 'documento'

class UpdateTipoDocumentoView(UpdateView):
    model = TipoDocumento
    fields = ['nome']
    success_url = reverse_lazy('documento-index')

    def form_valid(self, form, *args, **kwargs):
        messages.success(self.request, 'Tipo de Documento editado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Tivemos algum problema')
        return super().form_valid(form)

class DeleteTipoDocumentoView(DeleteView):
    model = TipoDocumento
    success_url = reverse_lazy('documento-index')

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
