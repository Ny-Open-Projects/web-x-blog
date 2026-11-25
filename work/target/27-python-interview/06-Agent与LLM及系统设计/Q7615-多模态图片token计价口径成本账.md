---
title: [Q7615] 多模态图片 token 计价口径与成本账
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7615 · 多模态图片的 token 计价口径与成本账

难度：P6 ｜ 标签：成本工程 / 多模态 / 计价

**问**：客服 Agent 支持用户发截图，上线后单会话成本涨了 5 倍，远超预期。查账发现"图片很贵"，但具体贵在哪、怎么算都说不清。各家图片 token 的计价口径是什么？多模态成本账怎么建、怎么控？

**答**：
- **结论**：图片 token 的计价口径三类：① **分辨率换算**（主流）——按 (宽×高) 映射到固定 patch/tile 数：OpenAI 系按 32px patch 数 × 系数，多 tile 大图加基础费；Anthropic 系按 (宽×高)/750 折算 token；Gemini 按 258px tile 计。共同规律：**token ∝ 像素面积**，且多数厂商有尺寸上限/自动缩放。② **视频/音频按时长**换算。③ 同图多轮重发——**每轮对话里历史消息的图片都会重新计费**（除非命中 prompt 缓存且图片位于缓存前缀），这是多轮客服场景成本爆炸的主因：一张 1k-token 图 × 10 轮 = 10k token 图费，用户感知不到。此外 base64 内嵌还会撑大请求体（见 Q7612）。5 倍成本通常 = 图片 token 单价高 + 历史图重发 + 无压缩上传三因叠加。
- **取舍**：控制手段按 ROI：① **压缩到够用分辨率**：OCR 类任务 1024-1536px 足够，缩到长边 1024 通常 token 降 50-75% 且精度几乎无损（先小样本实测精度-成本曲线）；② **历史图替换为文字**：多轮对话里，图片一经识别/总结就替换为文字描述（结构化 OCR 结果），只保留文字进历史——这是多轮场景最大的省钱项；③ **降质分级**：入口按意图分类（需要看图 vs 不需要），无关图拒收；低价值场景用支持图片的 mini 档模型；④ **缓存前缀放图**：固定图（商品图/说明图）放 prompt 缓存命中区，动态图放后段；⑤ 预算护栏：单会话图片 token 上限、单请求图数上限，超限走降级（只收文字）。
- **实战**：建模步骤：① 抽样统计图片尺寸分布 × 各家公式，算"每图 token"基线；② 从 trace 按会话算"图片费占比"，区分"首次识别"与"历史重发"两桶；③ 上线压缩与历史替换，对拍任务完成率（识别精度回归）；④ 建单位经济账：每会话图片成本、每解决单成本，设毛利护栏；⑤ 复盘项：图片费占比 >30% 告警，尺寸分布漂移（用户开始传长截图）触发重新测算。

```python
# 图片 token 计价模型（tile 口径）与多轮成本账（标准库模拟）
# 基线：Python 3.9+；真实公式按各家文档实现（示例为常见 tile 模型）

import math
from dataclasses import dataclass


@dataclass
class ImagePricing:
    tile_px: int            # tile 边长（如 512）
    tokens_per_tile: int    # 每 tile token
    max_long_edge: int      # 厂商自动缩放上限
    base_tokens: int = 0


def image_tokens(pricing: ImagePricing, width: int, height: int) -> int:
    """先按上限缩放，再按 tile 数计费（示例口径，以厂商文档为准）"""
    scale = min(1.0, pricing.max_long_edge / max(width, height))
    w, h = int(width * scale), int(height * scale)
    tiles = math.ceil(w / pricing.tile_px) * math.ceil(h / pricing.tile_px)
    return pricing.base_tokens + tiles * pricing.tokens_per_tile


def session_image_cost(pricing: ImagePricing, img: tuple[int, int], turns_with_img: int,
                       price_per_1k: float, history_replace: bool) -> float:
    """多轮里图片是否重发：替换为文字后只计首次"""
    count = 1 if history_replace else turns_with_img
    return image_tokens(pricing, *img) * count / 1000 * price_per_1k


def main() -> None:
    p = ImagePricing(tile_px=512, tokens_per_tile=850, max_long_edge=2048, base_tokens=85)

    # 用户原始截图 2000×1500
    t_raw = image_tokens(p, 2000, 1500)
    # 压缩到长边 1024
    t_small = image_tokens(p, 1024, 768)
    assert t_small < t_raw * 0.5, "长边 1024 应降到一半以下"
    print(f"原图 {t_raw} tok → 压缩后 {t_small} tok（省 {(1 - t_small / t_raw) * 100:.0f}%）")

    # 多轮账：10 轮都带图历史 vs 历史替换为文字
    cost_resend = session_image_cost(p, (2000, 1500), 10, 3.0, history_replace=False)
    cost_replace = session_image_cost(p, (1024, 768), 10, 3.0, history_replace=True)
    print(f"10 轮图重发 ¥{cost_resend:.3f} vs 压缩+历史替换 ¥{cost_replace:.3f}"
          f"（省 {(1 - cost_replace / cost_resend) * 100:.0f}%）")
    assert cost_replace < cost_resend * 0.2
    print("OK: 计价口径=面积tile 模型；压缩+历史文字替换是多模态降本两大杠杆")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么"历史图替换为文字"要防信息丢失？
→ 一句话提示：图片首次识别就摘要时，后续轮次可能需要图中细节（用户追问"左下角数字"）；正确做法是结构化识别结果（OCR 全文/关键区域坐标）入历史，摘要只压缩视觉信息、保留可检索的文本层，必要时带图 ID 重发原图。

**追问 2**：prompt 缓存对多模态的适用边界？
→ 一句话提示：图片在前缀缓存区才能省钱且要求逐字节一致——适合"固定参考图"场景；用户上传的动态图放前缀既不命中还把缓存前缀打碎，动态内容永远放后段。

## 背诵要点
- 图片 token ∝ 像素面积（tile/patch 口径，各厂商系数不同），计价前先按上限自动缩放；压缩到任务够用分辨率是第一杠杆（常省 50-75%）。
- 多轮会话历史图每轮重发计费：图片识别后替换为结构化文字是最大省钱项；固定图进缓存前缀、动态图放后段。
- 成本账分桶：首次识别费 vs 历史重发费；图片费占比 >30% 告警，尺寸分布漂移触发重测。

## 复盘追问
- 怎么实测"压缩是否伤识别精度"？提示：抽 200 张真实任务图，原图 vs 压缩图双跑对比任务指标（OCR 字符准确率/截图理解判对率），按任务类型分桶；精度降 <1% 且成本降 >50% 即可上线，关键任务保留原图通道。
- 视频输入的计价逻辑与图片有何不同？提示：按帧采样 × 每帧 tile + 时长折算，成本比图片高一个量级，通常要入口侧限时长/限分辨率，并优先用"抽帧 + 少量关键帧"策略替代整段视频。
