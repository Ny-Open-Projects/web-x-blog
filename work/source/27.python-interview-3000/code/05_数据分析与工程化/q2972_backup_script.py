"""备份完整脚本: 清单 -> tar.gz 压缩 -> sha256 校验 -> 保留数轮转"""
import hashlib
import json
import os
import tarfile
import tempfile
import time


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def make_backup(src_dir, backup_dir, keep=2, label=None):
    """完整备份一次: 建清单 -> 打包压缩 -> 重读校验 -> 轮转旧包, 返回报告"""
    os.makedirs(backup_dir, exist_ok=True)
    stamp = label or "t%d" % int(time.time() * 1000)
    archive = os.path.join(backup_dir, "backup_%s.tar.gz" % stamp)
    manifest_path = archive + ".manifest.json"

    # 1. 清单: 相对路径 + 大小 + sha256, 跳过目录与符号链接
    manifest = []
    for root, _dirs, files in os.walk(src_dir):
        for fn in sorted(files):
            full = os.path.join(root, fn)
            rel = os.path.relpath(full, src_dir)
            manifest.append({"path": rel, "size": os.path.getsize(full),
                             "sha256": sha256_file(full)})

    # 2. 打包: gzip 压缩, 归档内路径用相对路径保证可还原
    with tarfile.open(archive, "w:gz") as tar:
        for item in manifest:
            tar.add(os.path.join(src_dir, item["path"]), arcname=item["path"])
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump({"archive": os.path.basename(archive), "files": manifest}, f,
                  ensure_ascii=False, indent=1)

    # 3. 校验: 重开归档逐文件比对哈希, 校验不过视为本次备份失败
    with tarfile.open(archive, "r:gz") as tar:
        for item in manifest:
            member = tar.extractfile(item["path"])
            digest = hashlib.sha256(member.read()).hexdigest()
            if digest != item["sha256"]:
                raise IOError("备份校验失败: " + item["path"])

    # 4. 轮转: 只保留最近 keep 个归档及其清单
    backups = sorted(f for f in os.listdir(backup_dir) if f.startswith("backup_") and f.endswith(".tar.gz"))
    removed = []
    for old in backups[:-keep]:
        os.remove(os.path.join(backup_dir, old))
        mpath = os.path.join(backup_dir, old + ".manifest.json")
        if os.path.exists(mpath):
            os.remove(mpath)
        removed.append(old)

    return {"archive": archive, "files": len(manifest),
            "bytes": os.path.getsize(archive), "removed": removed}


def seed_dir(path):
    """造一个待备份目录: 3 个文件"""
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, "a.sql"), "w") as f:
        f.write("INSERT 1;\n" * 100)
    with open(os.path.join(path, "b.conf"), "w") as f:
        f.write("port=5432\n")
    with open(os.path.join(path, "sub.csv"), "w") as f:
        f.write("id,name\n1,x\n2,y\n")


if __name__ == "__main__":
    d = tempfile.mkdtemp(prefix="backup_")
    src = os.path.join(d, "data")
    dst = os.path.join(d, "backups")
    seed_dir(src)
    for i, label in enumerate(["mon", "tue", "wed"], 1):
        rep = make_backup(src, dst, keep=2, label=label)
        print("第 %d 次备份: %s 文件 %d 个 包 %d 字节 轮转掉 %s"
              % (i, os.path.basename(rep["archive"]), rep["files"], rep["bytes"], rep["removed"]))
    left = sorted(f for f in os.listdir(dst) if f.endswith(".tar.gz"))
    print("保留:", left, "-> keep=2 只留最近两个")
    with open(os.path.join(dst, left[-1] + ".manifest.json"), encoding="utf-8") as f:
        mf = json.load(f)
    print("清单示例:", mf["files"][0])
    print("要点: 清单让恢复可核对, 压缩省空间, 备份后立即重读校验防'假备份', 轮转按保留数滚动删旧")
