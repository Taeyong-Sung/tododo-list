from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Todo
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Add the following import
from django.http import HttpResponse

# Define the views
def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

def todo_index(request):
  return render(request, 'todos/index.html', { 'todos': todos })

def home(request):
  return render(request, 'home.html')

def todo_index(request):
  todos = Todo.objects.all()
  return render(request, 'todos/index.html', { 'todos': todos })

def todo_detail(request, todo_id):
  todo = Todo.objects.get(id=todo_id)
  return render(request, 'todos/detail.html', { 'todo': todo })

class TodoCreate(CreateView):
  model = Todo
  fields = '__all__'

class TodoUpdate(UpdateView):
  model = Todo
  fields = ['description']

class TodoDelete(DeleteView):
  model = Todo
  success_url = '/todos/'