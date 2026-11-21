---
title: [Q368] 爬虫合规:robots.txt 与抓取礼仪
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q368 · 爬虫合规:robots.txt 与抓取礼仪

> 难度:★★☆ | 标签:爬虫, robots, 合规

**问**:robots.txt 在爬虫中如何程序化遵守?除此之外还有哪些合规要点?

**答**:用标准库 `urllib.robotparser` 解析目标站 robots.txt,对每个 URL 调 `can_fetch(useragent, url)` 判断,并用 `crawl_delay`/`request_rate` 决定限速。合规要点还包括:①带真实 UA 和联系方式;②避开登录态/付费内容和个人信息(个保法/著作权边界);③尊重 `Cache-Control` 与版权;④高并发前先做压测评估对站点影响;⑤优先使用官方 API 或开放数据。

```python
# file: code/02_并发与网络工程/q368_robots.py
"""robots.txt 合规检查,离线演示 robotparser 用法。"""
import urllib.robotparser


def make_parser(robots_text: str) -> urllib.robotparser.RobotFileParser:
    rp = urllib.robotparser.RobotFileParser()
    rp.parse(robots_text.splitlines())  # 也可 rp.set_url + rp.read 在线拉取
    return rp


ROBOTS = """
User-agent: *
Disallow: /private/
Crawl-delay: 2

User-agent: edu-crawler
Allow: /
Disallow: /admin
"""

if __name__ == "__main__":
    rp = make_parser(ROBOTS)
    ua = "edu-crawler"
    print("can /posts :", rp.can_fetch(ua, "https://x.com/posts"))
    print("can /admin :", rp.can_fetch(ua, "https://x.com/admin"))
    print("can /private (其他UA):", rp.can_fetch("Baiduspider", "https://x.com/private/a"))
    print("crawl_delay:", rp.crawl_delay(ua))
```

**追问**:
- robots.txt 是法律还是道德约束?是行业惯例(robots 排除协议),不强制,但违反它加上高负载抓取可能构成不正当竞争或侵权证据,面试答"必须遵守"。
- crawl_delay 和 request_rate 有什么区别?——前者是两次请求最小间隔(秒),后者是「N 秒内最多 M 次」;两者同时给时取更保守的执行。
- robots.txt 拉取失败怎么处理?——404 视为全站允许(规范语义),5xx/超时应保守跳过或退避重试,缓存解析结果避免每 URL 拉一次。
- 登录态和付费内容为什么不能抓?——突破技术措施获取数据在民事/刑事上都有风险(著作权、不正当竞争、计算机信息系统安全),个保法还管个人信息;面试必须主动说出这条边界。
