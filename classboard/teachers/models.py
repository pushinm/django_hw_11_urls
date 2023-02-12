import imp
from django.db import models
from .validators.validators import validate_age
from persons.models import PersonAbstract
# from classes.models import Class
# from classboard.models import Classboard
# from classboard.models import Classboard
# Create your models here.

class Teacher(PersonAbstract):
    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'
        
        ordering = ['first_name', 'last_name']
        
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
        
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('teachers:view_teachers', kwargs={'pk': str(self.pk)})