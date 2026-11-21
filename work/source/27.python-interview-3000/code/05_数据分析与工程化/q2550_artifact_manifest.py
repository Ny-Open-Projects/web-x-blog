"""发布产物的校验和清单: SHA256 清单 + 校验, 截断损坏当场现形"""

import hashlib
import json
import os
import tempfile


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def build_manifest(artifacts):
    return {name: sha256_file(path) for name, path in sorted(artifacts.items())}


def verify(artifacts, manifest):
    for name, path in artifacts.items():
        if name not in manifest:
            raise KeyError(f"清单缺少产物 {name}")
        actual = sha256_file(path)
        if actual != manifest[name]:
            raise IOError(f"产物 {name} 校验失败: 期望 {manifest[name][:12]}, 实得 {actual[:12]}, 可能截断或被篡改")


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmp:
        paths = {}
        for name, body in {"orders.csv": b"id,amt\n1,100\n2,250\n",
                           "summary.json": b'{"orders": 2}'}.items():
            p = os.path.join(tmp, name)
            with open(p, "wb") as f:
                f.write(body)
            paths[name] = p
        manifest = build_manifest(paths)
        print("清单:", json.dumps({k: v[:12] for k, v in manifest.items()}))
        verify(paths, manifest)
        print("校验通过: 两个产物指纹一致")
        with open(paths["summary.json"], "ab") as f:
            f.write(b" truncated")            # 模拟传输截断
        try:
            verify(paths, manifest)
        except IOError as e:
            print("拦截:", e)
        else:
            raise AssertionError("损坏产物必须被拦截")
    print("要点: 清单随产物一起发, 消费端先验指纹再使用, 网络截断和手工改动都藏不住")
