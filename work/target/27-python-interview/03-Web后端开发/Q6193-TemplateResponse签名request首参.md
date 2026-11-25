---
title: "[Q6193] Starlette 0.29 的 TemplateResponse 签名：request 变成必填首参"
date: 2026-11-24
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6193 · Starlette 0.29 的 TemplateResponse 签名：request 变成必填首参

难度：P7 ｜ 标签：Starlette、TemplateResponse、签名变更、位置参数、Jinja2、升级迁移

**问**：升级 Starlette/FastAPI 后，模板页面全部 500，栈是 `TypeError: unhashable type: 'dict'` 或模板里 `request is undefined`。代码是 `TemplateResponse("index.html", {"request": request, "user": u})`。`TemplateResponse` 的签名什么时候变的？为什么参数顺序一变，错误不是"缺参数"而是更诡异的类型错误？怎么系统性排查这类升级回归？

**答**：
结论：Starlette 0.29 起把 `request` 提升为**第一个必填位置参数**：`TemplateResponse(request, name, context=None, ...)`，理由是模板里几乎总要 `request`（`url_for`、CSRF、`request.state`），让框架自动注入比每个调用点手写更可靠，也避免"忘记塞 request 导致模板静默取到 undefined"。旧调用 `TemplateResponse("index.html", {"request": ...})` 会把字符串当 `request`、把 dict 当 `name`，真正的模板名没了，报错点因此跑到渲染阶段（`unhashable type: 'dict'`、`'dict' object has no attribute 'endswith'`），而不是清晰的参数错误。

取舍：a) 迁移时一律用关键字参数 `TemplateResponse(request=request, name="index.html", context={...})`，让后续任何顺序调整都不再影响你；b) 别指望"位置参数兼容层"——0.x 版本可以随时破坏；把 Starlette/FastAPI 的小版本升级纳入回归测试（渲染一个最简模板）；c) 如果同时存在旧代码，写一个包装函数统一注入 `request`，把签名差异收敛到一处；d) 注意 `context` 里的 `request` 现在会被框架覆盖/补全，自己再塞一遍意义不大，但显式传也没坏处。

实战：事故形态是"灰度发布时首页 500 率 100%，回滚后恢复；第二次发布同样问题，因为测试只覆盖了 JSON 接口没渲染模板"。下面用两个类模拟旧/新签名，演示旧的位置调用在新类上如何"错位但能构造成功"，直到使用 `name` 才炸。

```python
import inspect


class OldTemplateResponse:
    def __init__(self, name, context=None, status_code=200):
        self.name = name
        self.context = context or {}
        self.status_code = status_code


class NewTemplateResponse:
    def __init__(self, request, name, context=None, status_code=200):
        self.request = request
        self.name = name
        self.context = dict(context or {})
        self.context.setdefault("request", request)
        self.status_code = status_code


class FakeRequest:
    def __init__(self, path="/"):
        self.path = path


print("[1] 旧签名:", inspect.signature(OldTemplateResponse))
print("[2] 新签名:", inspect.signature(NewTemplateResponse))

# 旧代码原样调用新类：位置参数错位，但构造阶段不报错
old_call = ("index.html", {"user": "u", "request": FakeRequest()})
tpl = NewTemplateResponse(*old_call)
print("[3] request 变成:", repr(tpl.request))
print("[4] name 变成:", type(tpl.name).__name__, tpl.name)
try:
    tpl.name.endswith(".html")
except AttributeError as e:
    print("[5] 直到渲染才炸:", e)

# 正确迁移：关键字参数
fixed = NewTemplateResponse(
    request=FakeRequest("/home"),
    name="index.html",
    context={"user": "u"},
)
print("[6] 关键字调用:", fixed.name, fixed.context["request"].path)

# 兼容包装：把旧调用收敛到一处
def render(name, context=None, **kwargs):
    return NewTemplateResponse(
        request=(context or {}).get("request", FakeRequest()),
        name=name,
        context=context,
        **kwargs,
    )


print("[7] 包装层兼容旧代码:", render("index.html", {"user": "u"}).name)
```

**追问一**：为什么不在新版本里做一个"检测第一个参数是不是字符串"的兼容分支？—— 那样会让签名在两个语义间摇摆：`request` 可能是任意对象，字符串也可能是某个自定义 request 类型；一旦猜错，错误被推迟得更深。库作者选择"破坏式明确"：升级即报错，让调用方一次性改对。对使用者来说，**关键字参数**是唯一能让这种破坏式变更"无感"的写法。

**追问二**：还有哪些 Starlette/FastAPI 升级是"位置参数错位"型破坏？—— 典型是 `RedirectResponse(url, status_code=307)` 这类签名基本稳定，但 `TemplateResponse`、`BackgroundTasks` 注入、以及 `Request`/`WebSocket` 的构造方式都变过；FastAPI 的 `Depends` 从默认值迁到 `Annotated` 也属于"看起来能跑、类型检查才发现"的变更。防御手段是：CI 里锁小版本 + 渲染冒烟测试 + `mypy`/`pyright` 抓签名不匹配，三者缺一都会让问题漏到线上。

## 背诵要点
- Starlette 0.29 起 `TemplateResponse(request, name, context)`，`request` 是必填首参。
- 旧位置调用会把 str 当 request、dict 当 name，错误延迟到渲染阶段（`unhashable`/`endswith`）。
- 迁移用关键字参数 + 渲染冒烟测试；不要依赖 0.x 的向后兼容。

## 复盘追问
- 升级后模板全 500 且报 `unhashable type: 'dict'`，如何从签名错位解释？（参数整体右移一位）
- 如何让框架小版本升级不把这类问题带到线上？（关键字参数、锁版本、模板冒烟、类型检查）
