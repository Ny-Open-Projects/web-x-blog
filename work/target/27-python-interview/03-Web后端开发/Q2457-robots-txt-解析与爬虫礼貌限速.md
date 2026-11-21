---
title: [Q2457] robots.txt 解析与爬虫礼貌限速
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2457 · robots.txt 解析与爬虫礼貌限速

> 难度:★★☆☆ | 标签:爬虫, robots, Crawl-delay

**问**:自己写爬虫时,robots.txt 的组匹配与前缀规则怎么实现?Crawl-delay 怎么遵守?

**答**:robots.txt 按组组织:相邻的 User-agent 行属于同一组(可声明多个别名),组内是 Disallow/Allow 前缀规则与 Crawl-delay;UA 匹配时精确名优先于 *,多个命中取最长者,无命中组则整站允许。规则裁决按最长前缀胜出,平局 Allow 优先——这让 Allow 能在 Disallow 目录里"开天窗",例如禁全站但放行 /public/。礼貌抓取的另一面是速率:Crawl-delay 是该组两次抓取的最小间隔,自己爬虫要用"下次允许时刻 = max(当前, 上次 + delay)"的调度保证间隔,按主机维度计时而不是按页面。要分清对象:robots 约束的是守规矩的爬虫(包括自己),对不读 robots 的恶意流量,防线是限流、指纹识别与封禁,两者不可互相替代。

```python
# file: code/03_Web后端开发/q2457_robots_crawl_delay.py
"""robots.txt 解析与爬虫礼貌限速(纯标准库)。"""


def parse_robots(text):
    """解析成组列表: 相邻 User-agent 行同组, 规则行之后的 UA 行另起一组。"""
    groups, current, last_was_ua = [], None, False
    for raw in text.splitlines():
        line = raw.split("#")[0].strip()
        if not line:
            continue
        key, _, value = line.partition(":")
        key, value = key.strip().lower(), value.strip()
        if key == "user-agent":
            if current is None or not last_was_ua:
                current = {"agents": [], "allow": [], "disallow": [], "delay": None}
                groups.append(current)
            current["agents"].append(value.lower())
            last_was_ua = True
        elif current is None:
            continue                              # 规则出现在组前, 忽略
        else:
            last_was_ua = False
            if key == "disallow" and value:
                current["disallow"].append(value)
            elif key == "allow" and value:
                current["allow"].append(value)
            elif key == "crawl-delay":
                current["delay"] = float(value)
    return groups


def pick_group(groups, agent):
    """精确匹配优先于 *, 多个命中取最长 agent 名。"""
    agent = agent.lower()
    matched = [g for g in groups if agent in g["agents"] or "*" in g["agents"]]
    if not matched:
        return None
    matched.sort(key=lambda g: -(max(len(a) for a in g["agents"] if a in (agent, "*"))))
    return matched[0]


def allowed(group, path):
    """前缀匹配: 最长者胜, 平局 Allow 优先。"""
    best, verdict = 0, True
    for rule in group["allow"] + group["disallow"]:
        if not path.startswith(rule):
            continue
        if len(rule) > best:
            best, verdict = len(rule), rule in group["allow"]
    return verdict


def next_allowed_time(group, last, now):
    """遵守 Crawl-delay: 下一次可抓取时刻。"""
    delay = group["delay"] or 1.0
    return max(now, last + delay)


TEXT = """
User-agent: *
Disallow: /private/
Crawl-delay: 2

User-agent: Googlebot
Disallow:
Allow: /
Crawl-delay: 10
"""
groups = parse_robots(TEXT)
star = pick_group(groups, "Bingbot")
google = pick_group(groups, "Googlebot")
print("Bingbot 组  : disallow={} delay={}".format(star["disallow"], star["delay"]))
print("Googlebot 组: allow={} delay={}".format(google["allow"], google["delay"]))

for agent, group, path, expect in [
        (star, star, "/public/a", True),
        (star, star, "/private/key.pem", False),
        (star, star, "/private", True),          # 前缀不完整, 不命中
        (google, google, "/private/x", True)]:   # Googlebot 组无 disallow
    ok = allowed(group, path)
    print("{:9s} {:16s} -> {}".format(group["agents"][0], path, ok))
    assert ok == expect, (path, ok, expect)

now, last = 100.0, 98.0
n1 = next_allowed_time(star, last, now)
n2 = next_allowed_time(star, n1, n1 + 0.1)
print("礼貌抓取时刻: {:.1f} -> {:.1f} -> {:.1f} (间隔不小于 Crawl-delay)".format(
    now, n1, n2))
assert n1 >= last + 2.0 and n2 >= n1 + 2.0
print("要点: robots 按组与最长前缀裁决, Allow 可在 Disallow 目录里开天窗, "
      "Crawl-delay 是对自己爬虫的礼貌约束, 对不读 robots 的恶意流量要靠限流")
```

**追问**:
- 空的 Disallow: 值表示什么?——表示该组无任何禁止,全站允许,解析器必须区分"空值"与"缺失行"。
- robots 与 sitemap 什么关系?——sitemap 告诉爬虫"有什么",robots 约束"能不能抓",两者常在同一文件里用 Sitemap: 行互相引用。
