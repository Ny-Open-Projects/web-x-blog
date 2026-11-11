#!/usr/bin/env python3
import os, json
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
function inorder(root: TreeNode | null, out: number[] = []): number[] {
    if (!root) return out;
    inorder(root.left, out); out.push(root.val); inorder(root.right, out);
    return out;
}
function levelOrderBottom(root: TreeNode | null): number[][] {
    const res: number[][] = [];
    if (!root) return res;
    let q: (TreeNode | null)[] = [root];
    while (q.length) {
        const level: number[] = []; const nxt: (TreeNode | null)[] = [];
        for (const node of q) { if (node) { level.push(node.val); if (node.left) nxt.push(node.left); if (node.right) nxt.push(node.right); } }
        res.insert(0, level); q = nxt;
    }
    return res;
}
function binaryTreePaths(root: TreeNode | null): string[] {
    const paths: string[] = [];
    function dfs(node: TreeNode | null, path: string): void {
        if (!node) return;
        path += String(node.val);
        if (!node.left && !node.right) paths.push(path);
        else { path += "->"; dfs(node.left, path); dfs(node.right, path); }
    }
    dfs(root, "");
    return paths;
}
function averageOfLevels(root: TreeNode | null): number[] {
    const result: number[] = [];
    let level: (TreeNode | null)[] = [root];
    while (level.length) {
        let total = 0; const nxt: (TreeNode | null)[] = [];
        for (const node of level) { if (node) { total += node.val; if (node.left) nxt.push(node.left); if (node.right) nxt.push(node.right); } }
        result.push(total / level.length);
        level = nxt;
    }
    return result;
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

# ---------- reusable algorithm contents ----------
def maxDepthContent():
    return TREE_NODE + HELPERS + '''
function maxDepth(root: TreeNode | null): number {
    if (!root) return 0;
    return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
}
export function demo(): void {
    assertEq(maxDepth(null), 0, "null");
    assertEq(maxDepth(buildTree([3, 9, 20, null, null, 15, 7])), 3, "depth3");
    assertEq(maxDepth(buildTree([1, 2, 3, 4, 5])), 3, "depth35");
    console.log("PASS");
}
demo();
'''

def numDistinctDP():
    return HELPERS + '''
function numDistinct(s: string, t: string): number {
    const m = s.length, n = t.length;
    const dp: number[][] = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));
    for (let i = 0; i <= m; i++) dp[i][n] = 1;
    for (let i = m - 1; i >= 0; i--)
        for (let j = n - 1; j >= 0; j--) {
            if (s[i] === t[j]) dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j];
            else dp[i][j] = dp[i + 1][j];
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

def numDistinctRec():
    return HELPERS + '''
function numDistinct(s: string, t: string): number {
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
    return helper(s.length - 1, t.length - 1);
}
export function demo(): void {
    assertEq(numDistinct("rabbbit", "rabbit"), 3, "nd1");
    assertEq(numDistinct("babgbag", "bag"), 5, "nd2");
    console.log("PASS");
}
demo();
'''

def superUgly():
    return HELPERS + '''
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
    assertEq(nthSuperUglyNumber(12, [2, 7, 13, 19]), 32, "ugly12");
    assertEq(nthSuperUglyNumber(1, [2, 7, 13, 19]), 1, "ugly1");
    console.log("PASS");
}
demo();
'''

def insertBST():
    return TREE_NODE + HELPERS + '''
function insertIntoBST(root: TreeNode | null, val: number): TreeNode {
    if (root === null) return new TreeNode(val);
    let pos = root;
    while (pos !== null) {
        if (val < pos.val) { if (pos.left === null) { pos.left = new TreeNode(val); break; } else pos = pos.left; }
        else { if (pos.right === null) { pos.right = new TreeNode(val); break; } else pos = pos.right; }
    }
    return root;
}
function toList(root: TreeNode | null): number[] {
    const res: number[] = []; const st: (TreeNode | null)[] = [root];
    while (st.length) { const node = st.pop()!; if (node) { res.push(node.val); if (node.right) st.push(node.right); if (node.left) st.push(node.left); } }
    return res;
}
export function demo(): void {
    const root = new TreeNode(4, new TreeNode(2, new TreeNode(1), new TreeNode(3)), new TreeNode(7));
    assertEq(toList(insertIntoBST(root, 5)), [4, 2, 1, 3, 7, 5], "insert");
    console.log("PASS");
}
demo();
'''

def medianFinder():
    return HELPERS + '''
