---
title: "[Q6190] DRF partial=True 的三态：缺席、null 与默认值"
date: 2026-11-23
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6190 · DRF partial=True 的三态：缺席、null 与默认值

难度：P6 ｜ 标签：DRF、Serializer、partial、PATCH、required、默认值

**问**：PATCH 接口写着 `Serializer(instance, data=request.data, partial=True)`，用户只改昵称，结果 bio 被清空、status 被重置成 `active`。`partial=True` 到底跳过了什么？它保证"没传的字段不写"吗？"字段缺席 / 显式 null / 有值"这三种状态在 DRF 里怎么区分？

**答**：
结论：`partial=True` 只做一件事——**跳过 required 校验**（缺字段不报错），它不改变"哪些字段会被写"的语义。真正的坑在业务代码：如果 update 里用了 `data.get(field, default)`、或者把 `validated_data` 和模型默认值合并，未传字段就会被默认值顶掉；`ModelSerializer.update()` 本身是 `setattr(instance, k, v) for k, v in validated_data.items()`，只写传进来的键。所以"被清空"几乎总是自己引入的合并逻辑。

取舍：要正确表达三态，必须区分"键是否存在"与"值是否为 None"：缺席 = 不动（`if "bio" in request.data`）；显式 `null` = 清空（字段需 `allow_null=True`，模型列需 nullable）；有值 = 覆盖。DRF 的 `validated_data` 只包含"传了且合法"的字段，可以直接用来判断缺席；Pydantic 侧对应 `model_fields_set` / `exclude_unset`。别用 `getattr(validated_data, name, default)`——那就是把"缺席"和"默认"混为一谈的根源。

实战：事故形态是"运营在后台只改了头像，结果用户简介和状态全被重置；前端因为 PATCH 返回 200 也不报警"。另一个隐性问题是 PUT 和 PATCH 共用一套序列化器：PUT 缺字段不报错（本该 400），前端以为"整体替换"其实只改了一部分。下面用纯 Python 模拟 DRF 的校验与 update 语义，展示三态差异与"default 兜底"造成的重置。

```python
DEFAULTS = {"nickname": "匿名", "bio": "", "status": "active"}
REQUIRED = ("nickname", "status")


def validate(data, partial):
    errors = {}
    if not partial:
        for name in REQUIRED:
            if name not in data:
                errors[name] = "required"
    return errors


def update(instance, data, partial):
    errs = validate(data, partial)
    if errs:
        return instance, errs
    out = dict(instance)
    for key, value in data.items():          # 只写传了的字段
        out[key] = value
    return out, {}


instance = dict(DEFAULTS)

print("[1] PUT 缺字段 -> 400:", update(instance, {"nickname": "bob"}, partial=False)[1])
print("[2] PATCH 缺字段 -> 允许:", update(instance, {"nickname": "bob"}, partial=True))


def bad_update(instance, data, partial):
    errs = validate(data, partial)
    if errs:
        return instance, errs
    out = {}
    for key, default in DEFAULTS.items():
        out[key] = data.get(key, default)    # 未传字段被"默认值"顶掉
    return out, {}


print("[3] 顺手用 default 兜底 -> 没传的字段被重置:", bad_update(instance, {"nickname": "bob"}, True)[0])
print("[4] 显式传 null 清空 bio:", update(instance, {"bio": None}, True)[0]["bio"])
print("[5] PATCH 三态：字段缺席=不动、null=清空、有值=覆盖")
```

**追问一**：为什么 PUT 和 PATCH 不能共用一套校验？—— PUT 语义是"整体替换"，缺字段应报 required（否则前端以为清空了、实际没动，契约不一致）；PATCH 是"局部更新"，缺字段表示不动。共用 partial 会让 PUT 静默接受不完整请求，或者让 PATCH 误报必填。正确做法是同一模型两套序列化器（`XxxCreateSerializer` / `XxxUpdateSerializer`），或显式分支。

**追问二**：`partial=True` 和字段的 `default` 一起用，最隐蔽的坑是什么？—— create 路径里 default 是"没传就用默认值"，update 路径里如果也照搬这套逻辑，就变成"没传就重置为默认值"。同一个序列化器同时服务创建和更新时，这个差异极难发现。判断方法：在 update 里打印 `validated_data.keys()`，看它是否只有客户端真正传的字段。

## 背诵要点
- `partial=True` 只跳过 required 校验，不改变写入语义；`ModelSerializer.update` 只 setattr `validated_data` 里的键。
- 三态要显式区分：`"bio" in request.data`（缺席=不动）、`None`（清空，需 allow_null）、有值（覆盖）。
- 用 `get(field, default)` 合并 = 把"缺席"当"重置"，PUT/PATCH 共用序列化器会放大这个 bug。

## 复盘追问
- PATCH 只改昵称却把其他字段重置，如何定位并给出三态实现？（缺席/null/有值、validated_data 键集）
- 为什么 PUT 与 PATCH 应分序列化器？共用的后果是什么？（整体替换 vs 局部更新、required 语义）
