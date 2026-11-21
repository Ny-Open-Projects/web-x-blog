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
