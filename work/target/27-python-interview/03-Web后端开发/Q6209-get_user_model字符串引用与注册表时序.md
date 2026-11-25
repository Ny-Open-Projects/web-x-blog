---
title: "[Q6209] get_user_model：字符串引用与注册表时序"
date: 2026-11-24
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6209 · get_user_model：字符串引用与注册表时序

难度：P6 ｜ 标签：Django、AUTH_USER_MODEL、get_user_model、AppRegistryNotReady、循环导入、外键引用

**问**：Django 为什么规定用户模型必须用 `AUTH_USER_MODEL = "app_label.ModelName"` 字符串引用，而不是直接 import？`get_user_model()` 在什么时机能调、什么时机必炸？模型 A 外键引用用户模型时为什么必须写 `settings.AUTH_USER_MODEL` 而不是 `get_user_model()`？项目中途换用户模型会怎样？

**答**：
结论：用户模型是全项目被依赖最多的模型，如果所有模块直接 `from app.models import User`，users app 就处在 import 图的最底端——settings 加载、其他 app 的模块级代码、第三方包都会拉起这条 import 链，循环导入与 `AppRegistryNotReady` 必然出现。字符串引用把"解析"延迟到 apps registry 就绪之后：`get_user_model()` 在 `django.setup()` 完成前调用必抛 `AppRegistryNotReady`，ready 后随时可调。模型字段引用必须用字符串形态 `models.ForeignKey(settings.AUTH_USER_MODEL, ...)`——因为模型类定义发生在 registry 构建期，那时 `get_user_model()` 尚不可用，Django 需要字符串在迁移与模型加载时延迟绑定。项目中途换用户模型是重操作：迁移需要 `Swappable` 语义或数据搬迁，官方立场是"项目开始就定对，中途换是迁移工程"。

取舍：a) 任何代码（views/serializers/signals/tasks）运行时取用户模型：`get_user_model()`，别 import 具体类，保持 AUTH_USER_MODEL 可替换；b) 模型字段引用：`settings.AUTH_USER_MODEL` 字符串；c) `get_user_model()` 的返回值可以缓存到**函数局部/请求作用域**，不要缓存到模块级常量——测试里 override AUTH_USER_MODEL 后模块级缓存会指向旧模型；d) 自定义用户模型的时机是项目第一周：`AbstractUser` 继承起步，字段后加都好办；e) 迁移文件里引用用户模型同样用字符串，让迁移在 registry 未就绪时也能被加载。

实战：事故形态是"通知服务直接 `from users.models import User`，celery worker 的启动路径绕过了 django.setup 的正常顺序，偶发 AppRegistryNotReady 且只在特定 import 顺序下出现（排查两天）；全库替换为 `get_user_model()` + 模型外键改 `settings.AUTH_USER_MODEL` 后，import 图解耦，启动顺序不再敏感"。下面模拟注册表时序与两种调用时机。

```python
APPS = {
    "settings.AUTH_USER_MODEL": "users.Member",
}


class AppsRegistry:
    def __init__(self):
        self.ready = False
        self.models = {}

    def get_model(self, dotted):
        if not self.ready:
            raise RuntimeError("AppRegistryNotReady")
        if dotted not in self.models:
            raise LookupError(dotted)
        return self.models[dotted]


apps = AppsRegistry()
AUTH_USER_MODEL = "users.Member"


def get_user_model():
    if not apps.ready:
        raise RuntimeError("AppRegistryNotReady: 注册表未就绪")
    return apps.models[AUTH_USER_MODEL]


try:
    get_user_model()
except RuntimeError as e:
    print("[1] settings/模块顶层调用:", e)

apps.models[AUTH_USER_MODEL] = type("Member", (), {})
apps.ready = True
print("[2] ready 后 get_user_model():", get_user_model())
print("[3] 字符串引用的意义: 配置层只存 'users.Member'，解析延迟到 apps.ready，避免模块级循环导入")
```

**追问一**：为什么模型定义里不能用 `get_user_model()` 作为外键目标？—— 模型类体在 **registry 构建期**执行，此时 apps.ready=False，`get_user_model()` 直接抛异常；即使侥幸通过，直接引用具体类也会把模型关系焊死在某个实现上，破坏 AUTH_USER_MODEL 的可替换性。字符串形态 `ForeignKey(settings.AUTH_USER_MODEL, ...)` 让 Django 在模型加载/迁移阶段做延迟绑定，同时保持可替换契约。同类规则适用于 `OneToOneField`（如 Profile 关联用户）与迁移文件中的引用。

**追问二**：`get_user_model()` 能不能在模块级缓存？测试里会发生什么？—— 能编译通过但会埋雷：模块 import 发生在 registry 就绪之后时，缓存的是当时的模型类；测试若用 `override_settings(AUTH_USER_MODEL=...)` 换测试用户模型，模块级缓存仍指向生产模型——外键校验、权限判断全部指向错误表，测试可能出现"通过但生产路径错"或直接迁移报错。正确姿势：每次调用 `get_user_model()`（它内部是字典查找，开销极低），或缓存进 request/task 生命周期。这也是"延迟解析 + 不缓存解析结果"在 Django 配置体系里的通用纪律。

## 背诵要点
- AUTH_USER_MODEL 字符串引用把解析延迟到 registry 就绪；`get_user_model()` 在 django.setup 完成前调用必抛 AppRegistryNotReady。
- 模型外键必须 `ForeignKey(settings.AUTH_USER_MODEL, ...)`：模型定义发生在 registry 构建期，get_user_model() 不可用且会焊死实现。
- 运行时代码统一 get_user_model()（不缓存到模块级），用户模型必须项目第一周定型，中途换是迁移工程。

## 复盘追问
- celery worker 偶发 AppRegistryNotReady 且与 import 顺序相关，怎么根治？（全库 get_user_model + 字符串外键，解耦 import 图）
- 为什么外键里 get_user_model() 会炸而 settings.AUTH_USER_MODEL 不会？（前者在 registry 构建期就需就绪，后者延迟绑定）
