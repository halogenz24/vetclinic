from django.urls import path
from .views import *
from appointment.views import *

app_name = "accounts"

urlpatterns = [
    path('patient/register', RegisterPatientView.as_view(), name='patient-register'),
    path('patient/profile/update/', EditPatientProfileView.as_view(), name='patient-profile-update'),
    # path('patient/profile/update/', EditPatientProfileView.as_view(), name='view-patient-list'),
    # path('vet/accounts/patient/', PatientListUserView.as_view(), name='view-patient-list'),
    path('vet/register', RegisterVetView.as_view(), name='vet-register'),
    path('vet/profile/update/', EditVetProfileView.as_view(), name='vet-profile-update'),


    path('view_user/register', RegisterView.as_view(), name='viewer-register'),
    path('patient/profile/update/', EditViewProfileView.as_view(), name='view-profile-update'),



    path('login', Login_clinic.as_view(), name='login'),
    path('logout', Logout_clinic.as_view(), name='logout'),
]