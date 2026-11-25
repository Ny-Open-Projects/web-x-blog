---
title: "[Q6202] Django system check：--deploy 门禁比人工清单可靠"
date: 2026-11-24
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6202 · Django system check：--deploy 门禁比人工清单可靠

难度：P6 ｜ 标签：Django、system check、check --deploy、CI 门禁、ERROR/WARNING、fail-level

**问**：上线前靠运维在群里发 checklist 逐条核对，人一忙就漏。Django 的 system check 框架是什么？`manage.py check --deploy` 与普通启动时自动跑的 check 有什么区别？自定义检查怎么注册？ERROR 和 WARNING 的分级怎么接进 CI 让"漏配"变成硬失败？

**答**：
结论：system check 是 Django 内置的**配置审计框架**：启动时自动跑一遍注册检查（`ALLOWED_HOSTS` 拼写、字段引用错误、URL 配置冲突等在启动期直接报错），而 `manage.py check --deploy` 会额外激活一批**部署专属检查**（DEBUG 是否关闭、SECRET_KEY 是否为默认值、CONN_MAX_AGE、SECURE_SSL_REDIRECT、静态文件配置等），这些检查在开发环境故意不跑，否则本地根本起不来。检查通过 `@register` 注册进框架，可声明 `deploy=True`（仅部署模式执行）和 `severity`（ERROR/WARNING/HINTS）；`--fail-level ERROR` 让出现 ERROR 时命令退出码非零，直接当 CI/CD 门禁。相比人工清单：检查代码化、可进版本库、随框架升级自动补充新条目。

取舍：a) 启动期自动 check 保持默认开启（`--skip-checks` 只该给性能敏感的本地工具用），配置错误在启动瞬间失败好过请求期500；b) 部署检查放进发布流水线（`python manage.py check --deploy --fail-level ERROR`），ERROR 硬失败、WARNING 进报告人工确认；c) 业务自定义检查（"生产禁用 email 后端 console"、"缓存必须配 Redis 不能 LocMem"）注册 `deploy=True`，把团队运维经验沉淀成代码；d) 检查要幂等、只读、不查外部服务（检查是启动路径/CI 路径，别让它连数据库），真要探活交给健康检查端点，两套机制别混淆；e) check 防配置错误，防不了数据/运行时故障——它是门禁不是监控。

实战：事故形态是"新环境从模板复制 settings，漏改 SECRET_KEY 且 DEBUG 保持 True，靠人肉 review 两次都漏掉；接 CI 后 `check --deploy` 直接报 'SECRET_KEY 是默认值' ERROR 级，发布流水线红掉；顺手把'生产必须 Redis 缓存'写成自定义检查，运维经验代码化"。下面模拟 check 框架的注册与部署模式分级。

```python
CHECKS = []


def register(deploy=False, severity="WARNING"):
    def deco(func):
        CHECKS.append((func, deploy, severity))
        return func
    return deco


@register()
def check_slow_startup():
    return "启动扫描路径过多"


@register(deploy=True, severity="ERROR")
def check_secret_key():
    return "SECRET_KEY 仍是示例默认值"


@register(deploy=True)
def check_conn_max_age():
    return "CONN_MAX_AGE=0，高并发下反复建连"


def run_checks(deploy=False):
    issues = []
    for func, only_deploy, sev in CHECKS:
        if only_deploy and not deploy:
            continue
        msg = func()
        if msg:
            issues.append((func.__name__, sev, msg))
    return issues


plain = run_checks()
dep = run_checks(deploy=True)
n_err = sum(1 for _, sev, _ in dep if sev == "ERROR")
print("[1] 普通启动:", plain, "——deploy 专属检查未运行")
print("[2] check --deploy:", dep)
print("[3] ERROR 计数:", n_err, "（>0 时按 --fail-level 让门禁失败）")
```

**追问一**：为什么 DEBUG=True 这类问题不在普通启动时报错，而要放到 --deploy？—— 开发环境的合理配置就是生产环境的致命配置：本地调试需要 DEBUG、console 邮件后端、LocMem 缓存；如果启动期就报错，所有开发者都会用 `--skip-checks` 绕过，检查体系整体失效。所以框架把"仅在部署有意义"的检查用 `deploy=True` 分组，由部署模式显式激活。这是"同一套代码，两种运行语境"的分组设计，等价于测试环境和生产环境的策略差。

**追问二**：system check 和健康检查端点（/healthz）分工是什么？—— check 是**静态配置审计**：不连外部依赖、幂等、秒级完成，回答"这次部署的配置有没有错误"，适合 CI 门禁与启动期；健康检查是**运行时探活**：真的连数据库/缓存探测，回答"这个实例现在能不能接流量"，适合 K8s 探针与负载均衡摘除。常见误用是把数据库探活写进 system check 导致 CI 依赖测试库，或把配置审计写进健康检查导致每次探针都跑全量检查。一句话：check 面向"部署对不对"，healthz 面向"实例活不活"。

## 背诵要点
- 启动自动跑基础 check；`check --deploy` 额外激活部署专属检查（DEBUG/SECRET_KEY/CONN_MAX_AGE 等）。
- 自定义检查 `register(deploy=True, severity=...)`；`--fail-level ERROR` 让 CI 硬失败，人肉 checklist 代码化。
- check 是静态配置审计（不连外部依赖），healthz 是运行时探活；门禁与探针不可互相替代。

## 复盘追问
- 为什么开发环境不该跑 deploy 检查？（开发配置=生产致命配置，启动期报错会逼所有人 skip-checks）
- 新环境漏改 SECRET_KEY 两次 review 都没拦住，什么机制能拦？（check --deploy ERROR 级门禁）
