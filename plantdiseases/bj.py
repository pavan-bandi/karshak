from django.db import models
from .models import bacterialdiseases,fungaldiseases
bacs=bacterialdiseases.objects.all()


for i in bacs:
    print(bacs.disease)