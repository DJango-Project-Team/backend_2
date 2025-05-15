from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='main_view'),  # 동아리 목록 페이지
    path('club/<int:club_id>/', views.club_detail, name='club_detail'),  # 동아리 상세 페이지
    path('club/<int:club_id>/apply/', views.application_form, name='application_form'),  # 신청 폼 페이지
    path('application_success/', views.application_success, name='application_success'),  # 신청 완료 페이지
]
