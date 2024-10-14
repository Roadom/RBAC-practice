from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.http.response import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import StudentAssessmentRecord
from .forms import StudentAssessmentRecordForm

class RecordsListView(LoginRequiredMixin, ListView):
    model = StudentAssessmentRecord
    context_object_name = "grades"
    template_name = "record/grades_list.html"
    login_url="/login"
    
    def get_queryset(self):
        if self.request.user.groups.filter(name__in=['Teacher', 'Principal', 'Admin']).exists():
            return StudentAssessmentRecord.objects.all()
        
        return StudentAssessmentRecord.objects.filter(student=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        user = self.request.user
        context['is_teacher'] = user.groups.filter(name='Teacher').exists()
        context['is_principal'] = user.groups.filter(name='Principal').exists()
        return context
    
class RecordsDetailView(DetailView):
    model = StudentAssessmentRecord
    template_name = "record/grades_detail.html"
    context_object_name = "grade"
    
    def get_queryset(self):
        if self.request.user.groups.filter(name__in=['Teacher', 'Principal']).exists():
            return StudentAssessmentRecord.objects.all()
        
        return StudentAssessmentRecord.objects.filter(student=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        user = self.request.user
        context['is_teacher'] = user.groups.filter(name='Teacher').exists()
        context['is_principal'] = user.groups.filter(name='Principal').exists()
        return context
    
class RecordsCreateView(CreateView):
    model = StudentAssessmentRecord
    success_url = '/home'
    form_class = StudentAssessmentRecord
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user 
        self.object.save()
        return HttpResponseRedirect(self.get_success_url()) 
    
    def get_queryset(self):
        if self.request.user.groups.filter(name__in=['Teacher', 'Principal']).exists():
            return StudentAssessmentRecord.objects.all()
        
        return StudentAssessmentRecord.objects.filter(student=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        user = self.request.user
        context['is_teacher'] = user.groups.filter(name='Teacher').exists()
        context['is_principal'] = user.groups.filter(name='Principal').exists()
        return context
    
class RecordsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = StudentAssessmentRecord
    template_name = "record/grades_form.html"
    success_url = '/'
    form_class = StudentAssessmentRecordForm
    
    def test_func(self):
        # Only allow teachers or principals to edit
        return self.request.user.groups.filter(name__in=['Teacher', 'Principal']).exists()

class RecordsDeleteView(DeleteView):
    model = StudentAssessmentRecord
    template_name = "record/grades_delete.html"
    success_url = '/home'
    
    def get_queryset(self):
        if self.request.user.groups.filter(name__in=['Teacher', 'Principal']).exists():
            return StudentAssessmentRecord.objects.all()
        
        else:
            raise PermissionDenied
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        user = self.request.user
        context['is_teacher'] = user.groups.filter(name='Teacher').exists()
        context['is_principal'] = user.groups.filter(name='Principal').exists()
        return context

