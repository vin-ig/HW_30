from django.conf.urls.static import static
from django.urls import path

from HW_28 import settings
from ad import views

urlpatterns = [
	path('', views.AdListView.as_view()),
	path('<int:pk>/', views.AdDetailView.as_view()),
	path('create/', views.AdCreateView.as_view()),
	path('<int:pk>/update/', views.AdUpdateView.as_view()),
	path('<int:pk>/image/', views.AdImageView.as_view()),
	path('<int:pk>/delete/', views.AdDeleteView.as_view()),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
