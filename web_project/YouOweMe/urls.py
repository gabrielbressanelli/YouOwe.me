from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_view, name="index_view"),
    path("debt", views.debt, name="debt"),
    path("total_paid", views.total_paid, name="total_paid")
]