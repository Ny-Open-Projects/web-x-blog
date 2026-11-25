---
title: [Q7123] Excel 导入类型推断破坏下游对账事故复盘
date: 2026-11-21
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7123 · Excel/CSV 导入类型推断破坏下游对账的事故复盘

难度：P6 ｜ 标签：事故复盘 / 数据质量 / pandas

**问**：业务方上传一份 Excel 对账单，导入后金额列部分行变字符串、部分行变数字；"00123" 这样的单号丢了前导零；"3/5" 被解析成日期。同一份数据每次上传口径还不一样。这类事故的机制是什么？怎么设计导入层让类型推断失效不了？

**答**：
- **结论**：机制是**按单元格/按行的启发式推断**：Excel 单元格自带类型（文本格式的 "123" 是字符串，数字格式是浮点），pandas `read_excel` 对字符串列再做逐元素转换，混合列就退化成 object；CSV 更狠——每行独立嗅探，前 1000 行没出现带前导零的值，后面行就转 int。三类经典破坏：前导零（单号/编码转 int 丢失）、长数字精度（银行卡号转 float 丢尾数，float 只有 15 位有效数字）、日期歧义（"3/5" 按区域解释成 3 月 5 日或 5 月 3 日）。防线不是"提高推断能力"而是**关掉推断**：导入层强制 `dtype=str` 读入 → 显式 schema 校验（正则/长度/校验位）→ 按业务类型显式转换（金额用 Decimal、编码保字符串、日期指定格式 `dayfirst=False` 固定口径）——"先当字符串审，再按 schema 转"。
- **取舍**：强制 str 读入会让内存上涨（全列字符串）且丢掉数值加速，要不要全量 str？对账类导入（金额必须逐分精确）必须 str+Decimal；分析类导入（丢了重读就行）可以宽松。另一个方案是上游约束：给业务方发固定模板 + 单元格预设格式，把问题左移——但要接受"模板约束不了人"，导入层校验仍是最后防线，两者是互补不是二选一。
- **实战**：① 导入函数签名里 schema 是必填参数（列名→类型+正则），没有 schema 不许 import；② 校验失败行进隔离区（Q1723 脏数据隔离）并回执给上传人，不许静默修；③ 金额转 Decimal 后入库 DECIMAL(18,4)，禁 float；④ 回归测试集里固化这三类坏样本（前导零/18 位卡号/歧义日期）作为门禁用例。

```python
# 导入层防线: dtype=str 读入 -> schema 校验 -> 显式转换; float 精度演示
# 基线: Python 3.9+ 标准库
import re
from dataclasses import dataclass
from decimal import Decimal


@dataclass
class ColumnSpec:
    name: str
    kind: str              # "code" | "amount" | "date"
    pattern: str = ""


def parse_cell(raw: str, spec: ColumnSpec) -> object:
    if spec.kind == "code":
        if not re.fullmatch(spec.pattern, raw):
            raise ValueError(f"{raw}: 编码格式非法(前导零丢失检查)")
        return raw                                   # 保持字符串
    if spec.kind == "amount":
        return Decimal(raw)                          # 禁 float
    if spec.kind == "date":
        return f"2026-{raw[-2:]}-{raw[:2]}"          # 固定口径, 不嗅探
    raise ValueError(spec.kind)


def main() -> None:
    # 前导零: str->int 丢零; 18位卡号: float 丢精度
    assert str(int("00123")) == "123"
    assert int(float("622202123456789012")) != 622202123456789012
    specs = [ColumnSpec("order_no", "code", r"\d{5}"),
             ColumnSpec("card", "code", r"\d{18}"),
             ColumnSpec("amount", "amount"),
             ColumnSpec("day", "date")]
    row = {"order_no": "00123", "card": "622202123456789012",
           "amount": "1234.56", "day": "03/05"}
    out = {s.name: parse_cell(row[s.name], s) for s in specs}
    assert out["order_no"] == "00123" and isinstance(out["card"], str)
    assert out["amount"] == Decimal("1234.56")
    assert out["day"] == "2026-05-03"                # 口径固定
    bad = dict(row, order_no="123")
    try:
        parse_cell(bad["order_no"], specs[0])
    except ValueError as e:
        print("拦截:", e)
    print("OK: str读入+schema校验+显式转换; 金额Decimal/编码保str/日期锁口径")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么银行卡号 18 位转 float 会丢尾数而 Decimal 不会？
→ 一句话提示：float 是二进制双精度只有 15-17 位十进制有效数字，超过即舍入；Decimal 是十进制精确表示——凡是"标识符"（卡号/单号/手机号）都应按字符串处理，语义是码不是数。

**追问 2**：CSV 每行独立嗅探导致"同列类型漂移"怎么在 pandas 里根治？
→ 一句话提示：`read_csv(..., dtype=str)` 全列读字符串后走显式转换；或新版指定 `dtype_backend` 与 `converters`——原则是推断只允许发生在有 schema 的边界上，不允许发生在数据内部。

## 背诵要点
- 机制 = 启发式逐行推断：前导零丢失、18 位数字 float 丢精度、日期区域歧义三大破坏；防线是"str 读入 + schema 校验 + 显式转换"。
- 对账/标识符类强制 str+Decimal（码不是数），分析类可宽松；模板约束左移与导入校验互补，后者不可省。
- 校验失败行进隔离区+回执，不静默修；三类坏样本进回归门禁。

## 复盘追问
- 为什么"提高推断能力"是错误方向？提示：推断的目标是猜对，但业务类型只有业务方知道，猜对的收益永远低于 schema 显式声明的确定性——推断越聪明掩盖的口径问题越深。
- 上线后怎么持续发现口径漂移？提示：导入层对每列记录"转换规则版本 + 失败率"，失败率突增说明上游模板/口径变了，比等对账不平才发现早一个周期。
