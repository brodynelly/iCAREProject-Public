from django.contrib import admin
from django.urls import path, include
from .views import PatientCreateView, PatientListView, PatientDeleteView, PatientDetailView, PatientUpdateView, ICareBoardView, MyBoardView

urlpatterns = [
    path('list/', PatientListView.as_view(), name='patient_list'),
    path('add/', PatientCreateView.as_view(), name='patient_add'),
    path('my_board/', MyBoardView.as_view(), name='my_board'),
    path('icare_board/', ICareBoardView.as_view(), name='icare_board'),
    path('icare_board/<str:geocode_id>/', ICareBoardView.as_view(), name='icare_board'),
    path('<str:pk>/', PatientDetailView.as_view(), name='patient_detail'),
    path('<str:pk>/edit/', PatientUpdateView.as_view(), name='patient_edit'),
    path('<str:pk>/delete/', PatientDeleteView.as_view(), name='patient_delete'),
]
