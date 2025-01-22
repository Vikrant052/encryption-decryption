from django.urls import path
from .views import AddDetailsView, DecryptDetailsView


urlpatterns = [
    path('add/', AddDetailsView.as_view(), name='add_details'),
    # path('verify/', VerifyDetailsView.as_view(), name='verify_details'),
    path('decrypt/', DecryptDetailsView.as_view(), name='decrypt_details'),
    

            
]
