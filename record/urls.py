from django.urls import path
from . import views

urlpatterns = [
    path('records', views.RecordsListView.as_view(), name="record.list"),
    #
    path('records/<int:pk>', views.RecordsDetailView.as_view(), name="records.detail"),
    path('records/<int:pk>/edit', views.RecordsUpdateView.as_view(), name="records.update"),
    path('records/new', views.RecordsCreateView.as_view(), name="records.new"),
    path('records/<int:pk>/delete', views.RecordsDeleteView.as_view(), name="records.delete"),
]