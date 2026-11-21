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

class CommentIn(serializers.Serializer):
    body = serializers.CharField()

    def validate_body(self, value):
        for w in self.context.get("banned_words", set()):
            if w.lower() in value.lower():
                raise serializers.ValidationError(f"包含敏感词 {w}")
        return value

class CommentOut(serializers.Serializer):
    body = serializers.CharField()
    mine = serializers.SerializerMethodField()

    def get_mine(self, obj):
        return obj.get("owner") == self.context.get("viewer")

bad = CommentIn(data={"body": "剧透:主角死了"}, context={"banned_words": {"剧透"}})
print(bad.is_valid(), bad.errors)
out = CommentOut({"body": "很好看", "owner": "alice"}, context={"viewer": "alice"})
print(out.data)
