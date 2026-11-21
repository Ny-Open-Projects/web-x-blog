try:
    from jose import jwt, JWTError
except ImportError:
    print("该题演示需要第三方库 python-jose:pip install python-jose(正文已讲清原理,安装后可运行)")
    raise SystemExit(0)

SECRET = 'a-very-long-random-secret-key-at-least-32-bytes'
ALLOWED_ALGS = ['HS256']            # 显式白名单,防算法混淆

def decode_token(token: str) -> dict:
    try:
        # algorithms 白名单必传;verify_exp 默认校验过期
        payload = jwt.decode(token, SECRET, algorithms=ALLOWED_ALGS)
    except JWTError as e:
        raise PermissionError(f'invalid token: {e}')
    if 'sub' not in payload:
        raise PermissionError('missing sub')
    return payload

def revoke(token: str, blacklist: set[str]):
    payload = decode_token(token)
    blacklist.add(token)            # 简化示例:生产用 Redis + TTL

blacklist: set[str] = set()
