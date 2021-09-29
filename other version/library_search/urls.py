from django.urls.conf import path
from . import views

app_name='library_search'

urlpatterns = [
    path("library_search/", views.lsblank, name="LSblank"),
    path("location_processing/", views.location_processing, name="location_processing" ),
    path("library_search/libid<int:id>",views.libraryDetails,name="library_details")
    # path("process_loc/", views.process_loc, name="process_loc" )
]