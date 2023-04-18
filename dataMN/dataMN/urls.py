from django.urls import path
from appDATA import views
from appDATA.views import DownloadFileView

urlpatterns = [
    path('download/', DownloadFileView.as_view(), name='download_file'),
    path('', views.index, name='index'),
    path('autoZ/', views.autoZ, name='autoZ'),
]
