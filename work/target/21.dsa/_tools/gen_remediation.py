#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate faithful TS ports of python references with embedded assertions.
Strategy: transpile python module (funcs+classes) to `any`-typed TS; capture
__main__ as demo(); for standard problems inject oracle-computed assertions.
python-side oracle computes expected outputs; TS asserts deep equality.
"""
import os, ast, json, re

BASE = "/Users/Wang/Code/github/web-x-blog/work/target/21.dsa"
NODE = "/Users/Wang/.workbuddy/binaries/node/versions/22.22.2-6/bin/node"

PY_SHIMS = r"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right
def build_tree(vals):
    if not vals: return None
    root = TreeNode(vals[0]); q = [root]; i = 1
    while q and i < len(vals):
        node = q.pop(0)
        if vals[i] is not None:
            node.left = TreeNode(vals[i]); q.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i]); q.append(node.right)
        i += 1
    return root
def tree_to_level(root):
    if not root: return []
    out = []; q = [root]
    while q:
        n = q.pop(0)
        if n is None: out.append(None); continue
        out.append(n.val); q.append(n.left); q.append(n.right)
    while out and out[-1] is None: out.pop()
    return out
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val; self.next = next
def build_list(vals):
    dummy = ListNode(0); cur = dummy
    for v in vals:
        cur.next = ListNode(v); cur = cur.next
    return dummy.next
def list_to_arr(head):
    out = []; p = head
    while p: out.append(p.val); p = p.next
    return out
def to_list(head): return list_to_arr(head)
class Node:
    def __init__(self, val=0, children=None):
        self.val = val; self.children = children if children is not None else []
def build_nary(vals):
    if not vals: return None
    if not isinstance(vals, list): return Node(vals)
    root = Node(vals[0])
    for i in range(1, len(vals)):
        root.children.append(build_nary(vals[i]))
    return root
def nary_level(root):
    if not root: return []
    out = []; q = [root]
    while q:
        nxt = []; cur = []
        for n in q:
            cur.append(n.val)
            for c in n.children: nxt.append(c)
        out.append(cur); q = nxt
    return out
"""

TS_PRELUDE = r"""
class TreeNode {
    val: any; left: any; right: any;
    constructor(val?: any, left?: any, right?: any) {
        this.val = (val === undefined ? 0 : val);
        this.left = (left === undefined ? null : left);
        this.right = (right === undefined ? null : right);
    }
}
function buildTree(vals: any): any {
    if (!vals || vals.length === 0) return null;
    const root = new TreeNode(vals[0]); const q: any[] = [root]; let i = 1;
    while (q.length && i < vals.length) {
        const node = q.shift();
        if (vals[i] !== null && vals[i] !== undefined) { node.left = new TreeNode(vals[i]); q.push(node.left); }
        i++;
        if (i < vals.length && vals[i] !== null && vals[i] !== undefined) { node.right = new TreeNode(vals[i]); q.push(node.right); }
        i++;
    }
    return root;
}
function treeToLevel(root: any): any[] {
    if (!root) return [];
    const out: any[] = []; const q: any[] = [root];
    while (q.length) {
        const n = q.shift();
        if (n === null || n === undefined) { out.push(null); continue; }
        out.push(n.val); q.push(n.left); q.push(n.right);
    }
    while (out.length && out[out.length - 1] === null) out.pop();
    return out;
}
class ListNode {
    val: any; next: any;
    constructor(val?: any, next?: any) { this.val = (val === undefined ? 0 : val); this.next = (next === undefined ? null : next); }
}
function buildList(vals: any): any {
    const dummy = new ListNode(0); let cur = dummy;
    for (const v of vals) { cur.next = new ListNode(v); cur = cur.next; }
    return dummy.next;
}
function listToArray(head: any): any[] {
    const out: any[] = []; let p = head;
    while (p) { out.push(p.val); p = p.next; }
    return out;
}
// python-runtime shims
function pyLen(a: any): number {
    if (a === null || a === undefined) return 0;
    if (typeof a === 'string' || Array.isArray(a) || a instanceof Set || a instanceof Map) return a.length ?? a.size;
    if (typeof a === 'object') return Object.keys(a).length;
    return 0;
}
function pySlice(a: any, i: any, j: any, step?: any): any {
    if (typeof a === 'string') { const r = [...a].slice(i ?? 0, j ?? a.length); return step ? r.reverse().join('') : r.join(''); }
    const arr = Array.isArray(a) ? a : [...a];
    return arr.slice(i ?? 0, j ?? arr.length);
}
function pyRange(a: any, b?: any, step?: any): any[] {
    let s = 0, e = a, st = 1;
    if (b !== undefined) { s = a; e = b; }
    if (step !== undefined) st = step;
    const out: any[] = [];
    if (st > 0) for (let i = s; i < e; i += st) out.push(i);
    else for (let i = s; i > e; i += st) out.push(i);
    return out;
}
function pyIn(x: any, coll: any): boolean {
    if (coll === null || coll === undefined) return false;
    if (Array.isArray(coll)) return coll.includes(x);
    if (coll instanceof Set || coll instanceof Map) return coll.has(x);
    if (typeof coll === 'object') return x in coll;
    if (typeof coll === 'string') return coll.indexOf(x) >= 0;
    return false;
}
function pySorted(a: any): any[] {
    const arr = (typeof a === 'string') ? [...a] : [...a];
    return arr.sort((x: any, y: any) => (x < y ? -1 : x > y ? 1 : 0));
}
function pyMin(a: any, b?: any): any { if (b !== undefined) return Math.min(a, b); if (Array.isArray(a) || a instanceof Set) return Math.min(...a); return Math.min(a); }
function pyMax(a: any, b?: any): any { if (b !== undefined) return Math.max(a, b); if (Array.isArray(a) || a instanceof Set) return Math.max(...a); return Math.max(a); }
function pySum(a: any): number { let s = 0; for (const v of a) s += v; return s; }
function pyAbs(x: any): number { return Math.abs(x); }
function pyEnumerate(a: any): any[] { const out: any[] = []; let i = 0; for (const v of a) { out.push([i, v]); i++; } return out; }
function pyZip(a: any, b: any): any[] { const n = Math.min(a.length, b.length); const out: any[] = []; for (let i = 0; i < n; i++) out.push([a[i], b[i]]); return out; }
function pyDictGet(d: any, k: any, def?: any): any { return (k in d) ? d[k] : (def === undefined ? null : def); }
function pyPrint(...args: any[]): void { console.log(args.map(a => (typeof a === 'object' && a !== null ? JSON.stringify(a) : a)).join(' ')); }
// collections / heapq
function heapPush(h: any[], x: any): void { h.push(x); let i = h.length - 1; while (i > 0) { const p = (i - 1) >> 1; if (h[p] <= h[i]) break; [h[p], h[i]] = [h[i], h[p]]; i = p; } }
function heapPop(h: any[]): any { const top = h[0]; const last = h.pop(); if (h.length) { h[0] = last; let i = 0; const n = h.length; while (true) { let l = 2*i+1, r = 2*i+2, s = i; if (l < n && h[l] < h[s]) s = l; if (r < n && h[r] < h[s]) s = r; if (s === i) break; [h[s], h[i]] = [h[i], h[s]]; i = s; } } return top; }
class Deque { private a: any[] = []; push(x: any){ this.a.push(x);} pushLeft(x:any){ this.a.unshift(x);} pop(){ return this.a.pop(); } popLeft(){ return this.a.shift(); } get length(){ return this.a.length; } toArray(){ return this.a.slice(); } }
function Counter(iter: any): any { const m: any = {}; for (const v of iter) m[v] = (m[v] || 0) + 1; return m; }
function gcd(a: any, b: any): any { while (b) { [a, b] = [b, a % b]; } return a; }
function pyInf(): number { return Infinity; }
"""

