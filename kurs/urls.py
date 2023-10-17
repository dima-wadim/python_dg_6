from django.urls import path

from kurs.apps import KursConfig
from kurs.views import BlogListView, BlogDetailView
from django.views.decorators.cache import cache_page
app_name = KursConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('view/<int:pk>/', cache_page(60)(BlogDetailView.as_view()), name='view'),
]