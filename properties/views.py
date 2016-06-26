from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Property
from .forms import PropertyForm
# Create your views here.
def properties_list(request):
    properties = Property.objects.all()
    context = {
        "title" : "Properties",
        "properties" : properties,
    }

    return render(request, "properties_list.html", context)

def property_create(request):
    form = PropertyForm(request.POST or None)
    if form.is_valid():
        property = form.save(commit=False)
        property.save()
        messages.success(request, "Property successfully created.")
        return HttpResponseRedirect(property.get_absolute_url())

    context = {
        "form" : form
    }

    return render(request, "property_form.html", context)

def property_detail(request, slug=None):
    property = get_object_or_404(Property, slug=slug)
    context = {
        "property" : property
    }

    return render(request, "property_detail.html", context)

def property_update(request, slug=None):
    property = get_object_or_404(Property, slug=slug)
    form = PropertyForm(request.POST or None, instance=property)
    if form.is_valid():
        property = form.save(commit=False)
        property.save()
        messages.success(request, "Property successfully saved.")
        return HttpResponseRedirect(property.get_absolute_url())

    context = {
        "property" : property,
        "form" : form,
    }

    return render(request, "property_form.html", context)

def property_delete(request, slug=None):
    property = get_object_or_404(Property, slug=slug)
    property.delete()
    messages.success(request, "Successfully deleted.")
    return redirect("properties:list")
