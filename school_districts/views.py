from django.shortcuts import render
from school_districts.models import StateMap
from django.http import JsonResponse

def state_view(request):
    context = {}
    context["GeoData"] = StateMap.objects.get(state="PA")
    return render(request, "state.html", context)

def state_map(request):
    state =  StateMap.objects.get(state="PA")
    context = state.map
    return JsonResponse(context)
