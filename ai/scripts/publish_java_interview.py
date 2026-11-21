#!/usr/bin/env python3
"""target/33-java-interview → blog/source/_posts 进站拷贝（可重复执行，以 target 为真源）。

- 体系精讲 + 实战演练 + 导览（00~21-*）→ _posts/java-interview/
- 背诵卡（22~34-背诵-*）→ _posts/java-interview-cards/
- 幂等：先清空两个目标目录再拷，防止改名卡片残留旧文件。
"""
import shutil
from pathlib import Path

TGT = Path("/Users/Wang/Code/github/web-x-blog/work/target/33-java-interview")
POSTS = Path("/Users/Wang/Code/github/web-x-blog/work/blog/source/_posts")
MAIN = POSTS / "java-interview"
CARDS = POSTS / "java-interview-cards"
TALK = POSTS / "java-interview-talk"


def sync(src: Path, dst: Path, exclude_recite: bool):
    if dst.exists():
        shutil.rmtree(dst)
    dst.mkdir(parents=True)
    n = 0
    for d in sorted(src.iterdir()):
        if d.is_dir() and not d.name.startswith("_") and not d.name.startswith("reports"):
            if exclude_recite and ("-背诵-" in d.name or "-话术-" in d.name):
                continue
            for f in sorted(d.glob("*.md")):
                shutil.copy2(f, dst / f.name)
                n += 1
    return n


def main():
    a = sync(TGT, MAIN, exclude_recite=True)
    # CARDS：清空后只拷背诵域
    if CARDS.exists():
        shutil.rmtree(CARDS)
    CARDS.mkdir(parents=True)
    b = 0
    for d in sorted(TGT.iterdir()):
        if d.is_dir() and "-背诵-" in d.name:
            for f in sorted(d.glob("*.md")):
                shutil.copy2(f, CARDS / f.name)
                b += 1
    # TALK：清空后只拷话术域
    if TALK.exists():
        shutil.rmtree(TALK)
    TALK.mkdir(parents=True)
    c = 0
    for d in sorted(TGT.iterdir()):
        if d.is_dir() and "-话术-" in d.name:
            for f in sorted(d.glob("*.md")):
                shutil.copy2(f, TALK / f.name)
                c += 1
    print(f"java-interview: {a} posts; java-interview-cards: {b} posts; java-interview-talk: {c} posts")


if __name__ == "__main__":
    main()
