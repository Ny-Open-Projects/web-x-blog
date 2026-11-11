#!/usr/bin/env python3
# svg_anim_extra.py — 第二批 SVG 动画生成器（9 种）：
# 双指针 / 滑动窗口 / 链表反转 / 队列 / 哈希链地址 / 回溯棋盘 / 贪心跳跃 / BFS 波纹 / 归并排序
# 与 svg_anim.py 同风格：暗色底 #0F172A，CSS keyframes 分步淡入淡出，自动循环播放


def _fade_style(total, dur):
    # 百分比窗口关键帧：整个序列 total*dur 秒一个周期，infinite 无限循环
    parts = ["<style>"]
    for s in range(total):
        a = s / total * 100
        b = (s + 1) / total * 100
        f = (b - a) * 0.12
        parts.append(
            f'.st{s} {{opacity:0}} @keyframes st{s} {{0%{{opacity:0}}{a:.2f}%{{opacity:0}}{a+f:.2f}%{{opacity:1}}{b-f:.2f}%{{opacity:1}}{b:.2f}%{{opacity:0}}100%{{opacity:0}}}}'
        )
    parts.append("</style>")
    return "\n".join(parts)


def _show(s, dur, total):
    return f'animation: st{s} {total * dur}s linear infinite both'


def _head(w, h, title):
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="system-ui,sans-serif">',
        f'<rect width="{w}" height="{h}" rx="12" fill="#0F172A"/>',
        f'<text x="{w // 2}" y="34" text-anchor="middle" fill="#E2E8F0" font-size="17" font-weight="600">{title}</text>',
    ]


# ---------- 1. 双指针（数组两数之和） ----------
def two_pointers_svg(vals=(2, 7, 11, 15), target=9, w=560, h=300):
    n = len(vals)
    cell_w, gap, left, base = 72, 16, 78, 140
    steps = []
    l, r = 0, n - 1
    while l < r:
        s = vals[l] + vals[r]
        if s == target:
            steps.append((l, r, f"arr[L] + arr[R] = {s} = {target}，命中！"))
            break
        if s > target:
            steps.append((l, r, f"arr[L] + arr[R] = {s} &gt; {target}，R 左移"))
            r -= 1
        else:
            steps.append((l, r, f"arr[L] + arr[R] = {s} &lt; {target}，L 右移"))
            l += 1
    dur = 1.5
    parts = _head(w, h, f"双指针 · 两数之和（target = {target}，自动循环播放）")
    for s_i, (l_i, r_i, note) in enumerate(steps):
        parts.append(f'<g style="{_show(s_i, dur, len(steps))}">')
        for k, v in enumerate(vals):
            x = left + k * (cell_w + gap)
            col = "#4A90D9"
            if k == l_i or k == r_i:
                col = "#FACC15" if l_i != r_i else "#F87171"
            if note.startswith("arr[L] + arr[R]") and "命中" in note and (k == l_i or k == r_i):
                col = "#34D399"
            parts.append(f'<rect x="{x}" y="{base - 46}" width="{cell_w}" height="46" rx="8" fill="{col}"/>')
            parts.append(f'<text x="{x + cell_w // 2}" y="{base - 16}" text-anchor="middle" fill="#F1F5F9" font-size="19" font-weight="700">{v}</text>')
        lx = left + l_i * (cell_w + gap) + cell_w // 2
        rx = left + r_i * (cell_w + gap) + cell_w // 2
        parts.append(f'<polygon points="{lx},{base - 54} {lx - 8},{base - 68} {lx + 8},{base - 68}" fill="#FACC15"/>')
        parts.append(f'<text x="{lx}" y="{base - 74}" text-anchor="middle" fill="#FACC15" font-size="14" font-weight="700">L</text>')
        parts.append(f'<polygon points="{rx},{base - 54} {rx - 8},{base - 68} {rx + 8},{base - 68}" fill="#FACC15"/>')
        parts.append(f'<text x="{rx}" y="{base - 74}" text-anchor="middle" fill="#FACC15" font-size="14" font-weight="700">R</text>')
        parts.append(f'<text x="{w // 2}" y="255" text-anchor="middle" fill="#94A3B8" font-size="14">{note}</text>')
        parts.append("</g>")
    parts.append(_fade_style(len(steps), dur))
    parts.append("</svg>")
    return "\n".join(parts)


# ---------- 2. 滑动窗口（无重复字符最长子串） ----------
def sliding_window_svg(s="abcabcbb", w=560, h=300):
    n = len(s)
    cell_w, gap, left, base = 52, 8, 55, 150
    steps = []  # (l, r, note, kind)  kind: expand/shrink/found
    char_pos = {}
    l = 0
    best_len, best_lr = 0, (0, 0)
    for r in range(n):
        ch = s[r]
        if ch in char_pos and char_pos[ch] >= l:
            steps.append((char_pos[ch] + 1, r, f"'{ch}' 重复 → L 跳到 {char_pos[ch] + 1}", "shrink"))
            l = char_pos[ch] + 1
        char_pos[ch] = r
        steps.append((l, r, f"窗口 [L..R] = '{s[l:r + 1]}'，长度 {r - l + 1}", "expand"))
        if r - l + 1 > best_len:
            best_len, best_lr = r - l + 1, (l, r)
    steps.append((best_lr[0], best_lr[1], f"最长无重复子串 '{s[best_lr[0]:best_lr[1] + 1]}'（长度 {best_len}）", "found"))
    dur = 1.5
    parts = _head(w, h, "滑动窗口 · 无重复字符的最长子串（自动循环播放）")
    for s_i, (l_i, r_i, note, kind) in enumerate(steps):
        parts.append(f'<g style="{_show(s_i, dur, len(steps))}">')
        if kind != "found":
            wx = left + l_i * (cell_w + gap) - 4
            ww = (r_i - l_i + 1) * (cell_w + gap) - gap + 8
            col = "#34D399" if kind == "expand" else "#F87171"
            parts.append(f'<rect x="{wx}" y="{base - 44}" width="{ww}" height="54" rx="10" fill="none" stroke="{col}" stroke-width="3"/>')
        for k, ch in enumerate(s):
            x = left + k * (cell_w + gap)
            in_win = l_i <= k <= r_i
            col = "#4A90D9" if in_win else "#334155"
            if kind == "found" and in_win:
                col = "#34D399"
            parts.append(f'<rect x="{x}" y="{base - 38}" width="{cell_w}" height="42" rx="8" fill="{col}"/>')
            parts.append(f'<text x="{x + cell_w // 2}" y="{base - 10}" text-anchor="middle" fill="#F1F5F9" font-size="18" font-weight="700">{ch}</text>')
        parts.append(f'<text x="{w // 2}" y="255" text-anchor="middle" fill="#94A3B8" font-size="14">{note}</text>')
        parts.append("</g>")
    parts.append(_fade_style(len(steps), dur))
    parts.append("</svg>")
    return "\n".join(parts)