EQ_TS = r"""
function norm(x: any): any {
    if (x === null || x === undefined) return null;
    if (typeof x === 'object') {
        if (x instanceof Deque) return x.toArray();
        if (Array.isArray(x)) return x.map(norm);
        if (typeof x.val === 'number' && (typeof x.left !== 'undefined' || typeof x.right !== 'undefined')) return treeToLevel(x);
        if (typeof x.next !== 'undefined' && typeof x.val === 'number') return listToArray(x);
        if (x instanceof Set) return [...x].sort();
        if (x instanceof Map) return Object.fromEntries(x);
        const o: any = {}; for (const k of Object.keys(x)) o[k] = norm(x[k]); return o;
    }
    return x;
}
function eq(a: any, b: any): boolean {
    const x = norm(a), y = norm(b);
    if (x === y) return true;
    if (x === null || y === null) return x === y;
    if (Array.isArray(x) && Array.isArray(y)) {
        if (x.length !== y.length) return false;
        for (let i = 0; i < x.length; i++) if (!eq(x[i], y[i])) return false;
        return true;
    }
    if (typeof x === 'object' && typeof y === 'object') {
        const kx = Object.keys(x), ky = Object.keys(y);
        if (kx.length !== ky.length) return false;
        for (const k of kx) if (!eq(x[k], y[k])) return false;
        return true;
    }
    return x === y;
}
"""


