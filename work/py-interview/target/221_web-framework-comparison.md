# 221. Python Web 框架对比：Django vs Flask vs Tornado

> 分类：Web 框架 | 难度：L2 | 题型：对比 | 频率：高 | 关键词：**Django** / **Flask** / **Tornado** / **大而全** / **微框架** / **异步**
> 原文锚点：第9章 9-1「三大主流框架：Django(大而全,内置ORM/Admin/插件丰富,搜狐等CMS爱用) / Flask(微框架,插件灵活组合,但过于灵活致结构不统一,有cookiecutter模板) / Tornado(微框架+异步网络库,知乎用其异步,轮子少需造得多)」

## 一句话总述
**三大主流 Python Web 框架**：Django 大而全（内置 ORM/Admin、插件丰富）；Flask 微框架（灵活、插件组合，但结构不统一）；Tornado 微框架 + 异步网络库（轮子少、需自己造）。

## 面试官视角
- **考察意图**：是否用过不止一个框架，并能从"设计哲学 + 优缺"对比，而非只说"都用过"。
- **P5** 能说出 Django/Flask/Tornado 三者及"Django 全、Flask 微、Tornado 异步" / **P6** 能讲清各自优缺点（Flask 灵活但结构乱→用 cookiecutter 统一模板；Tornado 轮子少生产力低） / **P7** 能补充"Tornado 在知乎主要用异步特性配什么""现代异步新秀 FastAPI/ASGI"。
- **红旗**：把 Tornado 当"只做 Web 框架"忽略它的异步网络库本质；或认为 Flask 没有 ORM（Flask-SQLAlchemy 是插件）。
- **惊艳点**：能点出"很多公司统一框架/模板降低维护成本，面试前先查目标公司用啥框架" `[经验]`。

## 主问答
**Q（面试官原话）：** Django、Flask、Tornado 有什么区别？各自适合什么场景？

**A · 标准答案骨架：**
1. **Django**：**大而全**框架，内置 ORM、Admin 后台、丰富的第三方插件；发展多年，适合内容管理系统（CMS）等——如搜狐等用得较多。
2. **Flask**：**微框架**，通过插件机制灵活组合（Flask-SQLAlchemy、Flask-Admin 等），中小公司和个人开发者喜欢；缺点是**过于灵活导致项目结构不统一、维护难**，常用 cookiecutter 生成统一模板。
3. **Tornado**：既是**微框架也是异步网络库**，可写 Web 应用也可做微服务/REST API；知乎用得较多（用其异步特性）。缺点是**第三方轮子/插件少**，常需自己造，生产力不如 Django/Flask。

**加分层**：多数公司会用统一框架或模板生成器降低跨项目维护成本；面试前可查目标公司用什么框架，重点搞熟那个。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 三大框架 | 基本认知 | Django全/Flask微/Tornado异步 | 换题 → 不及格 |
| L2 | Flask 优缺点 | 是否懂 | 灵活但结构乱 | 判 P5 |
| L3 | Tornado 特点 | 深入 | 微框架+异步网络库,轮子少 | 判 P6 |
| L4 | 为什么结构乱 | 工程 | 太灵活→cookiecutter统一 | 判 P6+ |
| L5 | 现代异步新秀 | 时效 | FastAPI/ASGI | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| Django/Flask/Tornado 三足鼎立长期成立 | 近年 FastAPI（ASGI）崛起 | 仍按"三大"答；可补"FastAPI 因异步+类型注解流行"显时效 |

## 关键代码
```python
# 三大框架最小示例对比 [实测, python]
# Flask
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hi(): return "hello"          # 微框架, 路由装饰器

# Django: views.py + urls.py 注册, ORM 内置
# Tornado: 异步 Handler + IOLoop
import tornado.ioloop, tornado.web
class Main(tornado.web.RequestHandler):
    def get(self): self.write("hello")
```

## ⚠️ 原文纠错
- 机翻还原：「wejungle / jungle / 江构 / 江go / jmo」→ **Django**；「flastictorato / flash / flassic / flashc / flast / flassqccookcor / flashme / flashcopycuter / flashsufatomy / flassy」→ **Flask**（及 Flask-SQLAlchemy / cookiecutter）；「torato / toronto / tomatototoradto / tomnether / tormeto / tatorato / tenater」→ **Tornado**；「pyraid / webPY / bottom」→ **Pyramid / web.py / Bottle**；「sufatomy / flashsufatomy」→ **SQLAlchemy / Flask-SQLAlchemy**；「surfatomy」→ **SQLAlchemy**。
- 原文"Django 内置 ORM/Admin，Tornado 微框架+异步网络库，Flask 微框架灵活需 cookiecutter 统一模板"——准确。
- 原文未提 FastAPI，已补时效点（见上表）。

## 总结与追问预判
三框架对比 = Django 全 / Flask 微 / Tornado 异步网络库；核心是"设计哲学 + 优劣"。可衔接：**WSGI（见 220 卡）**、**MVC（见 222 卡）**、**ORM（见 223 卡）**。
