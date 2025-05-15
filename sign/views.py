from django.shortcuts import render, redirect
from .models import Sign
from django.contrib import messages

# 로그인하는 로직
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('sign_up_id')        # HTML 폼에서 입력받은 ID
        password = request.POST.get('sign_up_password')  # HTML 폼에서 입력받은 PW

        try:
            user = Sign.objects.get(username=username, password=password)
            return render(request, 'New_Page_01.html', {'user': user})
        except Sign.DoesNotExist:
            messages.error(request, '아이디 또는 비밀번호가 일치하지 않습니다.')
            return render(request, 'Test_01.html')

    return render(request, 'sign/Test_01.html')


# 회원가입 로직
def sign_up_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        userid = request.POST['userid']
        password = request.POST['password']

        if Sign.objects.filter(username=username).exists():
            messages.error(request, "이미 존재하는 이름입니다.")
            return redirect('/sign/signup/')

        Sign.objects.create(username=username, email=email, userid=userid, password=password)
        return redirect('/')
    return render(request, 'sign/signup.html')