# ---------- 3. 链表反转（指针迁移） ----------
def linked_list_svg(vals=(1, 2, 3, 4), w=560, h=300):
    n = len(vals)
    box_w, box_h, node_gap, left, base = 72, 42, 42, 46, 130
    nx = lambda i: left + i * (box_w + node_gap)  # noqa: E731
    null_x = nx(n - 1) + box_w + node_gap + 6
    # 每步: (arrows {(a,b) b=None→null}, prev, cur, note)
    steps = [
        ({(i, i + 1) for i in range(n - 1)}, None, 0, "初始：prev = null，cur 指向头节点"),
    ]
    prev, cur = None, 0
    while cur is not None:
        # 已反转: 0→N, 1→0, ..., cur→cur-1；未反转: cur+1→cur+2→...→N
        arrows = {(0, None)}
        for i in range(1, cur + 1):
            arrows.add((i, i - 1))
        for i in range(cur + 1, n):
            arrows.add((i, i + 1) if i + 1 < n else (i, None))
        note = f"{vals[cur]} 反转指向 {'null' if prev is None else vals[prev]}"
        steps.append((arrows, cur, cur + 1 if cur + 1 < n else None, note))
        prev, cur = cur, cur + 1 if cur + 1 < n else None
    steps.append((steps[-1][0], n - 1, None, "完成！新头节点 = 最后一个节点"))
    dur = 1.5
    parts = _head(w, h, "链表反转 · 三指针逐步迁移（自动循环播放）")
    for s_i, (arrows, prev_i, cur_i, note) in enumerate(steps):
        parts.append(f'<g style="{_show(s_i, dur, len(steps))}">')
        for i, v in enumerate(vals):
            x = nx(i)
            col = "#4A90D9"
            if i == cur_i:
                col = "#FACC15"
            elif prev_i is not None and i <= prev_i:
                col = "#34D399"
            parts.append(f'<rect x="{x}" y="{base - box_h // 2}" width="{box_w}" height="{box_h}" rx="9" fill="{col}"/>')
            parts.append(f'<text x="{x + box_w // 2}" y="{base + 6}" text-anchor="middle" fill="#F1F5F9" font-size="18" font-weight="700">{v}</text>')
        parts.append(f'<rect x="{null_x}" y="{base - 18}" width="52" height="36" rx="8" fill="#334155"/>')
        parts.append(f'<text x="{null_x + 26}" y="{base + 6}" text-anchor="middle" fill="#94A3B8" font-size="14">null</text>')
        for (a, b) in arrows:
            if b is None:
                x1, x2 = nx(a) + box_w, null_x
            else:
                x1, x2 = nx(a) + box_w, nx(b) if b > a else nx(b) + box_w
            y = base + 2
            parts.append(f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="#E2E8F0" stroke-width="2.5" marker-end="url(#arr)"/>')
        if prev_i is not None:
            px = nx(prev_i) + box_w // 2
            parts.append(f'<text x="{px}" y="{base + 44}" text-anchor="middle" fill="#34D399" font-size="13" font-weight="700">prev</text>')
        if cur_i is not None:
            cx = nx(cur_i) + box_w // 2
            parts.append(f'<text x="{cx}" y="{base + 44}" text-anchor="middle" fill="#FACC15" font-size="13" font-weight="700">cur</text>')
        parts.append(f'<text x="{w // 2}" y="255" text-anchor="middle" fill="#94A3B8" font-size="14">{note}</text>')
        parts.append("</g>")
    parts.append('<defs><marker id="arr" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 z" fill="#E2E8F0"/></marker></defs>')
    parts.append(_fade_style(len(steps), dur))
    parts.append("</svg>")
    return "\n".join(parts)


# ---------- 4. 队列 FIFO（入队/出队） ----------
def queue_svg(w=560, h=300):
    cap = 6
    slot_w, left, base = 66, 72, 130
    steps = []  # (contents list, front, rear_end, note)
    q = []
    front = 0
    rear = 0
    steps.append(([], front, rear, "空队列，front = rear = 0"))
    for v in (10, 20, 30):
        q.append(v)
        rear += 1
        steps.append((q[:], front, rear, f"enqueue({v}) → rear 后移"))
    for _ in range(2):
        out = q.pop(0)
        front += 1
        steps.append((q[:], front, rear, f"dequeue() → {out}，front 后移"))
    steps.append((q[:], front, rear, "队列剩余元素：先入先出（FIFO）"))
    dur = 1.4
    parts = _head(w, h, "队列 · 先进先出 FIFO（自动循环播放）")
    for s_i, (contents, f_i, r_i, note) in enumerate(steps):
        parts.append(f'<g style="{_show(s_i, dur, len(steps))}">')
        for k in range(cap):
            x = left + k * (slot_w + 8)
            has = k < len(contents) + f_i and k >= f_i and (k - f_i) < len(contents)
            col = "#4A90D9" if has else "#1E293B"
            stroke = "#334155"
            if has and k == f_i:
                stroke = "#34D399"
            if has and k == r_i - 1:
                stroke = "#FACC15"
            parts.append(f'<rect x="{x}" y="{base - 34}" width="{slot_w}" height="44" rx="8" fill="{col}" stroke="{stroke}" stroke-width="2"/>')
            if has:
                v = contents[k - f_i]
                parts.append(f'<text x="{x + slot_w // 2}" y="{base - 5}" text-anchor="middle" fill="#F1F5F9" font-size="17" font-weight="700">{v}</text>')
        fx = left + f_i * (slot_w + 8) + slot_w // 2
        parts.append(f'<text x="{fx}" y="{base + 32}" text-anchor="middle" fill="#34D399" font-size="13" font-weight="700">front</text>')
        rx = left + r_i * (slot_w + 8) + slot_w // 2
        parts.append(f'<text x="{rx}" y="{base - 44}" text-anchor="middle" fill="#FACC15" font-size="13" font-weight="700">rear</text>')
        parts.append(f'<text x="{w // 2}" y="245" text-anchor="middle" fill="#94A3B8" font-size="14">{note}</text>')
        parts.append("</g>")
    parts.append(_fade_style(len(steps), dur))
    parts.append("</svg>")
    return "\n".join(parts)


# ---------- 5. 哈希表链地址法 ----------
def hash_chaining_svg(keys=(12, 7, 22, 8, 3), nbuckets=5, w=560, h=364):
    bucket_n = nbuckets
    bx, by, bh, bgap = 78, 74, 36, 12
    node_w = 58
    chain = {i: [] for i in range(bucket_n)}
    steps = []
    for k in keys:
        b = k % bucket_n
        chain[b].append(k)
        steps.append((b, {i: c[:] for i, c in chain.items()}, f"insert({k})：hash = {k} % {bucket_n} = {b}" + ("（冲突，链到表尾）" if len(chain[b]) > 1 else "")))
    look = keys[1]
    lb = look % bucket_n
    steps.append((lb, {i: c[:] for i, c in chain.items()}, f"find({look})：桶 {lb} 沿链查找 → 命中"))
    dur = 1.5
    parts = _head(w, h, "哈希表 · 链地址法解决冲突（自动循环播放）")
    for s_i, (hl, snap, note) in enumerate(steps):
        parts.append(f'<g style="{_show(s_i, dur, len(steps))}">')
        for i in range(bucket_n):
            y = by + i * (bh + bgap)
            parts.append(f'<rect x="{bx}" y="{y}" width="70" height="{bh}" rx="8" fill="{"#FACC15" if i == hl else "#334155"}"/>')
            parts.append(f'<text x="{bx + 35}" y="{y + 24}" text-anchor="middle" fill="#E2E8F0" font-size="15" font-weight="700">桶 {i}</text>')
            for j, v in enumerate(snap[i]):
                x = bx + 90 + j * (node_w + 34)
                col = "#4A90D9" if not (i == hl and note.startswith("find") and v == look) else "#34D399"
                parts.append(f'<rect x="{x}" y="{y}" width="{node_w}" height="{bh}" rx="8" fill="{col}"/>')
                parts.append(f'<text x="{x + node_w // 2}" y="{y + 24}" text-anchor="middle" fill="#F1F5F9" font-size="15" font-weight="700">{v}</text>')
                start_x = (bx + 70) if j == 0 else (x - 34)
                parts.append(f'<line x1="{start_x}" y1="{y + bh // 2}" x2="{x}" y2="{y + bh // 2}" stroke="#E2E8F0" stroke-width="2" marker-end="url(#harr)"/>')
        parts.append(f'<text x="{w // 2}" y="{by + bucket_n * (bh + bgap) + 26}" text-anchor="middle" fill="#94A3B8" font-size="14">{note}</text>')
        parts.append("</g>")
    parts.append('<defs><marker id="harr" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#E2E8F0"/></marker></defs>')
    parts.append(_fade_style(len(steps), dur))
    parts.append("</svg>")
    return "\n".join(parts)


# ---------- 6. 回溯棋盘（4 皇后） ----------
def backtrack_svg(w=560, h=320):
    n = 4
    cell = 46
    bx, by = 150, 66
    sol = [1, 3, 0, 2]
    steps = [
        ([(0, 0)], "#FACC15", "第 0 列：尝试第 0 行"),
        ([(0, 0)], "#F87171", "后续列无位置可放 → 回溯，撤销该皇后"),
        ([(1, 0)], "#FACC15", "第 0 列改放第 1 行"),
        ([(1, 0), (3, 1)], "#FACC15", "第 1 列：第 3 行安全"),
        ([(1, 0), (3, 1), (0, 2)], "#FACC15", "第 2 列：第 0 行安全"),
        ([(1, 0), (3, 1), (0, 2), (2, 3)], "#34D399", "第 3 列：第 2 行安全 → 解为 [1, 3, 0, 2]"),
    ]
    dur = 1.7
    parts = _head(w, h, "回溯 · 4 皇后（放置 → 冲突 → 回溯，自动循环播放）")
    for s_i, (queens, col, note) in enumerate(steps):
        parts.append(f'<g style="{_show(s_i, dur, len(steps))}">')
        for r in range(n):
            for c in range(n):
                x, y = bx + c * cell, by + r * cell
                fill = "#1E293B" if (r + c) % 2 == 0 else "#26334D"
                parts.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" fill="{fill}" stroke="#334155"/>')
        for (r, c) in queens:
            x, y = bx + c * cell, by + r * cell
            parts.append(f'<rect x="{x + 3}" y="{y + 3}" width="{cell - 6}" height="{cell - 6}" rx="6" fill="{col}" opacity="0.28"/>')
            parts.append(f'<text x="{x + cell // 2}" y="{y + cell - 10}" text-anchor="middle" font-size="26" fill="{col}">♛</text>')
        parts.append(f'<text x="{w // 2}" y="{by + n * cell + 40}" text-anchor="middle" fill="#94A3B8" font-size="14">{note}</text>')
        parts.append("</g>")
    parts.append(_fade_style(len(steps), dur))
    parts.append("</svg>")
    return "\n".join(parts)


# ---------- 7. 贪心跳跃（最远可达） ----------
def greedy_jump_svg(vals=(2, 3, 1, 1, 4), w=560, h=300):
    n = len(vals)
    bar_w, gap, left, base = 66, 14, 66, 170
    furthest = 0
    steps = []
    for i in range(n):
        if i > furthest:
            break
        furthest = max(furthest, i + vals[i])
        note = f"i = {i}：最远可达 = max({furthest}, {i} + {vals[i]}) = {furthest}"
        if furthest >= n - 1:
            note += " → 已覆盖终点！"
        steps.append((i, furthest, note))
    dur = 1.6
    parts = _head(w, h, "贪心 · 跳跃游戏（维护最远可达边界，自动循环播放）")
    for s_i, (i_i, fur, note) in enumerate(steps):
        parts.append(f'<g style="{_show(s_i, dur, len(steps))}">')
        for k, v in enumerate(vals):
            x = left + k * (bar_w + gap)
            reach = k + v
            col = "#334155" if reach > fur else ("#34D399" if reach >= n - 1 else "#4A90D9")
            if k == i_i:
                col = "#FACC15"
            h_bar = 28 + v * 26
            parts.append(f'<rect x="{x}" y="{base - h_bar}" width="{bar_w}" height="{h_bar}" rx="6" fill="{col}"/>')
            parts.append(f'<text x="{x + bar_w // 2}" y="{base - h_bar - 7}" text-anchor="middle" fill="#F1F5F9" font-size="15" font-weight="700">{v}</text>')
            parts.append(f'<text x="{x + bar_w // 2}" y="{base + 18}" text-anchor="middle" fill="#94A3B8" font-size="13">idx {k}</text>')
        fx = left + fur * (bar_w + gap) + bar_w // 2
        fx = min(fx, w - 60)  # 标签钳制在画布内
        parts.append(f'<line x1="{left - 8}" y1="{base + 30}" x2="{min(left - 8 + fur * (bar_w + gap), w - 24)}" y2="{base + 30}" stroke="#34D399" stroke-width="3"/>')
        parts.append(f'<text x="{fx}" y="{base + 48}" text-anchor="middle" fill="#34D399" font-size="13" font-weight="700">最远可达 {fur}</text>')
        parts.append(f'<text x="{w // 2}" y="270" text-anchor="middle" fill="#94A3B8" font-size="14">{note}</text>')
        parts.append("</g>")
    parts.append(_fade_style(len(steps), dur))
    parts.append("</svg>")
    return "\n".join(parts)


# ---------- 8. BFS 波纹扩散（网格最短路） ----------
def bfs_wave_svg(w=560, h=380):
    n = 5
    cell = 52
    bx, by = 145, 64
    blocked = {(1, 1), (2, 1), (3, 3)}
    levels = [[(0, 0)], [(1, 0), (0, 1)], [(2, 0), (0, 2)], [(3, 0), (1, 2), (0, 3)],
              [(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], [(4, 1), (3, 2), (2, 3), (1, 4)],
              [(4, 2), (2, 4)], [(4, 3), (3, 4)], [(4, 4)]]
    palette = ["#FACC15", "#FB923C", "#F87171", "#F472B6", "#C084FC",
               "#818CF8", "#60A5FA", "#34D399", "#2DD4BF"]
    dur = 1.0
    parts = _head(w, h, "BFS · 波纹式逐层扩散（起点 → 终点最短步数，自动循环播放）")
    total = len(levels)
    for s_i, lvl in enumerate(levels):
        parts.append(f'<g style="{_show(s_i, dur, len(levels))}">')
        for r in range(n):
            for c in range(n):
                x, y = bx + c * cell, by + r * cell
                if (r, c) in blocked:
                    parts.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" fill="#0B1120" stroke="#334155" stroke-width="1.5"/>')
                    parts.append(f'<text x="{x + cell // 2}" y="{y + cell // 2 + 6}" text-anchor="middle" fill="#475569" font-size="18">✕</text>')
                    continue
                parts.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" fill="#1E293B" stroke="#334155" stroke-width="1.5"/>')
        for li in range(s_i + 1):
            for (r, c) in levels[li]:
                x, y = bx + c * cell, by + r * cell
                parts.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" fill="{palette[li % len(palette)]}" opacity="{1.0 if li == s_i else 0.55}"/>')
                parts.append(f'<text x="{x + cell // 2}" y="{y + cell // 2 + 6}" text-anchor="middle" fill="#0F172A" font-size="16" font-weight="800">{li}</text>')
        parts.append(f'<text x="{w // 2}" y="{by + n * cell + 34}" text-anchor="middle" fill="#94A3B8" font-size="14">第 {s_i} 层扩散（数字 = 距起点的最短步数）</text>')
        parts.append("</g>")
    parts.append(_fade_style(total, dur))
    parts.append("</svg>")
    return "\n".join(parts)


# ---------- 9. 归并排序（分与合） ----------
def merge_sort_svg(vals=(5, 2, 9, 1, 7, 3), w=560, h=300):
    snaps = [
        (list(vals), "分：递归拆到单元素"),
        ([2, 5, 1, 9, 3, 7], "两两归并：[2,5] [1,9] [3,7]"),
        ([1, 2, 5, 9, 3, 7], "归并 [2,5] + [1,9] → [1,2,5,9]"),
        ([1, 2, 3, 5, 7, 9], "最终归并 → 全局有序"),
    ]
    bar_w, gap, left, base = 64, 14, 62, 180
    dur = 1.8
    parts = _head(w, h, "归并排序 · 分治（拆分 → 合并有序段，自动循环播放）")
    for s_i, (arr, note) in enumerate(snaps):
        parts.append(f'<g style="{_show(s_i, dur, len(snaps))}">')
        for k, v in enumerate(arr):
            x = left + k * (bar_w + gap)
            h_bar = 20 + v * 16
            col = "#4A90D9"
            if s_i == 3:
                col = "#34D399"
            elif s_i >= 2 and k < 4:
                col = "#C084FC"
            elif s_i >= 1:
                col = "#60A5FA"
            parts.append(f'<rect x="{x}" y="{base - h_bar}" width="{bar_w}" height="{h_bar}" rx="6" fill="{col}"/>')
            parts.append(f'<text x="{x + bar_w // 2}" y="{base - h_bar - 7}" text-anchor="middle" fill="#F1F5F9" font-size="15" font-weight="700">{v}</text>')
        parts.append(f'<text x="{w // 2}" y="255" text-anchor="middle" fill="#94A3B8" font-size="14">{note}</text>')
        parts.append("</g>")
    parts.append(_fade_style(len(snaps), dur))
    parts.append("</svg>")
    return "\n".join(parts)


# ---------- 10. 异步任务时序（concurrency 专属） ----------
def promise_timeline_svg(w=560, h=320):
    # 三个异步任务并发执行，按完成时刻先后 resolve：经典"按完成顺序输出"语义
    tasks = [("taskA", 0, 300, "#4A90D9"), ("taskB", 0, 100, "#34D399"), ("taskC", 0, 200, "#FACC15")]
    total_t = 320
    lane_h, lane_gap, left, top = 40, 18, 110, 74
    px = lambda t: left + t / total_t * (w - left - 90)  # noqa: E731
    steps = [
        (0, "t=0ms：三个任务并发启动", []),
        (100, "t=100ms：taskB 最先完成", ["taskB"]),
        (200, "t=200ms：taskC 完成", ["taskB", "taskC"]),
        (300, "t=300ms：taskA 完成 → 全部就绪", ["taskB", "taskC", "taskA"]),
    ]
    dur = 1.8
    parts = _head(w, h, "并发 · 异步任务时序（完成顺序 ≠ 启动顺序，自动循环播放）")
    # 泳道背景
    for s_i, (t_ms, note, done) in enumerate(steps):
        parts.append(f'<g style="{_show(s_i, dur, len(steps))}">')
        for li, (name, st, end, col) in enumerate(tasks):
            y = top + li * (lane_h + lane_gap)
            parts.append(f'<text x="{left - 14}" y="{y + lane_h // 2 + 5}" text-anchor="end" fill="#94A3B8" font-size="13" font-weight="600">{name}</text>')
            parts.append(f'<rect x="{left}" y="{y}" width="{w - left - 90}" height="{lane_h}" rx="8" fill="#1E293B"/>')
            x1, x2 = px(st), px(end)
            is_done = name in done
            parts.append(f'<rect x="{x1}" y="{y}" width="{max(x2 - x1, 4)}" height="{lane_h}" rx="8" fill="{col}" opacity="{1.0 if is_done else 0.35}"/>')
            parts.append(f'<text x="{(x1 + x2) // 2}" y="{y + lane_h // 2 + 5}" text-anchor="middle" fill="#0F172A" font-size="13" font-weight="700">{end}ms</text>')
            if is_done:
                parts.append(f'<circle cx="{px(end)}" cy="{y + lane_h // 2}" r="6" fill="{col}" stroke="#0F172A" stroke-width="2"/>')
        # 完成时刻竖虚线
        for li, (name, st, end, col) in enumerate(tasks):
            if name in done:
                x = px(end)
                parts.append(f'<line x1="{x}" y1="{top - 8}" x2="{x}" y2="{top + 3 * lane_h + 2 * lane_gap}" stroke="{col}" stroke-width="1.5" stroke-dasharray="4 4" opacity="0.7"/>')
        # 结果顺序
        ry = top + 3 * (lane_h + lane_gap) + 6
        seq = " → ".join(done) if done else "（等待中…）"
        parts.append(f'<text x="{w // 2}" y="{ry + 14}" text-anchor="middle" fill="#34D399" font-size="14" font-weight="700">完成顺序：{seq}</text>')
        parts.append(f'<text x="{w // 2}" y="{ry + 38}" text-anchor="middle" fill="#94A3B8" font-size="13">{note}</text>')
        parts.append("</g>")
    parts.append(_fade_style(len(steps), dur))
    parts.append("</svg>")
    return "\n".join(parts)