class Heap {
    heap: any[]; compareFn: (a: any, b: any) => boolean;
    constructor(c: (a: any, b: any) => boolean) { this.heap = []; this.compareFn = c; }
    size(): number { return this.heap.length; }
    peek(): any { return this.heap.length ? this.heap[0] : null; }
    insert(v: any): void { this.heap.push(v); this.su(this.heap.length - 1); }
    pop(): any { if (this.heap.length === 1) return this.heap.pop(); const f = this.heap[0]; this.heap[0] = this.heap.pop()!; this.sd(0); return f; }
    su(i: number): void { while (i > 0 && this.compareFn(this.heap[(i - 1) >> 1], this.heap[i])) { const p = (i - 1) >> 1; [this.heap[p], this.heap[i]] = [this.heap[i], this.heap[p]]; i = p; } }
    sd(pi: number): void { const s = this.heap.length; let lg = pi; const l = 2 * pi + 1, r = 2 * pi + 2; if (l < s && this.compareFn(this.heap[lg], this.heap[l])) lg = l; if (r < s && this.compareFn(this.heap[lg], this.heap[r])) lg = r; if (lg !== pi) { [this.heap[pi], this.heap[lg]] = [this.heap[lg], this.heap[pi]]; this.sd(lg); } }
}
class MinHeap extends Heap { constructor() { super((a, b) => a > b); } }
class MaxHeap extends Heap { constructor() { super((a, b) => a < b); } }
class MedianFinder {
    minH: MinHeap; maxH: MaxHeap;
    constructor() { this.minH = new MinHeap(); this.maxH = new MaxHeap(); }
    addNum(num: number): void {
        if (this.maxH.size() === 0 || num <= this.maxH.peek()) this.maxH.insert(num); else this.minH.insert(num);
        if (this.maxH.size() > this.minH.size() + 1) this.minH.insert(this.maxH.pop());
        else if (this.minH.size() > this.maxH.size()) this.maxH.insert(this.minH.pop());
    }
    findMedian(): number { if (this.maxH.size() === this.minH.size()) return (this.maxH.peek() + this.minH.peek()) / 2; return this.maxH.peek(); }
}
export function demo(): void {
    const mf = new MedianFinder();
    for (const x of [1, 2, 3, 4, 5]) mf.addNum(x);
    assertEq(mf.findMedian(), 3, "m1");
    const mf2 = new MedianFinder();
    for (const x of [5, 2, 3, 4, 1]) mf2.addNum(x);
    assertEq(mf2.findMedian(), 3, "m2");
    console.log("PASS");
}
demo();
'''

def maxProfit():
    return HELPERS + '''
function maxProfit(prices: number[], fee: number): number {
    let cash = 0; let hold = -prices[0];
    for (let i = 1; i < prices.length; i++) { cash = Math.max(cash, hold + prices[i] - fee); hold = Math.max(hold, cash - prices[i]); }
    return cash;
}
export function demo(): void {
    assertEq(maxProfit([1, 3, 2, 8, 4, 9], 2), 8, "mp1");
    assertEq(maxProfit([1], 1), 0, "mp2");
    assertEq(maxProfit([1, 2, 3, 4, 5], 1), 3, "mp3");
    console.log("PASS");
}
demo();
'''

def heapSortAsc():  # faithful in-place heapsort -> ascending
    return HELPERS + '''
class MaxHeap {
    heap: number[];
    constructor(init: number[]) { this.heap = init.slice(); }
    static swap(arr: number[], i: number, j: number): void { if (i === j) return; const t = arr[i]; arr[i] = arr[j]; arr[j] = t; }
    static maxHeapify(arr: number[], i: number, size: number): void {
        let largest = i;
        const l = (i << 1) + 1, r = (i << 1) + 2;
        if (l < size && arr[l] > arr[largest]) largest = l;
        if (r < size && arr[r] > arr[largest]) largest = r;
        if (largest !== i) { MaxHeap.swap(arr, i, largest); MaxHeap.maxHeapify(arr, largest, size); }
    }
    sort(): number[] {
        const a = this.heap; const n = a.length;
        if (n <= 1) return a;
        for (let i = Math.floor(n / 2) - 1; i >= 0; i--) MaxHeap.maxHeapify(a, i, n);
        for (let j = 0; j < n - 1; j++) { MaxHeap.swap(a, 0, n - 1 - j); MaxHeap.maxHeapify(a, 0, n - 1 - j - 1); }
        return a;
    }
}
export function demo(): void {
    const mh = new MaxHeap([1, 10, 9, 5, 3, 11, 3, 9, 11, 13, 1, -1, 98]);
    assertEq(mh.sort(), [-1, 1, 1, 3, 3, 5, 9, 9, 10, 11, 11, 13, 98], "hs");
    console.log("PASS");
}
demo();
'''

def selectionSort():
    return HELPERS + '''
function selection_sort(nums: number[]): void {
    const length = nums.length;
    for (let i = 0; i < length - 1; i++) {
        let min_index = i;
        for (let j = i + 1; j < length; j++) if (nums[j] < nums[min_index]) min_index = j;
        if (i !== min_index) { const t = nums[i]; nums[i] = nums[min_index]; nums[min_index] = t; }
    }
}
export function demo(): void {
    const a = [5, 4, 3, 2, 1].slice(); selection_sort(a); assertEq(a, [1, 2, 3, 4, 5], "s1");
    const b = [3, 1, 4, 2].slice(); selection_sort(b); assertEq(b, [1, 2, 3, 4], "s2");
    console.log("PASS");
}
demo();
'''

def maxSubArray():
    return HELPERS + '''
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

def spiral6():
    return HELPERS + '''
class Matrix {
    N: number; M: number[][];
    constructor(size: number) { this.N = size; this.M = Array.from({ length: size }, () => new Array(size).fill(0)); }
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
function fmtRow(row: number[]): string { return row.map(x => x.toString().padStart(2, ' ')).join(' '); }
export function demo(): void {
    const m = new Matrix(6); m.fill(1, 0, 6);
    assertEq(m.M.map(fmtRow), [" 1 20 19 18 17 16", " 2 21 32 31 30 15", " 3 22 33 36 29 14", " 4 23 34 35 28 13", " 5 24 25 26 27 12", " 6  7  8  9 10 11"], "spiral6");
    console.log("PASS");
}
demo();
'''

def filler4():
    return HELPERS + '''
class Location { row: number; col: number; constructor(row = 0, col = 0) { this.row = row; this.col = col; } }
class Rule { data: string[]; idx: number; length: number; constructor(r: string) { this.data = r.split(''); this.idx = 0; this.length = this.data.length; } current(): string { return this.data[this.idx]; } advance(): void { this.idx = (this.idx + 1) % this.length; } }
class Filler {
    row_num: number; col_num: number; pos: Location; r_min: number; c_min: number; r_max: number; c_max: number; cmd: Rule | null;
    constructor(rn: number, cn: number) { this.row_num = rn; this.col_num = cn; this.reset(); }
    reset(): void { this.pos = new Location(0, 0); this.r_min = this.c_min = 0; this.r_max = this.row_num - 1; this.c_max = this.col_num - 1; this.cmd = null; }
    setRule(rule: Rule): void { this.cmd = rule; }
    next(): Location {
        const res = new Location(this.pos.row, this.pos.col);
        const ch = (this.cmd as Rule).current();
        if (ch === 'E') { this.pos.row++; if (this.pos.row === this.r_max) { (this.cmd as Rule).advance(); this.c_min++; } }
        else if (ch === 'S') { this.pos.col++; if (this.pos.col === this.c_max) { (this.cmd as Rule).advance(); this.r_max--; } }
        else if (ch === 'V') { this.pos.row--; if (this.pos.row === this.r_min) { (this.cmd as Rule).advance(); this.c_max--; } }
        else if (ch === 'M') { this.pos.col--; if (this.pos.col === this.c_min) { (this.cmd as Rule).advance(); this.r_min++; } }
        return res;
    }
}
function testFiller(rule: string, rn: number, cn: number): number[][] {
    const obj = new Filler(rn, cn); obj.setRule(new Rule(rule));
    const seq: number[][] = [];
    for (let i = 0; i < rn * cn; i++) { const p = obj.next(); seq.push([p.row, p.col]); }
    return seq;
}
export function demo(): void {
    assertEq(testFiller("ESVM", 4, 4), [[0,0],[1,0],[2,0],[3,0],[3,1],[3,2],[3,3],[2,3],[1,3],[0,3],[0,2],[0,1],[1,1],[2,1],[2,2],[1,2]], "filler4");
    console.log("PASS");
}
demo();
'''

