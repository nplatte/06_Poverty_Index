from django.urls import path
import school_districts.views as school_views

urlpatterns = [
    path("PA", school_views.state_view, name="school_poverty_state_view"),
    path("PA/map", school_views.state_map, name="state_map"),
    path("add_data", school_views.upload_data_view, name="add_state_data"),
    path("PA/data", school_views.state_data, name="get_state_data") 
]