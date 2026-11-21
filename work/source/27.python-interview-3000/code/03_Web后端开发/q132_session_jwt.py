import hmac
import base64
import json

SECRET = b'change-me'

def make_session(store: dict, user: str) -> str:
    sid = 'sess-0001'
    store[sid] = {'user': user}                 # 服务端保存状态
    return sid

def check_session(store: dict, sid: str):
    return store.get(sid, {}).get('user')       # 有状态:查存储

def b64(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b'=').decode()

def sign_jwt(payload: dict) -> str:
    header = b64(json.dumps({'alg': 'HS256'}).encode())
    body = b64(json.dumps(payload).encode())
    sig = hmac.new(SECRET, f'{header}.{body}'.encode(), 'sha256').hexdigest()
    return f'{header}.{body}.{sig}'             # 无状态:签名即凭证

session_store: dict = {}
sid = make_session(session_store, 'alice')
token = sign_jwt({'sub': 'alice', 'exp': 4102444800})
print(check_session(session_store, sid), sign_jwt.__name__)
