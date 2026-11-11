#!/usr/bin/env python3
# svg_anim.py — 生成算法动态演示 SVG（内嵌 CSS keyframes 动画，可直接嵌入 markdown/HTML）
# 用法: python3 svg_anim.py bubble_sort out.svg
import sys

def bubble_sort_svg(vals=(5,4,3,2,1), w=560, h=320):
    n = len(vals)
    bar_w = 44; gap = 14; left = 60; base = 250
    unit = (base-60) / max(vals)
    colors = ["#4A90D9","#7B68EE","#50C878","#FFB347","#FF6F61","#9370DB","#20B2AA","#DC143C"]
    steps = []  # (round, j, highlight_i, highlight_j, swapped, order_snapshot)
    arr = list(vals)
    for i in range(n):
        for j in range(n-1-i):
            swapped = arr[j] > arr[j+1]
            steps.append((i, j, j, j+1, swapped, arr[:]))
            if swapped:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            steps.append((i, j, j, j+1, swapped, arr[:]))
    total = len(steps)
    dur = 1.1  # 每步秒数
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="system-ui,sans-serif">']
    parts.append(f'<rect width="{w}" height="{h}" rx="12" fill="#0F172A"/>')
    parts.append(f'<text x="{w//2}" y="34" text-anchor="middle" fill="#E2E8F0" font-size="17" font-weight="600">冒泡排序 · 两两比较 &amp; 交换（自动循环播放）</text>')
    for s in range(total):
        rnd, j, hi, hj, swapped, snap = steps[s]
        t0 = s*dur
        show = f'animation: st{s} {total*dur}s linear infinite both'
        parts.append(f'<g style="{show}">')
        for k, v in enumerate(snap):
            bh = v*unit
            x = left + k*(bar_w+gap)
            col = colors[(v-1) % len(colors)]
            if k in (hi, hj): col = "#FACC15" if not swapped else "#F87171"
            if k >= n-1-rnd: col = "#34D399"  # 已就位
            parts.append(f'<rect x="{x}" y="{base-bh}" width="{bar_w}" height="{bh}" rx="6" fill="{col}"/>')
            parts.append(f'<text x="{x+bar_w//2}" y="{base-bh-8}" text-anchor="middle" fill="#F1F5F9" font-size="15" font-weight="700">{v}</text>')
        parts.append(f'<text x="{w//2}" y="285" text-anchor="middle" fill="#94A3B8" font-size="13">第 {rnd+1} 轮 · 比较 arr[{hi}] 与 arr[{hj}]{" → 交换" if swapped else ""}</text>')
        parts.append('</g>')
    parts.append('<style>')
    for s in range(total):
        a = s/total*100; b = (s+1)/total*100; f = (b-a)*0.12
        parts.append(f'.st{s} {{opacity:0}} @keyframes st{s} {{0%{{opacity:0}}{a:.2f}%{{opacity:0}}{a+f:.2f}%{{opacity:1}}{b-f:.2f}%{{opacity:1}}{b:.2f}%{{opacity:0}}100%{{opacity:0}}}}')
    parts.append('</style></svg>')
    return "\n".join(parts)

