---
title: Python 网络爬虫
track: data
order: 5
summary: 用 requests + BeautifulSoup 把网页信息批量抓取下来，自己掌握数据来源。
---

# Python 网络爬虫

> 当数据不在数据库、也没有现成接口时，就用爬虫把网页上的信息抓取下来。

## 什么是爬虫

把互联网比作巨型蜘蛛网，网页是节点，爬虫就是沿设定路径**自动抓取每个节点信息**的程序（如电影类型、评分、价格）。

## 两步：请求 + 解析

```python
import requests
from bs4 import BeautifulSoup

# ① 请求网页，拿到 HTML
resp = requests.get("https://example.com/movies", headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
html = resp.text

# ② 用 BeautifulSoup 按标签定位、提取信息
soup = BeautifulSoup(html, "html.parser")
for item in soup.select(".movie"):
    title = item.select_one(".title").get_text(strip=True)
    score = item.select_one(".score").get_text(strip=True)
    print(title, score)
```

- `requests`：发 HTTP 请求，拿回网页内容。
- `BeautifulSoup`：按 CSS 选择器/标签从 HTML 里定位并提取字段。
- 抓多的数据用 `pandas.DataFrame` 存成表格，供后续分析。

## 注意事项

- **设 `User-Agent` 与 `timeout`**，加异常容错。
- **控制频率**，礼貌抓取，勿高频轰炸对方服务器。
- **遵守 robots 协议与法律法规**，不抓取敏感/受保护数据。

> 量化里，公开行情接口（如本站用的腾讯/东方财富）本质就是「结构化爬虫」的封装；会写爬虫，就永远不缺数据来源。
