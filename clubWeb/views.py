from django.shortcuts import render, get_object_or_404, redirect
from .models import Club, Application
from .forms import ApplicationForm

# 동아리 목록 페이지
def main_view(request):
    # DB에서 모든 동아리 정보 가져오기
    clubs = Club.objects.all()  # club_main 테이블에서 모든 동아리 정보 가져오기
    return render(request, 'club/main.html', {'clubs': clubs})

# 동아리 상세 페이지
def club_detail(request, club_id):
    club = get_object_or_404(Club, pk=club_id)
    return render(request, 'club/club_detail.html', {'club': club})

# 신청서 페이지
def application_form(request, club_id):
    club = get_object_or_404(Club, pk=club_id)  # club 객체를 가져옴

    if request.method == "POST":
        form = ApplicationForm(request.POST)
        print("폼 데이터: ", request.POST)  # 데이터가 잘 전달되고 있는지 확인
        if form.is_valid():
            application = form.save(commit=False)
            application.club = club  # 동아리 ID 자동 설정
            print("저장될 데이터: ", application)  # 데이터가 제대로 설정되었는지 확인
            application.save()  # 데이터 저장
            return redirect('application_success')
        else:
            print("폼 오류: ", form.errors)  # 폼이 유효하지 않다면 오류 출력

    else:
        form = ApplicationForm()  # GET 요청 시 빈 폼을 생성

    return render(request, 'club/application_form.html', {'form': form, 'club': club})  # 폼을 템플릿으로 전달
# 신청 완료 페이지
def application_success(request):
    return render(request, 'club/application_success.html')
