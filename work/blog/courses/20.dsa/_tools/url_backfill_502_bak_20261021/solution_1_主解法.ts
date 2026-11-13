
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

function findMaximizedCapital(k, w, profits, capital) {
    const n = profits.length;
    const projects = [];
    for (let i = 0; i < n; i++) projects.push([capital[i], profits[i]]);
    projects.sort((a, b) => a[0] - b[0]);
    const pq = [];
    let i = 0;
    for (let t = 0; t < k; t++) {
        while (i < n && projects[i][0] <= w) { heapPush(pq, -projects[i][1]); i++; }
        if (!pq.length) break;
        w += -heapPop(pq);
    }
    return w;
}
export function demo(): void {
    const cases = [
    { in: [2, 0, [1,2,3], [0,1,1]], want: 4 },
    { in: [3, 0, [1,2,3], [0,1,2]], want: 6 },
    { in: [1, 0, [1,2], [1,2]], want: 0 },
    { in: [2, 1, [1,2,3], [1,1,2]], want: 6 },
    ];
    let fail = false;
    for (const c of cases) {
        const got = findMaximizedCapital(...c.in);
        if (!eq(got, c.want)) { fail = true; console.log('FAIL', JSON.stringify(c.in), '=>', JSON.stringify(got), 'want', JSON.stringify(c.want)); }
    }
    if (fail) throw new Error('FAILED');
    console.log('PASS');
}
demo();
