from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Todo
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Add the following import
from django.http import HttpResponse

# Define the views
def about(request):
  return render(request, 'about.html')

def home(request):
  return render(request, 'home.html')

@login_required
def todo_index(request):
  todos = Todo.objects.filter(user=request.user)
  return render(request, 'todos/index.html', { 'todos': todos })

@login_required
def todo_detail(request, todo_id):
  todo = Todo.objects.get(id=todo_id)
  return render(request, 'todos/detail.html', { 'todo': todo })

class TodoCreate(LoginRequiredMixin, CreateView):
  model = Todo
  fields = ['name', 'description']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
  def get_success_url(self):
    return '/todos/'

class TodoUpdate(LoginRequiredMixin, UpdateView):
  model = Todo
  fields = ['description']

class TodoDelete(LoginRequiredMixin, DeleteView):
  model = Todo
  success_url = '/todos/'

class Home(LoginView):
  template_name = 'home.html'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('todo-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  return render(request, 'signup.html', {
    'form': form,
    'error_message': error_message
  })
  