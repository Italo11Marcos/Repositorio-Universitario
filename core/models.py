from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser, BaseUserManager
import os
import random

def path_and_rename(instance, filename):
    path = "documentos/pdfs/"
    ext = filename.split('.')[-1]
    original = filename.split('.')[0]
    rand = random.randint(11111111,99999999)
    filename = '{}+{}.{}'.format(original, rand, ext)
    return os.path.join(path, filename)


class UsuarioManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        # extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True')

        return self._create_user(email, password, **extra_fields)

class CustomUsuario(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    matricula = models.CharField(max_length=8)
    is_staff = models.BooleanField('Membro da equipe', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'matricula']

    def __str__(self):
        return self.email

    objects = UsuarioManager()
    
class Curso(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=45)

    def __str__(self):
        return self.nome

class Programa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=45)

    def __str__(self):
        return self.nome

class PalavrasChave(models.Model):
    nome = models.CharField(max_length=10)

    def __str__(self):
        return self.nome

class TipoDocumento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=10)

    def __str__(self):
        return self.nome

class Orientador(models.Model):
    matricula = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class AnoPublicacao(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ano = models.CharField(max_length=4, unique=True)

    def __str__(self):
        return self.ano

class Autor(models.Model):
    matricula = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Documento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=200)
    file = models.FileField(upload_to=path_and_rename)
    autor = models.ManyToManyField(Autor)
    programa = models.ForeignKey(Programa, on_delete=models.SET_NULL, null=True)
    orientador = models.ForeignKey(Orientador, on_delete=models.SET_NULL, null=True)
    keys = models.ManyToManyField(PalavrasChave)
    ano = models.ForeignKey(AnoPublicacao, on_delete=models.SET_NULL, null=True)
    tipo = models.ForeignKey(TipoDocumento, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo



