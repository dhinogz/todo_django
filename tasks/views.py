from django.shortcuts import render
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required

@login_required
def todo_view(request):

    context = {}

    return TemplateResponse(request, 'todo.html', context)
