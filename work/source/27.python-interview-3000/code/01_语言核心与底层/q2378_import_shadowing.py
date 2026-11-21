"""import 遮蔽排查:同名文件盖掉标准库的定位方法。"""
import os
import subprocess
import sys
import tempfile

if __name__ == "__main__":
    import json
    print("正常环境 json 来源:", json.__file__)

    shadow_dir = tempfile.mkdtemp(prefix="shadow_")
    with open(os.path.join(shadow_dir, "json.py"), "w") as f:
        f.write("value = '我是本地假 json'\n")

    probe = "import json; print(json.__file__); print(getattr(json, 'value', '真模块'))"
    proc = subprocess.run(
        [sys.executable, "-c", probe],
        cwd=shadow_dir,
        capture_output=True, text=True,
        env={**os.environ, "PYTHONPATH": shadow_dir},
    )
    print("被遮蔽时的加载来源与结果:")
    for line in proc.stdout.strip().splitlines():
        print("   ", line)

    print("排查1 sys.path 首位:", repr(sys.path[0]))
    print("排查2 sys.modules 指向:", sys.modules["json"].__file__)
    print("排查3 python -v 会打印每个模块的加载来源")
