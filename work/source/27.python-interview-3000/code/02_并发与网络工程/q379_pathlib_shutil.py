"""pathlib + shutil:构建与打包一个项目快照。"""
import shutil
import tempfile
from pathlib import Path

if __name__ == "__main__":
    project = Path(tempfile.mkdtemp()) / "myproj"
    src = project / "src"
    src.mkdir(parents=True)
    (src / "main.py").write_text("print('hi')", encoding="utf-8")
    (project / "data.csv").write_text("a,b\n1,2\n", encoding="utf-8")
    (project / "cache.tmp").write_text("junk", encoding="utf-8")

    # pathlib 遍历:只找 .py 文件
    for py in project.rglob("*.py"):
        print("py file:", py.relative_to(project), py.stat().st_size, "bytes")

    # shutil.copytree 备份,忽略 tmp 文件
    backup = project.parent / "myproj_backup"
    if backup.exists():
        shutil.rmtree(backup)
    shutil.copytree(project, backup, ignore=shutil.ignore_patterns("*.tmp"))

    # 打 zip 归档
    archive = shutil.make_archive(str(project.parent / "snapshot"), "zip",
                                  root_dir=str(backup))
    print("archive:", archive, Path(archive).stat().st_size, "bytes")
    print("备份内容:", sorted(p.name for p in backup.rglob("*")))