def dfs_tree_svg():
    # 二叉树最大深度 DFS 高亮动画：节点按访问顺序点亮，深度标尺同步
    nodes = {  # id: (x, y, val, children)
        1:(280,80,3,[2,3]), 2:(170,160,9,[]), 3:(390,160,20,[4,5]), 4:(320,230,15,[]), 5:(460,230,7,[])
    }
    order = [1,2,3,4,5]  # DFS 前序
    depths = {1:1,2:2,3:2,4:3,5:3}
    dur = 1.2
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="560" height="330" viewBox="0 0 560 330" font-family="system-ui,sans-serif">']
    parts.append('<rect width="560" height="330" rx="12" fill="#0F172A"/>')
    parts.append('<text x="280" y="32" text-anchor="middle" fill="#E2E8F0" font-size="17" font-weight="600">DFS 求最大深度 · 节点点亮顺序 = 递归访问顺序</text>')
    # 边
    edges = [(1,2),(1,3),(3,4),(3,5)]
    for a,b in edges:
        x1,y1 = nodes[a][0], nodes[a][1]; x2,y2 = nodes[b][0], nodes[b][1]
        parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#475569" stroke-width="2.5"/>')
    # 深度标尺
    for d,y in [(1,80),(2,160),(3,230)]:
        parts.append(f'<line x1="60" y1="{y}" x2="520" y2="{y}" stroke="#1E293B" stroke-dasharray="4 6"/>')
        parts.append(f'<text x="42" y="{y+4}" fill="#64748B" font-size="12">L{d}</text>')
    for s,nid in enumerate(order):
        x,y,v = nodes[nid][:3]; d = depths[nid]; t0 = s*dur
        parts.append(f'<g style="animation: n{s} {len(order)*dur}s linear infinite both">')
        parts.append(f'<circle cx="{x}" cy="{y}" r="24" fill="#4A90D9" stroke="#93C5FD" stroke-width="2.5"/>')
        parts.append(f'<text x="{x}" y="{y+6}" text-anchor="middle" fill="#fff" font-size="16" font-weight="700">{v}</text>')
        parts.append(f'<text x="{x+34}" y="{y-16}" fill="#FACC15" font-size="13" font-weight="600">L{d}</text>')
        parts.append('</g>')
    parts.append('<style>')
    for s in range(len(order)):
        a = s/len(order)*100; b = (s+1)/len(order)*100; f = (b-a)*0.18
        parts.append(f'@keyframes n{s} {{0%{{opacity:0}}{a:.2f}%{{opacity:0}}{a+f:.2f}%{{opacity:1}}{b-f:.2f}%{{opacity:1}}{b:.2f}%{{opacity:0}}100%{{opacity:0}}}}')
        parts.append(f'.n{s}{{opacity:0}}')
    parts.append('</style></svg>')
    return "\n".join(parts)

GENS = {"bubble_sort": bubble_sort_svg, "dfs_tree": dfs_tree_svg}

def binary_search_svg(vals=(1,3,5,7,9,11,13,15), target=11, w=560, h=300):
    n = len(vals); cell = 52; gap = 8; left = (w - n*(cell+gap))//2 + 10; top = 120
    steps = []; lo, hi = 0, n-1
    while lo <= hi:
        mid = (lo+hi)//2
        steps.append(("probe", lo, hi, mid, vals[mid] == target))
        if vals[mid] == target: break
        if vals[mid] < target: lo = mid+1
        else: hi = mid-1
    dur = 1.4
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="system-ui,sans-serif">']
    parts.append(f'<rect width="{w}" height="{h}" rx="12" fill="#0F172A"/>')
    parts.append(f'<text x="{w//2}" y="34" text-anchor="middle" fill="#E2E8F0" font-size="17" font-weight="600">二分查找 target={target} · 收缩区间[lo,hi]自动播放</text>')
    for s,(op,l,h,m,found) in enumerate(steps):
        t0 = s*dur
        parts.append(f'<g style="animation:bs{s} {len(steps)*dur}s linear infinite both">')
        for k in range(n):
            x = left + k*(cell+gap)
            inr = l <= k <= h
            bg = "#1E293B" if not inr else "#334155"
            if k == m: bg = "#FACC15" if not found else "#34D399"
            fg = "#64748B" if not inr else "#F1F5F9"
            parts.append(f'<rect x="{x}" y="{top}" width="{cell}" height="44" rx="8" fill="{bg}"/>')
            parts.append(f'<text x="{x+cell//2}" y="{top+28}" text-anchor="middle" fill="{fg}" font-size="16" font-weight="700">{vals[k]}</text>')
        ya = top-26; yb = top+70
        for k in (l,h):
            x = left + k*(cell+gap) + cell//2
            parts.append(f'<path d="M {x} {ya} L {x-7} {ya-9} L {x+7} {ya-9} Z" fill="#38BDF8"/>')
            parts.append(f'<path d="M {x} {yb} L {x-7} {yb+9} L {x+7} {yb+9} Z" fill="#38BDF8"/>')
        _cmp = "&lt;" if vals[m] < target else "&gt;"
        msg = f"区间[{l},{h}] 探测 mid={m}（值{vals[m]}）" + ("→ 命中!" if found else f"→ {vals[m]}{_cmp}{target} 收{'左' if vals[m]<target else '右'}")
        parts.append(f'<text x="{w//2}" y="240" text-anchor="middle" fill="#94A3B8" font-size="14">{msg}</text>')
        parts.append('</g>')
    parts.append('<style>')
    for s in range(len(steps)):
        a = s/len(steps)*100; b = (s+1)/len(steps)*100; f = (b-a)*0.10
        parts.append(f'.bs{s}{{opacity:0}} @keyframes bs{s}{{0%{{opacity:0}}{a:.2f}%{{opacity:0}}{a+f:.2f}%{{opacity:1}}{b-f:.2f}%{{opacity:1}}{b:.2f}%{{opacity:0}}100%{{opacity:0}}}}')
    parts.append('</style></svg>')
    return "\n".join(parts)

