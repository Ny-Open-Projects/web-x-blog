"""复制积压缓冲区: repl-backlog-size 与全量重同步的临界点"""
DEFAULT = 30 * 1024 * 1024

def tolerate_seconds(size_bytes, write_bps):
    return size_bytes / write_bps

print("默认 30MB backlog 的断线容忍时长:")
for mbps in (1, 10, 50):
    print(f"  写入 {mbps} MB/s -> 只兜 {tolerate_seconds(DEFAULT, mbps * 1024 * 1024):.1f} 秒")
need_bps, want_sec = 10 * 1024 * 1024, 60
print(f"写入 {need_bps // 1048576} MB/s 想兜 {want_sec} 秒: backlog 需 {need_bps * want_sec // 1048576} MB")
print("链条: 断线超时 -> 全量重同步 -> bgsave fork -> 又一次延迟毛刺")
