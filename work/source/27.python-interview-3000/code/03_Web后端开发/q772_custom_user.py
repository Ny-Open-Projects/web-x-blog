try:
    import django
    from django.conf import settings
except ImportError:
    print("该题演示需要第三方库 django:pip install django,原理见正文")
    raise SystemExit(0)

settings.configure(
    DEBUG=True,
    DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
    INSTALLED_APPS=[],
    USE_TZ=True,
)
django.setup()

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import connection, models

class UserManager(BaseUserManager):
    def create_user(self, username: str, password: str):
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=32, unique=True)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = "username"
    objects = UserManager()
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(CustomUser)

u = CustomUser.objects.create_user(username="alice", password="s3cret!")
print("密码校验:", u.check_password("s3cret!"))
print("存储的是哈希:", u.password.startswith("pbkdf2"))
