import resource

def try_limit(mb):
    try:
        limit = mb * 1024 * 1024
        resource.setrlimit(resource.RLIMIT_AS, (limit, limit))
        return True
    except (ValueError, OSError) as e:
        print("当前平台不支持设置 RLIMIT_AS:", e)
        return False

if __name__ == "__main__":
    print("""
容器内存超限现象:
  cgroup OOM kill -> 容器 exit 137
  python MemoryError -> 可捕获 常因单个大对象
排查:docker stats 看用量 inspect 看 OOMKilled 应用内 tracemalloc 定位
""")
    if try_limit(64):
        try:
            bytearray(200 * 1024 * 1024)
            print("分配成功,说明限制未生效")
        except MemoryError:
            print("如预期:超过 64MB 触发 MemoryError,这就是 limit 内的失败形态")