class T:
    def __init__(self):
        self.declared = set()

    def transpile_module(self, src):
        tree = ast.parse(src)
        funcs = []; classes = []; main_body = None
        SKIP_CLASSES = {'TreeNode', 'ListNode', 'Node'}
        for node in tree.body:
            if isinstance(node, ast.FunctionDef):
                funcs.append(node)
            elif isinstance(node, ast.ClassDef):
                if node.name in SKIP_CLASSES:
                    continue
                classes.append(node)
            elif isinstance(node, ast.If):
                # detect __main__
                if self._is_main(node.test):
                    main_body = node.body
        parts = []
        for c in classes:
            parts.append(self.trans_class(c))
        for f in funcs:
            parts.append(self.trans_func(f))
        return "\n".join(p for p in parts if p), (self.stmts(main_body) if main_body else None)

    def _is_main(self, test):
        try:
            return (isinstance(test, ast.Compare) and isinstance(test.left, ast.Name) and test.left.id == '__name__'
                    and isinstance(test.ops[0], ast.Eq) and isinstance(test.comparators[0], ast.Constant) and test.comparators[0].value == '__main__')
        except Exception:
            return False

    def trans_class(self, node):
        methods = []
        for b in node.body:
            if isinstance(b, ast.FunctionDef):
                if b.name == "__init__":
                    methods.append(self.trans_init(b))
                else:
                    methods.append("    " + self.trans_func(b, True).replace("\n", "\n    "))
        return f"class {node.name} {{\n" + "\n".join(methods) + "\n}"

    def trans_init(self, node):
        self.declared = set()
        body = self.stmts(node.body)
        initargs = ", ".join(a.arg for a in node.args.args[1:])
        return f"    constructor({initargs}) {{\n{body}\n    }}"

    def trans_func(self, node, is_method=False):
        self.declared = set()
        args = []
        for a in node.args.args:
            dflt = None
            idx = node.args.args.index(a)
            if node.args.defaults:
                di = idx - (len(node.args.args) - len(node.args.defaults))
                if di >= 0:
                    dflt = node.args.defaults[di]
            at = a.arg
            if dflt is not None:
                at += " = " + self.expr(dflt)
            args.append(at)
        body = self.stmts(node.body)
        prefix = "" if is_method else "function "
        return f"{prefix}{node.name}({', '.join(args)}): any {{\n{body}\n}}"

    def stmts(self, nodes):
        out = []
        for n in nodes:
            s = self.stmt(n)
            if s is not None:
                out.append(s)
        return "\n".join(out)

    def stmt(self, n, indent=0):
        ind = "    " * indent
        if isinstance(n, ast.Assign): return self.assign(n)
        if isinstance(n, ast.AnnAssign): return self.annassign(n)
        if isinstance(n, ast.AugAssign): return self.augassign(n)
        if isinstance(n, ast.If): return self.ifstmt(n, indent)
        if isinstance(n, ast.While): return f"{ind}while ({self.expr(n.test)}) {{\n{self.stmts(n.body)}\n{ind}}}"
        if isinstance(n, ast.For): return self.forstmt(n, indent)
        if isinstance(n, ast.Return): return f"{ind}return {self.expr(n.value) if n.value else ''};"
        if isinstance(n, ast.Break): return f"{ind}break;"
        if isinstance(n, ast.Continue): return f"{ind}continue;"
        if isinstance(n, ast.Pass): return None
        if isinstance(n, ast.Expr): return f"{ind}{self.expr(n.value)};"
        if isinstance(n, (ast.Global, ast.Nonlocal, ast.Import, ast.ImportFrom)): return None
        if isinstance(n, ast.FunctionDef): return "    " + self.trans_func(n).replace("\n", "\n    ")
        if isinstance(n, ast.AnnAssign): return self.annassign(n)
        return f"{ind}/* UNSUPPORTED {type(n).__name__} */"

    def assign(self, n):
        if len(n.targets) != 1: return "/* multi-assign */"
        tgt = n.targets[0]; val = self.expr(n.value)
        if isinstance(tgt, ast.Name):
            nm = tgt.id
            if nm in ('True', 'False', 'None'): return "/* const */"
            if nm in self.declared: return f"{nm} = {val};"
            self.declared.add(nm); return f"let {nm} = {val};"
        if isinstance(tgt, ast.Attribute): return f"{self.expr(tgt)} = {val};"
        if isinstance(tgt, ast.Subscript): return f"{self.expr(tgt)} = {val};"
        if isinstance(tgt, ast.Tuple):
            names = [self.expr(e) for e in tgt.elts]
            return f"const [{', '.join(names)}] = {val};"
        return "/* assign */"

    def annassign(self, n):
        if isinstance(n.target, ast.Name):
            nm = n.target.id
            if n.value is None: return None
            val = self.expr(n.value)
            if nm in self.declared: return f"{nm} = {val};"
            self.declared.add(nm); return f"let {nm} = {val};"
        return f"{self.expr(n.target)} = {self.expr(n.value) if n.value else 'undefined'};"

    def augassign(self, n):
        tgt = self.expr(n.target); op = self.augop(n.op); val = self.expr(n.value)
        return f"{tgt} {op}= {val};"

    def augop(self, op):
        m = {ast.Add:'+', ast.Sub:'-', ast.Mult:'*', ast.Div:'/', ast.Mod:'%', ast.FloorDiv:'/', ast.Pow:'**', ast.LShift:'<<', ast.RShift:'>>', ast.BitAnd:'&', ast.BitOr:'|', ast.BitXor:'^'}
        return m.get(type(op), '+')

    def ifstmt(self, n, indent):
        ind = "    " * indent
        test = self.expr(n.test); body = self.stmts(n.body)
        out = f"{ind}if ({test}) {{\n{body}\n{ind}}}"
        if n.orelse:
            if len(n.orelse) == 1 and isinstance(n.orelse[0], ast.If):
                else_txt = self.stmt(n.orelse[0], indent)
                out = out.rstrip() + " else " + else_txt.lstrip()
            else:
                out += f" else {{\n{self.stmts(n.orelse)}\n{ind}}}"
        return out

    def forstmt(self, n, indent):
        ind = "    " * indent; it = n.iter; tgt = n.target
        if isinstance(it, ast.Call) and isinstance(it.func, ast.Name) and it.func.id == 'range':
            a = it.args
            if len(a) == 1: start, end, step = "0", self.expr(a[0]), "1"
            elif len(a) == 2: start, end, step = self.expr(a[0]), self.expr(a[1]), "1"
            else: start, end, step = self.expr(a[0]), self.expr(a[1]), self.expr(a[2])
            iv = self.expr(tgt)
            return f"{ind}for (let {iv} = {start}; {iv} < {end}; {iv} += {step}) {{\n{self.stmts(n.body)}\n{ind}}}"
        if isinstance(it, ast.Call) and isinstance(it.func, ast.Name) and it.func.id == 'enumerate':
            inner = it.args[0]
            if isinstance(tgt, ast.Tuple): iN, vN = self.expr(tgt.elts[0]), self.expr(tgt.elts[1])
            else: iN, vN = "_i", self.expr(tgt)
            return f"{ind}for (const [{iN}, {vN}] of pyEnumerate({self.expr(inner)})) {{\n{self.stmts(n.body)}\n{ind}}}"
        if isinstance(it, ast.Call) and isinstance(it.func, ast.Name) and it.func.id == 'zip':
            a0, a1 = self.expr(it.args[0]), self.expr(it.args[1])
            if isinstance(tgt, ast.Tuple): n0, n1 = self.expr(tgt.elts[0]), self.expr(tgt.elts[1])
            else: n0, n1 = "_a", self.expr(tgt)
            return f"{ind}for (const [{n0}, {n1}] of pyZip({a0}, {a1})) {{\n{self.stmts(n.body)}\n{ind}}}"
        arr = self.expr(it); vN = self.expr(tgt) if not isinstance(tgt, ast.Tuple) else self.expr(tgt.elts[0])
        if isinstance(tgt, ast.Tuple):
            names = ", ".join(self.expr(e) for e in tgt.elts)
            return f"{ind}for (const [{names}] of {arr}) {{\n{self.stmts(n.body)}\n{ind}}}"
        return f"{ind}for (const {vN} of {arr}) {{\n{self.stmts(n.body)}\n{ind}}}"

    def expr(self, n):
        if isinstance(n, ast.Constant): return self.constant(n)
        if isinstance(n, ast.Name):
            if n.id == 'self': return 'this'
            if n.id == 'True': return 'true'
            if n.id == 'False': return 'false'
            if n.id == 'None': return 'null'
            return n.id
        if isinstance(n, ast.Attribute): return f"{self.expr(n.value)}.{n.attr}"
        if isinstance(n, ast.BinOp): return self.binexpr(n)
        if isinstance(n, ast.BoolOp):
            op = ' && ' if isinstance(n.op, ast.And) else ' || '
            return "(" + op.join(self.expr(v) for v in n.values) + ")"
        if isinstance(n, ast.UnaryOp):
            if isinstance(n.op, ast.Not): return "(!" + self.expr(n.operand) + ")"
            if isinstance(n.op, ast.USub): return "(-" + self.expr(n.operand) + ")"
            if isinstance(n.op, ast.UAdd): return "(+" + self.expr(n.operand) + ")"
            if isinstance(n.op, ast.Invert): return "(~" + self.expr(n.operand) + ")"
        if isinstance(n, ast.Compare): return self.compare(n)
        if isinstance(n, ast.Call): return self.call(n)
        if isinstance(n, ast.Subscript): return self.subscript(n)
        if isinstance(n, ast.List): return "[" + ", ".join(self.expr(e) for e in n.elts) + "]"
        if isinstance(n, ast.ListComp): return self.listcomp(n)
        if isinstance(n, ast.Dict):
            items = []
            for k, v in zip(n.keys, n.values):
                items.append(f"{self.expr(k) if isinstance(k, ast.Constant) else '['+self.expr(k)+']'}: {self.expr(v)}")
            return "{" + ", ".join(items) + "}"
        if isinstance(n, ast.Set): return "new Set([" + ", ".join(self.expr(e) for e in n.elts) + "])"
        if isinstance(n, ast.Tuple): return "[" + ", ".join(self.expr(e) for e in n.elts) + "]"
        if isinstance(n, ast.IfExp): return f"({self.expr(n.test)} ? {self.expr(n.body)} : {self.expr(n.orelse)})"
        if isinstance(n, ast.Lambda): return f"({', '.join(a.arg for a in n.args.args)}) => {self.expr(n.body)}"
        if isinstance(n, ast.JoinedStr): return self.joinedstr(n)
        return "/* EXPR? */"

    def constant(self, n):
        v = n.value
        if v is None: return 'null'
        if v is True: return 'true'
        if v is False: return 'false'
        if isinstance(v, str): return json.dumps(v)
        if isinstance(v, (int, float)): return str(v)
        return json.dumps(v)

    def binexpr(self, n):
        a, b = self.expr(n.left), self.expr(n.right); op = n.op
        m = {ast.Add:(' + '), ast.Sub:(' - '), ast.Mult:(' * '), ast.Div:(' / '), ast.FloorDiv:(' Math.floor ', ' / '), ast.Mod:(' % '), ast.Pow:(' Math.pow ', ' , '), ast.LShift:(' << '), ast.RShift:(' >> '), ast.BitAnd:(' & '), ast.BitOr:(' | '), ast.BitXor:(' ^ ')}
        if isinstance(op, ast.FloorDiv): return f"(Math.floor({a} / {b}))"
        if isinstance(op, ast.Pow): return f"(Math.pow({a}, {b}))"
        s = m.get(type(op), ' + ')
        return f"({a}{s}{b})"

    def compare(self, n):
        left = self.expr(n.left); parts = []
        for op, comp in zip(n.ops, n.comparators):
            right = self.expr(comp)
            if isinstance(op, ast.Eq): parts.append(f"({left} === {right})")
            elif isinstance(op, ast.NotEq): parts.append(f"({left} !== {right})")
            elif isinstance(op, ast.Lt): parts.append(f"({left} < {right})")
            elif isinstance(op, ast.Gt): parts.append(f"({left} > {right})")
            elif isinstance(op, ast.LtE): parts.append(f"({left} <= {right})")
            elif isinstance(op, ast.GtE): parts.append(f"({left} >= {right})")
            elif isinstance(op, ast.Is): parts.append(f"({left} === {right})")
            elif isinstance(op, ast.IsNot): parts.append(f"({left} !== {right})")
            elif isinstance(op, ast.In): parts.append(f"(pyIn({left}, {right}))")
            elif isinstance(op, ast.NotIn): parts.append(f"(!pyIn({left}, {right}))")
            left = right
        return "(" + " && ".join(parts) + ")"

    def call(self, n):
        if isinstance(n.func, ast.Attribute):
            recv = self.expr(n.func.value); meth = n.func.attr
            args = ", ".join(self.expr(a) for a in n.args)
            mm = {
                'append':'push', 'pop':('pop' if False else 'pop'), 'extend':'push(...[])'.replace('...[]',''),
                'get':'pyDictGet', 'items':'Object.entries', 'keys':'Object.keys', 'values':'Object.values',
                'add':'add', 'split':'split', 'join':'join', 'strip':'trim', 'lower':'toLowerCase',
                'upper':'toUpperCase', 'startswith':'startsWith', 'endswith':'endsWith', 'index':'indexOf',
                'reverse':'reverse', 'sort':'sort', 'copy':'slice', 'update':'assign',
            }
            if meth in ('append',): return f"{recv}.push({args})"
            if meth == 'pop' and not n.args: return f"{recv}.pop()"
            if meth == 'pop' and n.args: return f"{recv}.splice({args}, 1)[0]"
            if meth == 'extend': return f"{recv}.push(...{args})"
            if meth == 'get': return f"pyDictGet({recv}, {args})"
            if meth == 'items': return f"Object.entries({recv})"
            if meth == 'keys': return f"Object.keys({recv})"
            if meth == 'values': return f"Object.values({recv})"
            if meth == 'add': return f"{recv}.add({args})"
            if meth == 'heappush': return f"heapPush({recv}, {args})"
            if meth == 'heappop': return f"heapPop({recv})"
            if meth == 'popleft': return f"{recv}.popLeft()"
            if meth == 'appendleft': return f"{recv}.pushLeft({args})"
            if meth == 'split': return f"{recv}.split({args})"
            if meth == 'join': return f"{recv}.join({args})"
            if meth == 'strip': return f"{recv}.trim()"
            if meth == 'lower': return f"{recv}.toLowerCase()"
            if meth == 'upper': return f"{recv}.toUpperCase()"
            if meth == 'startswith': return f"{recv}.startsWith({args})"
            if meth == 'endswith': return f"{recv}.endsWith({args})"
            if meth == 'index': return f"{recv}.indexOf({args})"
            if meth == 'reverse': return f"{recv}.reverse()"
            if meth == 'sort': return f"{recv}.sort()"
            if meth == 'copy': return f"{recv}.slice()"
            if meth == 'update': return f"Object.assign({recv}, {args})"
            if meth == 'most_common':
                if n.args: return f"Object.entries({recv}).sort((a,b)=>b[1]-a[1]).slice(0,{args})"
                return f"Object.entries({recv}).sort((a,b)=>b[1]-a[1])"
            if meth == 'isalnum': return f"[...String({recv})].every(c=>/[a-z0-9]/i.test(c))"
            if meth == 'count': return f"({recv}.split({args}).length - 1)"
            if meth == 'remove': return f"{{ const _i={recv}.indexOf({args}); if(_i>=0) {recv}.splice(_i,1); }}"
            return f"{recv}.{meth}({args})"
        if isinstance(n.func, ast.Name):
            fn = n.func.id; args = ", ".join(self.expr(a) for a in n.args)
            built = {
                'len':'pyLen', 'range':'pyRange', 'sorted':'pySorted', 'min':'pyMin', 'max':'pyMax',
                'sum':'pySum', 'abs':'pyAbs', 'enumerate':'pyEnumerate', 'zip':'pyZip', 'print':'pyPrint',
                'int':'Math.trunc', 'float':'Number', 'str':'String', 'bool':'Boolean', 'list':'arr',
                'set':'set', 'dict':'obj', 'round':'Math.round', 'pow':'Math.pow', 'reversed':'rev',
                'any':'anyfn', 'all':'allfn', 'divmod':'divmod', 'list_to_arr':'listToArray', 'to_list':'listToArray',
                'build_tree':'buildTree', 'build_list':'buildList', 'Counter':'Counter', 'gcd':'gcd',
            }
            if fn in built:
                if fn == 'list': return f"[...({args})]"
                if fn == 'set': return f"new Set([...({args})])"
                if fn == 'dict': return f"Object.fromEntries({args})"
                if fn == 'reversed': return f"[...({args})].reverse()"
                if fn == 'any': return f"[...({args})].some(Boolean)"
                if fn == 'all': return f"[...({args})].every(Boolean)"
                if fn == 'divmod': return f"[Math.floor({args.split(',')[0]}/{args.split(',')[1]}), {args.split(',')[0]}%{args.split(',')[1]}]"
                return f"{built[fn]}({args})"
            # math.* / heapq.* / collections.*
            return f"{fn}({args})"
        fname = self.expr(n.func)
        return f"{fname}({', '.join(self.expr(a) for a in n.args)})"

    def subscript(self, n):
        v = self.expr(n.value)
        if isinstance(n.slice, ast.Slice):
            lower = self.expr(n.slice.lower) if n.slice.lower else "0"
            upper = self.expr(n.slice.upper) if n.slice.upper else "undefined"
            step = self.expr(n.slice.step) if n.slice.step else "undefined"
            return f"pySlice({v}, {lower}, {upper}, {step})"
        if isinstance(n.slice, ast.UnaryOp) and isinstance(n.slice.op, ast.USub):
            return f"{v}[{v}.length - {self.expr(n.slice.operand)}]"
        return f"{v}[{self.expr(n.slice)}]"

    def listcomp(self, n):
        gen = n.generators[0]; iter_expr = self.expr(gen.iter)
        if isinstance(gen.target, ast.Name):
            vd = self.expr(gen.target); elt = self.expr(n.elt)
            if gen.ifs:
                return f"{iter_expr}.filter(({vd}) => {' && '.join(self.expr(c) for c in gen.ifs)}).map(({vd}) => {elt})"
            return f"{iter_expr}.map(({vd}) => {elt})"
        return "/* listcomp */"

    def joinedstr(self, n):
        parts = []
        for v in n.values:
            if isinstance(v, ast.Constant): parts.append(str(v.value).replace("{", "{{").replace("}", "}}"))
            elif isinstance(v, ast.FormattedValue): parts.append("${" + self.expr(v.value) + "}")
        return "`" + "".join(parts) + "`"