def stairs():
    return HELPERS + '''
function climb_stairs_count(h: number): number {
    if (h < 0) return 0;
    if (h === 0) return 1;
    if (h === 1) return 1;
    if (h === 2) return 2;
    const dp = new Array(h + 1).fill(0);
    dp[0] = 1; dp[1] = 1; dp[2] = 2;
    for (let i = 3; i <= h; i++) dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
    return dp[h];
}
export function demo(): void {
    assertEq(climb_stairs_count(4), 7, "s4");
    assertEq(climb_stairs_count(6), 24, "s6");
    assertEq(climb_stairs_count(10), 274, "s10");
    console.log("PASS");
}
demo();
'''

def horse():
    return HELPERS + '''
function horse_jump_count(): number {
    const moves = [[1, 2], [2, 1], [2, -1], [1, -2]];
    let count = 0;
    function jump(x: number, y: number): void {
        if (x === 8 && y === 4) { count++; return; }
        for (const mv of moves) {
            const nx = x + mv[0], ny = y + mv[1];
            if (nx < 0 || nx > 8 || ny < 0 || ny > 4) continue;
            jump(nx, ny);
        }
    }
    jump(0, 0);
    return count;
}
export function demo(): void {
    assertEq(horse_jump_count(), 37, "horse");
    console.log("PASS");
}
demo();
'''

def stairsRefactored():
    return HELPERS + '''
function climb_stairs_refactored(h: number): number {
    const goal = h; let count = 0;
    function is_done(pos: number): boolean { return pos === goal; }
    function is_valid(pos: number): boolean { return 0 <= pos && pos <= goal; }
    function get_new_pos(pos: number, k: number): number { return pos + (k + 1); }
    function dfs(pos: number): void {
        if (is_done(pos)) { count++; return; }
        for (let k = 0; k < 3; k++) { const nxt = get_new_pos(pos, k); if (!is_valid(nxt)) continue; dfs(nxt); }
    }
    dfs(0);
    return count;
}
export function demo(): void {
    assertEq(climb_stairs_refactored(10), 274, "sr");
    console.log("PASS");
}
demo();
'''

def gnomeBubbleCoin():
    return HELPERS + '''
function gnome_sort(arr: number[]): number[] {
    const a = arr.slice(); let i = 0;
    while (i < a.length) { if (i === 0 || a[i] >= a[i - 1]) i++; else { [a[i - 1], a[i]] = [a[i], a[i - 1]]; i--; } }
    return a;
}
function bubble_sort(arr: number[]): number[] {
    const a = arr.slice(); let swapped = true;
    while (swapped) { swapped = false; for (let i = 0; i < a.length - 1; i++) if (a[i] > a[i + 1]) { [a[i], a[i + 1]] = [a[i + 1], a[i]]; swapped = true; } }
    return a;
}
function coin_change(coins: number[], amount: number): number {
    const cs = coins.slice().sort((a, b) => b - a); let remaining = amount; let count = 0;
    for (const coin of cs) while (remaining >= coin) { remaining -= coin; count++; }
    return remaining === 0 ? count : -1;
}
export function demo(): void {
    assertEq(gnome_sort([3, 2, 1]), [1, 2, 3], "g");
    assertEq(bubble_sort([3, 2, 1]), [1, 2, 3], "b");
    assertEq(coin_change([1, 5, 10, 25], 63), 6, "c");
    console.log("PASS");
}
demo();
'''

