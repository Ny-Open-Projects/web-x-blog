---
title: [Q7681] 多模态图片 token 折算与请求体积容量账
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7681 · 一张图吃掉几千 token：多模态请求的折算与体积账

难度：P6 ｜ 标签：容量规划、多模态、token 折算
基线：GPT-4o / Claude 3.5+ 图像计费（分辨率→tile→token 折算）；base64 内嵌 vs URL 引用。

**问**：文档解析服务上线多模态批改：每请求 1 张截图 + 提问。上线后单请求成本是纯文本的 20 倍、P99 延迟从 2s 涨到 9s。图片的 token 折算账怎么算？请求体积（base64）在容量上还藏了什么坑？

**答**：**结论**：两张账：① **token 折算账**——图片按分辨率切成 tile 再折算 token（GPT-4o high-detail：宽高各 /512 向上取整得 tile 数，每 tile ~170 token + 基础 85；Claude 按 (宽×高)/750 折算）。所以成本由**分辨率直接决定**：截图 2560×1440 传原图 vs 预缩到 1024 宽，token 差 4-6 倍；② **请求体积账**——base64 内嵌使 HTTP 体积膨胀 1.37 倍，2MB 截图变 2.7MB 请求体，网关/代理的 body 上限、上传带宽与延迟全被它放大。优化链：**客户端预缩放**（按模型 tile 粒度选目标分辨率）> **URL 引用**（传存储链接让供应商侧拉取，省请求体）> **裁剪 ROI**（只传有效区域）。延迟的大头常不是推理而是上传：内嵌 2.7MB 在公网上行要 1-3s。

**取舍**：预缩放的分寸：缩太小 OCR 精度掉——经验是按模型最小可读 tile（512px）对齐，小字文档保底 1024 宽；URL 引用的代价是多一次供应商侧下载（延迟 + 不支持私有网络），且部分接口只支持 base64。ROI 裁剪的信息损失风险最高，只适合"表格/单据"这类结构稳定的输入。

**实战**：token 折算与请求体积账（标准库模拟 GPT-4o 规则）：

```python
# 图片 token 折算账（GPT-4o high-detail 规则模拟）与请求体积账
import base64, math

def image_tokens(width: int, height: int) -> int:
    """GPT-4o high-detail: tile 化折算（tile 512px，~170 tok/tile + 85 基础）。"""
    w = min(width, 2048); h = min(height, 2048)     # 先缩到 ≤2048
    scale = 1024 / max(w, h)
    if scale < 1:
        w, h = int(w * scale), int(h * scale)       # 长边缩到 1024
    tiles = math.ceil(w / 512) * math.ceil(h / 512)
    return tiles * 170 + 85

def req_bytes(img_bytes: int, inline: bool = True) -> int:
    return int(img_bytes * 1.37) if inline else 200  # URL 引用只传链接

TEXT_TOKENS, OUTPUT_TOKENS = 300, 500
price_in, price_out = 2.5 / 1e6, 10 / 1e6   # 元/token 示例

cases = {
    "原图 2560x1440": (2560, 1440, 2_500_000),
    "预缩 1024 宽":    (1024, 576, 400_000),
    "ROI 裁剪 800x600": (800, 600, 180_000),
}
for name, (w, h, img_b) in cases.items():
    tok = image_tokens(w, h) + TEXT_TOKENS + OUTPUT_TOKENS
    body_kb = req_bytes(img_b) / 1024
    cost = tok * price_in + OUTPUT_TOKENS * price_out
    up_s = body_kb * 1024 / (10 * 1024 * 1024)   # 10Mbps 上行
    print(f"{name}: ~{tok} tok, 请求体 {body_kb:,.0f}KB, "
          f"上传~{up_s:.1f}s, 成本 {cost*1000:.2f} 厘/次")

# base64 膨胀实测
raw = b"\x89PNG" + b"x" * 1000
b64_len = len(base64.b64encode(raw))
print(f"\nbase64 膨胀: {len(raw)} -> {b64_len} bytes = x{b64_len/len(raw):.2f}")

# 折算账结论：预缩+URL 引用的组合收益
w0 = image_tokens(2560, 1440)
w1 = image_tokens(1024, 576)
print(f"图片 token: {w0} -> {w1}（省 {(1-w1/w0)*100:.0f}%），"
      f"请求体 3.4MB -> 0.3MB（URL 引用）")
```

**追问 1**：为什么"分辨率→tile→token"的折算对成本是阶梯函数而非线性？
提示：tile 按 512 向上取整，1024 宽和 1023 宽同为 2 列；缩放要按 tile 边界对齐才有收益，缩 100px 可能一分钱不省。

**追问 2**：URL 引用模式有什么安全与一致性问题？
提示：供应商侧拉取需要可访问 URL——签名 URL 过期、私有网络不可达、下载失败被计为推理错误；要设计带重试的签名时效与拉取失败兜底。

**追问 3**：多页 PDF 的页-图转换，页数与 token 的预算怎么控？
提示：页数 × 每页折算 token 上限 = 请求预算，超预算触发分批；分辨率策略按页内容分级（首页高清、正文页 1024），并监控"每文档平均 token"作为容量指标。

## 背诵要点
1. 图片成本由分辨率决定：GPT-4o high-detail 按 512px tile 折算（170 tok/tile + 85 基础），缩放必须按 tile 边界对齐才有收益。
2. base64 内嵌让请求体膨胀 1.37 倍，2MB 图变 2.7MB——上行带宽是延迟大头；URL 引用省体积但引入拉取失败面。
3. 优化链：客户端预缩放（tile 对齐）> URL 引用 > ROI 裁剪；监控"每请求平均图片 token"作为容量指标。

## 复盘追问
1. 上线时为什么没人算过"每请求图片 token"的账？折算规则当时查过供应商文档吗？
2. P99 从 2s 涨到 9s 的分解做过吗——上传、排队、推理各占多少？最后靠哪一招收回了多少？
