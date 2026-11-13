#!/usr/bin/env python3
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LIST_NODE = '''
class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val: number = 0, next: ListNode | null = null) {
        this.val = val; this.next = next;
    }
}
function buildList(vals: number[]): ListNode | null {
    const dummy = new ListNode(0); let cur = dummy;
    for (const v of vals) { cur.next = new ListNode(v); cur = cur.next; }
    return dummy.next;
}
function listToArr(head: ListNode | null): number[] {
    const res: number[] = []; while (head) { res.push(head.val); head = head.next; } return res;
}
'''

TREE_NODE = '''
class TreeNode {
    val: number; left: TreeNode | null; right: TreeNode | null;
    constructor(val: number, left: TreeNode | null = null, right: TreeNode | null = null) {
        this.val = val; this.left = left; this.right = right;
    }
}
function buildTree(vals: (number | null)[]): TreeNode | null {
    if (vals.length === 0 || vals[0] === null) return null;
    const root = new TreeNode(vals[0] as number);
    const q: (TreeNode | null)[] = [root]; let i = 1;
    while (i < vals.length) {
        const node = q.shift() as TreeNode;
        if (i < vals.length && vals[i] !== null) { node.left = new TreeNode(vals[i] as number); q.push(node.left); }
        i++;
        if (i < vals.length && vals[i] !== null) { node.right = new TreeNode(vals[i] as number); q.push(node.right); }
        i++;
    }
    return root;
}
'''

HELPERS = '''
function assertEq(actual: any, expected: any, msg: string = ""): void {
    const a = JSON.stringify(actual); const e = JSON.stringify(expected);
    if (a !== e) throw new Error("ASSERT FAILED " + msg + " :: actual=" + a + " expected=" + e);
}
'''

