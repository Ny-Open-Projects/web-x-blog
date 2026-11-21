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

from django.db import connection, models, transaction

class Mail(models.Model):
    to = models.CharField(max_length=64)
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Mail)

sent: list = []

def dispatch_mail(to: str):
    sent.append(f"mail->{to}")

with transaction.atomic():
    Mail.objects.create(to="a@b.c")
    transaction.on_commit(lambda: dispatch_mail("a@b.c"))
    print("事务未提交时已发送:", len(sent))
print("提交后已发送:", sent)

try:
    with transaction.atomic():
        Mail.objects.create(to="x")
        transaction.on_commit(lambda: dispatch_mail("x"))
        raise RuntimeError("回滚")
except RuntimeError:
    pass
print("回滚后不应发送:", "mail->x" not in sent)
