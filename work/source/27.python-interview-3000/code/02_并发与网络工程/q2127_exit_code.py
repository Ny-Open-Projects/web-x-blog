# -*- coding: utf-8 -*-
"""进程退出码约定: 0 成功、非 0 失败、1 默认异常。

- 约定 0 表示成功, 1-127 是失败码, 128+N 常用于被信号 N 杀死;
- sys.exit(n) 显式指定, 抛未捕获异常默认退 1, main 跑完退 0;
- 巡检/CI 靠退出码编排, 打印只是给人看的, 退出码才是给机器看的。
"""
import subprocess
import sys

CASES = {
    "ok": "import sys; sys.exit(0)",
    "fail3": "import sys; sys.exit(3)",
    "raise": "raise ValueError('boom')",
    "implicit": "print('done')",
}


def main():
    for tag, code in CASES.items():
        p = subprocess.run([sys.executable, "-c", code],
                           capture_output=True, text=True)
        print("%-9s returncode=%-2d stderr首行=%s" %
              (tag, p.returncode,
               (p.stderr.strip().splitlines() or [""])[0][:40]))
    print("约定映射: 0 成功 | 1 默认异常 | 3 业务自定义失败码")
    print("调用方只需 if rc != 0 就能编排, 无需解析输出")


if __name__ == "__main__":
    main()
