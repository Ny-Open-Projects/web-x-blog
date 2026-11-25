---
title: "[Q6099] OpenAPI schema 构建成本与启动耗时"
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6099 · OpenAPI schema 构建成本与启动耗时

难度：P6 | 标签：成本工程 | OpenAPI | 启动耗时

**问**：大后端服务接入数百个端点后，K8s 里 readiness 从 2s 变 12s，其中相当部分花在启动阶段的 OpenAPI 文档构建上。FastAPI/Starlette 的 schema 是什么时候构建的？成本随什么增长？怎么把它移出关键路径？

**答**：
结论：FastAPI 默认在**首次访问 `/openapi.json`** 时惰性构建 schema（`app.openapi()` 一次性遍历全部路由、依赖与模型生成 3.1 JSON），部分部署方式（文档预生成脚本、start 时预热）会把它挪到启动期。成本来源：路由数 × 依赖解析 × 模型 JSON Schema 化，其中 Pydantic 模型 `model_json_schema()` 是重头（每个嵌套模型都递归生成 + 引用去重），数百端点数千模型时是秒级 CPU。构建结果默认**不缓存自定义修改后的版本**（每次调用 `app.openapi()` 重新生成，除非覆写并缓存），文档站点刷新一次就重建一次。
取舍：三个降耗位：① 启动后构建一次缓存（覆写 `app.openapi` 返回缓存对象）；② 生产关闭文档路由（`openapi_url=None`）——文档只在构建流水线生成成静态文件发布；③ schema-first 流水线：CI 生成 openapi.json artifact，运行时不构建。
实战：度量口径 = `app.openapi()` 单次耗时 × 访问频率；任何对 schema 的定制（tag、示例）都应走缓存路径，避免每次请求重复计算。

```python
import time, json
from pydantic import BaseModel

# 构建成本的核心：模型 JSON Schema 化（递归 + $ref 去重）
class Item(BaseModel):
    id: int
    name: str
    tags: list[str] = []

class Order(BaseModel):
    id: int
    items: list[Item]
    buyer: "Buyer | None" = None

class Buyer(BaseModel):
    id: int
    nickname: str

Order.model_rebuild()

# schema 靠类生成：构建成本与端点引用的模型数量线性相关

t0 = time.perf_counter()
schema = Order.model_json_schema()
one = (time.perf_counter() - t0) * 1000
print(f"单模型 schema 化: {one:.2f} ms, $ref 复用 Buyer: {'Buyer' in json.dumps(schema)}")

# 路由级模拟：每个端点构建响应 schema 一次
class FakeRoute:
    def __init__(self, name, model):
        self.name, self.model = name, model
routes = [FakeRoute(f"ep{i}", Order) for i in range(300)]

t0 = time.perf_counter()
for r in routes:
    json.dumps(r.model.model_json_schema())
full = (time.perf_counter() - t0) * 1000
print(f"300 端点全量构建: {full:.0f} ms（启动期/首次文档访问的一次性 CPU）")

# 降耗位1：构建一次缓存（FastAPI 覆写 app.openapi 的同构写法）
class FakeApp:
    def __init__(self, routes):
        self.routes = routes
        self._cache = None
    def openapi(self):
        if self._cache is None:
            self._cache = {r.name: r.model.model_json_schema() for r in self.routes}
        return self._cache

app = FakeApp(routes)
t0 = time.perf_counter(); app.openapi(); t1 = time.perf_counter()
app.openapi(); t2 = time.perf_counter()
print(f"首次构建 {(t1-t0)*1000:.0f} ms → 缓存后 {(t2-t1)*1000:.3f} ms")

# 降耗位2：生产关文档路由（openapi_url=None），CI 里生成静态文件
def build_static_openapi(app, path):
    blob = json.dumps(app.openapi(), ensure_ascii=False)
    # 生产：写文件发布；运行时 0 构建成本
    return f"static openapi {len(blob)//1024} KB → 发布为 artifact"
print(build_static_openapi(app, "openapi.json"))

# 降耗位3：启动自检只校验"可构建"，不做全量构建
t0 = time.perf_counter()
ok = Order.model_json_schema() is not None
print(f"readiness 只做冒烟校验 {(time.perf_counter()-t0)*1000:.2f} ms（不做 300 端点全量）")
```

**追问 1**：为什么 FastAPI 选择"首次访问才构建"而不是 import 时构建？
- 追问 2 层：构建需要全部路由/依赖注册完成且模型命名空间稳定；import 时构建会被插件/动态路由打乱顺序，惰性化换取正确性。
- 追问 3 层：代价是首次文档访问的冷延迟（秒级），高频访问文档站点的团队必须自己加缓存层。

**追问 2**：schema-first（先有 openapi.json 再实现）与 code-first 的成本差异？
- 追问 2 层：schema-first 把构建移到 CI（生成 artifact + 契约 diff + 客户端代码生成），运行时零构建；code-first 灵活但把校验/文档成本压进服务进程。
- 追问 3 层：混合形态是"code-first 生成 + CI 发布静态文档"，生产进程 `openapi_url=None`，文档走 CDN。

## 背诵要点
1. OpenAPI schema 默认首次访问惰性构建，成本 = 路由数×依赖解析×模型递归 schema 化，数百端点秒级。
2. 降耗三件套：openapi() 结果缓存覆写、生产 openapi_url=None + CI 发布静态文档、readiness 只做冒烟校验。
3. 定制 schema 必须走缓存路径，否则每次文档访问重复全量计算。

## 复盘追问
1. 为什么 readiness 变慢没被启动日志暴露？——构建发生在首个文档请求或预热逻辑里，没有计时埋点；给 openapi() 加耗时日志即可定位。
2. 模型越多越慢的根本解法是什么？——按服务拆分 API 域，或 schema-first 把构建移出运行时。
