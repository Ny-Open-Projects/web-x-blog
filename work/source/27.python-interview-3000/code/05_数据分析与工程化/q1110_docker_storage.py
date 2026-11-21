
MOUNTS = {
    "volume": "docker 管理 生命周期独立 数据库等持久数据首选",
    "bind mount": "宿主机目录直挂 开发热加载注意 uid 权限映射",
    "tmpfs": "内存文件系统 敏感临时数据 容器停止即消失",
}

if __name__ == "__main__":
    for k, v in MOUNTS.items():
        print(f"{k:<12} {v}")
    print("""
存储驱动 overlay2:镜像只读层 + 容器可写层 写时复制
高频写入放 volume 避免写穿容器层
""")
    print("$ docker run -v pgdata:/var/lib/postgresql/data postgres")
    print("$ docker run -v $(pwd)/app:/app -w /app python:3.12 python main.py")
