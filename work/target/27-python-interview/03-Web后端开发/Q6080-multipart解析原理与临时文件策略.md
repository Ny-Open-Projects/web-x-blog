---
title: [Q6080] multipart 解析原理与临时文件落盘策略
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6080 · multipart 解析原理与临时文件落盘策略

> 难度:★★★☆ | 标签:原理深挖, multipart, 文件上传, Starlette

**问**：multipart/form-data 的报文结构（boundary 分帧）是什么、与 chunked 传输怎么叠加？Python 侧解析为什么"小文件进内存、大文件落临时盘"，这个阈值由谁决定、怎么调？`UploadFile` 的 `.file` 句柄生命周期（何时删除临时文件）与"解析阶段内存峰值"的关系是什么？恶意 multipart（超多 part/无终止 boundary）怎么防？

**答**：结论：multipart 报文是"boundary 串起的字节流"：`--boundary\r\n` + 每 part 的头（Content-Disposition: form-data; name/filename、Content-Type）+ 空行 + part 内容 + `--boundary--` 结尾——**解析本质是流式字节扫描**：在字节流里找 boundary 定界，所以 chunked 传输（分块到达）对解析完全透明，解析器只认"累积起来的字节序"。Python 侧（Starlette/FastAPI 用 multipart 库）的策略是**双阈值**：单个 part 超过 `max_file_size`（Starlette spool 阈值默认 1MB）就 spool 到 `tempfile.SpooledTemporaryFile`（内存 Rolls 到磁盘），整体数据超 `max_fields/max_files`（默认各 1000）拒绝——阈值可在 `request.form(max_files=..., max_fields=...)` 调。生命周期：`UploadFile.file` 是 spooled 临时文件，**在请求对象被 GC 时关闭并删除**（Starlette 注册了清理），两个事故源：a) 解析是**全量缓冲**——multipart 库默认把整个请求体读进内存再解析（Starlette 0.x 曾有 `max_part_size` 缺失导致的内存尖峰），1GB 上传 = 解析阶段进程内存尖峰 1GB+（Q6051 的一次性读入 OOM 的 multipart 变体），对策是前置 Content-Length 校验 + 流式代理直传 OSS（Q6064 预签名直传是根治）；b) 临时文件句柄被长期持有（异步任务里引用 UploadFile），请求结束后文件对象未释放、/tmp 堆积（配 K8s emptyDir 容量告警）。恶意防护三件：限 part 数/字段数（防 multipart 边界炸弹：巨量小 part 打爆解析器 CPU）、限单 part 尺寸与总尺寸、boundary 校验（超长 boundary 逐字节扫描成本）。

```python
# file: code/03-Web后端开发/q6080_multipart_parse.py
import sys, os, tempfile
from email.parser import BytesParser
from email.policy import HTTP

# 1) multipart 报文结构: boundary 分帧(标准库 email.parser 即可解析演示)
body = (
    b"--XBOUND\r\n"
    b'Content-Disposition: form-data; name="field1"\r\n\r\n'
    b"hello\r\n"
    b"--XBOUND\r\n"
    b'Content-Disposition: form-data; name="f"; filename="a.bin"\r\n'
    b"Content-Type: application/octet-stream\r\n\r\n"
    + b"\x00\x01" * 8 + b"\r\n"
    b"--XBOUND--\r\n"
)
raw = b"Content-Type: multipart/form-data; boundary=XBOUND\r\n\r\n" + body
msg = BytesParser(policy=HTTP).parsebytes(raw)
print("is_multipart:", msg.is_multipart())
for part in msg.iter_parts():
    cd = part.get("Content-Disposition", "")
    print("part:", "file" if part.get_filename() else "field",
          "| name:", part.get_param("name", header="content-disposition"),
          "| size:", len(part.get_payload(decode=True) or b""))

# 2) SpooledTemporaryFile: 内存滚动到磁盘的阈值行为(Starlette 底层同款机制)
stf = tempfile.SpooledTemporaryFile(max_size=64)     # 阈值 64B(演示)
stf.write(b"x" * 100)
print("超阈值后已滚动到磁盘:", stf._rolled if hasattr(stf, "_rolled") else "n/a")
stf.close()                                          # close 即删除(临时文件语义)

# 3) 生命周期事故: 句柄长期持有 -> 临时文件滞留
class Holder:
    keep = None
Holder.keep = tempfile.SpooledTemporaryFile()        # 模拟异步任务持有 UploadFile.file
Holder.keep.write(b"data")
print("请求结束但句柄被任务持有 -> 临时文件在 GC 前不会删除(需显式 close/任务结束释放)")
Holder.keep.close(); Holder.keep = None

# 4) 防护参数(Starlette 形态, 无需真起服务): 阈值清单
print("防护: request.form(max_files=10, max_fields=50) + 前置 Content-Length 校验 + 直传 OSS(根治)")
print("python:", sys.version.split()[0])
```

**追问**：1) multipart 库解析为什么可能比上传本身更耗 CPU？——boundary 扫描是逐字节比较（KMP/朴素查找混合），恶意构造"高频近似 boundary"让扫描退化为 O(n×m)；防御靠限 part 数 + 限制 boundary 长度（RFC 建议 70 字符内）+ 在网关层拦截。2) `UploadFile` 与 `bytes` 参数的差异在内存行为上意味着什么？——`f: bytes` 会把整个文件读进内存（模型字段），`f: UploadFile` 走 spooled 临时文件——大文件接口的参数类型就是内存策略，code review 里这是高危点；size 阈值判断要放在参数类型之前（前置 Content-Length）。3) 为什么推荐"预签名直传 OSS 根治"？——应用服务器只接元数据请求，文件字节流不经过 Python 进程（带宽、CPU、内存三项全免，Q6064 的成本账），代价是上传完成回调的校验流程（MD5/业务校验异步化），适合 >10MB 场景；小文件直传应用反而更简单。

## 背诵要点
- multipart=boundary 分帧的字节流，解析是流式扫描，chunked 对解析透明；小 part 进内存、大 part spool 落盘，阈值 Starlette 默认单 part 1MB、fields/files 各 1000。
- UploadFile.file 是 SpooledTemporaryFile，请求对象 GC 时删除；被异步任务长期持有会滞留 /tmp；解析阶段全量缓冲是内存尖峰主因。
- 防护三件：限 part/field 数、限尺寸（前置 Content-Length）、防 boundary 炸弹；>10MB 用预签名直传根治（Q6064）。

## 复盘追问
- 你们上传接口的参数类型是 bytes 还是 UploadFile？内存峰值在压测里是多少倍文件大小？（提示：用 100MB 文件实测进程 RSS 增量，明确"解析缓冲 + 解码副本"两笔账）
- /tmp 或 emptyDir 的临时文件滞留有没有监控？（提示：任务持有句柄的用例逐个审，GC 依赖改显式 close；容器层挂 tmpfs 大小告警，联动 Q6042 OOM 账）
