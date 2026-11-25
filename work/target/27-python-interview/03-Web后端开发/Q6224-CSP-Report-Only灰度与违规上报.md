---
title: "[Q6224] CSP Report-Only：灰度评估与违规上报"
date: 2026-11-24
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6224 · CSP Report-Only：灰度评估与违规上报

难度：P6 ｜ 标签：CSP、Report-Only、违规上报、灰度上线、nonce、default-src

**问**：Content-Security-Policy 和 Content-Security-Policy-Report-Only 两个头的区别是什么？为什么 CSP 上线必须走 Report-Only 灰度而不能直接拦？违规上报端点该收什么数据、要做什么防护？"独立 source-file 数降到 0 才允许切 enforce"这个上线判据怎么用？

**答**：
结论：两个头承载**同一份策略语法**，裁决行为不同：`Content-Security-Policy` 是**真拦截**（违规资源不加载/不执行），`Content-Security-Policy-Report-Only` 是**只评估只上报**（违规照常执行，但按策略算出"会被拦的清单"发到 report 端点）——这是 CSP 特有的"先模拟后生效"机制，别的安全头没有。必须灰度的原因：CSP 的拦截是**页面级的灾难放大**——策略漏放一个脚本来源，全站该脚本的所有用户立刻断功能，而且违规往往是"第三方埋点、A/B 实验代码、用户浏览器插件注入"这些开发期根本看不到的来源。灰度三阶段：①Report-Only 观察（覆盖全量页面与真实用户，收集违规清单）；②策略收敛（把合法来源补进策略，直到 report 端点的**独立 source-file 数降到 0**——不是请求数为 0，是"没有任何一个来源会误伤"）；③切 enforce（可以双头共存：enforce 一份 + Report-Only 一份更严的策略，继续观察下一轮收紧）。上报体是浏览器按规范发的 JSON：`{"csp-report": {"blocked-uri", "violated-directive", "source-file", "disposition", ...}}`。

取舍：a) report-uri vs report-to：`report-uri` 是老指令，`report-to` 基于 Reporting API（带 `Report-To` 头声明端点组、支持批量与分组），现代浏览器优先 report-to，兼容期两个都写；b) 上报端点防护是自带的责任：违规风暴（策略刚上线、某页面大面积违规）会让**自己的前端打爆自己的收集端点**——限流、采样（如只收 10%）、批量合并、按 source-file 去重计数是标配；端点必须同源或允许 CORS，否则浏览器静默丢弃；c) inline 脚本治理：Report-Only 会报出所有 inline 执行，收敛手段是 nonce（每响应随机，配合模板注入）或 hash，不要用 `'unsafe-inline'` 收场（等于白写 script-src）；d) 报告数据降噪：插件/浏览器扩展产生的违规（chrome-extension:// 来源）占报告大头，聚合时按 scheme 分桶单独忽略；e) 别忘了 Report-Only 不阻止数据外泄：上报阶段的 XSS 若真存在，攻击照常发生——灰度是"评估策略完整性"，不是"延迟修复漏洞"。

实战：事故形态是"直接上线 enforce 版 CSP：运营后台里一个老 jQuery 插件被拦，客服收到的投诉是'后台表格不能导出'，回滚还要等 CDN 缓存过期；重做：Report-Only 两周，报出 7 个遗漏来源（3 个埋点域名、1 个字体 CDN、2 个 inline 事件、1 个 eval），策略补齐后独立 source-file 连续 5 天为 0，切换 enforce 零故障"。下面模拟两阶段的裁决与上报。

