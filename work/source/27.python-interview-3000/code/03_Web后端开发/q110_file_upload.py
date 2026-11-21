try:
    from fastapi import FastAPI, UploadFile, File, HTTPException
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()
MAX_SIZE = 1024 * 1024  # 1MB

@app.post('/upload')
async def upload(file: UploadFile = File(...)):
    if file.content_type not in ('text/plain', 'image/png'):
        raise HTTPException(400, 'unsupported file type')
    size = 0
    while chunk := await file.read(64 * 1024):   # 分块流式读取
        size += len(chunk)
        if size > MAX_SIZE:
            raise HTTPException(413, 'file too large')
    return {'filename': file.filename, 'size': size}

@app.post('/uploads')
async def upload_many(files: list[UploadFile] = File(...)):
    return {'count': len(files), 'names': [f.filename for f in files]}
