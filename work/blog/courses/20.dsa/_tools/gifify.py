#!/usr/bin/env python3
# gifify.py — 博客动画 SVG → GIF（CSDN 图片上传兼容：svg 不可传，gif 可传）
# 原理：动画全部是 <g style="animation: stN ..."> 的分步显隐；冻结 = 去 <style> 关键帧，
#       每个 step 的 g 直接置 opacity 1/0，sharp(librsvg) 光栅化，PIL 合成循环 GIF
import glob, json, os, re, subprocess, sys
from PIL import Image

DSA = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa"
KIT = "/tmp/gifkit"
FR = f"{KIT}/frames"


def steps_of(svg):
    """兼容全部生成器前缀：st/n/bs/dp/sk；dp 为累积式（步骤出现后保留）。"""
    hits = re.findall(r'animation:\s*([a-z]+)(\d+)\s+([\d.]+)s([^"]*)', svg)
    if not hits:
        return [], 1.0, False
    from collections import Counter
    prefix = Counter(h[0] for h in hits).most_common(1)[0][0]
    sel = [h for h in hits if h[0] == prefix]
    ids = sorted({int(h[1]) for h in sel})
    cumulative = "infinite" not in sel[0][3]  # dp：linear {t0}s 1 both
    total = float(sel[0][2])
    dur = total / len(ids) if ids else 1.2
    return ids, max(0.45, min(1.6, dur * 0.85)), cumulative


def freeze(svg, k, cumulative=False):
    svg = re.sub(r"<style>.*?</style>", "", svg, flags=re.S)
    def sub(m):
        idx = int(m.group(2))
        on = (idx <= k) if cumulative else (idx == k)
        return f'style="opacity:{1 if on else 0}"'
    return re.sub(r'style="animation:\s*([a-z]+)(\d+)[^"]*"', sub, svg)


def main(only_dir=None):
    os.makedirs(FR, exist_ok=True)
    blogs = [only_dir] if only_dir else sorted(glob.glob(f"{DSA}/[0-9]*"))
    manifest = []
    plan = []  # (blog, gifname, png_paths, dur_ms)
    for bd in blogs:
        for svg_path in sorted(glob.glob(f"{bd}/animation*.svg")):
            base = os.path.basename(svg_path)[:-4]          # animation / animation_3
            gif = f"{bd}/{base}.gif"
            if os.path.exists(gif) and os.path.getmtime(gif) >= os.path.getmtime(svg_path):
                continue                                     # 已是最新
            svg = open(svg_path, encoding="utf-8").read()
            ids, dur, cumul = steps_of(svg)
            if not ids:
                print(f"  跳过（无动画步）: {svg_path}")
                continue
            pngs = []
            fdir = f"{FR}/{os.path.basename(bd)}"
            os.makedirs(fdir, exist_ok=True)
            for k in ids:
                fsvg = f"{fdir}/{base}_{k}.svg"
                fpng = f"{fdir}/{base}_{k}.png"
                open(fsvg, "w", encoding="utf-8").write(freeze(svg, k, cumul))
                manifest.append({"svg": fsvg, "png": fpng})
                pngs.append(fpng)
            plan.append((bd, base, gif, pngs, int(dur * 1000)))
    if manifest:
        json.dump(manifest, open(f"{KIT}/manifest.json", "w"))
        node = (f"const sharp=require('sharp'),fs=require('fs');"
                f"const jobs=JSON.parse(fs.readFileSync('{KIT}/manifest.json'));"
                f"(async()=>{{for(const j of jobs){{try{{await sharp(fs.readFileSync(j.svg))"
                f".png().toFile(j.png);}}catch(e){{console.log('ERR',j.svg,e.message);}}}}"
                f"console.log('raster',jobs.length);}})();")
        r = subprocess.run(["node", "-e", node], cwd=KIT, capture_output=True, text=True)
        if "raster" not in r.stdout:
            print("raster 失败:", r.stdout[-400:], r.stderr[-400:])
            sys.exit(1)
        print(f"光栅化 {len(manifest)} 帧")
    else:
        print("无待转换动画")
    n_ok = n_fail = 0
    for bd, base, gif, pngs, dur in plan:
        missing = [p for p in pngs if not os.path.exists(p)]
        if missing:
            n_fail += 1
            print(f"  缺帧 {gif}: {len(missing)}")
            continue
        frames = [Image.open(p).convert("RGB") for p in pngs]
        try:
            frames[0].save(gif, save_all=True, append_images=frames[1:],
                           duration=dur, loop=0, optimize=True)
            n_ok += 1
        except Exception as e:
            n_fail += 1
            print(f"  GIF失败 {gif}: {e}")
    print(f"GIF 合成 {n_ok} 个，失败 {n_fail}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
