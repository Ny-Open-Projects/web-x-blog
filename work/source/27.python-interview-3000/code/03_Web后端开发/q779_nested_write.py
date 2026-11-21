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

from django.db import connection, models, transaction
from rest_framework import serializers

class Poll(models.Model):
    question = models.CharField(max_length=64)
    class Meta:
        app_label = "demo"

class Choice(models.Model):
    poll = models.ForeignKey(Poll, related_name="choices", on_delete=models.CASCADE)
    text = models.CharField(max_length=64)
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Poll)
    se.create_model(Choice)

class ChoiceS(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ["text"]

class PollS(serializers.ModelSerializer):
    choices = ChoiceS(many=True)
    class Meta:
        model = Poll
        fields = ["id", "question", "choices"]

    def create(self, validated_data):
        choices = validated_data.pop("choices")
        with transaction.atomic():
            poll = Poll.objects.create(**validated_data)
            Choice.objects.bulk_create([Choice(poll=poll, **c) for c in choices])
        return poll

data = {"question": "选谁", "choices": [{"text": "A"}, {"text": "B"}]}
s = PollS(data=data)
print(s.is_valid(raise_exception=False))
poll = s.save()
print(poll.question, poll.choices.count())
