"""封装常用 Alembic 命令; 未安装时打印等价手工命令"""
import shutil
import subprocess

STEPS = [
    (["alembic", "init", "migrations"], "初始化迁移目录(仅首次)"),
    (["alembic", "revision", "--autogenerate", "-m", "add orders table"], "生成差异脚本"),
    (["alembic", "upgrade", "head"], "应用全部待执行迁移"),
    (["alembic", "downgrade", "-1"], "回滚上一个版本"),
    (["alembic", "history", "--verbose"], "查看版本链"),
]

if __name__ == "__main__":
    has_alembic = shutil.which("alembic") is not None
    for cmd, desc in STEPS:
        print(f"[{desc}] {' '.join(cmd)}")
        if has_alembic and cmd[0:2] == ["alembic", "history"]:
            subprocess.run(cmd, check=False)
    # env.py 关键配置: target_metadata = 模型 Base.metadata
    # sqlalchemy.url 建议从环境变量读取, 避免把生产连接串写进仓库
