try:
    import django
    from django.conf import settings
except ImportError:
    print("该题演示需要第三方库 django:pip install django,原理见正文")
    raise SystemExit(0)

settings.configure(
    DEBUG=True,
    CACHES={"default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"}},
    INSTALLED_APPS=[],
    TEMPLATES=[{
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [], "APP_DIRS": False, "OPTIONS": {},
    }],
    USE_TZ=True,
)
django.setup()

from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from django.template import Context, Template

tpl = Template("{% load cache %}{% cache 60 hero %}静态横幅{% endcache %}{{ name }}")
print(tpl.render(Context({"name": "alice"})))
key = make_template_fragment_key("hero")
print("片段缓存存在:", cache.get(key) is not None)
cache.delete(key)
print("删除后需重渲染:", cache.get(key) is None)
