from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as loginUser
from django.contrib.auth.decorators import login_required
from .models import *
import json
# from .forms import CutomerSingup, CustomerLogin, CutomerProfileForm, ProductForm, MerchantsProfileForm, RiderProfileForm, UpdatePriceForm
from django.contrib import messages
from django.views import View
from django.db.models import Q
# Create your views here.
def home(request):
    return render(request, 'base.html')

def About(request):
    return render(request, 'about.html')

def project(request):
    return render(request, 'project.html')

def service(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def _404_ (request):
    return render(request, '404.html')