import os
import socket
import ssl
import subprocess
import tempfile
import threading
import time
from datetime import datetime, timezone
from typing import Optional


def gen_cert(tmpdir: str, days: int) -> tuple:
    """自签证书: SAN 走 -config 扩展段(兼容老 openssl, 见 Q628)。"""
    key = os.path.join(tmpdir, "k.pem")
    cert = os.path.join(tmpdir, "c.pem")
    cnf = os.path.join(tmpdir, "san.cnf")
    with open(cnf, "w", encoding="utf-8") as f:
        f.write(
            "[req]\n"
            "distinguished_name = dn\n"
            "x509_extensions = v3_req\n"
            "prompt = no\n"
            "[dn]\n"
            "CN = svc.internal\n"
            "[v3_req]\n"
            "subjectAltName = DNS:svc.internal\n"
        )
    subprocess.run(
        ["openssl", "req", "-x509", "-newkey", "rsa:2048", "-nodes",
         "-keyout", key, "-out", cert, "-days", str(days), "-config", cnf],
        check=True, capture_output=True)
    return key, cert


def tls_server(ctx: ssl.SSLContext, lsock: socket.socket) -> None:
    while True:
        try:
            conn, _ = lsock.accept()
        except OSError:
            continue
        try:
            with ctx.wrap_socket(conn, server_side=True) as tls:
                tls.sendall(b"ok")
        except ssl.SSLError:
            pass
        except OSError:
            pass


def days_until_expiry(host: str, port: int, server_name: str,
                      cafile: Optional[str] = None) -> float:
    # 注: str | None 运行时求值要 3.10+, 兼容写法用 Optional
    if cafile:
        ctx = ssl.create_default_context(cafile=cafile)
    else:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
    with socket.create_connection((host, port), timeout=5) as raw:
        with ctx.wrap_socket(raw, server_hostname=server_name) as tls:
            cert = tls.getpeercert()
            if not cert:
                # CERT_NONE 下 getpeercert() 返回空 dict, 拿不到 notAfter,
                # 只能取 DER 借 openssl 解析有效期
                der = tls.getpeercert(binary_form=True)
                out = subprocess.run(
                    ["openssl", "x509", "-inform", "DER", "-noout", "-enddate"],
                    input=der, capture_output=True, check=True)
                # 输出形如 notAfter=Nov 12 08:00:00 2026 GMT
                not_after = out.stdout.decode().strip().split("=", 1)[1]
            else:
                not_after = cert["notAfter"]  # 'Nov 12 08:00:00 2026 GMT'
    expire = datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z").replace(
        tzinfo=timezone.utc)
    return (expire - datetime.now(timezone.utc)).total_seconds() / 86400


def check_host(host: str, port: int, name: str, warn: int = 30,
               critical: int = 7, **kwargs) -> str:
    try:
        days = days_until_expiry(host, port, name, **kwargs)
    except Exception as e:
        return f"CRITICAL {name}: 握手失败 {e!r}"
    if days < critical:
        return f"CRITICAL {name}: 仅剩 {days:.1f} 天过期!"
    if days < warn:
        return f"WARNING {name}: 剩余 {days:.1f} 天, 请安排续期"
    return f"OK {name}: 剩余 {days:.0f} 天"


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmpdir:
        # 快过期证书 (10 天) 与长效证书 (300 天)
        k1, c1 = gen_cert(tmpdir, days=10)
        k2, c2 = gen_cert(tmpdir, days=300)
        ports = {}
        for tag, key, crt in (("soon", k1, c1), ("long", k2, c2)):
            ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            ctx.load_cert_chain(crt, key)
            l = socket.socket()
            l.bind(("127.0.0.1", 0))
            l.listen(2)
            ports[tag] = l.getsockname()[1]
            threading.Thread(target=tls_server, args=(ctx, l), daemon=True).start()
        time.sleep(0.1)

        print(check_host("127.0.0.1", ports["soon"], "svc.internal"))
        print(check_host("127.0.0.1", ports["long"], "svc.internal"))
        print("巡检逻辑: 输出接入告警通道, ACME 自动续期做根治")
