from django.urls import path
from .views import contact_view

urlpatterns = [
    path('', contact_view,name='contact-view'),  # Assuming contact_view is also handled by project_list
]
