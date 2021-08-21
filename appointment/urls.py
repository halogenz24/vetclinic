from django.urls import path
from appointment.views import *
from django.conf import settings
from django.conf.urls.static import static


app_name = 'appointment'

urlpatterns = [

    path('', HomePageView.as_view(), name='home'),
    path('service', ServiceView.as_view(), name='service'),
    path('vet/appointment/create', AppointmentCreateView.as_view(), name='vet-appointment-create'),
    path('vet/appointment/', AppointmentListView.as_view(), name='vet-appointment'),
    path('<pk>/delete/', AppointmentDeleteView.as_view(), name='delete-appointment'),
    path('<pk>/patient/delete', PatientDeleteView.as_view(), name='delete-patient'),
    path('<pk>/patient/', PatientUpdateView.as_view(), name='patient-list'),
    path('patient-take-appointment/<pk>', TakeAppointmentView.as_view(), name='take-appointment'),
    path('search/', SearchView.as_view(), name='search'),
    path('patient/', PatientListView.as_view(), name='patient-list'),
    path('vet/appointment/views',viewlist.as_view(), name='view-list'),
    path('vet/appointment/view-list',viewlistuser.as_view(), name='view-list-user'),
    #path('patient/', PatientListView.as_view(), name='patient-list-view'),
    #path('patients/<int:appointment_id>', PatientPerAppointmentView.as_view(), name='patient-list'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
