---
title: [Q6132] DEBUG=True 生产泄露事故复盘
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6132 · DEBUG=True 生产泄露事故复盘

难度：P6 | 标签：Django、DEBUG、信息泄露、事故复盘

**问**：某 Django 服务上线时忘了改 `DEBUG`，一次 404/500 页面把 settings、URL 路由表、SQL 语句、环境变量快照全部展示给了公网用户。这类"调试模式泄露"都泄什么？为什么只在出错的请求才触发、更难被发现？如何从配置与流程上根治？

**答**：

**结论**：Django `DEBUG=True` 时泄露面包括：(1) 技术调试页——完整 traceback、每个局部变量的值（可能含密钥、token）、SQL 查询与参数；(2) 404 页列出全部已注册 URL 模式，给攻击者一张 API 地图；(3) `ALLOWED_HOSTS` 校验失败页面直接回显 Host 头（可被用于投毒链路）；(4) 静态文件/调试工具（`runserver`、django-debug-toolbar 若装了）暴露内网拓扑。只在异常/404 请求触发意味着日常探测（/healthz 200）完全正常，只有特定畸形请求才翻脸，监控与渗透扫描都容易漏。还有连带效应：DEBUG=True 时 Django 不收集错误报告（不发给 ADMINS/Sentry 钩子挂接点不同），线上故障反而无告警。

**取舍**：根治靠"默认安全 + 双保险"：配置上 `DEBUG` 从环境变量读且生产镜像强制 False；流程上用启动断言（`assert not settings.DEBUG if ENV=prod`，注意别用会随 -O 消失的 assert，改 raise）+ CI 扫描 `DEBUG = True` 字面量 + 发布 checklist 里"故意制造 500 验证调试页不存在"。Fail2ban 式的兜底：错误页模板统一定制，技术页在 prod 模板里不可能被渲染。

**实战**：同类泄露横向盘点：Flask debug 模式的 Werkzeug 调试器甚至可远程执行（werkzeug debugger pin 是缓解不是防线）、Spring Boot actuator、Go pprof 端点——复盘要做成横向排查而不是只修一处。

```python
# 配置硬断言示例（3.12 基线，标准库可运行）
import os, sys

ENV = os.environ.get("APP_ENV", "dev")
DEBUG = os.environ.get("APP_DEBUG", "0") == "1" if ENV != "prod" else False

def boot_guard(env: str, debug: bool):
    """启动期硬校验：生产环境 DEBUG 必须为 False，违规直接拒绝启动。"""
    if env == "prod" and debug:
        raise RuntimeError("REFUSING TO START: DEBUG must be False in prod")
    if env == "prod":
        print("boot guard OK: prod + DEBUG=False")

boot_guard(ENV, DEBUG)

# 泄露面清单化自检：扫描 settings 模块的敏感默认值
SENSITIVE_DEFAULTS = {
    "SECRET_KEY": None,            # None/默认值都是雷
    "ALLOWED_HOSTS": [],
    "SESSION_COOKIE_SECURE": False,
}
for k, bad in SENSITIVE_DEFAULTS.items():
    v = os.environ.get(k, None)
    if ENV == "prod" and (v in (None, "", "changeme")):
        print(f"[warn] {k} 未显式配置，生产禁止默认值")

print("横扫清单：Django DEBUG / Flask debug / actuator / pprof 端点")
```

**追问 1**：为什么 DEBUG=True 时异常页会显示局部变量？
答：Django 的技术页用 traceback 的 frame 内省逐帧渲染 locals；这是设计行为不是 bug——它假设该页面只在开发者环境可见，所以"环境区分"是唯一安全边界。

**追问 2**：Werkzeug 调试器的 PIN 机制为何不构成安全边界？
答：PIN 由机器标识推导，容器环境熵低（相同镜像相同 PIN）；且 XSS/SSRF 可读取 PIN 文件路径。历史上多起 RCE 都经 debugger console，结论就是生产禁止 debug 模式而非信任 PIN。

**追问 3**：如何让"忘了关 DEBUG"在发布流水线就被拦截？
答：三层：镜像构建时以 prod profile 渲染配置并断言；冒烟测试故意请求不存在路径断言返回非调试页；运行时启动守卫 raise——任何一层命中都拦住，成本最贵的是最后一层。

## 背诵要点

- DEBUG=True 泄露 traceback+locals、URL 路由表、Host 回显，且只在异常请求触发、监控难覆盖。
- Django DEBUG=True 时错误报告链路（ADMINS/Sentry 钩子）行为不同，故障告警反而缺失。
- 根治三层：环境变量强制 + CI 扫描字面量 + 启动期 raise 守卫；横向排查 Flask/actuator/pprof。

## 复盘追问

- 事故后如何确认泄露数据被利用过？(提示：访问日志检索 404 页与技术页特征 UA/路径)
- 环境配置矩阵（dev/staging/prod）如何用代码而非文档固化？(提示：settings 校验器 + 启动断言库)
