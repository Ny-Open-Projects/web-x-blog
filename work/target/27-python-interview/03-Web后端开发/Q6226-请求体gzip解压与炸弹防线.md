---
title: "[Q6226] 请求体 gzip 解压与炸弹防线：逐块限长闸门"
date: 2026-11-24
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6226 · 请求体 gzip 解压与炸弹防线：逐块限长闸门

难度：P6 ｜ 标签：gzip、Content-Encoding、解压炸弹、请求体限制、DEFLATE 压缩比、拒绝服务

**问**：客户端把 JSON 请求体用 gzip 压缩发上来（Content-Encoding: gzip），服务端解压有什么风险——"解压炸弹"是什么原理？为什么只限制 Content-Length 挡不住？两道尺寸闸门分别卡什么？解压超限时的正确处置是什么？

**答**：
结论：DEFLATE 对**高重复内容**的压缩比可以到 1000x 以上（重复字节串的 LZ77 匹配 + 霍夫曼编码），几 KB 的 gzip 载荷可解压出 GB 级明文——解压炸弹是"小体积密文骗过入口限流，在解压阶段膨胀打爆内存/耗尽 CPU"的攻击。**只限 Content-Length 挡不住**：它限制的是密文尺寸，炸弹的密文恰恰很小；而"先解压到内存再看大小"则是先被打爆才检查。正确防线是**两道闸门 + 逐块解压**：①**密文闸门**：Content-Length/实际收到的请求体上限（如 256KB），挡"下载量"，在解压前生效；②**明文闸门**：解压时**逐块读取**（每次 64KB），累计解压字节数一旦超过明文上限（如 1MB）**立即中断**并断开连接——炸弹在膨胀过程中就被掐死，内存峰值最多是"上限 + 一个块"，不会先撑爆再拒绝；③**声明校验**：只对显式 `Content-Encoding: gzip` 的请求解压，不做内容嗅探（magic bytes 猜测解压只会增加攻击面），不支持的编码回 415；④超限处置：立刻断开 + 记录攻击特征（来源、UA、载荷指纹），**不要**读完剩余数据（那是替攻击者消耗自己的带宽）。压缩比本身不是敌人——合法的批量导入、大 JSON 上传确实靠压缩省流量，防线要精准到"膨胀量"而不是一刀切禁压缩。

取舍：a) 上限取值：密文/明文比例上限（如 1:10）比绝对明文上限更贴合业务——正常 JSON 很少超过 10x，重复内容伪装的载荷比例异常即可拒；b) Web 服务器层的默认防护：Nginx `client_max_body_size` 限的是密文，解压发生在应用/中间层——别以为 Nginx 挡了就万事大吉，应用侧自己的闸门才是解压层的；c) 响应方向同样有这个问题：服务端把用户可控内容压缩回给浏览器时（动态 gzip），也可能放大缓存与带宽成本，但风险方向不同（打的是客户端/CDN）；d) HTTP/2 的 HEADERS 压缩（HPACK）历史上有类似炸弹变体（连接级字典膨胀），方向同理：任何"压缩 + 不限膨胀上限"的组合都要有逐块配额；e) 中间件实现位置：解压闸门放在框架中间件/网关统一做，业务代码拿到的一定是"已验身"的明文流——业务代码不该各自关心炸弹。

实战：事故形态是"开放接口收到可疑流量：监控显示单请求 CPU 时间飙到 30 秒、worker OOM 重启，抓包发现请求体只有 3KB 但 Content-Encoding: gzip——解压出 2GB 的重复 JSON 把 4 个 worker 全拖死；修复：中间件加逐块解压 + 明文 1MB 闸门 + 密文 256KB 闸门，超限断连并上报 WAF 封禁"。下面演示逐块限长防线。

