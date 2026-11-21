---
title: [Q108] BackgroundTasks 后台任务
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q108 · BackgroundTasks 后台任务

> 难度:★★☆ | 标签:FastAPI, BackgroundTasks

**问**:FastAPI 里如何执行响应后的后台任务?它适合什么场景,什么时候应该换任务队列?

**答**:在路由参数声明 `BackgroundTasks`,用 `tasks.add_task(func, *args)` 注册,任务在响应发送后于同一事件循环(或线程池,取决于函数是否 async)执行,适合发通知、写审计日志、清临时文件这类轻量异步收尾。它不持久化、不重试、随进程退出丢失,也不适合 CPU 密集任务;需要可靠投递时应使用 Celery/RQ/ARQ 等外部任务队列。

```python
# file: code/03_Web后端开发/q108_background_tasks.py
import time
try:
    from fastapi import FastAPI, BackgroundTasks
    import uvicorn
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()
sent: list[str] = []

def send_email(to: str, subject: str):
    time.sleep(1)                      # 同步函数:自动放入线程池执行
    sent.append(f'{to}:{subject}')

@app.post('/register')
def register(email: str, tasks: BackgroundTasks):
    tasks.add_task(send_email, email, 'welcome')   # 响应后执行
    return {'msg': 'registered, email will be sent'}

if __name__ == '__main__':
    uvicorn.run(app, port=8000)
```

**追问**:
- 多个 add_task 的执行顺序?——按注册顺序依次执行;同步任务在线程池,async 任务在事件循环。
- BackgroundTasks 失败了怎么办?——无人重试也不持久化,进程退出即丢;可靠场景必须上任务队列(Celery/ARQ)+ 重试策略。
- 后台任务和依赖清理谁先执行?——依赖清理先、后台任务后(响应发送后);顺序影响「任务里还能不能用 session」的判断。
- CPU 密集任务放 BackgroundTasks 会怎样?——占住事件循环拖垮全部请求;丢线程/进程池或独立 worker。
