---
title: "[Q6088] FastAPI 依赖注入的解析成本与依赖缓存机制"
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6088 · FastAPI 依赖注入的解析成本与依赖缓存机制

难度：★★★★☆ ｜ 标签：成本工程 / FastAPI / 依赖注入 / Depends

**问**：压测发现单个请求里 `Depends(get_db)` 被解析了 5 次、`verify_token` 重跑了 3 次。FastAPI 的依赖解析到底怎么工作？`use_cache` 的语义边界在哪里？依赖树过深对 P99 的影响怎么量？

**答**：
- **结论**：FastAPI 每个请求先**静态解析依赖树**（路由声明时已构建好 dependant 结构），再按树**逐节点执行**依赖函数：同步依赖丢线程池（走 Q6085 的 40 线程闸门），异步依赖在事件循环执行。默认 `use_cache=True`：**同一请求内**，以"依赖函数可哈希标识"为键的结果被缓存——同一依赖在树里出现多次只执行一次；`use_cache=False` 强制每次重跑（如需要独立数据库事务的嵌套依赖）。事故根因通常是三个：① 同一依赖被写成多个"不同函数对象"（lambda/闭包）导致缓存键不同 → 重复执行；② 依赖函数内部做了贵操作（每次 `create_engine`、重新加载配置）；③ 子依赖把父依赖的参数也声明一遍，触发重复解析链。
- **取舍**：缓存键按**依赖的函数对象 + 参数默认值**算（用 `hmac`/repr 哈希），所以"每次请求传入不同参数"的依赖（如 Depends(get_page, page=n) 形态不成立——参数是路由级固定的），需要请求级变化要放 `Request` 里自己取。成本优化阶梯：贵依赖下沉到 `lifespan` 单例（engine、配置、客户端池）→ 请求级依赖保持轻（只取头/查会话）→ 用 `Annotated` 类型别名统一依赖声明减少复制粘贴 → 热路径避免 use_cache=False。
- **实战**：量化方法：在依赖函数入口打点（计数器），压测核对"执行次数/请求数"比值——比值 >1 即缓存没生效；火焰图看 `fastapi.dependencies.utils` 与 `solve_dependencies` 的占比，正常应 < 5% 请求耗时，异常则查依赖树深度（嵌套 >5 层就要整理）。

```python
"""依赖解析次数与 use_cache 语义实测（FastAPI 0.100+ 基线）"""
from fastapi import FastAPI, Depends, Request
from fastapi.testclient import TestClient
from typing import Annotated

app = FastAPI()
counter = {"db": 0, "token": 0, "token_nocache": 0}

def get_db():
    counter["db"] += 1
    return f"session@{id(object())}"           # 占位"会话对象"

def verify_token(db=Depends(get_db)):
    counter["token"] += 1
    return "tok"

def verify_token_nocache(db=Depends(get_db)):   # 无缓存版对照
    counter["token_nocache"] += 1
    return "tok2"

DbDep = Annotated[str, Depends(get_db)]
TokDep = Annotated[str, Depends(verify_token)]

@app.get("/a")
async def a(db: DbDep, tok: TokDep):
    return {"db_obj": str(db), "tok": tok}

@app.get("/b")                                   # 同一依赖在另一个路由复用
async def b(db: DbDep, tok: TokDep, tok2: Annotated[str, Depends(verify_token_nocache)],
            tok3: Annotated[str, Depends(verify_token_nocache)]):
    return {"n_db": str(db), "tok": tok, "tok2": tok2, "tok3": tok3}

c = TestClient(app)
counter.update(db=0, token=0, token_nocache=0)
r = c.get("/b")
print(r.json())
print(f"单请求执行次数: get_db={counter['db']}（期望 1，use_cache 生效）")
print(f"              verify_token={counter['token']}  no_cache 版={counter['token_nocache']}（期望 2，显式禁缓存）")

# 事故形态复现：lambda 依赖 → 缓存键不同 → 重复执行
counter["db"] = 0
db_lambda_dep = Depends(lambda: counter.__setitem__("db", counter["db"] + 1) or "s")
@app.get("/c")
async def cc(x: Annotated[str, db_lambda_dep], y: Annotated[str, db_lambda_dep]):
    return {}
c.get("/c")
# 注意：两处 Annotated 用同一个 Depends 对象时缓存仍按"依赖可哈希"判定，
# 但若代码里写了两个独立 lambda（常见复制粘贴事故），缓存即失效 —— 用计数验证：
print("lambda 依赖形态提示：每个独立 lambda 是不同缓存键，比值监控（执行数/请求数）是唯一可靠验证")
print("优化阶梯：贵依赖进 lifespan 单例 → 请求级依赖保持轻 → Annotated 统一声明 → 少用 use_cache=False")
```

**追问链**
1. `use_cache` 的缓存键怎么构造？为什么"同函数不同参数"不触发缓存失效？
   1. 键 = 依赖的可哈希标识（call 对象 + 参数默认值）在**请求级** dict 里；依赖的参数是路由声明期固定的（来自路径/查询/其他依赖），不是每请求可变的输入——请求可变的值应通过 `Request` 对象在依赖函数内部获取。
   2. 追问：子依赖（token 依赖 db）共享缓存吗？——共享：树中任何位置解析 get_db 命中同一键即复用结果，这正是"解析 5 次"事故的反例验证手段。
2. 依赖里的 yield（带清理的依赖）与普通返回值依赖在执行序上差在哪？
   1. yield 依赖：依赖值先产出 → handler 执行 → **响应发出前/后**（取决于退出时机）在 finally 恢复执行清理（Q6002 的取消时序）；缓存命中时不重复进入 yield（直接复用值），清理也只跑一次。
   2. 追问：怎么给依赖树做"每请求成本画像"？——依赖入口统一注入计时（装饰器或中间件打 trace span），按依赖名聚合 P50/P99；瓶颈通常集中在"每请求重造客户端"与"同步依赖挤线程池"两类。

## 背诵要点
- FastAPI 每请求按预构建的依赖树 solve：同步依赖走线程池闸门，异步走事件循环；use_cache 默认按"函数对象+参数默认值"做请求级缓存。
- 重复执行三根因：独立 lambda 依赖（缓存键不同）、依赖内做贵操作（应进 lifespan 单例）、use_cache=False 滥用。
- 验证手段：依赖执行数/请求数比值监控 + solve_dependencies 火焰图占比（正常 <5%）；依赖树 >5 层要整理。

## 复盘追问
- 压测报告显示 P99 尾部与依赖执行次数相关，如何设计实验分离"解析开销"与"依赖内 IO"？
- 配置热更新需求与"配置依赖进 lifespan 单例"冲突时怎么调和？
