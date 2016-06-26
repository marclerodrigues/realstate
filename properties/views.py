from django.shortcuts import render
from .models import Property
# Create your views here.
def properties_list(request):
    properties = Property.objects.all()
    context = {
        "title" : "Properties",
        "properties" : properties,
    }

    return render(request, "properties_list.html", context)
