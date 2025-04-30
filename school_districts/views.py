from django.shortcuts import render, redirect
from school_districts.models import StateMap
from django.http import JsonResponse
from django.urls import reverse
from school_districts.forms import DistrictDataUploadForm

def state_view(request):
    context = {}
    context["GeoData"] = StateMap.objects.get(state="PA")
    return render(request, "state.html", context)

def state_map(request):
    state =  StateMap.objects.get(state="PA")
    context = state.map
    return JsonResponse(context)

def upload_data_view(request):
    context = {"form": DistrictDataUploadForm()}
    if request.method == "POST":
        filled = DistrictDataUploadForm(request.POST, request.FILES)
        if filled.is_valid():
            return redirect(reverse("school_poverty_state_view"))
    return render(request, "data.html", context)
