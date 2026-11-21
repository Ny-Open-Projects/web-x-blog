import hashlib

def fingerprint(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()[:8]

def asset_url(name: str, content: bytes) -> str:
    return f"/static/{name}.{fingerprint(content)}.css"

def cache_headers(is_fingerprinted: bool) -> dict:
    if is_fingerprinted:
        return {"Cache-Control": "public, max-age=31536000, immutable"}
    return {"Cache-Control": "no-cache"}   # 入口 HTML 走协商缓存

print(asset_url("app", b"body{color:red}"))
print(cache_headers(True), cache_headers(False))
