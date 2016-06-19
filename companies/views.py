from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Company

# Create your views here.
def companies_list(request):
    companies = Company.objects.all()
    context = {
        "title" : "Companies List",
        "companies" : companies
    }
    return render(request, "companies_list.html", context)
