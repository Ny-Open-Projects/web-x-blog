---
title: "[Q5204] filecmp 的 shallow 比较：同大小同 mtime 不等于同内容"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5204 · filecmp 的 shallow 比较：同大小同 mtime 不等于同内容

难度：P6 ｜ 标签：filecmp、shallow、mtime、增量同步、校验

**问**：增量同步脚本用 `filecmp.cmp(src, dst)` 判断文件是否变化，结果两份大小相同、mtime 被 `cp -p` 保齐的文件，内容明明不同却返回 `True`，漏同步。`filecmp.cmp` 默认到底比什么？`shallow=False` 的代价是什么？为什么它还会缓存结果？

**答**：
结论：`filecmp.cmp(f1, f2, shallow=True)` 默认是**浅比较**：先比 `os.stat` 的签名（`st_mode` 类型、`st_size`、`st_mtime`），签名相同就直接判"相同"，**不读内容**。所以"同大小 + 同 mtime"的不同文件会被误判。`shallow=False` 才真正逐块读内容；代价是每次全文件 IO，大文件/网络盘很慢。`filecmp` 还有一个模块级缓存：同一对 `(f1, f2, shallow, stat_sig)` 的结果会被记住，文件在缓存后又被改，可能拿到旧结论，需要 `filecmp.clear_cache()`。

取舍：a) 快速去重/构建缓存用 shallow，但要接受"mtime 被保留"的误判；b) 正确性优先（备份、发布、对账）用 `shallow=False` 或自己算哈希；c) 大文件先比 size，再比快速哈希（前 4KB + 尾部），最后才全量哈希；d) 分布式/跨机场景不能信 mtime（时钟漂移、时区、`cp -p`），用内容哈希或 ETag；e) `dircmp` 默认也用 shallow，做目录对比要显式传 `shallow=False`。

实战：事故形态是"发布系统用 `filecmp.cmp` 判断静态资源是否变化，CI 用 `cp -p` 保留了源文件的 mtime，两个不同版本的 `app.js` 大小恰好相同，发布被跳过，线上一直是旧包"。下面演示同大小同 mtime 的假阳性，以及浅/深比较的差异。

```python
import filecmp
import os
import tempfile

with tempfile.TemporaryDirectory() as d:
    p1 = os.path.join(d, "a.txt")
    p2 = os.path.join(d, "b.txt")
    with open(p1, "w") as f:
        f.write("hello")
    with open(p2, "w") as f:
        f.write("world")          # 同样 5 字节，内容不同

    st = os.stat(p1)
    os.utime(p2, ns=(st.st_atime_ns, st.st_mtime_ns))

    print("[1] 默认 shallow 比较:", filecmp.cmp(p1, p2))
    print("[2] shallow=False 比内容:", filecmp.cmp(p1, p2, shallow=False))
    filecmp.clear_cache()
    print("[3] 清缓存后仍按 stat:", filecmp.cmp(p1, p2, shallow=True))
    print("[4] dircmp 默认也走 shallow:", filecmp.dircmp(d, d).same_files)
```

**追问一**：`filecmp` 的缓存 key 包含什么？—— 它缓存 `(f1, f2, shallow)` 的结果，并用 stat 签名做失效判断（`_cache` 里存 `(sig, outcome)`）；如果文件被原地修改但 size/mtime 没变，缓存不会失效。长驻进程里做文件监控，要么每轮 `clear_cache()`，要么别用 `filecmp`，直接用 `hashlib`。

**追问二**：为什么不用 `os.path.getmtime` 自己比？—— 可以，但你会在"mtime 精度、时区、NFS 属性缓存、`cp -p`"上重复踩坑；`filecmp` 至少把"类型 + 大小 + mtime"打包成签名，并处理了部分平台差异。要内容正确性，最终仍要哈希；`filecmp` 只适合"快速排除绝大多数未变文件"的第一层过滤。

## 背诵要点
- `filecmp.cmp` 默认 shallow：只比类型/大小/mtime，不读内容；同签名不同内容会假阳性。
- `shallow=False` 才逐块比内容；大文件先 size + 快速哈希，再全量。
- 模块级缓存按 stat 签名失效，原地改文件可能拿到旧结果；跨机别信 mtime。

## 复盘追问
- 发布系统为什么漏发了一个内容不同的文件？（同大小同 mtime + shallow）
- `filecmp` 结果和实际不一致，缓存怎么清？（`filecmp.clear_cache()` 或改用哈希）