def dp_table_svg(w=560, h=310):
    # 0/1 背包或 LCS 风格的 DP 表逐格填充动画（以斐波那契一维表演示更直观）
    vals = [0,1,1,2,3,5,8,13]
    n = len(vals); cell = 48; gap = 8; left = (w-n*(cell+gap))//2+8; top = 110
    dur = 0.8
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="system-ui,sans-serif">']
    parts.append('<rect width="%d" height="%d" rx="12" fill="#0F172A"/>' % (w,h))
    parts.append(f'<text x="{w//2}" y="34" text-anchor="middle" fill="#E2E8F0" font-size="17" font-weight="600">DP 表逐格填充 · dp[i]=dp[i-1]+dp[i-2]</text>')
    for s in range(2, n):
        t0 = (s-2)*dur
        parts.append(f'<g style="animation:dp{s} {dur*2.2}s linear {t0}s 1 both">')
        for k in range(n):
            x = left+k*(cell+gap)
            filled = k <= s
            bg = "#34D399" if k==s else ("#334155" if filled else "#1E293B")
            fg = "#0F172A" if k==s else ("#F1F5F9" if filled else "#475569")
            parts.append(f'<rect x="{x}" y="{top}" width="{cell}" height="46" rx="8" fill="{bg}"/>')
            if filled:
                parts.append(f'<text x="{x+cell//2}" y="{top+30}" text-anchor="middle" fill="{fg}" font-size="16" font-weight="700">{vals[k]}</text>')
        if s >= 2:
            x1 = left+(s-1)*(cell+gap)+cell//2; x2 = left+(s-2)*(cell+gap)+cell//2; x3 = left+s*(cell+gap)+cell//2
            parts.append(f'<path d="M {x2} {top-8} Q {(x2+x3)//2} {top-40} {x3} {top-8}" stroke="#38BDF8" fill="none" stroke-width="2"/>')
            parts.append(f'<path d="M {x1} {top-8} Q {(x1+x3)//2} {top-40} {x3} {top-8}" stroke="#F472B6" fill="none" stroke-width="2"/>')
            parts.append(f'<text x="{w//2}" y="230" text-anchor="middle" fill="#94A3B8" font-size="14">dp[{s}] = dp[{s-1}] + dp[{s-2}] = {vals[s]}</text>')
        parts.append('</g>')
    parts.append('<style>')
    for s in range(2, n):
        parts.append(f'.dp{s}{{opacity:0}} @keyframes dp{s}{{0%{{opacity:0}}15%{{opacity:1}}80%{{opacity:1}}100%{{opacity:1}}}}')
    parts.append('</style></svg>')
    return "\n".join(parts)

def stack_svg(ops=(("push",1),("push",2),("push",3),("pop",None),("push",4),("pop",None)), w=560, h=310):
    dur = 1.2; base = 250; bw = 130; bx = 210
    stack = []; steps = []
    for op, v in ops:
        if op == "push": stack.append(v)
        else: stack.pop() if stack else None
        steps.append((op, v, stack[:]))
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="system-ui,sans-serif">']
    parts.append('<rect width="560" height="310" rx="12" fill="#0F172A"/>')
    parts.append('<text x="280" y="34" text-anchor="middle" fill="#E2E8F0" font-size="17" font-weight="600">栈 · 后进先出 LIFO（顶部进出）</text>')
    parts.append(f'<path d="M {bx-14} {base} L {bx-14} {base-180}" stroke="#475569" stroke-width="3"/>')
    parts.append(f'<path d="M {bx+bw+14} {base} L {bx+bw+14} {base-180}" stroke="#475569" stroke-width="3"/>')
    parts.append(f'<path d="M {bx-22} {base} L {bx+bw+22} {base}" stroke="#475569" stroke-width="3"/>')
    for s,(op,v,snap) in enumerate(steps):
        t0 = s*dur
        parts.append(f'<g style="animation:sk{s} {len(steps)*dur}s linear infinite both">')
        for i, val in enumerate(snap):
            y = base - (i+1)*52 + 6
            top_el = i == len(snap)-1
            col = "#FACC15" if top_el and op=="push" else ("#F87171" if top_el and op=="pop" else "#4A90D9")
            parts.append(f'<rect x="{bx}" y="{y}" width="{bw}" height="46" rx="8" fill="{col}"/>')
            parts.append(f'<text x="{bx+bw//2}" y="{y+30}" text-anchor="middle" fill="#0F172A" font-size="18" font-weight="700">{val}</text>')
        parts.append(f'<text x="430" y="120" fill="#94A3B8" font-size="14">{"push "+str(v) if op=="push" else "pop → 栈顶出"}</text>')
        parts.append(f'<text x="430" y="146" fill="#64748B" font-size="13">size={len(snap)}</text>')
        parts.append('</g>')
    parts.append('<style>')
    for s in range(len(steps)):
        a = s/len(steps)*100; b = (s+1)/len(steps)*100; f = (b-a)*0.15
        parts.append(f'.sk{s}{{opacity:0}} @keyframes sk{s}{{0%{{opacity:0}}{a:.2f}%{{opacity:0}}{a+f:.2f}%{{opacity:1}}{b-f:.2f}%{{opacity:1}}{b:.2f}%{{opacity:0}}100%{{opacity:0}}}}')
    parts.append('</style></svg>')
    return "\n".join(parts)

