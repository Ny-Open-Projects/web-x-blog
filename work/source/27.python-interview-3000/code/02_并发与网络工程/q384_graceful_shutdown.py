"""优雅停机:SIGTERM/SIGINT 处理 + 安全点检查。"""
import signal
import sys
import time

shutdown = False


def handle_signal(signum, frame):
    global shutdown
    print(f"\n收到信号 {signal.Signals(signum).name}, 置位停机标志")
    shutdown = True  # handler 内只做最轻量动作


def main():
    signal.signal(signal.SIGTERM, handle_signal)
    signal.signal(signal.SIGINT, handle_signal)  # Ctrl+C

    print("worker 启动, pid =", os_getpid(), "按 Ctrl+C 演示优雅停机")
    processed = 0
    while not shutdown:
        # 模拟处理一个任务
        time.sleep(0.2)
        processed += 1
        if processed >= 3:
            # 演示用:处理 3 个后向自己发 SIGTERM
            import os
            os.kill(os.getpid(), signal.SIGTERM)
    print(f"安全点检测到停机标志, 等待在途任务... 已处理 {processed} 个")
    print("关闭连接, 刷盘, 退出码 0")
    return 0


def os_getpid():
    import os
    return os.getpid()


if __name__ == "__main__":
    sys.exit(main())
