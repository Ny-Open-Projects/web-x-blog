"""路径包含判定:is_relative_to、commonpath 与穿越校验。"""
import os
from pathlib import Path

if __name__ == "__main__":
    base = Path("/var/log/app")
    print("组件级包含:", base.joinpath("a.log").is_relative_to(base))
    print("字符串前缀误判:", "/var/log/app2".startswith("/var/log/app"))

    print("commonpath:", os.path.commonpath(["/var/log/app", "/var/log/app/x"]))
    try:
        os.path.commonpath(["/var/log/app", "relative/thing"])
    except ValueError as exc:
        print("混用绝对相对:", exc)

    # 穿越 校验:归一化后再判定
    suspicious = Path("/var/log/app/../..").resolve()
    print("归一化后仍在基目录内:", suspicious.is_relative_to(base))
