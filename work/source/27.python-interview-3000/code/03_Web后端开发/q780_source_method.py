try:
    import django
    from django.conf import settings
except ImportError:
    print("该题演示需要第三方库 django、djangorestframework:pip install django djangorestframework,原理见正文")
    raise SystemExit(0)

settings.configure(
    DEBUG=True,
    INSTALLED_APPS=["rest_framework"],
    DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
    USE_TZ=True,
)
django.setup()

from django.db import connection, models
from rest_framework import serializers

class Profile(models.Model):
    bio = models.CharField(max_length=64, default="")
    class Meta:
        app_label = "demo"

class User(models.Model):
    name = models.CharField(max_length=32)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Profile)
    se.create_model(User)

u = User.objects.create(name="alice", profile=Profile.objects.create(bio="dev"))

class UserOut(serializers.ModelSerializer):
    bio = serializers.CharField(source="profile.bio", read_only=True)
    upper_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["name", "bio", "upper_name"]

    def get_upper_name(self, obj):
        return obj.name.upper()

print(UserOut(User.objects.select_related("profile").get(pk=u.pk)).data)
