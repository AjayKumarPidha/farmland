from django.urls import path
from farmland_app import views
urlpatterns = [
    path('', views.IndexPageView.as_view(), name="index"),
    path('about/', views.AboutPageView.as_view(), name="about"),
    path('blog/', views.BlogPageView.as_view(), name="blog"),
    path('blogsingle/', views.BlogSinglePageView.as_view(), name="blogsingle"), 
    path('contact/', views.ContactPageView.as_view(), name="contact"), 
    path('project/', views.ProjectPageView.as_view(), name="project"), 
    path('services/', views.ServicesPageView.as_view(), name="services"), 
    path('subscribe/', views.EmailSubscribeView.as_view(), name='subscribe')
    
]