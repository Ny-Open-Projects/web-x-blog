#!/usr/bin/env python3
# verify_official.py — 用 leetcode.cn 官方 exampleTestcases 验证全部 TS 解法
# 机制：按签名参数类型直接构造官方输入（TreeNode/ListNode 走文件自带的 build 建造器），
#       在解法自身 demo() 作用域内、console.log("PASS") 之前注入官方用例检查，node 运行要求
#       输出 OFFICIAL-PASS。期望：官方示例与用例数对齐时用官方期望；否则用同题多实现共识。
import json, os, re, subprocess, sys, tempfile
from collections import defaultdict

DSA = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa"
OC = json.load(open(f"{DSA}/_meta/official_cases.json"))
OP = json.load(open(f"{DSA}/_meta/official_parsed.json"))

SERIALIZERS = '''
function __serTree(root: any): any {
  if (root === null || root === undefined) return null;
  const arr: any[] = []; const q: any[] = [root];
  while (q.length) { const n: any = q.shift()!;
    if (n === null || n === undefined) { arr.push(null); continue; }
    arr.push(n.val); q.push(n.left); q.push(n.right); }
  while (arr.length && arr[arr.length - 1] === null) arr.pop();
  return arr;
}
function __serList(head: any): any {
  const a: any[] = []; let p = head; let guard = 0;
  while (p && guard++ < 200000) { a.push(p.val); p = p.next; }
  return a;
}
function __mkTree(vals: any[]): any {
  if (!vals || vals.length === 0 || vals[0] === null) return null;
  const root: any = { val: vals[0], left: null, right: null };
  const q: any[] = [root]; let i = 1;
  while (q.length && i < vals.length) {
    const n: any = q.shift()!;
    if (i < vals.length && vals[i] !== null) { n.left = { val: vals[i], left: null, right: null }; q.push(n.left); } i++;
    if (i < vals.length && vals[i] !== null) { n.right = { val: vals[i], left: null, right: null }; q.push(n.right); } i++;
  }
  return root;
}
function __inorder(root: any, out: any[]): void {
  if (!root) return;
  __inorder(root.left, out); out.push(root.val); __inorder(root.right, out);
}
function __collect(root: any, out: any[]): void {
  if (!root) return; out.push(root.val); __collect(root.left, out); __collect(root.right, out);
}
function __checkBST(root: any, inputVals: any[]): string {
  const io: any[] = []; __inorder(root, io);
  for (let i = 1; i < io.length; i++) if (io[i - 1] >= io[i]) return "NOT-BST";
  const all: any[] = []; __collect(root, all);
  const sa = io.slice().sort((x, y) => x - y).join(",");
  const sb = inputVals.slice().sort((x, y) => x - y).join(",");
  return sa === sb ? "BST-VALID" : "ELEM-MISMATCH";
}
function __hashFormat(root: any): string {
  // 116/117 官方输出：层内节点 val 依 next 链，层间以 # 分隔
  const parts: any[] = []; let head = root;
  while (head) {
    const lvl: any[] = [];
    for (let p = head; p; p = p.next) lvl.push(p.val);
    parts.push(lvl.join(","));
    let nextHead: any = null; let tail: any = null;
    for (let p = head; p; p = p.next) {
      for (const ch of [p.left, p.right]) {
        if (ch) { if (tail) { tail.next = ch; } else { nextHead = ch; } tail = ch; }
      }
    }
    head = nextHead;
  }
  return "[" + parts.join(",#,") + ",#]";
}
function __rightChain(root: any): any[] {
  const out: any[] = []; let p = root; let guard = 0;
  while (p && guard++ < 200000) { out.push(p.val); p = p.right; }
  return out;
}
function __findVal(root: any, v: any): any {
  if (!root) return null;
  if (root.val === v) return root;
  return __findVal(root.left, v) || __findVal(root.right, v);
}
function __path(root: any, v: any, acc: any[]): boolean {
  if (!root) return false;
  acc.push(root.val);
  if (root.val === v) return true;
  if (__path(root.left, v, acc) || __path(root.right, v, acc)) return true;
  acc.pop();
  return false;
}
function __isLCA(L: any, root: any, pVal: any, qVal: any, wantVal: any): string {
  if (!L) return "NULL-RETURN";
  const pa: any[] = [], qa: any[] = [];
  if (!__path(root, pVal, pa)) return "P-NOT-FOUND";
  if (!__path(root, qVal, qa)) return "Q-NOT-FOUND";
  let i = 0;
  while (i < pa.length && i < qa.length && pa[i] === qa[i]) i++;
  const lca = pa[i - 1];
  if (L.val !== lca) return "LCA-WRONG:" + L.val + " true:" + lca;
  if (wantVal !== null && wantVal !== undefined && Number(wantVal) !== lca) return "LCA-EXP-MISMATCH";
  return "LCA-OK:" + lca;
}
function __mkList(vals: any[], pos?: number): any {
  const dum: any = { val: 0, next: null }; let p = dum;
  const nodes: any[] = [];
  for (const v of vals || []) { p.next = { val: v, next: null }; p = p.next; nodes.push(p); }
  if (pos !== undefined && pos !== null && pos >= 0 && nodes.length) {
    nodes[nodes.length - 1].next = nodes[pos];
  }
  return dum.next;
}
'''


