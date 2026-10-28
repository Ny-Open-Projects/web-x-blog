#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
把 work/ 下的课程卡片批量落位到 hexo 博客，按课程物理分目录组织。

规则：
1. 每门课一个物理目录：blog/source/_posts/<course-slug>/
2. 每篇补齐 hexo front-matter: title / date / categories(课程中文名) / tags
3. categories 首项统一为课程中文名 -> hexo 自动生成 /categories/<课程名>/ 归档页(分页)
4. 正文首个与 title 重复的 h1 行移除，避免详情页标题重复
5. 生成首页课程导航 source/index.md（只列课程入口，不堆文章）
"""
import os, re, shutil, datetime, collections

WORK = "/Users/Wang/Code/github/web-x-blog/work"
BLOG = os.path.join(WORK, "blog")
POSTS = os.path.join(BLOG, "source", "_posts")

# 课程映射: 目录名 -> (课程中文名, 源目录)
COURSES = {
    "es":              ("Elasticsearch与Go实战", "target/es"),
    "apm":             ("APM监控系统实战", "target/apm"),
    "go-interview":    ("Go面试题集", "go-interview"),
    "mysql-interview": ("MySQL面试题集", "mysql-interview"),
    "py-interview":    ("Python服务端面试题集", "py-interview"),
    "mksz892":         ("云原生CI/CD实战", "target/mksz892"),
    "mksz737":         ("提示词工程与大模型实战", "target/mksz737"),
    "mksz920":         ("RAG全栈技术", "target/mksz920"),
    "mksz948":         ("SpringAI与RAG实战", "target/mksz948"),
    "mksz952":         ("LangChain4j实战", "target/mksz952"),
    "kcna":            ("Kubernetes与云原生KCNA", "target/kcna"),
    "k8stop":          ("Kubernetes集群部署", "target/k8stop"),
    "cka":             ("Kubernetes认证CKA", "target/cka"),
    "k8sprod":         ("Kubernetes生产实践", "target/k8sprod"),
    "lottery":         ("Go高并发抽奖项目", "target/lottery"),
    "paas":            ("自主开发PaaS平台", "target/paas"),
    "campus":          ("后端校招面试", "target/campus"),
    "storage":         ("六大数据库存储实战", "target/storage"),
    "code":            ("代码片段", "target/code"),
}


def parse_fm(text):
    """解析已有 front-matter，返回 (fm_dict, body)"""
    if not text.startswith("---"):
        return {}, text
    m = re.match(r"^---\n(.*?)\n---\n([\s\S]*)$", text)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).split("\n"):
        i = line.find(":")
        if i > 0:
            fm[line[:i].strip()] = line[i + 1:].strip()
    return fm, m.group(2)


def strip_list(v):
    """把 '[a, b]' 或 'a' 解析成 list"""
    if not v:
        return []
    v = v.strip()
    if v.startswith("[") and v.endswith("]"):
        v = v[1:-1]
    return [x.strip().strip('"\'') for x in v.split(",") if x.strip()]


def slugify(title, idx):
    """生成安全文件名片段"""
    s = re.sub(r"[\\/:*?\"<>|\[\]{}()（）【】。、，：；！？\s]+", "-", title)
    s = re.sub(r"-+", "-", s).strip("-")
    return (s[:70] or f"card-{idx}")


def first_h1(body):
    m = re.search(r"^#\s+(.+)$", body, re.M)
    return m.group(1).strip() if m else None


def main():
    # 备份旧 _posts（不删除，移到 /tmp）
    if os.path.isdir(POSTS):
        ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        bak = f"/tmp/hexo-posts-bak-{ts}"
        shutil.move(POSTS, bak)
        print(f"旧 _posts 已备份 -> {bak}")

    stats = collections.OrderedDict()
    for slug, (cname, src) in COURSES.items():
        srcdir = os.path.join(WORK, src)
        if not os.path.isdir(srcdir):
            print(f"[跳过] {slug}: 源目录不存在 {src}")
            continue
        files = []
        for root, _, fs in os.walk(srcdir):
            for f in fs:
                if f.endswith(".md"):
                    files.append(os.path.join(root, f))
        files.sort()
        outdir = os.path.join(POSTS, slug)
        os.makedirs(outdir, exist_ok=True)

        n = 0
        for idx, fp in enumerate(files, 1):
            raw = open(fp, encoding="utf-8", errors="ignore").read()
            fm, body = parse_fm(raw)

            # title: 优先已有 FM，其次正文首个 h1，再退化文件名
            title = fm.get("title", "").strip().strip('"\'')
            if not title:
                title = first_h1(body) or os.path.splitext(os.path.basename(fp))[0]
            title = title.strip()
            # 英文双引号会破坏 YAML：成对替换为中文引号「」，保留语义且安全
            if '"' in title:
                buf, opening = [], True
                for ch in title:
                    if ch == '"':
                        buf.append("「" if opening else "」")
                        opening = not opening
                    else:
                        buf.append(ch)
                title = "".join(buf).replace("\\", "")

            # date: 优先已有 FM，其次文件修改时间
            date = fm.get("date", "").strip().strip('"\'')
            if not date:
                mt = datetime.datetime.fromtimestamp(os.path.getmtime(fp))
                date = mt.strftime("%Y-%m-%d %H:%M:%S")

            # tags: 已有 tags + 原子分类并入，去重去空
            tags = strip_list(fm.get("tags", "")) + strip_list(fm.get("categories", ""))
            tags += [cname]
            seen, tg = set(), []
            for t in tags:
                t = t.strip()
                if t and t not in seen and len(t) <= 20:
                    seen.add(t)
                    tg.append(t)
            tags = tg[:8]

            # 移除与 title 重复的正文首行 h1
            h1 = first_h1(body)
            if h1 and (h1 == title or h1.replace(" ", "") == title.replace(" ", "")):
                body = re.sub(r"^#\s+.+\n", "", body, count=1)

            out = [
                "---",
                "disableNunjucks: true",
                f'title: "{title}"',
                f"date: {date}",
                f"categories: [{cname}]",
                "tags: [" + ", ".join(tags) + "]",
                "---",
                "",
                body.strip(),
                "",
            ]
            fn = f"{idx:04d}-{slugify(title, idx)}.md"
            open(os.path.join(outdir, fn), "w", encoding="utf-8").write("\n".join(out))
            n += 1
        stats[slug] = (cname, n)
        print(f"  {slug:<18} {n:>5} 篇 -> _posts/{slug}/")

    total = sum(v[1] for v in stats.values())
    print(f"\n落位完成: {len(stats)} 门课 / {total} 篇")

    # 生成课程导航页 /courses/（首页 index 由主题文章列表占用，导航走独立页）
    lines = [
        "---",
        "title: 课程总览",
        "---",
        "",
        "<h1 style='margin-bottom:6px'>课程总览</h1>",
        f"<p style='color:#666'>共 <b>{len(stats)}</b> 门课 / <b>{total}</b> 篇笔记。点课程进入，再点单篇看细节。</p>",
        "",
        "<div style='display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px;margin-top:18px'>",
    ]
    for slug, (cname, n) in stats.items():
        url = f"/categories/{cname}/"
        lines.append(
            f"  <a href='{url}' style='display:block;border:1px solid #e3e8ef;border-radius:10px;"
            f"padding:14px 16px;text-decoration:none;color:inherit'>"
            f"<div style='font-weight:700;font-size:16px'>{cname}</div>"
            f"<div style='color:#888;font-size:13px;margin-top:6px'>{n} 篇 · 目录 {slug}</div></a>"
        )
    lines += ["</div>", ""]
    cdir = os.path.join(BLOG, "source", "courses")
    os.makedirs(cdir, exist_ok=True)
    open(os.path.join(cdir, "index.md"), "w", encoding="utf-8").write("\n".join(lines))
    print(f"课程导航页已生成: source/courses/index.md（{len(stats)} 门课入口 -> /courses/）")


if __name__ == "__main__":
    main()
