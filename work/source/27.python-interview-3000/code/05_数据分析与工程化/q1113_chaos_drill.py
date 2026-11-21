import os
import subprocess
import sys
import tempfile
import time

def chaos_kill():
    p = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(60)"])
    time.sleep(0.3)
    p.terminate()   # 注入故障:杀进程
    p.wait(timeout=5)
    print(f"子进程退出码 {p.returncode}(-15 表示被 SIGTERM 杀死,自愈逻辑应在此后介入)")

def chaos_fill_disk(cap_mb=8, chunk_mb=1):
    """在临时目录写占位文件逼近磁盘压力,演练完立即清理"""
    path = os.path.join(tempfile.gettempdir(), "chaos_disk.bin")
    written = 0
    try:
        with open(path, "wb") as f:
            while written < cap_mb * 1024 * 1024:
                f.write(b"x" * (chunk_mb * 1024 * 1024))
                written += chunk_mb * 1024 * 1024
        print(f"已写入 {written // 1024 // 1024}MB,可观察服务在磁盘压力下的表现")
    finally:
        os.remove(path)
        print("演练文件已清理,磁盘恢复")

if __name__ == "__main__":
    chaos_kill()
    chaos_fill_disk()
    print("真实演练:预发环境 + 爆炸半径控制 + 中止开关 + 差距复盘")