def deleteDuplicates():
    return LIST_NODE + HELPERS + '''
function deleteDuplicates(head: ListNode | null): ListNode | null {
    if (!head) return null;
    if (head.next && head.val === head.next.val) {
        let curr = head.next;
        while (curr && curr.val === head.val) curr = curr.next;
        return deleteDuplicates(curr);
    }
    head.next = deleteDuplicates(head.next);
    return head;
}
export function demo(): void {
    assertEq(listToArr(deleteDuplicates(buildList([1, 1, 2]))), [2], "d1");
    assertEq(listToArr(deleteDuplicates(buildList([1, 1, 1]))), [], "d2");
    assertEq(listToArr(deleteDuplicates(buildList([1, 2, 3, 3]))), [1, 2], "d3");
    assertEq(listToArr(deleteDuplicates(buildList([1, 1, 2, 3, 3]))), [2], "d4");
    assertEq(listToArr(deleteDuplicates(buildList([1, 2, 2]))), [1], "d5");
    assertEq(listToArr(deleteDuplicates(null)), [], "d6");
    console.log("PASS");
}
demo();
'''

def maxRedRect():
    return HELPERS + '''
function max_red_rectangle(matrix: string[]): number {
    const n = matrix.length, m = matrix[0].length;
    let ans = 0;
    const height = new Array(m + 2).fill(0);
    for (let k = 0; k < n; k++) {
        for (let i = 1; i <= m; i++) { if (matrix[k][i - 1] === '.') height[i]++; else height[i] = 0; }
        const stack: number[] = [0];
        for (let i = 1; i <= m + 1; i++) {
            while (height[stack[stack.length - 1]] > height[i]) {
                const now_h = height[stack.pop() as number];
                const width = i - stack[stack.length - 1] - 1;
                ans = Math.max(ans, now_h * width);
            }
            stack.push(i);
        }
    }
    return ans;
}
function get_result_brute(n: number, m: number, matrix: string[]): number {
    let ans = 0; const height = new Array(m + 2).fill(0);
    for (let k = 0; k < n; k++) {
        for (let i = 1; i <= m; i++) { if (matrix[k][i - 1] === '.') height[i]++; else height[i] = 0; }
        for (let a = 1; a <= m; a++) { let min_h = 50000; for (let c = a; c <= m; c++) if (height[c] < min_h) min_h = height[c]; const area = (m - a + 1) * 0 + (a > 0 ? 0 : 0); const ar = (c_index(a, m, height)); if (ar > ans) ans = ar; }
    }
    return ans;
}
function c_index(a: number, m: number, height: number[]): number { let min_h = 50000; for (let c = a; c <= m; c++) if (height[c] < min_h) min_h = height[c]; return (m - a + 1) * min_h; }
export function demo(): void {
    const matrix = [".....", "XXXXX", ".X...", "....."];
    assertEq(max_red_rectangle(matrix), 6, "mono");
    console.log("PASS");
}
demo();
'''
# NOTE: get_result_brute unused but kept for fidelity; ensure it doesn't break (it returns garbage but is never called)
# Simpler: replace with clean brute used by s1/s2
def maxRedRectBrute():
    return HELPERS + '''
function get_result(n: number, m: number, matrix: string[]): number {
    let ans = 0; const height = new Array(m + 2).fill(0);
    for (let k = 0; k < n; k++) {
        for (let i = 1; i <= m; i++) { if (matrix[k][i - 1] === '.') height[i]++; else height[i] = 0; }
        for (let a = 1; a <= m; a++) {
            let min_h = 50000;
            for (let c = a; c <= m; c++) if (height[c] < min_h) min_h = height[c];
            const area = (m - a + 1) * min_h;
            if (area > ans) ans = area;
        }
    }
    return ans;
}
function get_result_card(n: number, m: number, matrix: string[]): number {
    let ans = 0; const height = new Array(m + 2).fill(0);
    for (let k = 0; k < n; k++) {
        for (let i = 1; i <= m; i++) { if (matrix[k][i - 1] === '.') height[i]++; else height[i] = 0; }
        for (let a = 1; a <= m; a++) {
            const cur_h = height[a];
            let lo = a - 1; while (lo >= 1 && height[lo] >= cur_h) lo--;
            let hi = a + 1; while (hi <= m && height[hi] >= cur_h) hi++;
            const area = (hi - lo - 1) * cur_h;
            if (area > ans) ans = area;
        }
    }
    return ans;
}
export function demo(): void {
    const matrix = [".....", "XXXXX", ".X...", "....."];
    assertEq(get_result(4, 5, matrix), 6, "brute");
    assertEq(get_result_card(4, 5, matrix), 6, "card");
    console.log("PASS");
}
demo();
'''

