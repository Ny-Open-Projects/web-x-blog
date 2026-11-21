import os

def rotate_policy(log_dir: str, keep: int = 5) -> list:
    return [
        f"每天切割 {log_dir}/app.log 按日期命名",
        "压缩 3 天前的归档 gzip",
        f"保留最近 {keep} 份, 超出删除最旧",
        "容器环境: stdout 输出, 日志驱动设 max-size",
    ]

for line in rotate_policy("/var/log/app"):
    print(line)
st = os.statvfs("/")
free_gb = st.f_bavail * st.f_frsize / 1024 ** 3
print(f"当前根分区可用: {free_gb:.1f} GB")
