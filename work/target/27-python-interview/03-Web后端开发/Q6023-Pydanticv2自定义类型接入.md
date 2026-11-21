---
title: [Q6023] Pydantic v2 自定义类型接入：__get_pydantic_core_schema__
date: 2026-11-20
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6023 · Pydantic v2 自定义类型接入：__get_pydantic_core_schema__

> 难度:★★★★ | 标签:Pydantic 2.x, core_schema, 自定义类型

**问**：想让第三方类型（如自研 Snowflake、ObjectId、Money）直接当 Pydantic v2 字段用，有哪两条接入路径？`__get_pydantic_core_schema__` 的执行时机与 `handler` 是什么？"轻量 AfterValidator" 与 "自定义 core schema" 的成本/能力边界在哪？

**答**：两条路径：1) **轻量路径 `Annotated[X, AfterValidator(fn)]`**——Rust 侧先按原生类型（int/str）校验，通过后把值交给 Python 函数包成目标类型：实现两行、够用，但**每个值一次 Rust→Python 回调**（Q6004 的边界税）；2) **深度路径 `__get_pydantic_core_schema__`**——在类上实现该类方法，Pydantic **构建模型时**（首次定义/import 期，一次性）调用它来生成该字段的 core schema；参数 `handler(source)` 允许你先取"默认推断 schema"再改写（wrap/after 组合）。深度路径的价值：把"解析+构造"完整声明成 schema 节点（如 `int_schema` + `after_validator_function`），仍是一次 Rust 校验+一次 Python 包装，但可以进一步用 `no_op`/自定义 serde 让 dump 也按你的语义走（比如 Snowflake dump 成 int 而不是报错）。能力边界：需要"值域约束/跨类型归一化（str/bytes/int 都能进）"时用深度路径的 `chain_schema`；只是后置检查用轻量路径。错误信息两路径都走 `PydanticCustomError` 才能保持统一的错误体验。

```python
# file: code/03_Web后端开发/q6023_pydantic_custom_type.py
try:
    from pydantic import BaseModel
    from pydantic_core import core_schema, PydanticCustomError
    HAVE_PYDANTIC = True
except ImportError:
    HAVE_PYDANTIC = False

if HAVE_PYDANTIC:
    class Snowflake:
        """第三方风格的自研类型: 接入 Pydantic v2 的深度路径"""
        __slots__ = ("value",)

        def __init__(self, value: int):
            if not (0 < value < (1 << 63)):
                raise ValueError("snowflake 越界")
            self.value = int(value)

        @classmethod
        def __get_pydantic_core_schema__(cls, source_type, handler):
            # 构建期一次性调用: 声明 int 校验 + Python 包装
            return core_schema.no_info_after_validator_function(
                cls,
                core_schema.int_schema(gt=0),
                serialization=core_schema.plain_serializer_function_ser_schema(
                    lambda s: str(s.value)),   # dump 成字符串(防 JS 精度丢失,Q2734)
            )

    class Order(BaseModel):
        id: Snowflake

    o = Order.model_validate({"id": 640918234567890123})
    print("校验通过,字段已是 Snowflake:", type(o.id).__name__, o.id.value)
    print("dump 为 JS 安全字符串:", Order.model_dump(o)["id"])
    try:
        Order.model_validate({"id": -1})
    except Exception as e:
        print("负数被拒:", type(e).__name__)
else:
    # 降级: 无 pydantic 时演示等价的纯 Python 校验逻辑
    class Snowflake:
        def __init__(self, value: int):
            if not (0 < value < (1 << 63)):
                raise ValueError("snowflake 越界")
            self.value = int(value)

    def parse(data: dict) -> dict:
        return {"id": Snowflake(data["id"])}      # Annotated[AfterValidator] 的手写等价

    print("降级说明: 未安装 pydantic(基线 2.x),演示手写等价校验")
    print("校验通过:", parse({"id": 640918234567890123})["id"].value)
    try:
        parse({"id": -1})
    except ValueError as e:
        print("负数被拒:", e)
```

**追问**：1) `handler(source)` 什么时候用？——想让"用户写的类型参数"（如 `Snowflake` 或 `Annotated[Snowflake, ...]` 的元数据）参与 schema 生成时，先 `handler(source)` 拿默认推断再 wrap；直接返回自定义 schema 则完全接管。2) 深度路径怎么支持"str 或 int 都能进"？——`core_schema.chain_schema([union_schema, ...])` 或 `custom_error` 归一化，构建期组合节点；比运行时 if/else 快。3) 为什么 dump 出 JS 要转字符串？——Snowflake 超过 JS `Number.MAX_SAFE_INTEGER`（Q2734），schema 里挂 `to_string_ser_schema` 让 Rust 序列化直出字符串，不进 Python 回调。

## 背诵要点
1. 轻量 = Annotated+AfterValidator（Rust 校验后 Python 回调）；深度 = __get_pydantic_core_schema__（构建期一次性声明 schema）。
2. 深度路径可同时声明序列化行为（to_string_ser_schema），dump 与校验一体化。
3. 接入时机在模型构建期而非每次校验；错误用 PydanticCustomError 保持统一体验。

## 复盘追问
1. 团队里同时存在轻量/深度两种接入，怎么定规范避免滥用？（提示：约定"仅后置校验用轻量；类型要在多处复用/涉及序列化语义才升级深度路径"，评审看 schema 复杂度）
2. 升级 pydantic 小版本后自定义 schema 报不兼容，怎么预防？（提示：核心 schema API 有版本面，锁次版本 + 契约测试覆盖自定义类型字段 + 在 CI 双 pydantic 版本矩阵跑模型用例）
