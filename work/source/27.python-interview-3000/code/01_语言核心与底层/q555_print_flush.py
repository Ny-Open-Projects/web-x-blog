import sys
import time

if __name__ == "__main__":
    print("stdout is a tty:", sys.stdout.isatty())
    print("redirecting changes buffering to block mode")

    print("progress 0", end="", flush=True)
    time.sleep(0.05)
    print(" -> 50", end="", flush=True)
    time.sleep(0.05)
    print(" -> 100", flush=True)          # 每步强制刷出

    print("stdout first")
    sys.stderr.write("stderr written\n")  # stderr 默认无缓冲
    print("done")