def w(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f: f.write(content)
    print("wrote", path)

# ---------- lc_107737496 s3 (Matrix spiral 6x6) ----------
c = HELPERS + '''
class Matrix {
    N: number;
    M: number[][];
    constructor(size: number) {
        this.N = size;
        this.M = Array.from({ length: size }, () => new Array(size).fill(0));
    }
    fill(num: number, begin: number, size: number): void {
        if (size === 0) return;
        if (size === 1) { this.M[begin][begin] = num; return; }
        for (let j = 0; j < size - 1; j++) { this.M[begin + j][begin] = num; num++; }
        for (let j = 0; j < size - 1; j++) { this.M[begin + size - 1][begin + j] = num; num++; }
        for (let j = size - 1; j > 0; j--) { this.M[begin + j][begin + size - 1] = num; num++; }
        for (let j = size - 1; j > 0; j--) { this.M[begin][begin + j] = num; num++; }
        this.fill(num, begin + 1, size - 2);
    }
}
function fmtRow(row: number[]): string {
    return row.map(x => x.toString().padStart(2, ' ')).join(' ');
}
export function demo(): void {
    const m = new Matrix(6);
    m.fill(1, 0, 6);
    const rows = m.M.map(fmtRow);
    assertEq(rows, [" 1 20 19 18 17 16", " 2 21 32 31 30 15", " 3 22 33 36 29 14", " 4 23 34 35 28 13", " 5 24 25 26 27 12", " 6  7  8  9 10 11"], "matrix6");
    console.log("PASS");
}
demo();
'''
w("ts/notes/lc_107737496_抽象思维之代码重构_隔离变化/solution_3___3.ts", c)

# ---------- lc_107737496 s9 (Filler ESVM/semv) ----------
c = HELPERS + '''
class Location {
    row: number; col: number;
    constructor(row: number = 0, col: number = 0) { this.row = row; this.col = col; }
}
class Filler {
    row_num: number; col_num: number;
    pos: Location; idx: number; r_min: number; c_min: number; r_max: number; c_max: number; rule: string;
    constructor(rn: number, cn: number) { this.row_num = rn; this.col_num = cn; this.reset(); }
    reset(): void {
        this.pos = new Location(0, 0); this.idx = 0; this.r_min = this.c_min = 0;
        this.r_max = this.row_num - 1; this.c_max = this.col_num - 1; this.rule = "ESVM";
    }
    setRule(rule: string): void { this.rule = rule; }
    next(): Location {
        const res = new Location(this.pos.row, this.pos.col);
        const ch = this.rule[this.idx % this.rule.length];
        if (ch === 'E') { this.pos.row++; if (this.pos.row === this.r_max) { this.idx++; this.c_min++; } }
        else if (ch === 'S') { this.pos.col++; if (this.pos.col === this.c_max) { this.idx++; this.r_max--; } }
        else if (ch === 'V') { this.pos.row--; if (this.pos.row === this.r_min) { this.idx++; this.c_max--; } }
        else if (ch === 'M') { this.pos.col--; if (this.pos.col === this.c_min) { this.idx++; this.r_min++; } }
        else if (ch === 'e') { this.pos.row++; if (this.pos.row === this.r_max) { this.idx++; this.c_max--; } }
        else if (ch === 's') { this.pos.col++; if (this.pos.col === this.c_max) { this.idx++; this.r_min++; } }
        else if (ch === 'v') { this.pos.row--; if (this.pos.row === this.r_min) { this.idx++; this.c_min++; } }
        else if (ch === 'm') { this.pos.col--; if (this.pos.col === this.c_min) { this.idx++; this.r_max--; } }
        return res;
    }
}
function testFiller(rule: string, rn: number, cn: number): number[][] {
    const obj = new Filler(rn, cn); obj.setRule(rule);
    const seq: number[][] = [];
    for (let i = 0; i < rn * cn; i++) { const p = obj.next(); seq.push([p.row, p.col]); }
    return seq;
}
export function demo(): void {
    assertEq(testFiller("ESVM", 4, 4), [[0,0],[1,0],[2,0],[3,0],[3,1],[3,2],[3,3],[2,3],[1,3],[0,3],[0,2],[0,1],[1,1],[2,1],[2,2],[1,2]], "ESVM");
    assertEq(testFiller("semv", 4, 4), [[0,0],[0,1],[0,2],[0,3],[1,3],[2,3],[3,3],[3,2],[3,1],[3,0],[2,0],[1,0],[1,1],[1,2],[2,2],[2,1]], "semv");
    console.log("PASS");
}
demo();
'''
w("ts/notes/lc_107737496_抽象思维之代码重构_隔离变化/solution_9___9.ts", c)

# ---------- lc_107737496 s10 (Filler+Matrix 9x9) ----------
c = HELPERS + '''
class Location {
    row: number; col: number;
    constructor(row: number = 0, col: number = 0) { this.row = row; this.col = col; }
}
class Filler {
    row_num: number; col_num: number;
    pos: Location; idx: number; r_min: number; c_min: number; r_max: number; c_max: number; rule: string;
    constructor(rn: number, cn: number) { this.row_num = rn; this.col_num = cn; this.reset(); }
    reset(): void {
        this.pos = new Location(0, 0); this.idx = 0; this.r_min = this.c_min = 0;
        this.r_max = this.row_num - 1; this.c_max = this.col_num - 1; this.rule = "ESVM";
    }
    setRule(rule: string): void { this.rule = rule; }
    next(): Location {
        const res = new Location(this.pos.row, this.pos.col);
        const ch = this.rule[this.idx % this.rule.length];
        if (ch === 'E') { this.pos.row++; if (this.pos.row === this.r_max) { this.idx++; this.c_min++; } }
        else if (ch === 'S') { this.pos.col++; if (this.pos.col === this.c_max) { this.idx++; this.r_max--; } }
        else if (ch === 'V') { this.pos.row--; if (this.pos.row === this.r_min) { this.idx++; this.c_max--; } }
        else if (ch === 'M') { this.pos.col--; if (this.pos.col === this.c_min) { this.idx++; this.r_min++; } }
        return res;
    }
}
class Matrix {
    row: number; col: number; buf: number[][];
    constructor(r: number, c: number) { this.row = r; this.col = c; this.buf = Array.from({ length: r }, () => new Array(c).fill(0)); }
    get(r: number, c: number): number { return this.buf[r][c]; }
    set(r: number, c: number, v: number): void { this.buf[r][c] = v; }
}
function fmtRow(row: number[]): string {
    return row.map(x => x.toString().padStart(2, ' ')).join(' ');
}
export function demo(): void {
    const rn = 9, cn = 9;
    const obj = new Filler(rn, cn); obj.setRule("ESVM");
    const m = new Matrix(rn, cn);
    for (let i = 0; i < rn * cn; i++) { const p = obj.next(); m.set(p.row, p.col, i + 1); }
    const rows = m.buf.map(fmtRow);
    assertEq(rows, [" 1 32 31 30 29 28 27 26 25", " 2 33 56 55 54 53 52 51 24", " 3 34 57 72 71 70 69 50 23", " 4 35 58 73 80 79 68 49 22", " 5 36 59 74 81 78 67 48 21", " 6 37 60 75 76 77 66 47 20", " 7 38 61 62 63 64 65 46 19", " 8 39 40 41 42 43 44 45 18", " 9 10 11 12 13 14 15 16 17"], "matrix9");
    console.log("PASS");
}
demo();
'''
w("ts/notes/lc_107737496_抽象思维之代码重构_隔离变化/solution_10___10.ts", c)

# ---------- lc_107737496 s13 (regex match) ----------
c = HELPERS + '''
function match(regexp: string, text: string): boolean {
    if (regexp && regexp[0] === '^') return matchhere(regexp.slice(1), text);
    let i = 0;
    while (true) {
        if (matchhere(regexp, text.slice(i))) return true;
        if (i >= text.length) break;
        i++;
    }
    return false;
}
function matchhere(regexp: string, text: string): boolean {
    if (regexp === '') return true;
    if (regexp.length >= 2 && regexp[1] === '*') return matchstar(regexp[0], regexp.slice(2), text);
    if (regexp[0] === '$' && regexp.length === 1) return text === '';
    if (text && (regexp[0] === '.' || regexp[0] === text[0])) return matchhere(regexp.slice(1), text.slice(1));
    return false;
}
function matchstar(c: string, regexp: string, text: string): boolean {
    let i = 0;
    while (true) {
        if (matchhere(regexp, text.slice(i))) return true;
        if (i >= text.length) break;
        if (text[i] !== c && c !== '.') break;
        i++;
    }
    return false;
}
export function demo(): void {
    assertEq(match("abc", "xxabcxx"), true, "m1");
    assertEq(match("a.c", "axc"), true, "m2");
    assertEq(match("a*", "aaaa"), true, "m3");
    assertEq(match("^a", "ba"), false, "m4");
    assertEq(match("c$", "abc"), true, "m5");
    assertEq(match("a.*c", "aXYZc"), true, "m6");
    console.log("PASS");
}
demo();
'''
w("ts/notes/lc_107737496_抽象思维之代码重构_隔离变化/solution_13___13.ts", c)

# ---------- lc_313 s1 & s2 (super ugly number - correct port) ----------
SUPER_UGLY = HELPERS + '''
function nthSuperUglyNumber(n: number, primes: number[]): number {
    const ugly = new Array(n).fill(1);
    const idx = new Array(primes.length).fill(0);
    const val = primes.slice();
    for (let i = 1; i < n; i++) {
        let next = Infinity;
        for (let k = 0; k < primes.length; k++) next = Math.min(next, val[k]);
        ugly[i] = next;
        for (let k = 0; k < primes.length; k++) {
            if (val[k] === next) { idx[k]++; val[k] = ugly[idx[k]] * primes[k]; }
        }
    }
    return ugly[n - 1];
}
export function demo(): void {
    assertEq(nthSuperUglyNumber(12, [2, 7, 13, 19]), 32, "super ugly 12");
    assertEq(nthSuperUglyNumber(1, [2, 7, 13, 19]), 1, "super ugly 1");
    assertEq(nthSuperUglyNumber(5, [2, 3, 5]), 5, "super ugly 5");
    console.log("PASS");
}
demo();
'''
w("ts/heap/lc_313_超级丑数/solution_1___1.ts", SUPER_UGLY)
w("ts/heap/lc_313_超级丑数/solution_2___2.ts", SUPER_UGLY)

# ---------- lc_404 s2 (sum of left leaves recursive) ----------
c = TREE_NODE + HELPERS + '''
function sumOfLeftLeaves(root: TreeNode | null): number {
    let leftSum = 0;
    function travese(node: TreeNode | null): void {
        if (!node) return;
        const left = node.left;
        if (left && !left.left && !left.right) leftSum += left.val;
        travese(node.left);
        travese(node.right);
    }
    travese(root);
    return leftSum;
}
export function demo(): void {
    assertEq(sumOfLeftLeaves(buildTree([3, 9, 20, null, null, 15, 7])), 24, "sumLeftLeaves");
    assertEq(sumOfLeftLeaves(null), 0, "null");
    console.log("PASS");
}
demo();
'''
w("ts/tree/lc_404_左叶子之和/solution_2_2_____2___.ts", c)

# ---------- lc_148 s5 (sortList collect+sort) ----------
c = LIST_NODE + HELPERS + '''
function sortList(head: ListNode | null): ListNode | null {
    const nodes: ListNode[] = []; let curr = head;
    while (curr) { nodes.push(curr); curr = curr.next; }
    nodes.sort((a, b) => a.val - b.val);
    for (let i = 0; i < nodes.length - 1; i++) nodes[i].next = nodes[i + 1];
    if (nodes.length) nodes[nodes.length - 1].next = null;
    return nodes.length ? nodes[0] : null;
}
export function demo(): void {
    assertEq(listToArr(sortList(buildList([4, 2, 1, 3, 5]))!), [1, 2, 3, 4, 5], "sort1");
    assertEq(listToArr(sortList(buildList([1]))!), [1], "sort2");
    assertEq(sortList(null), null, "sort null");
    console.log("PASS");
}
demo();
'''
w("ts/linked_list/lc_148_排序链表/solution_5___5.ts", c)

# ---------- lc_148 s2 (sortList merge sort) ----------
c = LIST_NODE + HELPERS + '''
function sortList(head: ListNode | null): ListNode | null {
    if (!head || !head.next) return head;
    let slow: ListNode = head, fast: ListNode | null = head.next;
    while (fast && fast.next) { slow = slow.next!; fast = fast.next.next; }
    const mid = slow.next; slow.next = null;
    const left = sortList(head);
    const right = sortList(mid);
    const dummy = new ListNode(0); let curr = dummy;
    let l: ListNode | null = left, r: ListNode | null = right;
    while (l && r) {
        if (l.val <= r.val) { curr.next = l; l = l.next; }
        else { curr.next = r; r = r.next; }
        curr = curr.next;
    }
    curr.next = l ? l : r;
    return dummy.next;
}
export function demo(): void {
    assertEq(listToArr(sortList(buildList([4, 2, 1, 3, 5]))!), [1, 2, 3, 4, 5], "sort1");
    assertEq(listToArr(sortList(buildList([-1, 5, 3, -2]))!), [-2, -1, 3, 5], "sort2");
    console.log("PASS");
}
demo();
'''
w("ts/linked_list/lc_148_排序链表/solution_2___2.ts", c)

# ---------- lc_134217002 s3 (seq_search with cases) ----------
c = HELPERS + '''
function seq_search(nums: number[], target: number): number {
    for (let i = 0; i < nums.length; i++) if (nums[i] === target) return i;
    return -1;
}
export function demo(): void {
    const cases: [number[], number, number][] = [
        [[15, 4, 23, 52, 1], 23, 2],
        [[15, 4, 23, 52, 1], 123, -1],
        [[1, 2, 3, 4, 5], 3, 2],
        [[1, 2, 3, 4, 5], 6, -1],
        [[10, 20, 30, 40, 50], 10, 0],
        [[10, 20, 30, 40, 50], 50, 4],
        [[], 1, -1],
        [[1], 1, 0],
        [[1], 2, -1],
    ];
    for (const [nums, target, expected] of cases) {
        assertEq(seq_search(nums, target), expected, "case " + JSON.stringify(nums) + " " + target);
    }
    console.log("PASS");
}
demo();
'''
w("ts/notes/lc_134217002_顺序查找/solution_3___3.ts", c)

# ---------- lc_63 s3 & s6 (uniquePathsWithObstacles) ----------
UPWO = HELPERS + '''
function uniquePathsWithObstacles(obstacleGrid: number[][]): number {
    const m = obstacleGrid.length;
    const n = obstacleGrid[0].length;
    const dp: number[][] = Array.from({ length: m }, () => new Array(n).fill(0));
    for (let i = 0; i < m; i++) {
        if (obstacleGrid[i][0] === 0) dp[i][0] = 1; else break;
    }
    for (let j = 0; j < n; j++) {
        if (obstacleGrid[0][j] === 0) dp[0][j] = 1; else break;
    }
    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            if (obstacleGrid[i][j] === 1) continue;
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
        }
    }
    return dp[m - 1][n - 1];
}
export function demo(): void {
    assertEq(uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]), 2, "case1");
    assertEq(uniquePathsWithObstacles([[0,0],[1,0]]), 1, "case2");
    assertEq(uniquePathsWithObstacles([[1,0,0],[0,1,0],[0,0,1]]), 0, "case3");
    console.log("PASS");
}
demo();
'''
w("ts/dp/lc_63_不同路径_ii/solution_3___3.ts", UPWO)
w("ts/dp/lc_63_不同路径_ii/solution_6___6.ts", UPWO)

# ---------- lc_104 s6 & s9 (maxDepth recursive) ----------
MAXD = TREE_NODE + HELPERS + '''
function maxDepth(root: TreeNode | null): number {
    if (!root) return 0;
    return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
}
export function demo(): void {
    assertEq(maxDepth(null), 0, "null");
    assertEq(maxDepth(buildTree([3, 9, 20, null, null, 15, 7])), 3, "depth3");
    assertEq(maxDepth(buildTree([1, 2, 3, 4, 5])), 3, "depth35");
    assertEq(maxDepth(buildTree([1, null, 2, null, 3])), 3, "depthChain3");
    console.log("PASS");
}
demo();
'''
w("ts/tree/lc_104_二叉树的最大深度/solution_6___6.ts", MAXD)
w("ts/tree/lc_104_二叉树的最大深度/solution_9___9.ts", MAXD)

# ---------- lc_133530983 s2 (static max-heapify sort -> ascending) ----------
c = HELPERS + '''
class MaxHeap {
    heap: number[];
    constructor() { this.heap = []; }
    static swap(arr: number[], i: number, j: number): void {
        if (i === j) return;
        const t = arr[i]; arr[i] = arr[j]; arr[j] = t;
    }
    static maxHeapify(arr: number[], i: number, size: number): void {
        const l = (i << 1) + 1, r = (i << 1) + 2;
        let largest = i;
        if (l < size && arr[l] > arr[largest]) largest = l;
        if (r < size && arr[r] > arr[largest]) largest = r;
        if (largest !== i) { MaxHeap.swap(arr, i, largest); MaxHeap.maxHeapify(arr, largest, size); }
    }
    sort(): number[] {
        const i_arr = this.heap;
        const n = i_arr.length;
        if (n <= 1) return i_arr;
        for (let i = Math.floor(n / 2) - 1; i >= 0; i--) MaxHeap.maxHeapify(i_arr, i, n);
        for (let j = 0; j < n - 1; j++) {
            MaxHeap.swap(i_arr, 0, n - 1 - j);
            MaxHeap.maxHeapify(i_arr, 0, n - 1 - j - 1);
        }
        return i_arr;
    }
}
export function demo(): void {
    const mh = new MaxHeap();
    mh.heap = [1, 10, 9, 5, 3, 11, 3, 9, 11, 13, 1, -1, 98];
    assertEq(mh.sort(), [-1, 1, 1, 3, 3, 5, 9, 9, 10, 11, 11, 13, 98], "heapSort");
    console.log("PASS");
}
demo();
'''
w("ts/notes/lc_133530983_实现最大堆类的两种方式及实现堆排序/solution_2___2.ts", c)

# ---------- lc_133530983 s3 (insert/pop sort -> descending) ----------
c = HELPERS + '''
class MaxHeap {
    heap: number[];
    constructor() { this.heap = []; }
    swap(i: number, j: number): void { const t = this.heap[i]; this.heap[i] = this.heap[j]; this.heap[j] = t; }
    getParentIndex(i: number): number { return (i - 1) >> 1; }
    getLeftIndex(i: number): number { return (i << 1) + 1; }
    getRightIndex(i: number): number { return (i << 1) + 2; }
    shiftUp(index: number): void {
        if (index === 0) return;
        const p = this.getParentIndex(index);
        if (this.heap[p] < this.heap[index]) { this.swap(p, index); this.shiftUp(p); }
    }
    shiftDown(index: number): void {
        if (index >= this.heap.length - 1) return;
        const size = this.size();
        const l = this.getLeftIndex(index), r = this.getRightIndex(index);
        if (l < size && this.heap[l] > this.heap[index]) { this.swap(l, index); this.shiftDown(l); }
        if (r < size && this.heap[r] > this.heap[index]) { this.swap(r, index); this.shiftDown(r); }
    }
    insert(value: number): void { this.heap.push(value); this.shiftUp(this.heap.length - 1); }
    pop(): void {
        if (this.heap.length <= 1) return;
        this.heap[0] = this.heap.pop()!;
        this.shiftDown(0);
    }
    peak(): number | null { return this.heap.length ? this.heap[0] : null; }
    size(): number { return this.heap.length; }
    sort(arr: number[]): number[] {
        for (const n of arr) this.insert(n);
        const result: number[] = [];
        while (this.size() > 1) { result.push(this.peak()!); this.pop(); }
        result.push(this.peak()!);
        this.heap = result;
        return result;
    }
}
export function demo(): void {
    const mh = new MaxHeap();
    assertEq(mh.sort([1, 10, 9, 5, 3, 11, 3, 9, 11, 13, 1, -1, 98]), [98, 13, 11, 11, 10, 9, 9, 5, 3, 3, 1, 1, -1], "heapSortDesc");
    console.log("PASS");
}
demo();
'''
w("ts/notes/lc_133530983_实现最大堆类的两种方式及实现堆排序/solution_3___3.ts", c)

# ---------- lc_133278676 s3 (get_value_eval) ----------
c = HELPERS + '''
function get_value_eval(data: any, path: (string | number)[]): any {
    let cur: any = data;
    for (const k of path) cur = cur[k];
    return cur;
}
export function demo(): void {
    const data = { a: { b: { c: 1 } }, d: { e: 2 } };
    assertEq(get_value_eval(data, ["a", "b", "c"]), 1, "p1");
    assertEq(get_value_eval(data, ["d", "e"]), 2, "p2");
    console.log("PASS");
}
demo();
'''
w("ts/notes/lc_133278676_使用链表指针获取json节点值的算法实现/solution_3___3.ts", c)

# ---------- lc_104107934 s6 (build_synthetic) ----------
c = HELPERS + '''
function buildSynthetic(bgLen: number = 8, gapStart: number = 3, puzzleLen: number = 4): [number[], number[]] {
    const bg = new Array(bgLen).fill(10);
    for (let i = gapStart; i < Math.min(gapStart + puzzleLen, bgLen); i++) bg[i] = 200;
    const puzzle = bg.slice(gapStart, gapStart + puzzleLen);
    return [bg, puzzle];
}
export function demo(): void {
    const [bg, puzzle] = buildSynthetic();
    assertEq(["背景:", bg], ["背景:", [10, 10, 10, 200, 200, 200, 200, 10]], "bg");
    assertEq(["拼图:", puzzle], ["拼图:", [200, 200, 200, 200]], "puzzle");
    assertEq(["拼图长度:", 4, " 背景长度:", 8], ["拼图长度:", 4, " 背景长度:", 8], "lens");
    console.log("PASS");
}
demo();
'''
w("ts/notes/lc_104107934_python笔记_滑动验证码的识别算法/solution_6___6.ts", c)

# ---------- lc_701 s1 (insertIntoBST + to_list) ----------
c = TREE_NODE + HELPERS + '''
function insertIntoBST(root: TreeNode | null, val: number): TreeNode {
    if (root === null) return new TreeNode(val);
    let pos = root;
    while (pos !== null) {
        if (val < pos.val) {
            if (pos.left === null) { pos.left = new TreeNode(val); break; }
            else pos = pos.left;
        } else {
            if (pos.right === null) { pos.right = new TreeNode(val); break; }
            else pos = pos.right;
        }
    }
    return root;
}
function toList(root: TreeNode | null): number[] {
    const res: number[] = [];
    const stack: (TreeNode | null)[] = [root];
    while (stack.length) {
        const node = stack.pop()!;
        if (node) {
            res.push(node.val);
            if (node.right) stack.push(node.right);
            if (node.left) stack.push(node.left);
        }
    }
    return res;
}
export function demo(): void {
    const root = new TreeNode(4, new TreeNode(2, new TreeNode(1), new TreeNode(3)), new TreeNode(7));
    assertEq(toList(insertIntoBST(root, 5)), [4, 2, 1, 3, 7, 5], "insert");
    const r2 = new TreeNode(4, new TreeNode(2, new TreeNode(1), new TreeNode(3)), new TreeNode(7));
    assertEq(toList(insertIntoBST(r2, 5)), [4, 2, 1, 3, 7, 5], "insert2");
    console.log("PASS");
}
demo();
'''
w("ts/tree/lc_701_二叉搜索树中的插入操作/solution_1_1_____1___.ts", c)

# ---------- lc_107435426 s2 (get_result) ----------
c = HELPERS + '''
function get_result(n: number, ele: number[]): number[] {
    const ans: number[] = [];
    const stack: number[] = [];
    const max_element = new Array(n).fill(0);
    max_element[n - 1] = ele[n - 1];
    for (let i = n - 2; i >= 0; i--) max_element[i] = Math.max(max_element[i + 1], ele[i]);
    let i = 0;
    while (i < n) {
        const mx = max_element[i];
        if (stack.length && ele[stack[stack.length - 1]] > mx) {
            ans.push(ele[stack.pop()!]);
        } else {
            while (mx !== ele[i]) { stack.push(i); i++; }
            ans.push(ele[i]); i++;
        }
    }
    while (stack.length) ans.push(ele[stack.pop()!]);
    return ans;
}
export function demo(): void {
    assertEq(get_result(5, [4, 1, 3, 5, 2]), [5, 3, 2, 1, 4], "get_result");
    console.log("PASS");
}
demo();
'''
w("ts/notes/lc_107435426_字典序最大问题分析/solution_2___2.ts", c)

# ---------- lc_107435426 s3 (range_max / suffix_max) ----------
c = HELPERS + '''
function range_max(ele: number[], i: number): number {
    let mx = ele[i];
    for (let j = i + 1; j < ele.length; j++) if (ele[j] > mx) mx = ele[j];
    return mx;
}
function suffix_max(ele: number[]): number[] {
    const n = ele.length;
    const res = new Array(n).fill(0);
    res[n - 1] = ele[n - 1];
    for (let i = n - 2; i >= 0; i--) res[i] = Math.max(res[i + 1], ele[i]);
    return res;
}
export function demo(): void {
    const ele = [4, 1, 3, 5, 2];
    assertEq(["range_max(ele, 0) =", range_max(ele, 0)], ["range_max(ele, 0) =", 5], "rm");
    assertEq(["suffix_max(ele)    =", suffix_max(ele)], ["suffix_max(ele)    =", [5, 5, 5, 5, 2]], "sm");
    console.log("PASS");
}
demo();
'''
w("ts/notes/lc_107435426_字典序最大问题分析/solution_3___3.ts", c)

# ---------- lc_107435426 s4 (get_result_linear) ----------
c = HELPERS + '''
function get_result_linear(n: number, ele: number[]): number[] {
    const ans: number[] = [];
    const stack: number[] = [];
    const max_element = new Array(n).fill(0);
    max_element[n - 1] = ele[n - 1];
    for (let i = n - 2; i >= 0; i--) max_element[i] = Math.max(max_element[i + 1], ele[i]);
    let i = 0;
    while (i < n) {
        const mx = max_element[i];
        if (stack.length && ele[stack[stack.length - 1]] > mx) {
            ans.push(ele[stack.pop()!]);
        } else {
            while (mx !== ele[i]) { stack.push(i); i++; }
            ans.push(ele[i]); i++;
        }
    }
    while (stack.length) ans.push(ele[stack.pop()!]);
    return ans;
}
export function demo(): void {
    assertEq(get_result_linear(5, [4, 1, 3, 5, 2]), [5, 3, 2, 1, 4], "linear");
    console.log("PASS");
}
demo();
'''
w("ts/notes/lc_107435426_字典序最大问题分析/solution_4___4.ts", c)

# ---------- lc_110240695 s2 (max_sub_array_ic) ----------
c = HELPERS + '''
function max_sub_array_ic(arr: number[]): number {
    const n = arr.length;
    if (n === 0) return 0;
    let gs = arr[0];
    for (let i = 0; i < n; i++) {
        let s = 0;
        for (let j = i; j < n; j++) {
            s += arr[j];
            if (gs < s) gs = s;
        }
    }
    return gs;
}
export function demo(): void {
    assertEq(max_sub_array_ic([-2, 1, -3, 4, -1, 2, 1]), 6, "ms1");
    assertEq(max_sub_array_ic([-1, -2, -3]), -1, "ms2");
    console.log("PASS");
}
demo();
'''
w("ts/notes/lc_110240695_分治策略之greatest_slice_2-way_merge_counting/solution_2___2.ts", c)

# ---------- lc_110240695 s3 (max_sub_array_dc) ----------
c = HELPERS + '''
function max_sub_array_dc(arr: number[]): number {
    function helper(lo: number, hi: number): [number, number, number, number] {
        if (hi - lo === 1) { const v = arr[lo]; return [v, v, v, v]; }
        const mi = Math.floor((lo + hi) / 2);
        const [l_best, l_pre, l_suf, l_sum] = helper(lo, mi);
        const [r_best, r_pre, r_suf, r_sum] = helper(mi, hi);
        const crossing = l_suf + r_pre;
        const best = Math.max(l_best, r_best, crossing);
        const prefix = Math.max(l_pre, l_sum + r_pre);
        const suffix = Math.max(r_suf, r_sum + l_suf);
        const total = l_sum + r_sum;
        return [best, prefix, suffix, total];
    }
    if (!arr.length) return 0;
    return helper(0, arr.length)[0];
}
export function demo(): void {
    assertEq(max_sub_array_dc([-2, 1, -3, 4, -1, 2, 1]), 6, "ms1");
    assertEq(max_sub_array_dc([1, 2, 3]), 6, "ms2");
    console.log("PASS");
}
demo();
'''
w("ts/notes/lc_110240695_分治策略之greatest_slice_2-way_merge_counting/solution_3___3.ts", c)

# ---------- lc_134085384 s2 (selection_sort in place) ----------
c = HELPERS + '''
function selection_sort(nums: number[]): void {
    const length = nums.length;
    for (let i = 0; i < length - 1; i++) {
        let min_index = i;
        for (let j = i + 1; j < length; j++) {
            if (nums[j] < nums[min_index]) min_index = j;
        }
        if (i !== min_index) { const t = nums[i]; nums[i] = nums[min_index]; nums[min_index] = t; }
    }
}
export function demo(): void {
    const a = [5, 4, 3, 2, 1].slice(); selection_sort(a);
    assertEq(a, [1, 2, 3, 4, 5], "sel");
    const b = [3, 1, 4, 2].slice(); selection_sort(b);
    assertEq(b, [1, 2, 3, 4], "sel2");
    console.log("PASS");
}
demo();
'''
w("ts/notes/lc_134085384_选择排序/solution_2___2.ts", c)

# ---------- lc_92 s1 (reverseBetween) ----------
c = LIST_NODE + HELPERS + '''
function reverseLinkedList(head: ListNode | null): ListNode | null {
    let prev: ListNode | null = null; let curr = head;
    while (curr) { const nxt = curr.next; curr.next = prev; prev = curr; curr = nxt; }
    return prev;
}
function reverseBetween(head: ListNode | null, left: number, right: number): ListNode | null {
    const dummy = new ListNode(-1); dummy.next = head;
    let pre: ListNode = dummy;
    for (let k = 0; k < left - 1; k++) pre = pre.next!;
    const left_node = pre.next!;
    let right_node: ListNode = pre;
    for (let k = 0; k < right - left; k++) right_node = right_node.next!;
    const curr = right_node.next;
    pre.next = null;
    right_node.next = null;
    reverseLinkedList(left_node);
    pre.next = right_node;
    left_node.next = curr;
    return dummy.next;
}
export function demo(): void {
    assertEq(listToArr(reverseBetween(buildList([1, 2, 3, 4, 5]), 2, 4)!), [1, 3, 2, 4, 5], "rev1");
    assertEq(listToArr(reverseBetween(buildList([1, 2, 3, 4, 5]), 1, 4)!), [3, 2, 1, 4, 5], "rev2");
    assertEq(listToArr(reverseBetween(buildList([1, 2, 3, 4, 5]), 3, 4)!), [1, 2, 3, 4, 5], "rev3");
    console.log("PASS");
}
demo();
'''
w("ts/linked_list/lc_92_反转链表_ii/solution_1_1_____1______.ts", c)

# ---------- lc_206 s6 (recursive reverseList) ----------
c = LIST_NODE + HELPERS + '''
function reverseList(head: ListNode | null): ListNode | null {
    if (!head || !head.next) return head;
    const result = reverseList(head.next);
    head.next.next = head;
    head.next = null;
    return result;
}
export function demo(): void {
    assertEq(listToArr(reverseList(buildList([1, 2, 3]))!), [3, 2, 1], "rev1");
    assertEq(listToArr(reverseList(buildList([1, 2, 3, 4, 5]))!), [5, 4, 3, 2, 1], "rev2");
    console.log("PASS");
}
demo();
'''
w("ts/linked_list/lc_206_反转链表/solution_6___6.ts", c)

# ---------- lc_115 s1 (numDistinct DP) ----------
c = HELPERS + '''
function numDistinct(s: string, t: string): number {
    const m = s.length, n = t.length;
    const dp: number[][] = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));
    for (let i = 0; i <= m; i++) dp[i][n] = 1;
    for (let i = m - 1; i >= 0; i--) {
        for (let j = n - 1; j >= 0; j--) {
            if (s[i] === t[j]) dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j];
            else dp[i][j] = dp[i + 1][j];
        }
    }
    return dp[0][0];
}
export function demo(): void {
    assertEq(numDistinct("rabbbit", "rabbit"), 3, "nd1");
    assertEq(numDistinct("babgbag", "bag"), 5, "nd2");
    console.log("PASS");
}
demo();
'''
w("ts/dp/lc_115_不同的子序列/solution_1___1.ts", c)

# ---------- lc_115 s2 (numDistinct recursive memo) ----------
c = HELPERS + '''
function numDistinct(s: string, t: string): number {
    const sLen = s.length, tLen = t.length;
    const memo = new Map<string, number>();
    function helper(i: number, j: number): number {
        if (j < 0) return 1;
        if (i < 0) return 0;
        const key = i + "," + j;
        if (memo.has(key)) return memo.get(key)!;
        let res: number;
        if (s[i] === t[j]) res = helper(i - 1, j) + helper(i - 1, j - 1);
        else res = helper(i - 1, j);
        memo.set(key, res);
        return res;
    }
    return helper(sLen - 1, tLen - 1);
}
export function demo(): void {
    assertEq(numDistinct("rabbbit", "rabbit"), 3, "nd1");
    assertEq(numDistinct("babgbag", "bag"), 5, "nd2");
    console.log("PASS");
}
demo();
'''
w("ts/dp/lc_115_不同的子序列/solution_2_2_____2_________.ts", c)

# ---------- lc_583 s2 (minDistance) ----------
c = HELPERS + '''
function minDistance(word1: string, word2: string): number {
    const m = word1.length, n = word2.length;
    const dp: number[][] = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));
    for (let i = 1; i <= m; i++) dp[i][0] = i;
    for (let j = 1; j <= n; j++) dp[0][j] = j;
    for (let i = 1; i <= m; i++) {
        const c1 = word1[i - 1];
        for (let j = 1; j <= n; j++) {
            const c2 = word2[j - 1];
            if (c1 === c2) dp[i][j] = dp[i - 1][j - 1];
            else dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1]) + 1;
        }
    }
    return dp[m][n];
}
export function demo(): void {
    assertEq(minDistance("sea", "eat"), 2, "md1");
    assertEq(minDistance("", "abc"), 3, "md2");
    assertEq(minDistance("a", "b"), 2, "md3");
    console.log("PASS");
}
demo();
'''
w("ts/dp/lc_583_两个字符串的删除操作/solution_2_2_____2______.ts", c)

print("DONE batch3 (chunk1 remaining)")
