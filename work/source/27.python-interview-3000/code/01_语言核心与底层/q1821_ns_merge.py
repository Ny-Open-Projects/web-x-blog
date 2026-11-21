"""命名空间包的多路径合并:两个目录拼同一个包。"""
import os
import subprocess
import sys
import tempfile


def build(root):
    v1 = os.path.join(root, "site_one")
    v2 = os.path.join(root, "site_two")
    os.makedirs(os.path.join(v1, "myns"), exist_ok=True)   # 无 __init__.py
    os.makedirs(os.path.join(v2, "myns"), exist_ok=True)
    with open(os.path.join(v1, "myns", "alpha.py"), "w") as f:
        f.write("WHO = 'site_one'\n")
    with open(os.path.join(v2, "myns", "beta.py"), "w") as f:
        f.write("WHO = 'site_two'\n")
    return v1, v2


PROBE = (
    "import myns, myns.alpha, myns.beta;"
    "print('无 __init__ 的包 __file__ 是 None:', myns.__file__ is None);"
    "print('portion 数:', len(list(myns.__path__)));"
    "print('alpha 来自', myns.alpha.WHO, '| beta 来自', myns.beta.WHO)"
)


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as root:
        v1, v2 = build(root)
        env = dict(os.environ, PYTHONPATH=v1 + os.pathsep + v2,
                   PYTHONDONTWRITEBYTECODE="1")
        p = subprocess.run([sys.executable, "-c", PROBE],
                           capture_output=True, text=True, env=env)
        print(p.stdout.strip() or p.stderr.strip().splitlines()[-1])