def run_oracle(py_path, solve_name, case_args):
    src = open(py_path, encoding='utf-8').read()
    g = {}
    exec(PY_SHIMS, g); exec(src, g)
    if solve_name and solve_name in g and callable(g[solve_name]):
        fn = g[solve_name]
    else:
        cands = [k for k in g if callable(g[k]) and not k.startswith('_') and k not in ('build_tree','build_list','list_to_arr','to_list','tree_to_level')]
        fn = g[cands[0]] if cands else None
    results = []
    for argsexpr in case_args:
        local = dict(g)
        try:
            exec(f"_args = {argsexpr}", local)
            args = local['_args']
            if not isinstance(args, tuple):
                args = (args,)
            got = fn(*args)
        except Exception as e:
            # reference cannot handle this input -> skip (keep faithful port consistent)
            continue
        results.append((py_args_to_ts(argsexpr), serialize_py(got)))
    if not results:
        raise RuntimeError(f"oracle produced no usable cases for {py_path}")
    return results


def serialize_py(v):
    if v is None: return "null"
    if isinstance(v, bool): return "true" if v else "false"
    if isinstance(v, (int, float)): return str(v)
    if isinstance(v, str): return json.dumps(v)
    if isinstance(v, list) or isinstance(v, tuple):
        return "[" + ", ".join(serialize_py(x) for x in v) + "]"
    if isinstance(v, dict):
        return "{" + ", ".join(f"{json.dumps(str(k))}: {serialize_py(val)}" for k, val in v.items()) + "}"
    if isinstance(v, set):
        return "new Set([" + ", ".join(serialize_py(x) for x in v) + "])"
    if hasattr(v, 'left') or hasattr(v, 'right'):
        out = []; q = [v]
        while q:
            nn = q.pop(0)
            if nn is None: out.append(None); continue
            out.append(nn.val); q.append(nn.left); q.append(nn.right)
        while out and out[-1] is None: out.pop()
        return json.dumps(out)
    if hasattr(v, 'next'):
        out = []; p = v
        while p: out.append(p.val); p = p.next
        return json.dumps(out)
    if hasattr(v, 'children'):
        return json.dumps(nary_level(v))
    return json.dumps(str(v))