def heap_svg(vals=(3,1,6,5,2,4), w=560, h=320):
    # 最小堆插入上浮动画：依次 insert，展示 shiftUp 后的堆结构
    dur = 1.5
    snapshots = []; heap = []
    import heapq
    for v in vals:
        heapq.heappush(heap, v)
        snapshots.append((f"insert {v} → 上浮到正确位置", heap[:]))
    n_snap = len(snapshots)
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="system-ui,sans-serif">']
    parts.append('<rect width="560" height="320" rx="12" fill="#0F172A"/>')
    parts.append('<text x="280" y="30" text-anchor="middle" fill="#E2E8F0" font-size="17" font-weight="600">最小堆 · 逐个插入自动上浮（数组=完全二叉树）</text>')
    for s,(msg, snap) in enumerate(snapshots):
        t0 = s*dur
        parts.append(f'<g style="animation:hp{s} {n_snap*dur}s linear infinite both">')
        n = len(snap)
        pos = {}
        for i in range(n):
            depth = (i + 1).bit_length()  # 节点 i（0 基）所在层，1 起
            idx_in_level = i - (2**(depth-1) - 1)
            level_cnt = 2**(depth-1)
            x = 280 + (idx_in_level+0.5-level_cnt/2) * (400/level_cnt)
            y = 60 + (depth-1)*62
            pos[i] = (x,y)
        for i in range(n):
            p = (i-1)//2
            if i>0:
                x1,y1 = pos[p]; x2,y2 = pos[i]
                parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#475569" stroke-width="2"/>')
        for i,v in enumerate(snap):
            x,y = pos[i]
            is_new = i == n-1
            col = "#FACC15" if is_new else "#4A90D9"
            parts.append(f'<circle cx="{x}" cy="{y}" r="21" fill="{col}" stroke="#93C5FD" stroke-width="2"/>')
            parts.append(f'<text x="{x}" y="{y+6}" text-anchor="middle" fill="#0F172A" font-size="14" font-weight="700">{v}</text>')
        parts.append(f'<text x="280" y="305" text-anchor="middle" fill="#94A3B8" font-size="13">{msg} ｜ 数组: {snap}</text>')
        parts.append('</g>')
    parts.append('<style>')
    for s in range(n_snap):
        a = s/n_snap*100; b = (s+1)/n_snap*100; f = (b-a)*0.12
        parts.append(f'.hp{s}{{opacity:0}} @keyframes hp{s}{{0%{{opacity:0}}{a:.2f}%{{opacity:0}}{a+f:.2f}%{{opacity:1}}{b-f:.2f}%{{opacity:1}}{b:.2f}%{{opacity:0}}100%{{opacity:0}}}}')
    parts.append('</style></svg>')
    return "\n".join(parts)

GENS.update({"binary_search": binary_search_svg, "dp_table": dp_table_svg, "stack": stack_svg, "heap": heap_svg})

if __name__ == "__main__":
    kind = sys.argv[1]; out = sys.argv[2]
    svg = GENS[kind]()
    with open(out, "w") as f: f.write(svg)
    print(f"wrote {out} ({len(svg)} bytes)")
