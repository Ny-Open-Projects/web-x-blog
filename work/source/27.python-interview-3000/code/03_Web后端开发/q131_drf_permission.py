# Django + DRF 模块级代码
try:
    from rest_framework.permissions import BasePermission, SAFE_METHODS
    from rest_framework.authentication import TokenAuthentication
except ImportError:
    print("该题演示需要第三方库 djangorestframework:pip install djangorestframework(正文已讲清原理,安装后可运行)")
    raise SystemExit(0)

class IsAdminOrReadOnly(BasePermission):
    """安全方法放行,写操作仅管理员"""
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return bool(request.user and request.user.is_authenticated)
        return bool(request.user and request.user.is_staff)

    def has_object_permission(self, request, view, obj):
        # 对象级:普通用户只能读自己创建的资源
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_staff or getattr(obj, 'owner_id', None) == request.user.id

class BookViewSet:
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    # 请求流程: Token 认证确定 user -> has_permission -> get_object -> has_object_permission
