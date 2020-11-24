from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, UserManager
)
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email', unique=True)
    name = models.CharField('이름', max_length=30, blank=False)
    is_staff = models.BooleanField('_staff status',
                                   default=False,
                                   help_text=_('Designates whether the user can log into thid admin site.'),

    )
    is_active = models.BooleanField(_('active'),
                                    default=False,
                                    help_text=_(
                                        'Designates whether this user should be treated as active.'
                                        'Unselect this instead of deleting accounts'
                                    ),
    )
    date_joined = models.DateTimeField('가입일', default=timezone.now)

    object = UserManager()

    USERNAME_FIELD = 'email'   # email을 사용자의 식별자로 설정
    REQUIRED_FIELDS = ['name'] # 필수입력 값

    class Meta:
        # 사용자가 읽기 쉬운 객체으 ㅣ이름으로 관리자 화면에서 표시
        verbose_name = _('user')
        # verbose_name 의 복수형
        verbose_name_plural = _('users')
        swappable = 'AUTH_USER_MODEL'
        db_table = "user"

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)