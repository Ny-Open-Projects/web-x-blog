# 27 号课扩量缺口方案（_GAP_PLAN）

> 生成：2026-11-18 夜班第 0.5 步。扩量目标 5000+，缺口 ≈2000。本文件是所有批次的出题清单，按缺口逐个出题，不许漫游。
> 题号分配：01→Q5001-5499 / 02→Q5501-5999 / 03→Q6001-6499 / 04→Q6501-6999 / 05→Q7001-7499 / 06→Q7501-7999；笔试题 A100 起（编程题+场景题）。

## 01 语言核心与底层（源库未覆盖/过浅）

1. 3.12 PEP 695 type 语句与 TypeAliasType 的运行时行为
2. 3.13 / 3.14 free-threading 下的 dict/list 线程安全语义边界
3. PEP 649/749 延迟注解求值（3.14 默认）对 typing 生态的影响
4. `sys.monitoring`（PEP 669）替代 sys.settrace 的成本模型
5. `__static_attributes__` / 3.13 编译器产物与代码分析工具
6. immortal objects 在 3.12+ 的实际表现与 refcount 观测
7. PyPy/Jython 语义差异常考点：GIL、GC、str 互操作
8. `frame.f_trace_lines/ops` 与调试器实现原理
9. PEP 657 错误位置细粒度化（3.11 traceback）与异常组 ExceptionGroup 深挖
10. `except*` 语义边界：嵌套、再抛、与 TaskGroup 的配合
11. 描述符协议 3.13 `__set_name__` + slot wrapper 细节
12. `typing.TypeVar` 默认值（PEP 696）与泛型协议实战
13. `functools.cache` vs `lru_cache` 内存画像与 COW 陷阱
14. zipapp / 冻结导入 / PEX 打包的导入器差异
15. `gc.get_referents` 定位泄漏环 + tracemalloc 快照对比实战
16. `pickle` 协议 5 out-of-band 缓冲与安全边界
17. 3.12 f-string PEP 701 语法解禁后的嵌套陷阱

## 02 并发与网络工程

1. 3.13 asyncio 独立解释器 / PythonRunner 与子解释器并行（PEP 734）
2. `asyncio.eager_task_factory`（3.12）降低启动延迟
3. TaskGroup 异常聚合的 `ExceptionGroup` 拆包与部分失败回滚
4. uvloop 与默认 loop 的事件循环成本差异实测方法
5. asyncio `timeout` contextmanager 嵌套/重入语义
6. `loop.run_in_executor` 与线程池饱和时的背压设计
7. socket `MSG_PEEK` / SO_REUSEPORT 多进程 accept 风暴
8. TLS 1.3 0-RTT 重放风险与 ssl.SSLContext 配置
9. HTTP/2 多路复用下的队头阻塞与 Python 客户端选型
10. 心跳/半开连接检测的保活矩阵（TCP keepalive vs 应用层 ping）
11. 结构化并发取消风暴：取消时序与 cleanup 幂等
12. `concurrent.futures` 全局解释器下线程池大小公式化推导
13. 多进程 `multiprocessing.shared_memory` 生命周期与泄漏
14. `socket.sendfile` 零拷贝路径与限制
15. 代理链路（SOCKS/HTTP CONNECT）的实现细节与超时分层
16. grpc/protobuf 流式调用在 asyncio 下的取消传播

## 03 Web 后端开发

1. FastAPI `lifespan` 与启动失败回滚编排
2. FastAPI 依赖 `yield` 的 finally 在请求取消时的时序
3. Pydantic v2 `model_config` 性能矩阵：strict/lax、validate_assignment 成本
4. Pydantic v2 Rust 核心序列化边界：自定义 serializer 何时反而更慢
5. Starlette middleware 与 ASGI 纯函数中间件的取舍
6. SSE / WebSocket 在 uvicorn 多 worker 下的会话粘性
7. Django 5 async views 与 ORM sync 桥接的线程池耗尽
8. Django select_for_update(skip_locked=true) 任务队列模式
9. DRF 限流的自定义节流键与分布式计数
10. 优雅停机：SIGTERM → drain → 连接排空清单（K8s preStop）
11. 幂等键设计：请求指纹 + 存储层约束兜底
12. 文件上传大对象：分片/直传 OSS/校验回执
13. JWT vs opaque token 撤销矩阵与双 token 轮换
14. OpenAPI 契约测试（schemathesis 思路）与破坏性变更防线
15. 服务网格下 Python 服务的超时预算分配（重试预算）
16. 3.12+ `perf` profiler 与 py-spy 生产定位路径

