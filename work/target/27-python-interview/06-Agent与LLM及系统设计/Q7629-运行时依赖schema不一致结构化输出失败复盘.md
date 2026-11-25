---
title: [Q7629] 运行时依赖与生成期 schema 不一致导致结构化输出失败复盘
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7629 · 构建期与运行时 Pydantic 版本不一致导致结构化输出校验全挂的事故复盘

难度：P6 ｜ 标签：事故复盘 / 结构化输出 / 环境一致性

**问**：灰度 pod 上线后，所有结构化输出（schema 约束的 JSON）在 Pydantic 校验阶段报"字段类型不匹配"，而本地与构建镜像里同一份代码测试全绿。复盘发现运行时镜像的 Pydantic 版本与构建期不同。为什么"schema 由 pydantic 生成"会让版本差异直接变成线上故障？怎么把"构建期产物 ≠ 运行时环境"这类问题在部署门禁拦下？

**答**：
- **结论**：机制是**schema 的生成依赖运行时的类定义行为**：Pydantic v2 生成 JSON Schema 的细节（Optional 默认值、额外字段策略、字符串/整数宽松转换、`Literal` 展开）随版本微调——构建期用版本 A 生成的 schema 发给模型，运行时用版本 B 校验返回值，两边规则不一致时模型按 A 的 schema 输出、B 判定违规，校验全挂且**重试也是全挂**（错误在契约层不在采样层）。镜像不一致的来源：基础镜像 floating tag（`python:3.12-slim`）、构建期与运行期分别 pip install 且无锁（Q7102/Q7131 同源）、构建产物（wheel/冻结的 schema 文件）与运行环境重新推导。防线分层：① **镜像不可变**——构建时解析依赖并烧进镜像（多阶段构建，运行期不再 install），运行时与构建期是同一个文件系统；② **schema 指纹**——把生成后的 JSON Schema 哈希写进部署清单，运行时启动自检重新生成并比对哈希，不一致拒启；③ **校验失败监控**区分"采样质量"（部分字段错）与"契约漂移"（全量挂），后者直接触发回滚。
- **取舍**：schema 在构建期"冻结成文件"还是运行时动态生成？冻结（生成后入库作为工件）让模型契约可评审、可 diff、与代码版本绑定，代价是改 schema 要走构建流程；动态生成灵活但把运行时依赖行为引入了模型契约。生产推荐冻结+启动校验，动态生成只用于实验环境。
- **实战**：① CI 产物含 schema 文件 + pydantic 版本钉死进锁文件，镜像构建 `--no-cache --only-binary`；② 启动自检：`hashlib(schema) == manifest.schema_sha`，不一致 fail-fast；③ 监控校验失败率按"错误类型分布"分桶：类型错误比例 >80% 且命中率 100% = 契约漂移签名；④ 升级 Pydantic 的变更单里必须含"schema diff"环节（新旧 JSON Schema 对比），不是跑绿测试就行。

```python
# 契约漂移防线: schema 指纹入部署清单, 运行时启动自检比对
# 基线: Python 3.9+ 标准库
import json
from hashlib import sha256


def schema_fingerprint(schema: dict) -> str:
    return sha256(json.dumps(schema, sort_keys=True).encode()).hexdigest()[:16]


def build_manifest(schema: dict, pydantic_ver: str) -> dict:
    return {"schema_sha": schema_fingerprint(schema),
            "generator": f"pydantic=={pydantic_ver}"}


def startup_check(schema_now: dict, manifest: dict) -> None:
    got = schema_fingerprint(schema_now)
    if got != manifest["schema_sha"]:
        raise SystemExit(
            f"schema 指纹不一致 {got} != {manifest['schema_sha']} "
            f"(generator={manifest['generator']}), 拒启")


def main() -> None:
    # 构建期: strict schema
    build_schema = {"type": "object", "additionalProperties": False,
                    "properties": {"qty": {"type": "integer"},
                                   "note": {"type": ["string", "null"]}}}
    manifest = build_manifest(build_schema, "2.9.0")
    startup_check(build_schema, manifest)          # 一致: 通过
    # 运行时: 版本差异 -> Optional 处理不同, nullable 变 anyOf 缺失
    runtime_schema = {"type": "object",
                      "properties": {"qty": {"type": "integer"},
                                     "note": {"type": "string"}}}  # 漂移
    try:
        startup_check(runtime_schema, manifest)
    except SystemExit as e:
        print("拦截:", str(e)[:60], "...")
    print("OK: 构建期冻结 schema+指纹自检; 契约漂移与采样质量分桶监控")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么"校验全挂 + 重试无效"是契约漂移的判别签名，而不是模型能力问题？
→ 一句话提示：采样问题（模型偶尔输出错字段）表现为部分失败、重试有救；契约漂移是两边规则系统性不一致，模型照着旧 schema 输出永远过不了新校验——失败率 100% 且错误类型集中，此时重试只烧钱。

**追问 2**：升级 Pydantic 时"schema diff"要重点看哪些字段？
→ 一句话提示：Optional/默认值的 nullable 表达（type 数组 vs anyOf）、additionalProperties 默认值、数值宽松转换相关约束、Literal 与枚举的展开方式——这些是 Pydantic 版本间最常变的 JSON Schema 细节，直接决定模型输出契约。

## 背诵要点
- 根因 = schema 由运行时类定义动态生成，构建期/运行时 Pydantic 版本不一致 → 模型按旧契约输出、新契约校验全挂且重试无效。
- 防线：镜像不可变（运行期不再 install）+ schema 指纹（构建冻结入 manifest，启动自检比对拒启）+ 失败分桶监控（全量挂=漂移签名，触发回滚）。
- 生产 schema 冻结成工件（可评审/diff），动态生成仅限实验；Pydantic 升级变更单必含 JSON Schema diff。

## 复盘追问
- 为什么"本地测试全绿"在此类事故里毫无信号？提示：本地与构建共享同一依赖解析结果，事故发生在运行环境重新解析依赖的环节——环境一致性的验证点必须在部署产物（镜像指纹/schema 指纹）上，不在测试机上。
- 启动自检比对 schema 指纹为什么比比对版本号更可靠？提示：版本号相同也可能因构建差异/环境变量影响生成行为，指纹比对的是最终产物本身；版本号可作辅助诊断信息，不作判据。