```python
# 请求体压缩头(gzip)的服务端解压与炸弹防线
import gzip
import io

raw = b"{" + b'"field":"a",' * 400 + b'"last":1}'
compressed = gzip.compress(raw)
print(f"[1] 原始 {len(raw)}B -> 压缩后 {len(compressed)}B (比例 {len(raw) // len(compressed)}x)")

MAX_PLAIN = 1 << 20          # 明文上限 1MB
MAX_CIPHER = 256 * 1024      # 密文上限 256KB


def read_body(chunks: bytes, declared_gzip: bool) -> str:
    """按声明解压, 逐块限长读取, 任何超限立即中断 -- 炸弹在膨胀过程中就被掐死"""
    if not declared_gzip:
        return chunks.decode("utf-8")[:MAX_PLAIN].decode("utf-8", "ignore")
    total = 0
    out = io.BytesIO()
    with gzip.GzipFile(fileobj=io.BytesIO(chunks)) as gz:
        while True:
            block = gz.read(64 * 1024)
            if not block:
                break
            total += len(block)
            if total > MAX_PLAIN:
                raise ValueError(f"解压超过 {MAX_PLAIN}B 明文上限, 拒绝并断开")
            out.write(block)
    return out.getvalue().decode("utf-8")


print("[2] 正常请求: 解压成功, 长度", len(read_body(compressed, True)))

bomb = gzip.compress(b"A" * (8 << 20))     # 8MB 明文压成几 KB
print(f"[3] 炸弹载荷: 明文 {8 << 20}B -> 压缩 {len(bomb)}B")
try:
    read_body(bomb, True)
except ValueError as exc:
    print("    防线生效:", exc)

print("[4] 两道尺寸闸门都要设: Content-Length 密文上限挡'下载量', 解压逐块累计挡'膨胀量'")
print("[5] 声明校验: 只对显式声明 gzip 解压, 不做内容嗅探; 支持的编码要参与协商")
print("[6] 缓存层注意: 解压后的 ETag/Content-Length 变了, 缓存键要区分压缩前后")
```

**追问一**：为什么解压要逐块而不是一次 `gzip.decompress(chunks)`？逐块读取的实现里还有什么容易漏的细节？—— 一次 `gzip.decompress` 是"先膨胀完再检查"：2GB 的炸弹在函数返回前就已把内存吃满，闸门形同虚设；逐块 `read(64KB)` 让检查点插在膨胀过程中，累计超限即刻抛出——内存上界 = 明文上限 + 一个块。容易漏的细节：①**CPU 闸门**：极深的多层压缩（gzip 套 gzip）或病态 DEFLATE 流（解压极慢但膨胀不超标）会绕过尺寸闸门消耗 CPU——给解压加时间预算（如 1 秒）或整体请求超时；②**流式读取**：真实服务里请求体是从网络流进来的，正确形态是"边收边解压边计数"，密文闸门先看 Content-Length 头再做流式双计数，本例为演示把密文一次性载入是最简形态；③**多成员 gzip**：gzip 文件格式允许多个成员拼接，某些实现解完第一个成员就停，剩余成员成为走私通道——Python 的 GzipFile 会继续读后续成员，行为正确但要意识到这个差异；④错误路径：抛异常后连接处置是断开（RST/关闭）而不是回 200/413 后继续读——读剩余数据就是在替攻击者消耗自己。

**追问二**：Vary: Accept-Encoding 与解压后缓存的关系是什么？为什么说"缓存键要区分压缩前后"？—— 服务端对同一资源按 `Accept-Encoding` 返回 gzip 或明文两种表示，响应必须带 `Vary: Accept-Encoding` 告诉缓存层"按这个请求头区分缓存条目"——漏掉 Vary 的经典事故是：压缩代理把 gzip 版本缓存后发给了不支持 gzip 的客户端（老代理/中间盒直接解不出）。"缓存键区分压缩前后"指的是应用层自己做内容缓存（如把解压后的请求体做 Key 缓存校验结果）时：同一个密文请求体解压出同一明文应命中同一缓存键（按明文 Key），但如果按密文字节做 Key，同一明文的不同压缩器输出（不同压缩级别/字典）会缓存多份；反过来响应侧按密文缓存是性能优化（不重复压缩）但必须挂上 Vary。ETag 同理：资源被压缩传输时 ETag 要区分强/弱或按表示分别生成——这些是"压缩进入请求/响应路径后，缓存语义矩阵多了一个维度"的具体表现。

## 背诵要点
- DEFLATE 压缩比可超 1000x：几 KB 密文解出 GB 明文；只限 Content-Length 挡不住（它限的是密文）。
- 两道闸门：密文上限（收包阶段）+ 明文上限（解压逐块累计，超限立即中断断连），内存上界 = 上限 + 一个块。
- 只解显式声明的 Content-Encoding，不嗅探；超限别读完剩余数据；另加 CPU/时间预算防慢炸弹。

## 复盘追问
- 为什么一次 gzip.decompress 让闸门失效？（先膨胀完才返回，2GB 已吃进内存；逐块 read 让检查点插进膨胀过程）
- 响应侧同一资源的压缩与缓存怎么共存？（Vary: Accept-Encoding 区分表示；应用层缓存键选明文，密文缓存要挂 Vary）
