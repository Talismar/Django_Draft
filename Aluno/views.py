from django.shortcuts import render, redirect
from .models import Aluno
from .form import AlunoForm


def get_post_method(request):

  if request.method == "POST":

    form = AlunoForm(request.POST)

    if form.is_valid():

      alter_form = form.save(commit=False)
      alter_form.gender = " | ".join(dict(request.POST)['gender'])
      
      alter_form.save()
      
      return redirect("/")

  forms = AlunoForm
  aluno = Aluno.objects.all() 

  return render(request, "get.html", {"forms": forms, "aluno": aluno})