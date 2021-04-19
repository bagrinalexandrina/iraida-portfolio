from django.shortcuts import render
from .models import Project
def index(request):
    all_entries = Project.objects.all()
    print(all_entries)
    context = { 'projects' : all_entries }
    return render(request, 'index.html', context)