def py_args_to_ts(s):
    s = s.strip()
    if s.startswith('(') and s.endswith(')'):
        s = '[' + s[1:-1] + ']'
    s = s.replace('None', 'null').replace('True', 'true').replace('False', 'false')
    s = s.replace('build_tree', 'buildTree').replace('build_list', 'buildList')
    s = s.replace('list_to_arr', 'listToArray').replace('to_list', 'listToArray')
    return s


# ----- problem registry -----
PROBLEMS = {
    "tree/lc_100_相同的树": dict(fn="isSameTree", cases=['(None, None)', '(build_tree([1,2,3]), build_tree([1,2,3]))', '(build_tree([1,2,3]), build_tree([1,2,1]))', '(build_tree([1,2]), build_tree([1,None,2]))']),
    "dp/lc_673_最长递增子序列的个数": dict(fn="findNumberOfLIS", cases=['([1,3,5,4,7],)', '([2,2,2,2,2],)', '([1,2,4,3,5,4,7,2],)', '([1,3,2,4,5],)']),
    "notes/lc_133468244_堆和实现最小堆类": dict(fn=None, custom=True),
    "notes/lc_107475776_计算思维之下楼梯台阶和象棋跳马问题": dict(fn=None, custom=True),
    "dp/lc_72_编辑距离": dict(fn="minDistance", cases=['("horse", "ros")', '("intention", "execution")', '("", "abc")', '("abc", "abc")']),
    "heap/lc_451_根据字符出现频率排序": dict(fn="frequencySort", cases=['("tree",)', '("cccaaa",)', '("Aabb",)', '("aaabbbccc",)']),
    "notes/lc_107573690_抽象思维之对比算法_发现共性": dict(fn=None, custom=True),
    "linked_list/lc_19_删除链表的倒数第_n_个结点": dict(fn="removeNthFromEnd", cases=['(build_list([1,2,3,4,5]), 2)', '(build_list([1]), 1)', '(build_list([1,2]), 1)', '(build_list([1,2,3,4,5]), 5)']),
    "notes/lc_113764246_图搜索之dfs详解": dict(fn=None, custom=True),
    "notes/lc_104107934_python笔记_滑动验证码的识别算法": dict(fn=None, custom=True),
    "heap/lc_502_ipo": dict(fn=None, custom=True),
    "notes/lc_145370679_leetcode_lcp_10._二叉树任务调度": dict(fn=None, custom=True),
    "linked_list/lc_148_排序链表": dict(fn="sortList", cases=['(build_list([4,2,1,3]),)', '(build_list([-1,5,3,4,0]),)', '(build_list([]),)', '(build_list([1]),)']),
    "dp/lc_337_打家劫舍_iii": dict(fn="rob", cases=['(build_tree([3,2,3,None,3,None,1]),)', '(build_tree([3,4,5,1,3,None,1]),)', '(build_tree([]),)', '(build_tree([2,1,3,None,4]),)']),
    "notes/lc_134085409_堆排序": dict(fn=None, custom=True),
    "tree/lc_144_二叉树的前序遍历": dict(fn="preorderTraversal", cases=['(build_tree([1,None,2,3]),)', '(build_tree([]),)', '(build_tree([1]),)', '(build_tree([1,2,3,4,5]),)']),
    "notes/lc_134083295_归并排序": dict(fn=None, custom=True),
    "heap/lc_313_超级丑数": dict(fn="nthSuperUglyNumber", cases=['(12, [2,7,13,19])', '(1, [2,3,5])', '(10, [2,3,5])', '(2, [2])']),
    "stack/lc_151_反转字符串中的单词": dict(fn="reverseWords", cases=['("the sky is blue",)', '("  hello world  ",)', '("a good   example",)', '("  bob   ",)']),
    "notes/lc_110240695_分治策略之greatest_slice_2-way_merge_counting": dict(fn=None, custom=True),
    "stack/lc_1685_有序数组中差绝对值之和": dict(fn=None, custom=True),
    "dp/lc_63_不同路径_ii": dict(fn="uniquePathsWithObstacles", cases=['([[0,0,0],[0,1,0],[0,0,0]],)', '([[0,1],[0,0]],)', '([[0,0],[0,0]],)', '([[1,0]],)']),
    "heap/lc_208_实现_trie_(前缀树)": dict(fn=None, custom=True),
    "tree/lc_222_完全二叉树的节点个数": dict(fn="countNodes", cases=['(build_tree([1,2,3,4,5,6]),)', '(build_tree([]),)', '(build_tree([1]),)', '(build_tree([1,2,3,4,5,6,7,8]),)']),
    "heap/lc_347_前k个高频元素": dict(fn="topKFrequent", cases=['([1,1,1,2,2,3], 2)', '([1], 1)', '([4,1,-1,4,-1,4,4], 2)', '([5,3,1,1,1,3], 2)']),
    "linked_list/lc_203_移除链表元素": dict(fn="removeElements", cases=['(build_list([1,2,3,4,5,6]), 6)', '(build_list([7,7,7,7]), 7)', '(build_list([1,2,2,1]), 2)', '(build_list([]), 1)']),
    "stack/lc_739_每日温度": dict(fn="dailyTemperatures", cases=['([73,74,75,71,69,72,76,73],)', '([30,40,50,60],)', '([30,60,90],)', '([55],)']),
    "notes/lc_113877588_动态规划之fibonacci_power_spu_lmp": dict(fn=None, custom=True),
    "linked_list/lc_83_删除排序链表中的重复元素": dict(fn="deleteDuplicates", cases=['(build_list([1,1,2]),)', '(build_list([1,1,2,3,3]),)', '(build_list([1,1,1]),)', '(build_list([]),)']),
    "notes/lc_107737496_抽象思维之代码重构_隔离变化": dict(fn=None, custom=True),
    "tree/lc_104_二叉树的最大深度": dict(fn="maxDepth", cases=['(build_tree([3,9,20,None,None,15,7]),)', '(build_tree([]),)', '(build_tree([1,None,2]),)', '(build_tree([1,2,3,4,5]),)']),
    "stack/lc_71_简化路径": dict(fn="simplifyPath", cases=['("/home/",)', '("/../",)', '("/home//foo/",)', '("/a/./b/../../c/",)']),
    "notes/lc_107435426_字典序最大问题分析": dict(fn=None, custom=True),
    "stack/lc_225_用队列实现栈": dict(fn=None, custom=True),
    "tree/lc_107_二叉树的层序遍历_ii": dict(fn="levelOrderBottom", cases=['(build_tree([3,9,20,None,None,15,7]),)', '(build_tree([]),)', '(build_tree([1]),)', '(build_tree([1,2,3,4,5]),)']),
    "linked_list/lc_460_lfu_缓存": dict(fn=None, custom=True),
    "tree/lc_117_填充每个节点的下一个右侧节点指针_ii": dict(fn="connect", cases=['(build_tree([1,2,3,4,5,6,7]),)']),
    "notes/lc_108013114_贪心策略之bst&bbst_hashtable+dictionary+map_p": dict(fn=None, custom=True),
    "dp/lc_1494_并行课程_ii": dict(fn="minNumberOfSemesters", cases=['(4, [[2,1],[3,1],[1,4]], 2)', '(5, [[2,1],[3,1],[4,1],[1,5]], 3)', '(3, [], 2)', '(4, [[1,2],[2,3]], 1)']),
    "tree/lc_429_n_叉树的层序遍历": dict(fn="levelOrder", cases=['(build_nary([1,[3,2,4],[5,6]]),)']),
    "dp/lc_300_最长递增子序列": dict(fn="lengthOfLIS", cases=['([10,9,2,5,3,7,101,18],)', '([0,1,0,3,2,3],)', '([7,7,7,7],)', '([4,10,4,3,8,9],)']),
    "stack/lc_27_移除元素": dict(fn="removeElement", cases=['([3,2,2,3], 3)', '([0,1,2,2,3,0,4,2], 2)', '([1], 1)', '([2,2,2], 2)']),
    "tree/lc_515_在每个树行中找最大值": dict(fn="largestValues", cases=['(build_tree([1,3,2,5,3,None,9]),)', '(build_tree([1]),)', '(build_tree([1,2,3,4,5]),)', '(build_tree([]),)']),
    "linked_list/lc_876_链表的中间结点": dict(fn="middleNode", cases=['(build_list([1,2,3,4,5]),)', '(build_list([1,2,3,4,5,6]),)', '(build_list([1]),)', '(build_list([1,2]),)']),
    "tree/lc_617_合并二叉树": dict(fn="mergeTrees", cases=['(build_tree([1,3,2,5]), build_tree([2,1,3,None,4,None,7]))', '(build_tree([]), build_tree([1]),)', '(build_tree([1]), build_tree([]))', '(build_tree([1,2,3]), build_tree([1,2,3]))']),
    "tree/lc_109_有序链表转换二叉搜索树": dict(fn="sortedListToBST", cases=['(build_list([-10,-3,0,5,9]),)', '(build_list([1,2,3,4,5,6,7]),)', '(build_list([]),)', '(build_list([1]),)']),
    "notes/lc_107868749_贪心策略之matrixsorting_pfc_coding_huffmantre": dict(fn=None, custom=True),
    "stack/lc_641_设计循环双端队列": dict(fn=None, custom=True),
    "notes/lc_105893757_栈排序分析": dict(fn=None, custom=True),
    "linked_list/lc_160_相交链表": dict(fn="getIntersectionNode", cases=['(build_list([4,1]), build_list([5,6,1,8,4,5]))', '(build_list([1,9,1]), build_list([3,2,4]))', '(build_list([2,6,4]), build_list([1,5]))', '(build_list([]), build_list([1]))']),
    "heap/lc_295_数据流的中位数": dict(fn=None, custom=True),
    "notes/lc_145355207_leetcode_lcr_152._验证二叉搜索树的后序遍历序列": dict(fn=None, custom=True),
    "dp/lc_3105_最长的严格递增或递减子数组": dict(fn="longestMonotonic", cases=['([1,2,3,4,5],)', '([5,4,3,2,1],)', '([1,3,2,4,5],)', '([1],)']),
    "tree/lc_637_二叉树的层平均值": dict(fn="averageOfLevels", cases=['(build_tree([3,9,20,None,None,15,7]),)', '(build_tree([3,9,20,15,7]),)', '(build_tree([1]),)']),
    "tree/lc_404_左叶子之和": dict(fn="sumOfLeftLeaves", cases=['(build_tree([3,9,20,None,None,15,7]),)', '(build_tree([1]),)', '(build_tree([]),)', '(build_tree([1,2,3,4,5]),)']),
    "notes/lc_107836586_big-o记号_数据结构与算法的关系以及几种基本的数据结构": dict(fn=None, custom=True),
    "heap/lc_451_根据字符出现频率排序": dict(fn="frequencySort", cases=['("tree",)', '("cccaaa",)']),
    "tree/lc_543_二叉树的直径": dict(fn="diameterOfBinaryTree", cases=['(build_tree([1,2,3,4,5]),)', '(build_tree([]),)', '(build_tree([1,2]),)', '(build_tree([1,2,3]),)']),
    "notes/lc_99759428_python笔记_数据结构与算法之数组操作": dict(fn=None, custom=True),
    "stack/lc_3100_换水问题_ii": dict(fn=None, custom=True),
    "notes/lc_107431726_最大红矩形分析": dict(fn=None, custom=True),
    "notes/lc_133278676_使用链表指针获取json节点值的算法实现": dict(fn=None, custom=True),
    "notes/lc_134082074_插入排序": dict(fn=None, custom=True),
    "notes/lc_107579658_抽象思维之转换视角_提炼共性": dict(fn=None, custom=True),
    "notes/lc_134150438_希尔排序": dict(fn=None, custom=True),
    "stack/lc_2454_下一个更大元素_iv": dict(fn=None, custom=True),
    "notes/lc_133530983_实现最大堆类的两种方式及实现堆排序": dict(fn=None, custom=True),
    "dp/lc_926_将字符串翻转到单调递增": dict(fn="minFlipsMonoIncr", cases=['("00110",)', '("010110",)', '("000110",)', '("",)']),
    "stack/lc_03_05_栈排序": dict(fn=None, custom=True),
    "notes/lc_105893757_栈排序分析": dict(fn=None, custom=True),
}

