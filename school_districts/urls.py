from django.urls import path
import school_districts.views as school_views

urlpatterns = [
    path("PA", school_views.state_view, name="school_poverty_state_view"),
    path("PA_map", school_views.state_map, name="state_map")
]