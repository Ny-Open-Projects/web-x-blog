"""对称加密概念:标准库实现 加密混淆 + HMAC 认证 的完整流程。
生产请用 cryptography 的 Fernet/AESGCM,此处演示原理。"""
import base64
import hashlib
import hmac
import os

KEY = hashlib.sha256(b"env-secret-key").digest()  # 32 字节密钥


def derive_keystream(nonce: bytes, length: int) -> bytes:
    """用 SHA256 计数器模式生成密钥流,演示流式加密原理。"""
    stream = b""
    counter = 0
    while len(stream) < length:
        stream += hmac.new(KEY, nonce + counter.to_bytes(4, "big"), hashlib.sha256).digest()
        counter += 1
    return stream[:length]


def encrypt(plaintext: bytes) -> bytes:
    nonce = os.urandom(16)  # 每次加密必须用全新随机 nonce
    stream = derive_keystream(nonce, len(plaintext))
    ciphertext = bytes(a ^ b for a, b in zip(plaintext, stream))
    tag = hmac.new(KEY, nonce + ciphertext, hashlib.sha256).digest()  # Encrypt-then-MAC
    return nonce + ciphertext + tag


def decrypt(blob: bytes) -> bytes:
    nonce, tag, ciphertext = blob[:16], blob[-32:], blob[16:-32]
    expect = hmac.new(KEY, nonce + ciphertext, hashlib.sha256).digest()
    if not hmac.compare_digest(expect, tag):
        raise ValueError("认证失败:密文被篡改或密钥不符")
    stream = derive_keystream(nonce, len(ciphertext))
    return bytes(a ^ b for a, b in zip(ciphertext, stream))


if __name__ == "__main__":
    blob = encrypt("机密数据 salary=12345".encode())
    print("密文 b64:", base64.b64encode(blob).decode()[:40], "...")
    print("解密:", decrypt(blob).decode())
    tampered = bytearray(blob)
    tampered[20] ^= 0xFF
    try:
        decrypt(bytes(tampered))
    except ValueError as e:
        print("防篡改生效:", e)
