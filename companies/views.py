from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Company
from .forms import CompanyForm

# Create your views here.
def companies_list(request):
    companies = Company.objects.all()
    context = {
        "title" : "Companies List",
        "companies" : companies
    }
    return render(request, "companies_list.html", context)

def company_create(request):
    form = CompanyForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Company successfully created.")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form": form,
    }
    return render(request, "company_form.html", context)

def company_detail(request, slug=None):
    instance = get_object_or_404(Company, slug=slug)
    context = {
        "title" : "Company",
        "object" : instance
    }
    return render(request, "company_detail.html", context)
