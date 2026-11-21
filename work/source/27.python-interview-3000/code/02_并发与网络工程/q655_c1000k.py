import subprocess
import sys
import platform


def read_sysctl(name: str) -> str:
    if sys.platform == "darwin":
        r = subprocess.run(["sysctl", name], capture_output=True, text=True)
        return r.stdout.strip().split(":")[-1].strip() if r.returncode == 0 else "N/A"
    try:
        with open("/proc/sys/" + name.replace(".", "/")) as f:
            return f.read().strip()
    except OSError:
        return "N/A"


def estimate(per_conn_app_kb: float, per_conn_kernel_kb: float,
             total_ram_gb: float, target: int) -> dict:
    app_gb = per_conn_app_kb * target / 1024 / 1024
    kern_gb = per_conn_kernel_kb * target / 1024 / 1024
    return {
        "app 内存 GB": round(app_gb, 1),
        "内核缓冲 GB": round(kern_gb, 1),
        "合计 GB": round(app_gb + kern_gb, 1),
        "是否可行": app_gb + kern_gb < total_ram_gb * 0.7,
    }


if __name__ == "__main__":
    print("平台:", platform.system())
    print("内核 somaxconn:", read_sysctl("kern.ipc.somaxconn" if sys.platform == "darwin"
                                          else "net.core.somaxconn"))
    if sys.platform != "darwin":
        print("fs.file-max:", read_sysctl("fs.file-max"))
        print("nf_conntrack max:", read_sysctl("net.nf_conntrack_max"))

    print("\n百万连接内存估算:")
    print("  默认缓冲 (每连接 内核200KB+应用50KB):",
          estimate(50, 200, 8, 1_000_000))
    print("  调优后   (每连接 内核16KB+应用10KB):  ",
          estimate(10, 16, 8, 1_000_000))
    print("  16GB 内存 调优后:",
          estimate(10, 16, 16, 1_000_000))
    print("结论: 不调缓冲百万连接需要 ~240GB; 调优后合计 ~25GB, 按 0.7 水位判据建议 36GB+ 内存起步(32GB 需再压缓冲)")
