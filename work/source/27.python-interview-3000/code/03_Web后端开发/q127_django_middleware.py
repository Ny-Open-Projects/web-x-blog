# myapp/middleware.py (Django 模块级代码)
import time
import uuid

def request_id_middleware(get_response):
    def middleware(request):
        rid = request.headers.get('X-Request-ID', str(uuid.uuid4())[:8])
        request.rid = rid
        start = time.perf_counter()
        response = get_response(request)            # 内层处理
        response['X-Request-ID'] = rid
        response['X-Cost-Ms'] = str(round((time.perf_counter() - start) * 1000, 2))
        return response
    return middleware

class TimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.start = time.perf_counter()
        response = self.get_response(request)
        print(f'{request.path} took {time.perf_counter() - self.start:.3f}s')
        return response

# settings.py 注册(列表第一项最外层):
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'myapp.middleware.request_id_middleware',
#     'myapp.middleware.TimingMiddleware',
#     ... 其余内置中间件 ...
# ]
