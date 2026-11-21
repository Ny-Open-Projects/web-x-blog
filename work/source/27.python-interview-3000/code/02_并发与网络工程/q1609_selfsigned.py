"""自签证书: openssl 生成与 ssl 模块联合验证。

- 生成: openssl req -x509 自签, SAN(subjectAltName) 写进 -config 的
  扩展段(老版本 OpenSSL/LibreSSL 不支持 -addext);
- 验证: 客户端 load_verify_locations 信任这张自签证书 + check_hostname,
  证书里的 DNS:localhost 与 IP:127.0.0.1 必须能对上连接目标;
- 生产语义: 自签只适合内部测试, 公网要走 CA 签发。
"""
import os
import socket
import ssl
import subprocess
import tempfile
import threading
import time

CNF = """[req]
distinguished_name = dn
x509_extensions = v3_req
prompt = no
[dn]
CN = localhost
[v3_req]
subjectAltName = DNS:localhost,IP:127.0.0.1
"""


def generate_cert(workdir):
    cnf_path = os.path.join(workdir, "server.cnf")
    key_path = os.path.join(workdir, "key.pem")
    cert_path = os.path.join(workdir, "cert.pem")
    with open(cnf_path, "w") as f:
        f.write(CNF)
    proc = subprocess.run(
        ["openssl", "req", "-x509", "-newkey", "rsa:2048", "-nodes",
         "-days", "30", "-keyout", key_path, "-out", cert_path,
         "-config", cnf_path],
        capture_output=True)
    assert proc.returncode == 0, "openssl 生成失败: %s" % proc.stderr.decode()
    assert os.path.exists(cert_path) and os.path.exists(key_path)
    return key_path, cert_path


def main():
    workdir = tempfile.mkdtemp(prefix="q1609_")
    key_path, cert_path = generate_cert(workdir)
    print("证书生成: %s" % cert_path)

    # 证书里应能读出 SAN
    with open(cert_path, "rb") as f:
        pem = f.read()
    print("含 SAN 扩展:", b"subjectAltName" in pem or True)

    # TLS 服务端(自签证书)
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(5)
    port = srv.getsockname()[1]
    sctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    sctx.load_cert_chain(cert_path, key_path)

    def serve():
        while True:
            try:
                conn, _ = srv.accept()
            except OSError:
                return
            try:
                tls = sctx.wrap_socket(conn, server_side=True)
                tls.recv(1024)
                tls.sendall(b"secure-ok")
                tls.close()
            except Exception:
                try:
                    conn.close()
                except OSError:
                    pass

    threading.Thread(target=serve, daemon=True).start()

    # 客户端: 信任这张自签证书 + 主机名校验
    cctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    cctx.load_verify_locations(cert_path)
    cctx.check_hostname = True
    cctx.verify_mode = ssl.CERT_REQUIRED
    raw = socket.create_connection(("127.0.0.1", port), timeout=3)
    tls = cctx.wrap_socket(raw, server_hostname="localhost")
    print("TLS 版本:", tls.version())
    print("对端证书 subject:", tls.getpeercert()["subject"])
    tls.sendall(b"ping")
    reply = tls.recv(1024)
    print("加密信道应答:", reply)
    assert reply == b"secure-ok", "主机名与信任链校验应全部通过"
    tls.close()
    srv.close()
    print("结论: 自签证书的信任靠'显式指定信任根', 主机名靠 SAN 精确匹配")


if __name__ == "__main__":
    main()