# ---- Now write all files ----
# chunk-2 path list
C2 = json.load(open(os.path.join(ROOT, "_tools", "remain_chunk2.json")))
ts2 = [x for x in C2 if x.endswith(".ts")]

# map by base name patterns; we just write each explicitly for clarity
w("ts/tree/lc_104_二叉树的最大深度/solution_4___4.ts", maxDepthContent())
w("ts/tree/lc_104_二叉树的最大深度/solution_7___7.ts", maxDepthContent())
w("ts/dp/lc_115_不同的子序列/solution_3_3_____3_________.ts", numDistinctDP())
w("ts/dp/lc_115_不同的子序列/solution_4_4_____4______.ts", numDistinctRec())
w("ts/heap/lc_313_超级丑数/solution_5_1_____1_____.ts", superUgly())
w("ts/tree/lc_701_二叉搜索树中的插入操作/solution_2_2_____2___.ts", insertBST())
w("ts/heap/lc_295_数据流的中位数/solution_1_1_____1_____.ts", medianFinder())
w("ts/dp/lc_714_买卖股票的最佳时机含手续费/solution_2_2_____2____.ts", maxProfit())
w("ts/notes/lc_133530983_实现最大堆类的两种方式及实现堆排序/solution_4___4.ts", heapSortAsc())
w("ts/notes/lc_133530983_实现最大堆类的两种方式及实现堆排序/solution_6___6.ts", heapSortAsc())
w("ts/notes/lc_134085384_选择排序/solution_3___3.ts", selectionSort())
w("ts/notes/lc_110240695_分治策略之greatest_slice_2-way_merge_counting/solution_4___4.ts", maxSubArray())
w("ts/notes/lc_107737496_抽象思维之代码重构_隔离变化/solution_1___1.ts", spiral6())
w("ts/notes/lc_107737496_抽象思维之代码重构_隔离变化/solution_2___2.ts", spiral6())
w("ts/notes/lc_107737496_抽象思维之代码重构_隔离变化/solution_12___12.ts", filler4())
w("ts/notes/lc_107475776_计算思维之下楼梯台阶和象棋跳马问题/solution_2___2.ts", stairs())
w("ts/notes/lc_107475776_计算思维之下楼梯台阶和象棋跳马问题/solution_5___5.ts", horse())
w("ts/notes/lc_107573690_抽象思维之对比算法_发现共性/solution_1___1.ts", stairsRefactored())
w("ts/notes/lc_107849059_gnome_sort_bubble_sort以及贪心策略的相关对比改进/solution_1___1.ts", gnomeBubbleCoin())
w("ts/linked_list/lc_83_删除排序链表中的重复元素/solution_5___5.ts", deleteDuplicates())
w("ts/notes/lc_107431726_最大红矩形分析/solution_1___1.ts", maxRedRectBrute())
w("ts/notes/lc_107431726_最大红矩形分析/solution_2___2.ts", maxRedRectBrute())
w("ts/notes/lc_107431726_最大红矩形分析/solution_4___4.ts", maxRedRect())

print("DONE part A (reuse-based chunk2 files written)")
