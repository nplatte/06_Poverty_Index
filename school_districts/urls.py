from django.urls import path
import school_districts.views as school_views

urlpatterns = [
    path("PA", school_views.state_view, name="view_state_map"),
    path("PA/map", school_views.state_map, name="get_state_map"),
    path("add_data", school_views.upload_data, name="add_state_data"),
    path("PA/data", school_views.state_data, name="get_state_data"),
    path("add_map", school_views.upload_map, name="add_state_map") 
]