```python
# CSP Report-Only: 灰度评估与违规上报
import json
from datetime import datetime, timezone

POLICY = "default-src 'self'; script-src 'self' 'nonce-R4nd0m'; report-to csp-endpoint"


def build_headers(enforce: bool) -> dict:
    name = "Content-Security-Policy" if enforce else "Content-Security-Policy-Report-Only"
    return {name: POLICY}


def evaluate(doc_sources: list, enforce: bool) -> list:
    """模拟浏览器裁决: 违规记录在 enforce=拦截/上报, report-only=仅上报放行"""
    blocked, allowed = [], []
    for src in doc_sources:
        legal = src == "self" or src.startswith("nonce:")
        (blocked if not legal else allowed).append(src)
    mode = "block" if enforce else "report-only: 放行但记录"
    for src in blocked:
        report = {
            "csp-report": {
                "blocked-uri": "inline",
                "violated-directive": "script-src-elem",
                "source-file": "https://app.example/page",
                "disposition": mode,
            }
        }
        print(f"    违规 {src} -> {mode}")
        print("       上报体:", json.dumps(report, ensure_ascii=False)[:96], "...")
    return blocked


print("[1] 两个头, 一份策略: Report-Only 只看只报, CSP 才真拦截")
print("    enforce 头:", build_headers(True))
print("    report 头:", build_headers(False))

print("[2] 灰度三阶段: 1) Report-Only 观察全量页面违规清单 -> 2) 策略收敛到零误伤 -> 3) 切 enforce")
page = ["self", "nonce:R4nd0m", "inline", "https://cdn.legacy-tracker.example"]
evaluate(page, enforce=False)

print("[3] 切换 enforce 后同样的违规被拦截:")
evaluate(page, enforce=True)

print("[4] 观察指标: report-uri/report-to 收到的独立 source-file 数 -- 降到 0 才允许上线拦截")
print("[5] 注意: Report-Only 与 enforce 可同响应共存(双头), 但 report-uri 必须是同源或受 CORS 允许的端点")
ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
print("[6] 上报端点要限流: 违规风暴会自己打爆自己 (时间戳", ts + ")")
```

**追问一**：nonce 方案的完整闭环是什么？为什么 nonce 必须每响应随机、且中间件不能缓存带 nonce 的页面？—— 闭环：服务端每个响应生成随机 nonce（`secrets.token_urlsafe`）→ 写进 CSP 头的 `'nonce-xxx'` → 同一值注入页面里每个合法 `<script nonce="xxx">` → 浏览器只执行 nonce 匹配的 inline 脚本。必须每响应随机：nonce 是用来对抗**标记注入**的——攻击者注入的 `<script>` 没有/猜不到当前 nonce 就不执行；固定 nonce 等于给攻击者预发了通行证。因此：①带 nonce 的页面**不能进 HTTP 缓存/CDN**（缓存命中会把上一个用户的 nonce 发给下一个用户，脚本全部失效或被复用）；②模板引擎要提供统一的 nonce 注入变量，避免漏标；③`'strict-dynamic'` 可让 nonce 脚本动态加载的外链脚本自动放行，减少第三方脚本清单维护成本。nonce 与 hash 是二选一的 inline 治理路径：内容固定的第三方代码可用 hash，业务代码用 nonce。

**追问二**：Report-Only 观察期的报告里，哪些信号说明策略已经可以切 enforce？什么情况下"source-file 为 0"仍然不能切？—— 切换判据不只是独立 source-file 数：①**时间覆盖**：要覆盖周末/大促/运营活动等低频页面被真实访问的窗口，老后台页面可能一个月没人开——0 报告可能只是"没人访问"；②**分桶分析**：`chrome-extension://`、`about:`、`data:` 来源单列（插件噪声），真实业务来源清零才算数；③**violated-directive 分布**：如果违规集中在 frame-ancestors（被别人 iframe 嵌入），那是嵌套防护的正常拦截不是误伤，可以切；如果集中在 script-src 的业务域名，就是漏配。0 报告仍不能切的场景：采样上报（只收 10%）时 0 可能是抽样偏差；端点故障期间的数据空洞；以及低流量页面（报告到达率本身低）——对这类页面用后台主动回归清单兜底，而不是等报告。

## 背诵要点
- Report-Only = 同一份策略只评估只上报不拦截；enforce 才真拦；两者可双头共存分阶段收紧。
- 灰度三阶段：Report-Only 收清单 → 策略收敛（独立 source-file 归零）→ 切 enforce；漏配一个来源 = 页面级故障。
- 上报端点必做：限流、采样、按 source-file 去重、插件噪声分桶；inline 治理用 nonce（每响应随机、禁缓存）或 hash。

## 复盘追问
- 为什么 CSP 不能直接 enforce 上线？（拦截页面级放大；埋点/插件/实验代码等开发期不可见来源必须靠真实用户报告）
- nonce 为什么不能配 CDN 缓存？（缓存命中把 A 的 nonce 发给 B，脚本失效或被复用；带 nonce 响应必须绕缓存）
