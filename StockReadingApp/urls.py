"""StockReadingApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from stockreading.views import (
    CurrentListingView,
    HistoricListingView,
    StockReadingCreateView,
)

urlpatterns = [
    path('', CurrentListingView.as_view(), name='current-listing'),
    path('historic/', HistoricListingView.as_view(), name='historic-listing'),
    path('create/', StockReadingCreateView.as_view(success_url="?success=1"), name='create-reading'),
    path('admin/', admin.site.urls),
    path('api/', include('stockreading.api.urls')),
]
