from django.db import models

DISCIPLINE = [
  ("Matemática", "Matemática"),
  ("Português", "Português"),
  ("English", "English"),
  ("História", "História"),
  ("Geografica", "Geografica")
]

class Aluno(models.Model):

  name = models.CharField(max_length=100)
  
  # Este é multipla escolhar - DEU CERTO FAZER COM A CLASS FORM TAMBEM
  gender = models.CharField(max_length = 255, blank=True)

  discipline = models.CharField(max_length=70, choices=DISCIPLINE)

  def __str__(self):
    return self.name