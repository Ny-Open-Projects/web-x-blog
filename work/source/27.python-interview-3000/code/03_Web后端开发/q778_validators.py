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

from rest_framework import serializers

order = []

class Signup(serializers.Serializer):
    name = serializers.CharField()
    password = serializers.CharField()
    password2 = serializers.CharField()

    def validate_name(self, value):
        order.append("field:name")
        return value.strip()

    def validate(self, attrs):
        order.append("object:validate")
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError("两次密码不一致")
        return attrs

s = Signup(data={"name": " alice ", "password": "x", "password2": "x"})
print(s.is_valid(), s.validated_data["name"])
print(order)
