from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostListView2

urlpatterns = [
  path('', PostListView.as_view(), name='home'),
  path('about_us/', views.about, name='about'),
  path('post/<int:pk>/', PostDetailView.as_view(), name='news_detail'),
  path('gallery/', views.gallery, name='gallery'),
  path('news/', PostListView2.as_view(),name='news'),
  path('programs/', views.programs, name='programs'),
  path('staff/', views.staff, name='staff'),
  path('admission/', views.admission, name='admission'),
  path('careers/', views.careers, name='careers'),
  path('contact_us/', views.contact, name='contact'),


]