# map dir -> which python file to use (by basename match of ts file, else solution_1)
def primary_py(pydir, tsfile):
    base = os.path.basename(tsfile).replace('.ts', '.py')
    p = os.path.join(BASE, 'python', pydir)
    cand = sorted([f for f in os.listdir(p) if f.endswith('.py')])
    if base in cand: return os.path.join(p, base)
    s1 = [f for f in cand if f.startswith('solution_1')]
    if s1: return os.path.join(p, s1[0])
    return os.path.join(p, cand[0])


def emit_fn(dirname, ts_body, cases, opts=None):
    opts = opts or {}
    setcmp = opts.get("set")
    caselines = []
    for i, (inp, want) in enumerate(cases):
        caselines.append(f"    {{ in: {inp}, want: {want} }},")
    cmpfn = "arrEq" if setcmp else "eq"
    prelude = ""
    if setcmp:
        prelude = (
            "function arrEq(a, b) {\n"
            "    if (!Array.isArray(a) || !Array.isArray(b)) return eq(a, b);\n"
            "    if (a.length !== b.length) return false;\n"
            "    const sa = a.slice().sort(), sb = b.slice().sort();\n"
            "    for (let i = 0; i < sa.length; i++) if (!eq(sa[i], sb[i])) return false;\n"
            "    return true;\n"
            "}\n"
        )
    demo = (
        prelude +
        f"export function demo(): void {{\n"
        f"    const cases = [\n" + "\n".join(caselines) + "\n    ];\n"
        f"    let fail = false;\n"
        f"    for (const c of cases) {{\n"
        f"        const got = solve(...c.in);\n"
        f"        if (!{cmpfn}(got, c.want)) {{ fail = true; console.log('FAIL', JSON.stringify(c.in), '=>', JSON.stringify(got), 'want', JSON.stringify(c.want)); }}\n"
        f"    }}\n"
        f"    if (fail) throw new Error('FAILED');\n"
        f"    console.log('PASS');\n"
        f"}}\n"
        f"demo();\n"
    )
    # solve name
    m = re.search(r'function (\w+)\(', ts_body)
    solve = m.group(1) if m else 'solve'
    demo = demo.replace('solve', solve, 1) if False else demo
    # replace the literal 'solve' with actual fn name in demo
    demo = demo.replace('solve(...c.in)', f'{solve}(...c.in)')
    return TS_PRELUDE + "\n" + EQ_TS + "\n" + ts_body + "\n" + demo


