from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView
from django.views.generic.edit import (
    SingleObjectTemplateResponseMixin,
    ModelFormMixin,
    ProcessFormView
)
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.urls import reverse_lazy
from string import Template
import sqlite3
# Create your views here.
from app.models import Study, School
from app.forms import StudyForm

class IndexView(TemplateView):
    template_name = 'app/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['studies'] = Study.objects.all()
        return context

class StudyListView(ListView):
    model = Study
    context_object_name = 'studies'
    template_name='app/study-list.html'

class StudyDeleteView(DeleteView):
    model = Study
    context_object_name = 'study'
    template_name = 'app/study-delete.html'
    success_url = reverse_lazy('app:list')
    
    def get_success_url(self):
        messages.info(self.request, 'Vous venez de supprimer l\'étudiant {}'.format(self.object))
        return self.success_url

class BaseCreateUpdateView(ModelFormMixin, ProcessFormView):
    
    def get(self, request, *args, **kwargs):
        #pk = 
        self.object = None
        if kwargs.get('pk'):
            self.object = self.get_object()
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        self.object = None
        print(kwargs)
        if kwargs.get('pk'):
            self.object = self.get_object()
        return super().post(request, *args, **kwargs)
        

class StudyCreateUpdateView(SingleObjectTemplateResponseMixin, BaseCreateUpdateView):
    model = Study
    context_object_name = 'study'
    template_name = 'app/study-edit.html'
    form_class = StudyForm
    title = Template('$title d\'un étudiant')
    #fields = ('first_name', 'last_name', 'serial_number', 'school')
    success_url = reverse_lazy('app:list')
    '''
    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def form_valid(self, form):
        #school = form.instance.school_
        data = form.cleaned_data
        new_school = School(
            code = data.get('code'),
            label = data.get('school_name'),
            post_box = data.get('boite_postal')
        )
        new_school.save()
        #print(form.instance.school.get(pk=5))
        #form.instance.school.add(new_school)
        form.save()
        return super(StudyCreateUpdateView, self).form_valid(form)
    '''
    

    def get_context_data(self, **kwargs):
        context = super(StudyCreateUpdateView, self).get_context_data(**kwargs)
        if self.object:
            self.title = self.title.substitute(title='Edition')
        else:
            self.title = self.title.substitute(title='Ajout')
        ctx_data = {
            'title':self.title,
            'action': 'Enregister'
        }
        context['context'] = ctx_data
        return context

class GestionBD(object):
    requete = '''
    
    '''
    def __init__(self):
        self.createDB(self.requete)
        cursor

    def createDB(self, requete):
        pass
    
    def insertIntoTable(self, requete):
        pass
    
    def deleteIntoTable(self, requete):
        pass
    def updateIntoTable(self, requete):
        pass