## 04 数据库与缓存

1. SQLAlchemy 2.0 `Session.merge` vs `get` 身份图陷阱
2. SQLAlchemy 2.0 异步引擎 + 事务边界与超时传递
3. PostgreSQL 行级锁矩阵：FOR UPDATE / SKIP LOCKED / NOWAIT
4. MVCC 膨胀：autovacuum 调参实例与 dead tuple 监控
5. 分区表路由与查询裁剪（PG declarative partitioning）
6. Redis 7 Functions vs Lua 脚本的部署与原子性
7. Redis Cluster hash tag 的批量/事务约束
8. 缓存一致性：binlog 订阅（Canal 思路）vs 双删的失败矩阵
9. Redis 大 key 扫描（SCAN + memory usage）与拆桶方案
10. 本地缓存两级架构：进程内 LRU + Redis 的失效广播
11. 连接池参数推导：pool_size/max_overflow/timeout 与并发上限
12. 慢查询治理：pg_stat_statements → 计划回归（pg_plan_insights 思路）
13. 幂等表设计：唯一约束 + 状态机 + 事务发件箱
14. 游标流式读取大结果集（server-side cursor）与内存曲线
15. 乐观锁版本号 vs CAS vs 隔离级别的选型矩阵
16. Redis `WAIT`/副本确认与主从切换丢写窗口

## 05 数据分析与工程化

1. pandas 2.x Arrow dtype 后端（`dtype_backend="pyarrow"`）迁移矩阵
2. pandas copy-on-write（CoW）默认化后的链式赋值坑
3. pytest-xdist 分片策略与用例独立性改造
4. property-based testing（hypothesis）在序列化层的落地
5. 环境可复现：uv lock / pip-tools 的锁链与镜像分层
6. CI 中的 Python 缓存策略（wheel 缓存、pre-commit 秒级化）
7. 结构化日志：structlog 上下文绑定与 trace_id 贯穿
8. OpenTelemetry Python：手动 span vs auto-instrumentation 成本
9. SLO 燃烧率告警的窗口公式与误报压测
10. 特征/数据漂移监控的统计口径（PSI/KS）实现
11. A/B 平台的分流哈希一致性（murmur + 盐）与SRM 检查
12. 大表导出内存治理：chunked parquet 流水线
13. mypy strict 化路线图与三方库 stub 缺失应对
14. ruff + pyright 的规则分层与 monorepo 增量检查
15. 预发布数据脱敏：确定性与格式保留加密取舍
16. 灰度发布 Python 服务的指标护栏（错误率/延迟分位自动回滚）

## 06 Agent 与 LLM 及系统设计

1. Agent 评估：LLM-as-judge 的偏差校准与固定集回归
2. ReAct 循环的步数预算与死循环熔断设计
3. RAG 分块策略矩阵：语义分块 vs 递归 vs 版式感知
4. 混合检索 RRF 融合权重与 rerank 成本分层
5. 向量库选型：pgvector / milvus / qdrant 的一致性与过滤能力
6. Embedding 模型更换的迁移路线：双写-回填-切换
7. 多 Agent 编排的消息总线 vs 图编排（langgraph 思路）
8. MCP Streamable HTTP 会话恢复与工具权限治理
9. LLM 网关：限流/预算/降级矩阵与多供应商路由
10. Prompt 版本管理与灰度实验平台化
11. 流式输出的背压与取消（SSE 中断的计费一致性）
12. 结构化输出：json schema 约束解码的失败重试设计
13. 一致性哈希在多租户分片网关的实测迁移量
14. SAGA 补偿在 LLM 工具调用链的落地（部分失败回滚）
15. 敏感数据出站审计：工具调用白名单 + 脱敏中间层
16. 长上下文成本工程：上下文裁剪/摘要缓存的预算模型

## 笔试题（A100 起，编程题/场景题）

A100 分块日志聚合器（生成器+内存上限）｜A101 限流器四连（令牌桶/滑动窗口/分布式/预热）｜A102 幂等下单场景题（超时+重试+唯一约束）｜A103 缓存击穿场景题（singleflight + 逻辑过期）｜A104 分布式任务分片场景题（SKIP LOCKED + 心跳续租）
