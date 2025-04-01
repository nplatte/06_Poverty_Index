from django.urls import path
import school_districts.views as school_views

urlpatterns = [
    path("PA", school_views.state_view)
]