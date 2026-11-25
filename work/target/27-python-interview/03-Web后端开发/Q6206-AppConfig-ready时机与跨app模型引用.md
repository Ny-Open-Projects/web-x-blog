---
title: "[Q6206] AppConfig.ready：时机、半初始化与跨 app 模型引用"
date: 2026-11-24
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6206 · AppConfig.ready：时机、半初始化与跨 app 模型引用

难度：P6 ｜ 标签：Django、AppConfig、ready、AppRegistryNotReady、循环导入、信号注册

**问**：为什么在 `AppConfig.ready()` 里 `get_model("other_app.Model")` 有时直接抛 `AppRegistryNotReady`？ready 的执行顺序由什么决定？`INSTALLED_APPS` 顺序和它什么关系？为什么官方反复强调"ready 里只注册信号、别 import 别的 models"？在 settings.py 里直接 `from app.models import X` 会发生什么？

**答**：
结论：Django 启动分两段：先加载全部 app 的模型注册表（model registry），完成后 `apps.ready` 置 True，再按 **INSTALLED_APPS 的顺序**逐个调用各 app 的 `ready()`。ready 执行时 registry 已就绪，所以 ready 里 `get_model` 本身是安全的——抛 `AppRegistryNotReady` 的真实场景是"在 ready 之前就解析模型"：settings.py/urls.py 顶层 import 模型、`apps.py` 模块级代码取模型、或 ready 里同步 import 了另一个 app 的 models 模块而后者模块级代码又回头依赖自己——循环导入 + 半初始化 registry 双重雷区。跨 app 模型引用的官方规则：ready 里只做**注册类**动作（信号 connect、模板 tag 注册、check 注册），模型引用一律用**字符串延迟解析**（信号回调触发时才 `apps.get_model`）。

取舍：a) ready 里 import 本 app 的 models：可以（本 app 已加载）；跨 app 的 models：不要（执行顺序由 INSTALLED_APPS 决定，前面的 app ready 时后面的可能还没准备好，尤其 import 会触发对方模块级副作用）；b) 需要在 ready 里校验跨 app 配置：用字符串 + try/except 延迟到首请求，或放到 system check；c) 信号 receiver 里解析模型：每次回调走 `apps.get_model`（registry 就绪后开销可忽略）或 receiver 定义处捕获 `AppRegistryNotReady` 兜底；d) `settings.py` 里 import 任何 models 都是禁忌——settings 是启动链最前端，registry 还没建立；需要 settings 感知模型信息的设计本身就是错的，应反向（模型/ready 读 settings）；e) 测试环境注意 `django.setup()` 后才 ready，测试代码顶层 import 模型要放在 `django.setup()` 之后。

实战：事故形态是"users 的 ready 里直接 `from billing.models import Account` 做 quota 校验，某次 INSTALLED_APPS 调序把 users 挪到 billing 前，billing 的 models 模块级又 import users 的常量，启动循环导入；重构为 ready 只 connect 信号、回调里 `apps.get_model('billing.Account')` 延迟解析，调序不再影响启动"。下面模拟注册表时序与两种姿势。

```python
APPS = ["users", "billing"]


class AppsRegistry:
    def __init__(self):
        self.ready = False
        self.models = {}

    def get_model(self, dotted):
        if not self.ready:
            raise RuntimeError("AppRegistryNotReady: apps 尚未就绪")
        if dotted not in self.models:
            raise LookupError(f"模型不存在: {dotted}")
        return self.models[dotted]


reg = AppsRegistry()


def users_ready_bad(r):
    # 反例：users.ready 里直接解析 billing 的模型
    r.get_model("billing.Account")


def users_ready_good(r):
    # 正例：ready 只注册信号回调，模型引用延迟到信号触发时解析
    def on_account_changed(sender, dotted, **kwargs):
        r.get_model(dotted)             # 运行时才解析，apps 已 ready
    return ("signal registered", "billing.Account")


try:
    users_ready_bad(reg)
except RuntimeError as e:
    print("[1] users.ready 先于 billing 执行，直接取模型:", e)

print("[2] 正确姿势:", users_ready_good(reg))
reg.models["billing.Account"] = "Account"
reg.ready = True
print("[3] ready 后解析成功:", reg.get_model("billing.Account"))
print("[4] 规则: ready 里只做信号注册/配置检查，跨 app 模型引用一律字符串+延迟解析")
```

**追问一**：ready 是串行还是并行？执行顺序对什么敏感？—— 串行，按 INSTALLED_APPS 声明顺序。敏感点：a) ready 里读"全局单例/配置"时，前面 app 的 ready 已经生效（如第三方 app 注册了默认配置）；b) 信号的注册顺序决定 `send` 时的回调顺序（同 sender 按注册先后执行），依赖回调顺序的业务本身就是脆弱设计；c) 调 INSTALLED_APPS 顺序是常见的事故源——ready 之间通过 import 产生的隐式依赖在调序时爆炸，这正是"ready 里禁止跨 app import"的原因。

**追问二**：`AppRegistryNotReady` 在哪些具体位置最容易踩到？—— 按踩坑频率：①settings.py 顶层 import models（启动最前端）；②urls.py 模块级 `get_model`/import models（settings 加载完但 registry 未填充完——部分场景 urls 先于 apps 导入）；③第三方包在 import 副作用里访问 registry；④ celery/管理脚本绕过 `django.setup()` 直接 import models；⑤测试文件顶层 import 模型且未走 pytest-django/django.setup 流程。统一防法：凡"模块级"代码只放配置常量与函数定义，一切模型解析延迟到函数调用时。

## 背诵要点
- 启动顺序：先建全部 model registry → apps.ready=True → 按 INSTALLED_APPS 顺序串行调各 app ready()。
- ready 只做注册类动作（信号/模板 tag/check），跨 app 模型引用一律字符串 + 运行时 `apps.get_model` 延迟解析。
- AppRegistryNotReady 高发位置：settings/urls 模块级 import、celery 绕过 django.setup、测试顶层 import。

## 复盘追问
- ready 里 get_model 为什么可能失败而信号回调里不会？（ready 触发时序与注册表就绪时序的错位）
- INSTALLED_APPS 调序引发循环导入，根因是什么？（ready/模块级代码间的隐式 import 依赖）
