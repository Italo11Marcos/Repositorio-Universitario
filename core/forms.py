from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

#Cursos Form
class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome']

    def clean_nome(self):
        nome = self.cleaned_data['nome']

        #Checa se o 'nome' não passa de 45 caracteres
        if len(nome) > 45:
            raise ValidationError(_('Limite máx de 45 caracteres'))

        return nome

#Programas Form
class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields = ['nome']

    def clean_nome(self):
        nome = self.cleaned_data['nome']

        #Checa se o 'nome' não passa de 45 caracteres
        if len(nome) > 45:
            raise ValidationError(_('Limite máx de 45 caracteres'))

        return nome

#PalavrasChave Form
class KeyForm(forms.ModelForm):
    class Meta:
        model = PalavrasChave
        fields = ['nome']

    def clean_nome(self):
        nome = self.cleaned_data['nome']

        #Checa se o 'nome' não passa de 10 caracteres
        if len(nome) > 10:
            raise ValidationError(_('Limite máx de 10 caracteres'))

        return nome

#Tipos Documentos Form
class TipoDocumentoForm(forms.ModelForm):
    class Meta:
        model = TipoDocumento
        fields = ['nome']

    def clean_nome(self):
        nome = self.cleaned_data['nome']

        #Checa se o 'nome' não passa de 10 caracteres
        if len(nome) > 10:
            raise ValidationError(_('Limite máx de 10 caracteres'))

        return nome

#Ano Publicacao Form
class AnoPublicacaoForm(forms.ModelForm):
    class Meta:
        model = AnoPublicacao
        fields = ['ano']

    def clean_ano(self):
        ano = self.cleaned_data['ano']

        #Checa se o 'ano' não passa de 10 caracteres
        if int(ano) < 1985:
            raise ValidationError(_('Publicação Inválida'))
        if int(ano) > 2021:
            raise ValidationError(_('Publicação Inválida'))

        return ano

#Orientador Form
class OrientadorForm(forms.ModelForm):
    class Meta:
        model = Orientador
        fields = ['matricula', 'nome']

    def clean_matricula(self):
        matricula = self.cleaned_data['matricula']

        #Checa se a matrícula tem mais de 8 caracteres
        if len(str(matricula)) > 8:
            raise ValidationError(_('Matrícula deve ter 8 caracteres'))

        return matricula

    def clean_nome(self):
        nome = self.cleaned_data['nome']

        #Checa se o nome tem mais de 200 caracteres
        if len(nome) > 200:
            raise ValidationError(_('Nome não deve passar de 200 caracteres'))

        return nome 

#Autor Form
class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['matricula', 'nome']

    def clean_matricula(self):
        matricula = self.cleaned_data['matricula']

        #Checa se a matrícula tem mais de 8 caracteres
        if len(str(matricula)) > 8:
            raise ValidationError(_('Matrícula deve ter 8 caracteres'))

        return matricula

    def clean_nome(self):
        nome = self.cleaned_data['nome']

        #Checa se o nome tem mais de 200 caracteres
        if len(nome) > 200:
            raise ValidationError(_('Nome não deve passar de 200 caracteres'))

        return nome

#Documento Form
class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['titulo', 'file', 'autor', 'programa', 'orientador', 'keys', 'ano', 'tipo']

    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
    
        #Checa se o Documento tem mais de 200 aracteres
        if len(str(titulo)) > 200:
            raise ValidationError(_('Título deve ter menos de 200 caracteres'))

        return titulo

        