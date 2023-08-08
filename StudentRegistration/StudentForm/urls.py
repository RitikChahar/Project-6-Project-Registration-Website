from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.get_otp),
    path('verify-otp/', views.verify_otp),
    path('upload-resume/', views.handle_resume_upload),
    path('all-details/', views.get_all_details),
    path('social-media/', views.get_social_media),
]