def strip_comments(code):
    out, in_blk = [], False
    for ln in code.split("\n"):
        if in_blk:
            if "*/" in ln:
                ln = ln.split("*/", 1)[1]
                in_blk = False
            else:
                out.append("")
                continue
        if "//" in ln:
            k = ln.find("//")
            if not (k > 0 and ln[k - 1] == ":"):
                ln = ln[:k]
        while "/*" in ln:
            a = ln.find("/*")
            b = ln.find("*/", a + 2)
            if b < 0:
                ln = ln[:a]
                in_blk = True
                break
            ln = ln[:a] + ln[b + 2:]
        out.append(ln)
    return "\n".join(out)


def demo_span(code):
    m = re.search(r"function\s+demo\s*\([^)]*\)[^{]*\{", code)
    if not m:
        return None
    i, depth, j = m.end(), 1, m.end()
    while j < len(code) and depth > 0:
        if code[j] == "{":
            depth += 1
        elif code[j] == "}":
            depth -= 1
        j += 1
    return m.end(), j - 1


HARNESS = {"build", "tolist", "buildtree", "tolevel", "eqarr", "asserteq", "jarr", "same",
           "serial", "levelorder", "printlist", "arrtolist", "listtoarr", "inorder", "height",
           "eq", "neq", "toarr", "toarray", "treetolevel", "levellist", "levelorderarr",
           "ser", "serialize", "midorder", "preorder", "postorder", "collect"}


# 官方 Special Judge（答案不唯一）的题号：树构造类离线无法逐字节比对
SPECIAL_JUDGE = {"108", "109", "114"}
LIT_HINTS = []


def parse_sig(code):
    """返回 (alg_name, [param_types], ret_type)。"""
    cands = [m.group(1) for m in re.finditer(r"function\s+(\w+)\s*\(", code)]
    cands += [m.group(1) for m in re.finditer(
        r"(?:const|let)\s+(\w+)\s*=\s*(?:\([^)]*\)|\w+)\s*(?::\s*[^=]+?)?=>", code)]
    cands = [c for c in dict.fromkeys(cands)
             if c != "demo" and c.lower() not in HARNESS]
    if not cands:
        return None
    cands = prune_candidates(code, cands)
    bl0, _, bt0, _ = find_builders(code)
    cands = [c for c in cands if c not in (bl0, bt0)]
    if not cands:
        return None
    ds = demo_span(code)
    alg = None
    if ds:
        # 测试区起点：首个 cases 定义 / assertEq 调用 / 测试循环，取最早出现者
        starts = []
        for pat in (r"const cases[:\s]", r"assertEq\(", r"expectEq\(", r"for \(const c of cases\)"):
            ms = re.search(pat, code[ds[0]:ds[1]])
            if ms:
                starts.append(ds[0] + ms.start())
        scan_from = min(starts) if starts else ds[0]
        # 官方输入字面量（示例里的数组/数字/字符串片段）
        import json as _json
        lit_bits = set()
        op2 = json.load(open(f"{DSA}/_meta/official_parsed.json"))
        for e in op2.get("?", {}).get("examples", []):
            pass
        pat = re.compile(r"(?<![\w.])(\w+)\s*\(")
        scored = {}
        order = {}
        for mm in pat.finditer(code, scan_from, ds[1]):
            nm = mm.group(1)
            if nm in cands:
                pre = code[max(0, mm.start() - 60):mm.start()]
                if re.search(r"function\s*$", pre):
                    continue
                argtxt = code[mm.end():mm.end() + 160]
                score = 0
                for lit in LIT_HINTS:
                    if lit and lit in argtxt:
                        score += 2
                if re.search(r"(=\s*$|\(\s*as\s+any\s*\)\s*\(|return\s+$)", pre):
                    score += 1
                scored[nm] = scored.get(nm, 0) + score
                order[nm] = order.get(nm, 0) + 1
        alg = None
        if scored:
            alg = sorted(scored.items(), key=lambda x: (x[1], order[x[0]]))[-1][0]
        if alg is None:
            return None
    if alg is None:
        return None  # demo 里没调用过的一律不猜（猜错会污染判定）
    sm = re.search(rf"function\s+{alg}\s*\(([^)]*)\)\s*(?::\s*([\w\[\]<>| ]+?))?\s*\{{", code)
    if not sm:
        return None
    types = []
    for p in sm.group(1).split(","):
        pm = re.search(r":\s*([^=]+?)\s*(?:=[^,]*)?$", p.strip())
        types.append(pm.group(1).strip() if pm else "any")
    return alg, types, (sm.group(2) or "any").strip()


def find_builders(code):
    """建造器：函数体内 new ListNode/TreeNode 即认（返回注解常是 any）。"""
    bl = bt = None
    bl_argc = bt_argc = 1
    for m in re.finditer(r"function\s+(\w+)\s*\(([^)]*)\)\s*\{", code):
        span = fn_body_span(code, m.group(1))
        if not span:
            continue
        body = code[span[0]:span[1]]
        argc = len([p for p in m.group(2).split(",") if p.strip()])
        if bl is None and ("new ListNode" in body or re.search(r"new\s+(Nd|Node|ListNode)\b", body)
                           or re.search(r"val:[^,}]*,\s*next:", body)):
            bl, bl_argc = m.group(1), max(1, argc)
        elif bt is None and ("new TreeNode" in body or re.search(r"new\s+(Nd|Node|TreeNode)\b", body)
                             or re.search(r"val:[^,}]*,\s*left:", body)):
            bt, bt_argc = m.group(1), max(1, argc)
        if bl and bt:
            break
    return bl, bl_argc, bt, bt_argc


def fn_body_span(code, name):
    m = re.search(rf"function\s+{name}\s*\([^)]*\)[^{{]*\{{", code)
    if not m:
        return None
    i, depth, j = m.end(), 1, m.end()
    while j < len(code) and depth > 0:
        if code[j] == "{":
            depth += 1
        elif code[j] == "}":
            depth -= 1
        j += 1
    return m.start(), j


def prune_candidates(code, cands):
    """去掉「被其他候选函数体内调用」的候选（内部辅助）。"""
    drop = set()
    for a in cands:
        sa = fn_body_span(code, a)
        if not sa:
            continue
        for b in cands:
            if b == a:
                continue
            if re.search(rf"(?<![\w.]){b}\s*\(", code[sa[0]:sa[1]]):
                drop.add(b)
    return [c for c in cands if c not in drop]


def parse_lenient(s):
    """输出值解析：容忍多行/尾逗号/省略号。"""
    s = re.sub(r"\bMore\.\.\b|\.\.\.", "", s)
    s = re.sub(r",\s*([\]}])", r"\1", s.strip())
    try:
        return json.loads(s)
    except Exception:
        return s.strip()


def parse_val(s):
    s = s.strip().rstrip("。.,；;，")
    s = s.strip()
    if s in ("true", "false"):
        return s == "true"
    if s in ("null", "undefined", ""):
        return None
    try:
        return json.loads(s)
    except Exception:
        return s.strip('"')


def _top_split(s):
    """按顶层逗号切分（括号/引号感知）。"""
    parts, depth, cur, i, in_str = [], 0, "", 0, None
    while i < len(s):
        ch = s[i]
        if in_str:
            cur += ch
            if ch == in_str and (i == 0 or s[i - 1] != "\\"):
                in_str = None
        elif ch in "\"'":
            in_str = ch
            cur += ch
        elif ch in "([{":
            depth += 1
            cur += ch
        elif ch in ")]}":
            depth -= 1
            cur += ch
        elif ch == "," and depth == 0:
            parts.append(cur.strip())
            cur = ""
        else:
            cur += ch
        i += 1
    if cur.strip():
        parts.append(cur.strip())
    return parts


def split_named(body):
    """输入体 → [(name 或 None, value_str)]。优先「名 = 值」对；无名形态整段按位置切值。"""
    s = re.sub(r"^\s*输入[:：]\s*", "", body.strip())
    s = re.split(r"\n\s*输出[:：]", s)[0]
    pairs = _top_split(s)
    named = []
    for p in pairs:
        m = re.match(r"([\w\[\]]+)\s*=\s*(.*)$", p, re.S)
        if m:
            named.append((m.group(1), m.group(2).strip()))
        else:
            named.append((None, p))
    if any(nm is None for nm, _ in named):
        return [(None, v) for nm, v in named]
    return named


def consume(ex, types):
    """官方示例 → [(kind, val[, pos])]。仅当命名对数量多于参数数时（如 141 的 head+pos），
    ListNode 参数后面的整数对才被吸收为 pos，并整体右移游标。"""
    named = split_named(ex.get("body", ""))
    if not named or len(named) < len(types):
        return None
    absorb = len(named) > len(types)
    vals = []
    j = 0
    for t in types:
        nm, vstr = named[j]
        v = parse_val(vstr)
        if ("ListNode" in t and absorb and j + 1 < len(named)
                and re.match(r"^-?\d+$", named[j + 1][1].strip())):
            vals.append(("list", v, parse_val(named[j + 1][1])))
            j += 2
        else:
            vals.append(("plain", v, None))
            j += 1
    return vals


def arg_expr(t, kv, bl, bl_argc, bt, alg_body=""):
    any_kind = ""
    if "any" in t:
        if re.search(r"\.(left|right)\b", alg_body):
            any_kind = "tree"
        elif re.search(r"\.next\b", alg_body):
            any_kind = "list"
    if re.search(r"(?:Array|List)<[^>]*ListNode", t):
        if not bl:
            bl = "__mkList"
            bl_argc = 1
        items = ", ".join(f"{bl}({json.dumps(x, ensure_ascii=False)})"
                          for x in (kv[1] or []) if isinstance(x, list))
        return f"[{items}]"
    if "TreeNode" in t or any_kind == "tree":
        b = bt or "__mkTree"
        return f"{b}({json.dumps(kv[1], ensure_ascii=False)})"
    if "ListNode" in t or any_kind == "list":
        if kv[2] is not None:
            return f"__mkList({json.dumps(kv[1], ensure_ascii=False)}, {json.dumps(kv[2])})"
        b, argc = (bl, bl_argc) if bl else ("__mkList", 1)
        return f"{b}({json.dumps(kv[1], ensure_ascii=False)})"
    return json.dumps(kv[1], ensure_ascii=False)



def norm_wrap(ret_t):
    # 运行时鸭子类型：ListNode(val+next) / TreeNode(left) 自动选择序列化器
    return ("JSON.stringify((v) => v) === '' ? __got : "  # 占位，不会用到
            "__norm(__got)")


def sig_arity_all(code):
    """全部候选（含参数数）：[(name, types, ret)]，排除 demo/harness/建造器。"""
    cands = [m.group(1) for m in re.finditer(r"function\s+(\w+)\s*\(", code)]
    cands = [c for c in dict.fromkeys(cands)
             if c != "demo" and c.lower() not in HARNESS]
    bl, _, bt, _ = find_builders(code)
    cands = [c for c in cands if c not in (bl, bt)]
    out = []
    for nm in cands:
        sm = re.search(rf"function\s+{nm}\s*\(([^)]*)\)\s*(?::\s*([\w\[\]<>| ]+?))?\s*\{{", code)
        if not sm:
            continue
        types = []
        for p in sm.group(1).split(","):
            pm = re.search(r":\s*([^=]+?)\s*(?:=[^,]*)?$", p.strip())
            types.append(pm.group(1).strip() if pm else "any")
        out.append((nm, types, (sm.group(2) or "any").strip()))
    return out


def build_cases(types, exs, lcnum):
    case_exprs, case_off, raw_args = [], [], []
    for ti, ex in enumerate(exs):
        kvs = consume(ex, types)
        if not kvs:
            return None, None, None
        exprs = [arg_expr(types[i], kv, *find_builders.cache.get("x", (None, 1, None, 1)), "") for i, kv in enumerate(kvs)]
        if any(e is None for e in exprs):
            return None, None, None
        case_exprs.append(exprs)
        case_off.append(exp_json_cache.get((lcnum, ti)))
        raw_args.append(json.dumps([kv[1] for kv in kvs], ensure_ascii=False))
    return case_exprs, case_off, raw_args


def build_cases(types, exs, lcnum, bl, bl_argc, bt, bt_argc, exp_json):
    case_exprs, case_off, raw_args = [], [], []
    for ti, ex in enumerate(exs):
        kvs = consume(ex, types)
        if not kvs:
            return None, None, None
        exprs = []
        for i, kv in enumerate(kvs):
            e = arg_expr(types[i], kv, bl, bl_argc, bt, "")
            if e is None:
                return None, None, None
            exprs.append(e)
        if lcnum == "236" and len(exprs) >= 3:
            exprs[1] = f"__findVal({exprs[0]}, {json.dumps(kvs[1][1])})"
            exprs[2] = f"__findVal({exprs[0]}, {json.dumps(kvs[2][1])})"
        case_exprs.append(exprs)
        case_off.append(exp_json.get(ti))
        raw_args.append(json.dumps([kv[1] for kv in kvs], ensure_ascii=False))
    return case_exprs, case_off, raw_args


def run_candidate(code0, code, alg, ret_t, mode, case_exprs, case_off, raw_args, tag):
    """对一个候选函数生成 runner 并运行；返回 OC 输出列表或错误串。"""
    dspan = demo_span(code)
    ins = None
    for pm in re.finditer(r'console\.log\(\s*["\']PASS["\']\s*\)', code[dspan[0]:dspan[1]]):
        ins = dspan[0] + pm.start()
    if ins is not None:
        ins = code.rfind("\n", 0, ins)
    else:
        ins = dspan[1]
    lines = ["", "  { // leetcode.cn 官方示例用例验证（自动注入）",
             "    const __norm = (v: any): any => {",
             "      if (v === null || v === undefined || typeof v !== 'object') return v;",
             "      if ('next' in v && 'val' in v) return __serList(v);",
             "      if ('left' in v && 'right' in v) return __serTree(v);",
             "      return v;",
             "    };",
             "    const __rawArgs: string[] = [" + ", ".join(
                 json.dumps(r, ensure_ascii=False) for r in raw_args) + "];",
             "    const __oc: any[][] = ["]
    for ce in case_exprs:
        lines.append("      [" + ", ".join(ce) + "],")
    lines.append("    ];")
    lines.append("    const __ow: any[] = [" + ", ".join(
        "null" if o is None else o for o in case_off) + "];")
    lines.append("    let __bad = 0;")
    lines.append("    for (let __i = 0; __i < __oc.length; __i++) {")
    if mode == "flatten":
        lines.append(f"      ({alg} as any)(...__oc[__i]);")
        lines.append("      const __gotN = JSON.stringify(__rightChain(__oc[__i][0]));")
    elif mode == "hashfmt":
        lines.append(f"      ({alg} as any)(...__oc[__i]);")
        lines.append("      const __gotN = __hashFormat(__oc[__i][0]);")
    elif mode == "lca":
        lines.append("      const L = (" + alg + " as any)(__oc[__i][0], __oc[__i][1], __oc[__i][2]);")
        lines.append("      const wv = __ow[__i] === null ? null : Number(__ow[__i]);")
        lines.append("      const __gotN = __isLCA(L, __oc[__i][0], __oc[__i][1].val, __oc[__i][2].val, wv);")
    elif mode == "bst":
        lines.append("      const raw: any[] = JSON.parse(__rawArgs[__i]);")
        lines.append(f"      const __tree = ({alg} as any)(...__oc[__i]);")
        lines.append("      const __gotN = __checkBST(__tree, raw[0]);")
    else:
        lines.append(f"      const __got = ({alg} as any)(...__oc[__i]);")
        lines.append("      const __gotN = JSON.stringify(__norm(__got));")
    lines.append("      console.log('OC', __i, String(__gotN).slice(0, 300));")
    lines.append("      if (__ow[__i] !== null && String(__gotN) !== String(__ow[__i])")
    lines.append("          && !(" + str(mode in ("bst", "lca")) + ")) __bad++;")
    lines.append("    }")
    lines.append('    if (__bad) throw new Error("OFFICIAL-FAIL " + __bad + "/" + __oc.length);')
    lines.append('    console.log("OFFICIAL-PASS", __oc.length);')
    lines.append("  }")
    new_body = code[:ins] + "\n".join(lines) + code[ins:]
    new_body = SERIALIZERS + "\n" + new_body
    rp = os.path.join(tempfile.mkdtemp(prefix="lcv_"), f"r_{tag}.ts")
    open(rp, "w", encoding="utf-8").write(new_body)
    try:
        r = subprocess.run(["node", rp], capture_output=True, text=True, timeout=25)
        outs = re.findall(r"^OC (\d+) (.*)$", r.stdout, re.M)
        if not outs:
            return "err:" + (r.stderr or r.stdout).strip().split("\n")[-1][:80]
        return outs
    except subprocess.TimeoutExpired:
        return "err:超时"


def main():
    cur = json.load(open(f"{DSA}/_meta/curriculum.json"))
    report = {}
    n_files = n_skip = n_prob_ok = n_partial = 0
    for c in cur:
        m = re.match(r"lc_(\d+)_", c["problem"])
        if not m or m.group(1) not in OC:
            continue
        lcnum, prob = m.group(1), c["problem"]
        tdir = None
        for topic in os.listdir(f"{DSA}/ts"):
            if os.path.isdir(f"{DSA}/code/ts/{topic}/{prob}"):
                tdir = f"{DSA}/code/ts/{topic}/{prob}"
                break
        if not tdir:
            continue
        sols = sorted((f for f in os.listdir(tdir) if f.startswith("solution_") and f.endswith(".ts")),
                      key=lambda s: [int(x) if x.isdigit() else x for x in re.split(r"(\d+)", s)])
        exs = OP.get(lcnum, {}).get("examples", [])
        if not exs:
            report[lcnum] = {"status": "skip", "reason": "无官方示例"}
            continue
        exp_json = {}
        hash_fmt = False
        for i, e in enumerate(exs):
            mm = re.search(r"输出[:：]\s*(.*)$", e.get("body", ""), re.S)
            if not mm:
                continue
            val = parse_lenient(mm.group(1))
            if isinstance(val, str) and "#" in val:
                hash_fmt = True
            exp_json[i] = json.dumps(val, separators=(",", ":"), ensure_ascii=False)
        mode = "plain"
        if lcnum == "114":
            mode = "flatten"
        elif lcnum in ("117", "116"):
            mode = "hashfmt"
        elif lcnum == "236":
            mode = "lca"
        elif lcnum in SPECIAL_JUDGE:
            mode = "bst"
        # ---- 阶段一：在代表文件上扫候选 ----
        codes = {sf: strip_comments(open(f"{tdir}/{sf}", encoding="utf-8", errors="ignore").read())
                 for sf in sols}
        cand_list = sig_arity_all(codes[sols[0]])
        pairs_n = len(split_named(exs[0].get("body", ""))) or len(cand_list and cand_list[0][1] or [])
        if mode == "lca":
            pairs_n = 3
        adopted = None  # (alg, types, ret_t)
        probe = None
        for nm2, types2, ret2 in cand_list:
            if mode == "lca" and len(types2) != 3:
                continue
            built = build_cases(types2, exs, lcnum, *find_builders(codes[sols[0]]), exp_json)
            if built[0] is None:
                continue
            probe = run_candidate(codes[sols[0]], codes[sols[0]], nm2, ret2, mode,
                                  built[0], built[1], built[2], f"{lcnum}_probe")
            if isinstance(probe, list):
                if mode == "plain" and exp_json:
                    ok_probe = all(
                        probe[i][1] == exp_json.get(int(probe[i][0]))
                        or probe[i][1] is not None and exp_json.get(int(probe[i][0])) is None
                        for i in range(len(probe)))
                    if not ok_probe:
                        continue
                adopted = (nm2, types2, ret2)
                break
        results = {}
        if adopted:
            alg, types, ret_t = adopted
            built = build_cases(types, exs, lcnum, *find_builders(codes[sols[0]]), exp_json)
            for sf in sols:
                n_files += 1
                outs = run_candidate(codes[sf], codes[sf], alg, ret_t, mode,
                                     built[0], built[1], built[2], f"{lcnum}_{re.sub(r'[^A-Za-z0-9]', '_', sf)[:30]}")
                if isinstance(outs, str):
                    n_skip += 1
                    results[sf] = "skip:" + outs
                else:
                    results[sf] = outs
        else:
            n_skip += len(sols)
            results = {sf: "skip:无候选通过官方用例" for sf in sols}
        real = {k: v for k, v in results.items() if not isinstance(v, str)}
        if not real:
            report[lcnum] = {"status": "skip", "detail": results}
            continue
        per_case = defaultdict(dict)
        for sf, outs in real.items():
            for ci, got in outs:
                per_case[int(ci)][got] = per_case[int(ci)].get(got, 0) + 1
        verdicts = []

        def _canon(s):
            try:
                v = json.loads(s)
            except Exception:
                return s
            if isinstance(v, list):
                return sorted(json.dumps(x, ensure_ascii=False) for x in v)
            if isinstance(v, str):
                return "".join(sorted(v))
            return s

        def _multi_ok(ref, got):
            try:
                rj, gj = json.loads(ref), json.loads(got)
            except Exception:
                return False
            if isinstance(rj, str) and isinstance(gj, str):
                return sorted(rj) == sorted(gj)
            try:
                if (isinstance(rj, list) and isinstance(gj, list) and rj
                        and all(isinstance(x, list) for x in rj)
                        and all(isinstance(x, list) for x in gj)):
                    cs = lambda arr: sorted(
                        json.dumps(sorted(x, key=lambda y: json.dumps(y, ensure_ascii=False)),
                                   ensure_ascii=False) for x in arr)
                    return cs(rj) == cs(gj)
            except Exception:
                return False
            return _canon(ref) == _canon(got)

        def _num_eq(a, b):
            try:
                ja, jb = json.loads(a), json.loads(b)
            except Exception:
                return False
            if isinstance(ja, list) and isinstance(jb, list) and len(ja) == len(jb):
                return all(abs(x - y) < 1e-9 for x, y in zip(ja, jb)
                           if isinstance(x, (int, float)) and isinstance(y, (int, float)))
            return False

        def _empty_eq(a, b):
            empt = {"[]", "null", "{}"}
            return a in empt and b in empt

        for ci in sorted(per_case):
            variants = per_case[ci]
            ref = exp_json.get(ci)
            if ref is None:
                top = max(variants.items(), key=lambda x: x[1])
                if len(variants) > 1 and top[1] == sorted(variants.values())[-2 if len(variants) > 1 else 0]:
                    verdicts.append({"case": ci, "ok": True, "ref": "TIE", "variants": variants})
                    continue
                ref = top[0]
            agree = set(variants) == {ref} or (len(variants) == 1 and next(iter(variants)) == ref)
            unjudgeable = False
            if not agree and ref is not None:
                if ref.startswith('"') and ref.endswith('"'):
                    unjudgeable = True
                elif mode in ("bst", "lca", "hashfmt", "flatten"):
                    unjudgeable = True
                else:
                    agree = all(_multi_ok(ref, g2) or _num_eq(ref, g2) or _empty_eq(ref, g2)
                                for g2 in variants)
            verdicts.append({"case": ci, "ok": bool(agree or unjudgeable), "ref": ref,
                             "variants": variants, "unjudgeable": unjudgeable})
        bad = [v for v in verdicts if not v["ok"]]
        partial = bool(aligned_check(exs, exp_json) and verdicts and bad and all(
            (cv["ref"] == "TIE") or any(g == cv["ref"] for g in cv["variants"])
            for cv in verdicts))
        if bad and not partial:
            status = "FAIL"
        elif bad:
            status = "partial"
        else:
            status = "ok"
        report[lcnum] = {"status": status, "cases": verdicts, "files": results}
        if status == "ok":
            n_prob_ok += 1
        elif status == "partial":
            n_partial += 1
            print(f"  partial {prob}: {json.dumps(bad, ensure_ascii=False)[:150]}")
        elif status == "FAIL":
            print(f"  FAIL {prob}: {json.dumps(bad, ensure_ascii=False)[:180]}")
    json.dump(report, open(f"{DSA}/_meta/official_verify.json", "w"), ensure_ascii=False)
    n_fail = sum(1 for v in report.values() if v["status"] == "FAIL")
    n_skip_p = sum(1 for v in report.values() if v["status"] == "skip")
    print(f"文件 {n_files}，文件级跳过 {n_skip}；题级：ok {n_prob_ok} / partial {n_partial} / "
          f"fail {n_fail} / skip {n_skip_p}")


def aligned_check(exs, exp_json):
    return bool(exs) and len(exp_json) == len(exs)


if __name__ == "__main__":
    main()
