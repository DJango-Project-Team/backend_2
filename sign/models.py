from django.db import models

#아래는 회원가입시 필요한 DB
class Sign(models.Model):
    username = models.CharField(max_length=200, unique=True) #이름
    email = models.EmailField(max_length=200, unique=True) #이메일
    userid = models.CharField(max_length=12, primary_key=True) #아이디
    password = models.CharField(max_length=200) #비밀번호

    def __str__(self):
        return self.username