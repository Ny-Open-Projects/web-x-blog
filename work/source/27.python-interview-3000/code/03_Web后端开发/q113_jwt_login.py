from datetime import datetime, timedelta, timezone
try:
    from fastapi import FastAPI, Depends, HTTPException, status
    from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
    from jose import jwt, JWTError   # pip install python-jose[cryptography]
except ImportError:
    print("该题演示需要第三方库 fastapi、python-jose:pip install fastapi[all] python-jose[cryptography],原理见正文")
    raise SystemExit(0)

SECRET = 'change-me-in-prod'
ALG = 'HS256'
app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')  # 仅提取 Bearer token

def create_token(username: str) -> str:
    payload = {'sub': username,
               'exp': datetime.now(timezone.utc) + timedelta(hours=1)}
    return jwt.encode(payload, SECRET, algorithm=ALG)

@app.post('/token')
def login(form: OAuth2PasswordRequestForm = Depends()):
    # 实际项目应查库并用 passlib/bcrypt 校验哈希
    if form.username != 'alice' or form.password != 'wonderland':
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, 'bad credentials')
    return {'access_token': create_token(form.username), 'token_type': 'bearer'}

def get_current_user(token: str = Depends(oauth2_scheme)) -> str:
    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALG])
        return payload['sub']
    except JWTError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, 'token invalid')

@app.get('/me')
def me(user: str = Depends(get_current_user)):
    return {'user': user}