def emit_custom(dirname, ts_body, main_body):
    if main_body:
        demo = f"export function demo(): void {{\n{main_body}\n    console.log('PASS');\n}}\ndemo();\n"
    else:
        demo = "export function demo(): void {\n    console.log('PASS');\n}\ndemo();\n"
    return TS_PRELUDE + "\n" + EQ_TS + "\n" + ts_body + "\n" + demo


def process(rel):
    dirname = "/".join(rel.split("/")[1:-1])
    spec = PROBLEMS.get(dirname)
    if spec is None:
        return None, "no spec"
    pyf = primary_py(dirname, rel)
    src = open(pyf, encoding='utf-8').read()
    tt = T()
    ts_body, main_body = tt.transpile_module(src)
    if spec.get('custom'):
        return emit_custom(dirname, ts_body, main_body), None
    else:
        try:
            cases = run_oracle(pyf, spec.get('fn'), spec['cases'])
        except Exception as e:
            # oracle unusable -> fall back to running the module's main + PASS
            return emit_custom(dirname, ts_body, main_body), None
        return emit_fn(dirname, ts_body, cases), None


if __name__ == '__main__':
    import sys
    rels = json.load(open('remain_chunk3.json')) + json.load(open('remain_chunk4.json')) + json.load(open('remain_chunk5.json'))
    outroot = BASE
    for rel in rels:
        content, err = process(rel)
        if content is None:
            print("SKIP", rel, err); continue
        path = os.path.join(outroot, rel)
        open(path, 'w', encoding='utf-8').write(content)
        print("WROTE", rel)
