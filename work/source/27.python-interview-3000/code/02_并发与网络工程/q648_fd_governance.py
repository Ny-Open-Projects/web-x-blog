import os
import resource
import socket


def count_fds() -> int:
    if os.path.isdir("/proc/self/fd"):
        return len(os.listdir("/proc/self/fd"))
    return len(os.listdir("/dev/fd"))  # macOS


def show_rlimit() -> tuple:
    soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
    print(f"RLIMIT_NOFILE: soft={soft} hard={hard}")
    return soft, hard


if __name__ == "__main__":
    soft, hard = show_rlimit()
    # 尝试把软限提到硬限 (无需 root)
    try:
        resource.setrlimit(resource.RLIMIT_NOFILE, (hard, hard))
        print(f"软限已提升至硬限: {resource.getrlimit(resource.RLIMIT_NOFILE)[0]}")
        resource.setrlimit(resource.RLIMIT_NOFILE, (soft, hard))  # 恢复
    except (ValueError, PermissionError) as e:
        print(f"提升受限: {e!r}")

    base = count_fds()
    print(f"当前 fd 数: {base}")

    # 泄漏演示: 200 个 socket 不关闭
    leaked = [socket.socket() for _ in range(200)]
    after_leak = count_fds()
    print(f"打开 200 个 socket 后: {after_leak} (+{after_leak - base})")

    # 正确姿势: 上下文管理器保证释放
    with socket.socket() as auto_closed:
        during = count_fds()
    after_close = count_fds()
    print(f"with 语句期间 {during}, 退出后 {after_close} (自动回收)")

    for s in leaked:
        s.close()
    print(f"手动关闭泄漏 socket 后: {count_fds()}")
    assert count_fds() <= base + 2
