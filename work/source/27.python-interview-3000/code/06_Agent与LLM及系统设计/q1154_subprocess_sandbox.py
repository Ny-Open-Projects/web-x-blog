"""subprocess 沙箱:超时 + 资源限制 + 隔离模式执行用户代码,stderr 摘要回传。"""
import resource, subprocess, sys, textwrap


def run_user_code(code: str, timeout=2):
    preexec = None
    if sys.platform != "win32":
        def preexec():
            for res_id, limit in ((resource.RLIMIT_CPU, (2, 2)),
                                  (resource.RLIMIT_AS, (256 * 1024 * 1024,) * 2),
                                  (resource.RLIMIT_FSIZE, (1024 * 1024,) * 2)):
                try:
                    resource.setrlimit(res_id, limit)
                except (ValueError, OSError):
                    pass                    # 个别 rlimit 平台不支持时跳过
    try:
        p = subprocess.run(
            [sys.executable, "-I", "-c", code],  # -I 隔离:忽略环境与用户 site
            capture_output=True, text=True, timeout=timeout,
            preexec_fn=preexec, cwd="/tmp" if sys.platform != "win32" else None,
        )
    except subprocess.TimeoutExpired:
        return {"code": -9, "stdout": "",
                "stderr_summary": "killed by timeout"}   # 超时被杀,stderr 不可靠
    return {
        "code": p.returncode,
        "stdout": p.stdout[:2000],
        "stderr_summary": p.stderr.strip().splitlines()[-1][:200] if p.stderr else "",
    }


if __name__ == "__main__":
    r1 = run_user_code(textwrap.dedent("""
        total = sum(i * i for i in range(100))
        print("sum =", total)
    """))
    print("正常执行:", r1)
    assert r1["code"] == 0 and "sum = 328350" in r1["stdout"]

    r2 = run_user_code("while True: pass", timeout=1)
    print("死循环:", r2)
    assert r2["code"] != 0, "超时任务必须被杀死"
    print("超时防护生效,退出码", r2["code"])

    r3 = run_user_code("1/0")
    print("异常回传:", r3["stderr_summary"])
    assert "ZeroDivisionError" in r3["stderr_summary"], "stderr 摘要可供模型修复"
    print("subprocess 沙箱通过")
