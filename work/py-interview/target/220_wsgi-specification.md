# 220. WSGI 规范：Web 服务器与 Python 框架的桥梁

> 分类：Web 框架 | 难度：L2 | 题型：原理 | 频率：高 | 关键词：**WSGI** / **网关接口** / **environ** / **start_response** / **可调用对象**
> 原文锚点：第9章 9-1「WSGI = Python Web 服务器网关接口(PEP 3333); 定义: 可调用对象接收 environ(dict)+start_response(callback) 返回可迭代字节; 解决 python webserver 乱象, 任意框架可部署在任意 server(uWSGI/Gunicorn); wsgiref 内置 simple_server 演示, 端口8888」

## 一句话总述
**WSGI 是 Python Web 服务器与 Web 应用/框架之间的一套标准网关接口（PEP 3333）**：应用实现"接收 environ 字典 + start_response 回调、返回可迭代字节序列"的可调用对象，Server 据此调用它——于是任意框架能跑在任意 WSGI Server 上。

## 面试官视角
- **考察意图**：是否真懂"为什么需要 WSGI"以及它的函数签名契约，而非只背名字。
- **P5** 能说出 WSGI 是 Web 服务器与 Python 应用间的标准接口 / **P6** 能说出 WSGI app 的契约：environ + start_response + 返回可迭代字节 / **P7** 能讲清"WSGI 出现前 CGI/FastCGI 混乱、无统一接口"，并区分 WSGI Server（uWSGI/Gunicorn/Nginx）与应用层框架（Django/Flask）。
- **红旗**：把 WSGI 当成某个具体服务器（如说"WSGI 就是 uWSGI"）；或认为 WSGI app 返回字符串即可（必须字节）。
- **惊艳点**：能点出"WSGI 是同步阻塞模型，异步场景有 ASGI 补位（Django Channels/FastAPI）" `[经验]`。

## 主问答
**Q（面试官原话）：** 什么是 WSGI？为什么需要它？它的接口是怎么定义的？

**A · 标准答案骨架：**
1. **是什么**：WSGI（Web Server Gateway Interface）是 Python 定义的**服务器与 Web 应用/框架之间的标准网关接口**（PEP 3333，旧版 PEP 333）。
2. **为什么需要**：WSGI 出现前部署方式混乱（mod_python、CGI、FastCGI 等），缺乏统一接口，无法让任意框架跑在任意服务器上；有了 WSGI，Web Server（如 uWSGI、Gunicorn）和框架（Django、Flask）各自按规范实现，就能自由组合。
3. **接口契约**：应用是一个**可调用对象**，接收两个参数——① `environ`（含请求路径、query string 等环境信息的字典，由 Server 提供）；② `start_response(status, headers)` 回调（状态码 + 响应头）；函数**返回一个可迭代的字节序列**（如 `[b"hello world"]`）。

**加分层**：源文件用 `wsgiref.simple_server` 内置 Server 在 8888 端口跑起一个最小 WSGI app；框架（如 Django/Flask）本质就是把这种简单 app 层层封装成 Application 类 + 路由 + Request/Response 对象。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | WSGI 是什么 | 基本认知 | 服务器与应用的接口标准 | 换题 → 不及格 |
| L2 | 接口签名 | 是否懂契约 | environ + start_response + 字节 | 判 P5 |
| L3 | 为什么需要 | 历史动机 | 统一部署, 任意组合 | 判 P6 |
| L4 | WSGI Server 有哪些 | 工程 | uWSGI/Gunicorn/Nginx | 判 P6+ |
| L5 | WSGI 的局限 | 进阶 | 同步阻塞, ASGI 补位 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| WSGI 规范（PEP 3333）长期有效 | 异步场景出现 ASGI（PEP 3333 之后） | 仍按"WSGI 同步契约"答；可补"ASGI 用于异步（FastAPI/Channels）" |

## 关键代码
```python
# 最小 WSGI 应用（wsgiref 启动，端口 8888）[实测, python]
from wsgiref.simple_server import make_server
def myapp(environ, start_response):
    status = "200 OK"
    headers = [("Content-Type", "text/html; charset=utf-8")]
    start_response(status, headers)
    name = environ.get("QUERY_STRING", "")
    return [f"hello {name}".encode("utf-8")]   # 必须返回字节序列
httpd = make_server("", 8888, myapp)
httpd.serve_forever()
```

## ⚠️ 原文纠错
- 机翻还原：「WS加i / WSEI / WS加 / WS加a」→ **WSGI**；「PP三三三四 / PP三三三」→ **PEP 3333 / PEP 333**（WSGI 规范）；「wewebserver / gencom / GUincom」→ **Web Server（Nginx 等）**；「UWSGI」→ **uWSGI**；「pyononwebserver」→ **Python web server**；「WSGIINF / simleserver / macserver」→ **wsgiref / simple_server / make_server**；「四个八端口」→ **8888**；「environ」准确；「startresponse」→ **start_response**；「pandas」→ **headers**（HTTP 头）；「STML」→ **text/html**；「UTF八」→ **UTF-8**；「helloword」→ **hello world**；「杠杠靠」→ **__call__**；「ER / qerstrring / carorstring」→ **URL / query string**。
- 原文"凡是网络传输都需要传输字节"准确（WSGI app 返回字节而非 str）。
- 原文未提 ASGI，已补"WSGI 同步阻塞、ASGI 补位异步"时效性要点。

## 总结与追问预判
WSGI = Web 服务器与应用间的标准接口契约（environ + start_response + 字节）。面试官常顺问"框架对比""MVC/ORM"，可衔接：**框架对比（见 221 卡）**、**MVC（见 222 卡）**、**ORM（见 223 卡）**。
