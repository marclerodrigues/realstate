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
    company = get_object_or_404(Company, slug=slug)
    context = {
        "title" : "Company",
        "company" : company
    }
    return render(request, "company_detail.html", context)

def company_update(request, slug=None):
    company = get_object_or_404(Company, slug=slug)
    form = CompanyForm(request.POST or None, instance=company)
    if form.is_valid():
        company = form.save(commit=False)
        company.save()
        messages.success(request, "Successfully saved.")
        return HttpResponseRedirect(company.get_absolute_url())

    context = {
        "title" : "Company",
        "company" : company,
        "form" : form
    }

    return render(request, "company_form.html", context)

def company_delete(request, slug=None):
    company = get_object_or_404(Company, slug=slug)
    company.delete()
    messages.success(request, "Successfully deleted.")
    return redirect("companies:list")
