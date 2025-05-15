# clubWeb/apps.py

from django.apps import AppConfig
from django.db.utils import OperationalError

class ClubwebConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "clubWeb"

    def ready(self):
        from .models import Club
        try:
            # A, B, C 동아리가 없으면 생성
            if Club.objects.count() == 0:
                Club.objects.create(name='A', description='A 동아리 설명입니다.')
                Club.objects.create(name='B', description='B 동아리 설명입니다.')
                Club.objects.create(name='C', description='C 동아리 설명입니다.')
        except OperationalError:
            # 마이그레이션 전에는 테이블이 없을 수 있음
            pass
