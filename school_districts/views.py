from django.shortcuts import render, redirect
from school_districts.models import StateMap, SchoolDistrict
from django.http import JsonResponse
from django.urls import reverse
from school_districts.forms import DistrictDataUploadForm, MapDataUploadForm
import pandas as pd

def state_view(request):
    context = {}
    context["GeoData"] = StateMap.objects.get(state="PA")
    return render(request, "state.html", context)

def state_map(request):
    state =  StateMap.objects.get(state="PA")
    context = state.map
    return JsonResponse(context)

def state_data(request):
    school_districts = SchoolDistrict.objects.filter(state="PA")
    context = {d.school_district : [d.total_pop, d.poverty_pop] for d in school_districts}
    return JsonResponse(context)

def upload_data(request):
    context = {"form": DistrictDataUploadForm()}
    if request.method == "POST":
        filled = DistrictDataUploadForm(request.POST, request.FILES)
        if filled.is_valid():
            map_file_to_model(request.FILES["state_data"])
            return redirect(reverse("view_state_map"))
    return render(request, "data.html", context)

def upload_map(request):
    context = {"form": MapDataUploadForm()}
    if request.method == "POST":
        filled = MapDataUploadForm(request.POST, request.FILES)
        if filled.is_valid():
            return redirect(reverse("view_state_map"))
    return render(request, "data.html", context)

def map_file_to_model(file_data):
    data = pd.read_excel(file_data)
    for i, row in data[2:].iterrows():
        new = SchoolDistrict.objects.create(
            state=row["Table with column headers in row 3"],
            school_district=row["Unnamed: 3"],
            total_pop=row["Unnamed: 5"],
            poverty_pop=row["Unnamed: 6"]
        )
        new.save()