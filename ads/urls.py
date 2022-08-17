from django.urls import path

from ads import views

urlpatterns = [
	path('', views.AdListView.as_view()),
	path('<int:pk>/', views.AdDetailView.as_view()),
	path('create/', views.AdCreateView.as_view()),
	path('update/', views.AdUpdateView.as_view()),
	path('delete/<int:pk>/', views.AdDeleteView.as_view()),
]
