#!/usr/bin/env python3
"""docx -> 纯文本（零依赖：zipfile + 正则剥 <w:t>/<w:p>）。"""
import sys, re, zipfile, pathlib

def docx_to_text(p):
    try:
        z = zipfile.ZipFile(p)
        xml = z.read("word/document.xml").decode("utf-8", "ignore")
    except Exception as e:
        return f"[ERR] {e}"
    # 段落边界
    xml = re.sub(r"</w:p>", "\n", xml)
    xml = re.sub(r"<w:tab[^>]*/>", "\t", xml)
    xml = re.sub(r"<w:br[^>]*/>", "\n", xml)
    # 抽取所有 <w:t ...>text</w:t>
    texts = re.findall(r"<w:t[^>]*>(.*?)</w:t>", xml, re.S)
    # 重新按段落聚合：上面把 </w:p> 换行后再抓 w:t 会丢结构；改为逐段处理
    # 简化：直接拼接 w:t，按 \n 分段已在 xml 阶段插入，但 w:t 抽取丢段落。
    # 采用：遍历段落
    paras = re.split(r"</w:p>", xml)
    out = []
    for para in paras:
        ts = re.findall(r"<w:t[^>]*>(.*?)</w:t>", para, re.S)
        line = "".join(ts)
        line = (line.replace("&amp;", "&").replace("&lt;", "<")
                .replace("&gt;", ">").replace("&quot;", '"').replace("&apos;", "'"))
        if line.strip():
            out.append(line.strip())
    return "\n".join(out)

if __name__ == "__main__":
    src = pathlib.Path(sys.argv[1])
    outdir = pathlib.Path("/tmp/quant_docx")
    outdir.mkdir(exist_ok=True)
    for f in sorted(src.glob("*.docx")):
        txt = docx_to_text(f)
        out = outdir / (f.stem + ".txt")
        out.write_text(txt, encoding="utf-8")
        print(f"{out.name}: {len(txt)} chars")
