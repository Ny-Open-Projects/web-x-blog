---
title: "[Q7240] 切到 dictConfig 后日志全没了：disable_existing_loggers 默认是 True"
date: 2026-11-24
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7240 · 切到 dictConfig 后日志全没了：disable_existing_loggers 默认是 True

难度：P6 ｜ 标签：logging、dictConfig、disable_existing_loggers、迁移

基线：Python 3.12 标准库 `logging.config.dictConfig`；用 `StringIO` 捕获输出。

**问**：日志配置从 `basicConfig` 迁到 `dictConfig`（写在 `logging.yaml`/`settings.py` 里），本地跑测试没问题，上线后有服务"日志变少了一半"：框架启动日志还在，但业务模块（尤其第三方 SDK、早期 import 的模块）的日志全没了，级别调成 DEBUG 也不出。配置里明明写了 root 的 handler 和 level。为什么？

**答**：
- **结论**：`dictConfig` 有一个默认 `disable_existing_loggers: True`：配置生效时，**所有已存在但没出现在配置里的 logger 会被 `disabled = True`**。模块顶层的 `logger = logging.getLogger(__name__)` 在 import 期就创建了，配置加载时它们已经存在；只要配置里没逐个列出（或没列它们的父 logger），就被静默禁用——`logger.info()` 连 `isEnabledFor` 都过不了，不会有任何报错。
- **取舍**：① 显式写 `disable_existing_loggers: False`，让未列出的 logger 继续向 root 传播（最常见、最安全）；② 在配置里列出所有业务 logger（可维护性差，新模块容易漏）；③ 用 `logging.getLogger()` 的层级关系：配置了父 logger `app`，子 logger `app.order` 不会被禁用吗？**会**——判定依据是"名字是否在配置的 `loggers` 里"，不是前缀匹配。所以别指望层级自动豁免。
- **实战**：① 迁移时先加 `disable_existing_loggers: False`，再逐步把需要的 logger 显式化；② 写一个启动自检：配置后遍历 `logging.Logger.manager.loggerDict`，把 `disabled=True` 的 logger 名打出来（生产上这行日志能救命）；③ 单测里用 `caplog` 断言"业务 logger 能出日志"，而不是只断言 root；④ 注意 `fileConfig` 的同名参数默认也是 True，从 ini 迁移过来同样会踩。

```python
"""dictConfig 默认禁用已存在的 logger：业务日志静默消失。"""
import io
import logging
import logging.config


def build_config(disable_existing: bool, buf: io.StringIO) -> dict:
    return {
        "version": 1,
        "disable_existing_loggers": disable_existing,
        "formatters": {"plain": {"format": "%(levelname)s %(name)s %(message)s"}},
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "plain",
                "stream": buf,
            }
        },
        "root": {"level": "DEBUG", "handlers": ["console"]},
    }


def scenario(disable_existing: bool, name: str) -> None:
    buf = io.StringIO()
    logger = logging.getLogger(name)          # 模拟"配置前就 import 并建好"的 logger
    logger.setLevel(logging.DEBUG)

    logging.config.dictConfig(build_config(disable_existing, buf))
    logger.info("业务日志：订单已创建")
    logger.warning("业务告警：库存不足")

    print(f"disable_existing_loggers={disable_existing}")
    print("  logger.disabled =", logger.disabled)
    print("  捕获到的输出:", repr(buf.getvalue()))

    # 清理，避免影响下一个场景
    logging.config.dictConfig({"version": 1, "disable_existing_loggers": False})
    logging.getLogger().handlers.clear()


if __name__ == "__main__":
    scenario(True, "app.order")
    print()
    scenario(False, "app.order")

    # 列出被禁用的 logger：生产启动自检就查这个
    buf = io.StringIO()
    early = logging.getLogger("app.payment")
    logging.config.dictConfig(build_config(True, buf))
    disabled = [n for n, lg in logging.Logger.manager.loggerDict.items()
                if isinstance(lg, logging.Logger) and lg.disabled]
    print("\n被禁用的 logger:", disabled)
    print("结论：dictConfig 默认禁用已存在的 logger；迁移时第一件事是显式关掉它")
```

**追问一**：配置里写了 `app` 这个父 logger，为什么 `app.order` 还是被禁用？

→ 解析：`disable_existing_loggers` 的判定是"这个 logger 对象的名字是否出现在配置的 `loggers` 键里"，与层级前缀无关。`app.order` 不在 `loggers` 中，就被当成"配置之外的历史对象"禁用。想豁免只有两条路：把它也写进 `loggers`（哪怕只写 `{"level": "NOTSET"}`），或者全局关掉 `disable_existing_loggers`。层级只影响**消息传播**（`propagate` 到父 logger 的 handler），不影响"是否被禁用"。

**追问二**：为什么"日志变少"比"日志报错"更难排查？

→ 解析：被禁用的 logger 在 `logger.info()` 里第一行 `isEnabledFor` 就返回 False，直接 return，**不抛异常、不打 warning**；调用方看到的是"代码执行了但没输出"。排查只能靠对比"配置前后同一个 logger 的 `disabled`/`handlers`/`effective level`"，或者启动时打印 logger 树快照。所以日志配置变更要像其他配置一样做**启动自检 + 冒烟**：起服务后打一条已知 logger 的测试日志，验证它出现在采集端，而不是等人发现"线上没日志"。
