from django.shortcuts import render


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

class Todo:
  def __init__(self, name, description):
    self.name = name
    self.description = description

todos = [
  Todo('Kitchen', 'Clean Stove',),
]