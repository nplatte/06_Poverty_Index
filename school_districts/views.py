from django.shortcuts import render
from school_districts.models import StateMap

def state_view(request):
    context = {}
    context["GeoData"] = StateMap.objects.get(state="PA")
    return render(request, "state.html", context)
