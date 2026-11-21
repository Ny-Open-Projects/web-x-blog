# settings.py 关键配置(模块级自洽示意)
DEBUG = True
BASE_DIR = '/srv/myproject'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [f'{BASE_DIR}/templates'],        # 全局模板目录
    'APP_DIRS': True,                          # 自动发现各 app 的 templates/
    'OPTIONS': {'context_processors': [
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
    ]},
}]

STATIC_URL = '/static/'
STATICFILES_DIRS = [f'{BASE_DIR}/assets']     # 项目级静态目录
STATIC_ROOT = f'{BASE_DIR}/staticfiles'       # collectstatic 汇总目标
MEDIA_URL = '/media/'                          # 用户上传
MEDIA_ROOT = f'{BASE_DIR}/media'

# 开发期: runserver 自动服务 static
# 生产: python manage.py collectstatic 后由 Nginx alias /static/ -> STATIC_ROOT
print(STATIC_ROOT)
