from django.shortcuts import render

def state_view(request):
    context = {}
    return render(request, "state.html", context)
