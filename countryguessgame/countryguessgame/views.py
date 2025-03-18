import json
import os
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def load_countries():
    file_path = os.path.join(settings.BASE_DIR, 'myapp/data/countries.json')
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

@login_required
def guess_country(request):
    user_guess = request.GET.get('guess', '').strip().lower()
    countries = load_countries()

    if user_guess in [c.lower() for c in countries]:
        request.user.score += 1
        request.user.save()
        return JsonResponse({"correct": True, "score": request.user.score})
    return JsonResponse({"correct": False, "score": request.user.score})

def home(request):
    return render(request, 'main.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def styles(request):
    return render(request, 'styles.css')