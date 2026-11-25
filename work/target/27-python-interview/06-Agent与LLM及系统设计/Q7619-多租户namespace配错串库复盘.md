---
title: [Q7619] 多租户向量库 namespace 配错导致串库复盘
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7619 · 多租户向量库 namespace 配错导致数据串库事故复盘

难度：P6 ｜ 标签：事故复盘 / 多租户 / 向量库隔离

**问**：RAG 平台用向量库按租户隔离（namespace/分区），某租户反馈"搜到了别家的内部文档"。排查发现是新接入的 ingestion 服务把 namespace 参数传错了（默认值兜底到了公共 namespace）。这类隔离事故的完整机理、排查与防线是什么？和"权限与索引不同步"（Q7581）是同一类问题吗？

**答**：
- **结论**：机理分层：① **隔离参数是"约定值"不是"强制值"**——namespace/filter 参数由每个调用方自己传，任何一个新服务/脚本传错（默认值、空串落到默认分区、大小写差异）就跨过隔离边界；向量库本身不校验"这个租户是否有权写这个 namespace"；② **查询侧同病**——查询服务若在某条代码路径漏传 filter（比如重排序后的二次查询），召回不受租户约束；③ **数据已经写串后的扩散**——错误 namespace 的数据被正常查询召回，污染用户上下文，且用户可能已经看过敏感内容（不可撤回）。与 Q7581 的区别：Q7581 是"权限模型变化后索引没同步"（同步问题），本题是"隔离边界靠调用纪律维持"（设计问题）——一个是数据状态漂移，一个是边界没有机制强制。防线：① **写侧**：ingestion 服务不接收裸 namespace 参数，租户上下文从认证态（token/session）解析后在服务端注入，调用方传了也忽略或校验一致性；② **读侧**：检索入口统一封装，filter 必须含租户谓词，缺租户上下文的查询直接拒绝（fail-closed）；③ **审计**：抽样比对"namespace 与数据来源租户"的一致性，写入路径打 tag 便于事后清洗；④ **兜底**：租户间数据物理隔离（独立 collection/独立实例）给最高敏感租户——隔离强度与租户敏感度分级。
- **取舍**：逻辑隔离（namespace+filter）vs 物理隔离（独立 collection/实例）：逻辑隔离成本低、规模灵活，但安全性取决于调用纪律，适合"平台强治理 + 租户间敏感度低"；物理隔离运维成本高（Q6608 多租户成本分界同源），适合金融/医疗类租户。中间态：同 collection + 服务端强制注入 filter + 定期审计，多数 SaaS 的选择。事故处理上，串库数据的"召回不可撤回"意味着除了清洗还要评估泄露面（哪些会话读过、是否需要通知）——这是与一般数据 bug 最大的不同。
- **实战**：落地：① 检索/写入 SDK 收敛为唯一入口，租户谓词在入口层强制注入（中间件模式）；② namespace 命名规则与租户 ID 映射集中在配置中心，禁止各服务自行拼字符串；③ 审计 job：随机抽样对象比对 tag 与 namespace，不一致即告警 + 自动隔离该批次；④ 串库应急 runbook：停写 → 界定泄露面（查询日志按租户+时间切片）→ 清洗错误数据 → 通知与复盘；⑤ 集成测试带"跨租户拒访"用例（租户 A 的查询永远不含租户 B 的文档）。

```python
# 多租户向量库隔离：服务端强制注入租户谓词（fail-closed）
# 基线：Python 3.9+ 标准库；真实场景向量库 metadata filter + SDK 收敛
from dataclasses import dataclass, field


@dataclass
class VectorStore:
    """namespace -> [(doc_id, tenant)]"""
    ns: dict[str, list[tuple[str, str]]] = field(default_factory=dict)


def ingest_sdk(store: VectorStore, ns: str, doc_id: str, tenant: str,
               trusted_tenant: str) -> bool:
    """写入入口：namespace 必须与认证态租户一致，调用方传错也拦。"""
    if ns != f"t-{trusted_tenant}":
        raise ValueError(f"namespace {ns} 与认证租户 {trusted_tenant} 不一致")
    store.ns.setdefault(ns, []).append((doc_id, tenant))
    return True


def search_sdk(store: VectorStore, tenant_ctx: str, query_ns: str | None = None) -> list[str]:
    """fail-closed：缺租户上下文直接拒绝；查询强制带租户谓词。"""
    if not tenant_ctx:
        raise PermissionError("missing tenant context")
    ns = f"t-{tenant_ctx}"
    if query_ns is not None and query_ns != ns:
        raise PermissionError("cross-tenant query rejected")
    return [doc for doc, t in store.ns.get(ns, []) if t == tenant_ctx]


def main() -> None:
    store = VectorStore()
    ingest_sdk(store, "t-a", "d1", "a", trusted_tenant="a")
    ingest_sdk(store, "t-b", "d2", "b", trusted_tenant="b")

    # 事故形态复现：ingestion 传默认 namespace -> 现在被入口拦截
    try:
        ingest_sdk(store, "default", "d3", "b", trusted_tenant="b")
        raise AssertionError("should reject")
    except ValueError:
        pass

    # 查询侧：租户 A 永远看不到 B 的文档；漏传上下文直接拒绝
    assert search_sdk(store, "a") == ["d1"]
    try:
        search_sdk(store, "")
        raise AssertionError("should reject")
    except PermissionError:
        pass
    try:
        search_sdk(store, "a", query_ns="t-b")
        raise AssertionError("should reject")
    except PermissionError:
        pass
    print("OK: 隔离边界必须机制化——服务端注入谓词 + fail-closed, 不靠调用纪律")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么串库事故要按"泄露事件"而不是"数据 bug"处理？
→ 一句话提示：错误数据可能已被召回进用户上下文、被看过甚至被引用——不可撤回；处理要包含泄露面界定（查询日志切片）、影响评估与通知流程，而不只是修数据。

**追问 2**：审计抽样怎么设计才能在污染扩散前发现？
→ 一致性抽查按写入批次（ingestion job 粒度）比 tag 与 namespace，覆盖率要够高且新服务上线首周全检；发现不一致立即冻结该批次并回滚写入——扩散速度取决于审计延迟。

## 背诵要点
- 逻辑隔离（namespace/filter）的安全性取决于调用纪律，任何新调用方传错即跨边界；隔离参数必须由服务端从认证态注入，fail-closed（缺上下文拒绝）。
- 与 Q7581 区分：那是权限-索引同步漂移（状态问题），本题是隔离边界无机制强制（设计问题）；最高敏感租户上物理隔离（独立 collection/实例）。
- 串库 = 泄露事件：停写 → 界定泄露面 → 清洗 → 通知；审计按写入批次比 tag/namespace，新服务首周全检。

## 复盘追问
- 为什么"默认值兜底到公共 namespace"这种参数设计是事故温床？提示：默认值让"没传"静默通过而不是报错；多租户参数的正确默认是"必须显式传、缺失即 fail-closed"，便利性默认值在隔离场景全部反模式。
- 统一 SDK 入口与"各服务直连向量库"的治理账怎么算？提示：直连意味着每个服务复制一遍隔离逻辑，出错面 = 服务数；SDK 收敛是开发成本换"单点强制"，敏感度高的平台必须收敛并配套 SDK 版本治理。
