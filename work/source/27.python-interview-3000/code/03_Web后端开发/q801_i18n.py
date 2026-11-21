try:
    import django
    from django.conf import settings
except ImportError:
    print("该题演示需要第三方库 django:pip install django,原理见正文")
    raise SystemExit(0)

settings.configure(
    DEBUG=True,
    USE_I18N=True,
    LANGUAGES=[("en", "English"), ("zh-hans", "简体中文")],
    INSTALLED_APPS=[],
    USE_TZ=True,
)
django.setup()

from django.utils import translation
from django.utils.translation import gettext as _

print(_("Welcome"))   # 未安装 .mo 目录时原样返回 msgid
print(_("Hello %(name)s") % {"name": "alice"})
with translation.override("zh-hans"):
    print("当前语言:", translation.get_language())
print("恢复后语言:", translation.get_language())
