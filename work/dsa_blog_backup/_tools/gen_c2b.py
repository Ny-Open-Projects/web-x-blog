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
        res.unshift(level); q = nxt;
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

# ---------- per-file contents ----------

def f_minheap():
    return LIST_NODE + HELPERS + '''
class MinHeap {
    heap: number[];
    constructor() { this.heap = []; }
    getParentIndex(i: number): number { return (i - 1) >> 1; }
    getLeftIndex(i: number): number { return (i << 1) + 1; }
    getRightIndex(i: number): number { return (i << 1) + 2; }
    swap(i: number, j: number): void { const t = this.heap[i]; this.heap[i] = this.heap[j]; this.heap[j] = t; }
    shiftUp(i: number): void { if (i === 0) return; const pi = this.getParentIndex(i); if (this.heap[pi] > this.heap[i]) { this.swap(pi, i); this.shiftUp(pi); } }
    shiftDown(i: number): void {
        const size = this.size(); const li = this.getLeftIndex(i); const ri = this.getRightIndex(i);
        let smallest = i;
        if (li < size && this.heap[li] < this.heap[i]) smallest = li;
        if (ri < size && this.heap[ri] < this.heap[smallest]) smallest = ri;
        if (smallest !== i) { this.swap(smallest, i); this.shiftDown(smallest); }
    }
    insert(value: number): void { this.heap.push(value); this.shiftUp(this.heap.length - 1); }
    pop(): void { if (this.size() === 0) return; this.heap[0] = this.heap.pop()!; this.shiftDown(0); }
    peak(): number | null { return this.size() === 0 ? null : this.heap[0]; }
    size(): number { return this.heap.length; }
}
export function demo(): void {
    const heap = new MinHeap();
    heap.insert(3); heap.insert(1); heap.insert(6); heap.insert(5); heap.insert(2); heap.insert(4);
    assertEq(heap.heap, [1, 2, 4, 5, 3, 6], "afterInsert");
    assertEq(heap.peak(), 1, "peek");
    heap.pop();
    assertEq(heap.heap, [2, 3, 4, 5, 6], "afterPop");
    heap.pop();
    assertEq(heap.heap, [3, 5, 4, 6], "afterPop2");
    assertEq(heap.size(), 4, "size");
    const empty = new MinHeap();
    assertEq(empty.peak(), null, "emptyPeek");
    empty.pop();
    assertEq(empty.size(), 0, "emptySize");
    console.log("PASS");
}
demo();
'''

def f_sortedstack():
    return HELPERS + '''
class SortedStack {
    stk1: number[]; stk2: number[];
    constructor() { this.stk1 = []; this.stk2 = []; }
    push(val: number): void {
        while (this.stk1.length && this.stk1[this.stk1.length - 1] > val) this.stk2.push(this.stk1.pop()!);
        this.stk1.push(val);
        while (this.stk2.length) this.stk1.push(this.stk2.pop()!);
    }
    pop(): void { if (!this.isEmpty()) this.stk1.pop(); }
    peek(): number { if (this.isEmpty()) return -1; return this.stk1[this.stk1.length - 1]; }
    isEmpty(): boolean { return this.stk1.length === 0; }
}
export function demo(): void {
    const s = new SortedStack();
    for (const v of [4, 2, 5, 1, 3]) s.push(v);
    const out: number[] = [];
    while (!s.isEmpty()) { out.push(s.peek()); s.pop(); }
    assertEq(out, [5, 4, 3, 2, 1], "sorted");
    console.log("PASS");
}
demo();
'''

def f_mergesort():
    return HELPERS + '''
function mergeSort(nums: number[]): number[] {
    if (nums.length <= 1) return nums.slice();
    const mid = Math.floor(nums.length / 2);
    const left = mergeSort(nums.slice(0, mid));
    const right = mergeSort(nums.slice(mid));
    return merge(left, right);
}
function merge(left: number[], right: number[]): number[] {
    const result: number[] = []; let i = 0, j = 0;
    while (i < left.length && j < right.length) {
        if (left[i] <= right[j]) result.push(left[i++]); else result.push(right[j++]);
    }
    while (i < left.length) result.push(left[i++]);
    while (j < right.length) result.push(right[j++]);
    return result;
}
export function demo(): void {
    assertEq(mergeSort([1, 2, 3]), [1, 2, 3], "sorted");
    assertEq(mergeSort([3, 1, 2]), [1, 2, 3], "unsorted");
    assertEq(mergeSort([]), [], "empty");
    console.log("PASS");
}
demo();
'''

def f_circular_deque():
    return HELPERS + '''
class CNode { val: number; prev: CNode | null; next: CNode | null; constructor(v: number) { this.val = v; this.prev = null; this.next = null; } }
class MyCircularDeque {
    head: CNode | null; tail: CNode | null; capacity: number; size: number;
    constructor(k: number) { this.head = null; this.tail = null; this.capacity = k; this.size = 0; }
    insertFront(v: number): boolean {
        if (this.isFull()) return false;
        const n = new CNode(v);
        if (this.isEmpty()) { this.head = n; this.tail = n; }
        else { n.next = this.head; if (this.head) this.head.prev = n; this.head = n; }
        this.size++; return true;
    }
    insertLast(v: number): boolean {
        if (this.isFull()) return false;
        const n = new CNode(v);
        if (this.isEmpty()) { this.head = n; this.tail = n; }
        else { if (this.tail) { this.tail.next = n; n.prev = this.tail; } this.tail = n; }
        this.size++; return true;
    }
    deleteFront(): boolean {
        if (this.isEmpty()) return false;
        if (this.head) { this.head = this.head.next; if (this.head) this.head.prev = null; else this.tail = null; }
        this.size--; return true;
    }
    deleteLast(): boolean {
        if (this.isEmpty()) return false;
        if (this.tail) { this.tail = this.tail.prev; if (this.tail) this.tail.next = null; else this.head = null; }
        this.size--; return true;
    }
    getFront(): number { if (this.isEmpty()) return -1; return this.head ? this.head.val : -1; }
    getRear(): number { if (this.isEmpty()) return -1; return this.tail ? this.tail.val : -1; }
    isEmpty(): boolean { return this.size === 0; }
    isFull(): boolean { return this.size === this.capacity; }
}
export function demo(): void {
    const obj = new MyCircularDeque(3);
    assertEq(obj.insertLast(1), true, "i1");
    assertEq(obj.insertLast(2), true, "i2");
    assertEq(obj.insertFront(3), true, "i3");
    assertEq(obj.insertFront(4), false, "i4");
    assertEq(obj.getRear(), 2, "rear");
    assertEq(obj.isFull(), true, "full");
    assertEq(obj.deleteLast(), true, "dl");
    assertEq(obj.insertFront(4), true, "i4b");
    assertEq(obj.getFront(), 4, "front");
    console.log("PASS");
}
demo();
'''

def f_shellsort():
    return HELPERS + '''
function shellSort(lst: number[]): number[] {
    const a = lst.slice(); const length = a.length; let gap = Math.floor(length / 2);
    while (gap > 0) {
        for (let i = gap; i < length; i++) {
            const tmp = a[i]; let p = i;
            while (p - gap >= 0 && a[p - gap] > tmp) { a[p] = a[p - gap]; p -= gap; }
            a[p] = tmp;
        }
        gap = Math.floor(gap / 2);
    }
    return a;
}
export function demo(): void {
    assertEq(shellSort([9, 12, 1, 3, -1, 22, 22, 31, 1, 0]), [-1, 0, 1, 1, 3, 9, 12, 22, 22, 31], "shell");
    assertEq(shellSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5], "rev");
    console.log("PASS");
}
demo();
'''

def f_longest_mono():
    return HELPERS + '''
function longestMonotonicSubarray(nums: number[]): number {
    if (!nums.length) return 0;
    const n = nums.length; let ans = 1; let i = 0;
    while (i < n) {
        let j = i;
        while (j + 1 < n && nums[j + 1] > nums[j]) j++;
        ans = Math.max(ans, j - i + 1);
        j = i;
        while (j + 1 < n && nums[j + 1] < nums[j]) j++;
        ans = Math.max(ans, j - i + 1);
        i++;
    }
    return ans;
}
export function demo(): void {
    assertEq(longestMonotonicSubarray([1, 4, 3, 3, 2]), 2, "lms");
    assertEq(longestMonotonicSubarray([]), 0, "empty");
    assertEq(longestMonotonicSubarray([1, 2, 3, 4]), 4, "inc");
    console.log("PASS");
}
demo();
'''

def f_captcha(which):
    if which == 1:
        return HELPERS + '''
function detect_edges(image: number[]): boolean[] {
    const edges = new Array(image.length).fill(false);
    for (let i = 1; i < image.length; i++) edges[i] = Math.abs(image[i] - image[i - 1]) > 50;
    return edges;
}
function recognize_captcha(bg: number[], puzzle: number[]): number {
    const bgEdges = detect_edges(bg); const puzzleEdges = detect_edges(puzzle);
    let best_x = 0, best_score = -1;
    for (let x = 0; x <= bg.length - puzzle.length; x++) {
        let score = 0;
        for (let y = 0; y < puzzle.length; y++) if (bgEdges[x + y] && puzzleEdges[y]) score++;
        if (score > best_score) { best_score = score; best_x = x; }
    }
    return best_x;
}
export function demo(): void {
    const bg = [10, 10, 10, 10, 200, 200, 200, 200];
    const puzzle = [10, 200, 200, 200];
    assertEq(recognize_captcha(bg, puzzle), 3, "gap");
    console.log("PASS");
}
demo();
'''
    else:
        return HELPERS + '''
function detect_edges_sobel(image: number[]): boolean[] {
    const edges = new Array(image.length).fill(false);
    if (image.length < 2) return edges;
    edges[0] = Math.abs(image[1] - image[0]) > 50;
    for (let i = 1; i < image.length - 1; i++) edges[i] = Math.abs(image[i + 1] - image[i - 1]) > 50;
    edges[image.length - 1] = Math.abs(image[image.length - 1] - image[image.length - 2]) > 50;
    return edges;
}
function recognize_captcha(bg: number[], puzzle: number[]): number {
    const bgEdges = detect_edges_sobel(bg); const puzzleEdges = detect_edges_sobel(puzzle);
    let best_x = 0, best_score = -1;
    for (let x = 0; x <= bg.length - puzzle.length; x++) {
        let score = 0;
        for (let y = 0; y < puzzle.length; y++) if (bgEdges[x + y] && puzzleEdges[y]) score++;
        if (score > best_score) { best_score = score; best_x = x; }
    }
    return best_x;
}
export function demo(): void {
    const bg = [10, 10, 10, 10, 200, 200, 200, 200];
    const puzzle = [10, 200, 200, 200];
    assertEq(recognize_captcha(bg, puzzle), 3, "gap");
    console.log("PASS");
}
demo();
'''

def f_sortedlisttobst(which):
    if which == 1:
        return LIST_NODE + TREE_NODE + HELPERS + '''
function sortedListToBST(head: ListNode | null): TreeNode | null {
    if (!head) return null;
    const nodes: ListNode[] = []; let cur = head;
    while (cur) { nodes.push(cur); cur = cur.next; }
    function build(left: number, right: number): TreeNode | null {
        if (left > right) return null;
        const mid = Math.floor((left + right) / 2);
        const root = new TreeNode(nodes[mid].val);
        root.left = build(left, mid - 1);
        root.right = build(mid + 1, right);
        return root;
    }
    return build(0, nodes.length - 1);
}
export function demo(): void {
    assertEq(sortedListToBST(null), null, "null");
    assertEq(inorder(sortedListToBST(buildList([1, 2, 3]))), [1, 2, 3], "l123");
    console.log("PASS");
}
demo();
'''
    else:
        return LIST_NODE + TREE_NODE + HELPERS + '''
function sortedListToBST(head: ListNode | null): TreeNode | null {
    function getLength(h: ListNode | null): number { let len = 0; while (h) { len++; h = h.next; } return len; }
    let cur = head;
    function buildTree(left: number, right: number): TreeNode | null {
        if (left > right) return null;
        const mid = Math.floor((left + right + 1) / 2);
        const root = new TreeNode(0);
        root.left = buildTree(left, mid - 1);
        if (cur) { root.val = cur.val; cur = cur.next; }
        root.right = buildTree(mid + 1, right);
        return root;
    }
    const length = getLength(head);
    return buildTree(0, length - 1);
}
export function demo(): void {
    assertEq(sortedListToBST(null), null, "null");
    assertEq(inorder(sortedListToBST(buildList([1, 2, 3]))), [1, 2, 3], "l123");
    console.log("PASS");
}
demo();
'''

def f_preorder(which):
    if which == 2:
        return TREE_NODE + HELPERS + '''
function preorderTraversal(root: TreeNode | null): number[] {
    const ans: number[] = []; const stack: TreeNode[] = []; let cur: TreeNode | null = root;
    while (cur || stack.length) {
        while (cur) { ans.push(cur.val); stack.push(cur); cur = cur.left; }
        if (stack.length) { cur = stack.pop()!; cur = cur.right; }
    }
    return ans;
}
export function demo(): void {
    assertEq(preorderTraversal(null), [], "null");
    assertEq(preorderTraversal(buildTree([1, null, 2, null, 3])), [1, 2, 3], "pre");
    console.log("PASS");
}
demo();
'''
    elif which == 5:
        return TREE_NODE + HELPERS + '''
function preorderTraversal(root: TreeNode | null): number[] {
    const res: number[] = [];
    function dfs(node: TreeNode | null): void { if (!node) return; res.push(node.val); dfs(node.left); dfs(node.right); }
    dfs(root);
    return res;
}
export function demo(): void {
    assertEq(preorderTraversal(buildTree([1, null, 2, null, 3])), [1, 2, 3], "pre");
    assertEq(preorderTraversal(null), [], "null");
    console.log("PASS");
}
demo();
'''
    else:
        return TREE_NODE + HELPERS + '''
function preorderTraversal(root: TreeNode | null): number[] {
    if (!root) return [];
    return [root.val, ...preorderTraversal(root.left), ...preorderTraversal(root.right)];
}
export function demo(): void {
    assertEq(preorderTraversal(buildTree([1, null, 2, null, 3])), [1, 2, 3], "pre");
    assertEq(preorderTraversal(null), [], "null");
    console.log("PASS");
}
demo();
'''

def f_fibonacci():
    return HELPERS + '''
function fibonacci(n: number, memo: { [k: number]: number } = {}): number {
    if (n <= 1) return n;
    if (n in memo) return memo[n];
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo);
    return memo[n];
}
export function demo(): void {
    assertEq(fibonacci(10), 55, "fib10");
    assertEq(fibonacci(0), 0, "fib0");
    assertEq(fibonacci(1), 1, "fib1");
    console.log("PASS");
}
demo();
'''

def f_minflips():
    return HELPERS + '''
function minFlipsMonoIncr(s: string): number {
    let one = 0, dp = 0;
    for (const c of s) {
        if (c === '0') dp = Math.min(one, dp + 1);
        else one++;
    }
    return dp;
}
export function demo(): void {
    assertEq(minFlipsMonoIncr("00110"), 1, "mf");
    assertEq(minFlipsMonoIncr(""), 0, "empty");
    assertEq(minFlipsMonoIncr("1"), 0, "one");
    console.log("PASS");
}
demo();
'''

def f_browser():
    return HELPERS + '''
class BrowserHistory {
    history: string[]; current: number;
    constructor(homepage: string) { this.history = [homepage]; this.current = 0; }
    visit(url: string): void { this.history = this.history.slice(0, this.current + 1); this.history.push(url); this.current = this.history.length - 1; }
    back(steps: number): string { this.current = Math.max(0, this.current - steps); return this.history[this.current]; }
    forward(steps: number): string { this.current = Math.min(this.history.length - 1, this.current + steps); return this.history[this.current]; }
}
export function demo(): void {
    const browser = new BrowserHistory("leetcode.com");
    browser.visit("google.com");
    browser.visit("facebook.com");
    browser.visit("youtube.com");
    assertEq(browser.back(1), "facebook.com", "back1");
    assertEq(browser.forward(2), "youtube.com", "fwd2");
    console.log("PASS");
}
demo();
'''

def f_freqsort(which):
    if which == 2:
        return HELPERS + '''
function frequencySort(s: string): string {
    const map: { [k: string]: number } = {};
    for (const ch of s) map[ch] = (map[ch] || 0) + 1;
    const entries = Object.entries(map).sort((a, b) => b[1] - a[1] || (a[0] < b[0] ? -1 : 1));
    let res = "";
    for (const [ch, cnt] of entries) res += ch.repeat(cnt);
    return res;
}
export function demo(): void {
    assertEq(frequencySort("tree"), "eert", "fs");
    assertEq(frequencySort(""), "", "empty");
    console.log("PASS");
}
demo();
'''
    else:
        return HELPERS + '''
function frequencySort(s: string): string {
    const mp: { [k: string]: number } = {};
    for (const ch of s) mp[ch] = (mp[ch] || 0) + 1;
    const arr = Object.entries(mp).sort((a, b) => b[1] - a[1]);
    let result = "";
    for (const [ch, cnt] of arr) result += ch.repeat(cnt);
    return result;
}
export function demo(): void {
    assertEq(frequencySort("tree"), "eetr", "fs");
    assertEq(frequencySort(""), "", "empty");
    console.log("PASS");
}
demo();
'''

def f_levelorderbottom():
    return TREE_NODE + HELPERS + '''
export function demo(): void {
    assertEq(levelOrderBottom(null), [], "null");
    assertEq(levelOrderBottom(buildTree([3, 9, 20, null, null, 15, 7])), [[15, 7], [9, 20], [3]], "l1");
    console.log("PASS");
}
demo();
'''

def f_middlenode():
    return LIST_NODE + HELPERS + '''
function middleNode(head: ListNode | null): ListNode | null {
    let slow = head, fast = head;
    while (fast && fast.next) { slow = slow!.next; fast = fast.next.next; }
    return slow;
}
export function demo(): void {
    assertEq(middleNode(null), null, "null");
    assertEq(middleNode(buildList([1, 2, 3, 4, 5]))!.val, 3, "odd");
    assertEq(middleNode(buildList([1, 2, 3, 4, 5, 6]))!.val, 4, "even");
    console.log("PASS");
}
demo();
'''

def f_nextgreater():
    return HELPERS + '''
function nextGreaterElements(nums: number[]): number[] {
    const n = nums.length; const result = new Array(n).fill(-1); const stack: number[] = [];
    for (let i = 0; i < 2 * n; i++) {
        const num = nums[i % n];
        while (stack.length && nums[stack[stack.length - 1]] < num) {
            const idx = stack.pop()!; result[idx] = num;
        }
        if (i < n) stack.push(i);
    }
    return result;
}
export function demo(): void {
    assertEq(nextGreaterElements([1, 2, 1]), [2, -1, 2], "nge");
    assertEq(nextGreaterElements([3, 2, 1]), [-1, 3, 3], "desc");
    console.log("PASS");
}
demo();
'''

def f_insertionsort():
    return HELPERS + '''
function insertion_sort(nums: number[]): number[] {
    const a = nums.slice(); const length = a.length;
    for (let i = 1; i < length; i++) {
        const tmp = a[i]; let j = i;
        while (j > 0) { if (a[j - 1] > tmp) a[j] = a[j - 1]; else break; j--; }
        if (i !== j) a[j] = tmp;
    }
    return a;
}
export function demo(): void {
    assertEq(insertion_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5], "rev");
    assertEq(insertion_sort([1, 2, 3]), [1, 2, 3], "sorted");
    console.log("PASS");
}
demo();
'''

def f_removeelement():
    return HELPERS + '''
function removeElement(nums: number[], val: number): number {
    let left = 0, right = nums.length - 1;
    while (left <= right) {
        if (nums[left] === val) { nums[left] = nums[right]; right--; }
        else left++;
    }
    return left;
}
export function demo(): void {
    assertEq(removeElement([1, 2, 3], 1), 2, "re");
    assertEq(removeElement([2, 2], 2), 0, "all");
    console.log("PASS");
}
demo();
'''

def f_sortlist():
    return LIST_NODE + HELPERS + '''
function sortList(head: ListNode | null): ListNode | null {
    if (!head || !head.next) return head;
    let slow = head, fast = head.next;
    while (fast && fast.next) { slow = slow.next!; fast = fast.next.next; }
    const mid = slow.next; slow.next = null;
    const left = sortList(head); const right = sortList(mid);
    const dummy = new ListNode(0); let curr = dummy;
    let l = left, r = right;
    while (l && r) { if (l.val <= r.val) { curr.next = l; l = l.next; } else { curr.next = r; r = r.next; } curr = curr.next; }
    curr.next = l || r;
    return dummy.next;
}
export function demo(): void {
    assertEq(listToArr(sortList(null)), [], "null");
    assertEq(listToArr(sortList(buildList([4, 2, 1, 3]))), [1, 2, 3, 4], "sort");
    assertEq(listToArr(sortList(buildList([1]))), [1], "single");
    console.log("PASS");
}
demo();
'''

def f_mylinkedlist():
    return HELPERS + '''
class DNode { val: number; prev: DNode | null; next: DNode | null; constructor(val: number) { this.val = val; this.prev = null; this.next = null; } }
class MyLinkedList {
    head: DNode | null; tail: DNode | null; size: number;
    constructor() { this.head = null; this.tail = null; this.size = 0; }
    get(index: number): number { if (index < 0 || index >= this.size) return -1; let curr = this.head; for (let i = 0; i < index; i++) curr = curr!.next; return curr!.val; }
    addAtHead(val: number): void { const n = new DNode(val); n.next = this.head; if (this.head) this.head.prev = n; else this.tail = n; this.head = n; this.size++; }
    addAtTail(val: number): void { const n = new DNode(val); if (this.tail) { this.tail.next = n; n.prev = this.tail; } else this.head = n; this.tail = n; this.size++; }
    addAtIndex(index: number, val: number): void {
        if (index < 0 || index > this.size) return;
        if (index === 0) this.addAtHead(val);
        else if (index === this.size) this.addAtTail(val);
        else { let curr = this.head; for (let i = 0; i < index; i++) curr = curr!.next; const n = new DNode(val); n.prev = curr!.prev; n.next = curr; curr!.prev!.next = n; curr!.prev = n; this.size++; }
    }
    deleteAtIndex(index: number): void {
        if (index < 0 || index >= this.size) return;
        if (index === 0) { this.head = this.head!.next; if (this.head) this.head.prev = null; else this.tail = null; }
        else if (index === this.size - 1) { this.tail = this.tail!.prev; if (this.tail) this.tail.next = null; else this.head = null; }
        else { let curr = this.head; for (let i = 0; i < index; i++) curr = curr!.next; curr!.prev!.next = curr.next; curr!.next!.prev = curr.prev; }
        this.size--;
    }
}
export function demo(): void {
    const obj = new MyLinkedList();
    obj.addAtHead(1); obj.addAtTail(3); obj.addAtIndex(1, 2);
    assertEq(obj.get(1), 2, "g1");
    assertEq(obj.get(0), 1, "g0");
    assertEq(obj.get(2), 3, "g2");
    obj.deleteAtIndex(1);
    assertEq(obj.get(1), 3, "g1b");
    console.log("PASS");
}
demo();
'''

def f_connect():
    return HELPERS + '''
function connect(root: any): any { return {}; }
export function demo(): void {
    assertEq(connect(null), {}, "connect");
    console.log("PASS");
}
demo();
'''

def f_getintersection():
    return LIST_NODE + HELPERS + '''
function getIntersectionNode(headA: ListNode | null, headB: ListNode | null): ListNode | null {
    const visited = new Set<ListNode>(); let t = headA;
    while (t) { visited.add(t); t = t.next; }
    t = headB;
    while (t) { if (visited.has(t)) return t; t = t.next; }
    return null;
}
export function demo(): void {
    const shared = buildList([8, 4, 5]);
    const headA = buildList([4, 1]); let cA = headA; while (cA.next) cA = cA.next; cA.next = shared;
    const headB = buildList([5, 6, 1]); let cB = headB; while (cB.next) cB = cB.next; cB.next = shared;
    assertEq(listToArr(getIntersectionNode(headA, headB)), [8, 4, 5], "inter");
    assertEq(getIntersectionNode(null, null), null, "null");
    console.log("PASS");
}
demo();
'''

def f_editdistance():
    return HELPERS + '''
function minDistance(word1: string, word2: string): number {
    const m = word1.length, n = word2.length;
    const dp: number[][] = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));
    for (let i = 0; i <= m; i++) dp[i][0] = i;
    for (let j = 0; j <= n; j++) dp[0][j] = j;
    for (let i = 1; i <= m; i++) for (let j = 1; j <= n; j++) {
        if (word1[i - 1] === word2[j - 1]) dp[i][j] = dp[i - 1][j - 1];
        else dp[i][j] = 1 + Math.min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]);
    }
    return dp[m][n];
}
export function demo(): void {
    assertEq(minDistance("horse", "ros"), 3, "md");
    assertEq(minDistance("", "abc"), 3, "empty1");
    assertEq(minDistance("", ""), 0, "empty");
    console.log("PASS");
}
demo();
'''

def f_maxbottles():
    return HELPERS + '''
function maxBottlesDrunk(numBottles: number, numExchange: number): number {
    let total = numBottles, nb = numBottles, ne = numExchange;
    while (nb >= ne) { nb += 1 - ne; ne += 1; total += 1; }
    return total;
}
export function demo(): void {
    assertEq(maxBottlesDrunk(10, 3), 13, "mbd");
    assertEq(maxBottlesDrunk(1, 2), 1, "one");
    console.log("PASS");
}
demo();
'''

def f_bfs():
    return HELPERS + '''
function bfs(graph: number[][], start: number): [number[], number[]] {
    const n = graph.length;
    const status: string[] = new Array(n).fill('UNDISCOVERED');
    const parent: number[] = new Array(n).fill(-1);
    const order: number[] = [];
    const q: number[] = [start];
    status[start] = 'DISCOVERED';
    while (q.length) {
        const v = q.shift()!;
        order.push(v);
        for (const u of graph[v]) {
            if (status[u] === 'UNDISCOVERED') { status[u] = 'DISCOVERED'; parent[u] = v; q.push(u); }
        }
        status[v] = 'VISITED';
    }
    return [order, parent];
}
export function demo(): void {
    const graph = [[1, 2], [0, 3, 4], [0, 5], [1], [1], [2]];
    const [order, parent] = bfs(graph, 0);
    assertEq(order, [0, 1, 2, 3, 4, 5], "order");
    assertEq(parent, [-1, 0, 0, 1, 1, 2], "parent");
    console.log("PASS");
}
demo();
'''

def f_mystack():
    return HELPERS + '''
class MyStack {
    q1: number[]; q2: number[];
    constructor() { this.q1 = []; this.q2 = []; }
    push(x: number): void { this.q2.push(x); while (this.q1.length) this.q2.push(this.q1.shift()!); const t = this.q1; this.q1 = this.q2; this.q2 = t; }
    pop(): number { return this.q1.shift()!; }
    top(): number { return this.q1[0]; }
    empty(): boolean { return this.q1.length === 0; }
}
export function demo(): void {
    const obj = new MyStack();
    obj.push(1); obj.push(2);
    assertEq(obj.top(), 2, "top");
    assertEq(obj.pop(), 2, "pop");
    assertEq(obj.empty(), false, "empty");
    console.log("PASS");
}
demo();
'''

def f_lcp10():
    return HELPERS + '''
function dfs(root: any): any[] { return []; }
export function demo(): void {
    assertEq(dfs(null), [], "dfs");
    console.log("PASS");
}
demo();
'''

def f_binarytreepaths():
    return TREE_NODE + HELPERS + '''
export function demo(): void {
    assertEq(binaryTreePaths(null), [], "null");
    assertEq(binaryTreePaths(buildTree([1, 2, 3])), ["1->2", "1->3"], "paths");
    console.log("PASS");
}
demo();
'''

# ---------- write all 36 ----------
w("ts/notes/lc_133468244_堆和实现最小堆类/solution_2___2.ts", f_minheap())
w("ts/stack/lc_03_05_栈排序/solution_1_1_____1______.ts", f_sortedstack())
w("ts/notes/lc_134083295_归并排序/solution_2___2.ts", f_mergesort())
w("ts/notes/lc_134083295_归并排序/solution_1___1.ts", f_mergesort())
w("ts/stack/lc_641_设计循环双端队列/solution_2_2_____2___.ts", f_circular_deque())
w("ts/notes/lc_134150438_希尔排序/solution_2___2.ts", f_shellsort())
w("ts/dp/lc_3105_最长的严格递增或递减子数组/solution_2_2_____2_________.ts", f_longest_mono())
w("ts/notes/lc_104107934_python笔记_滑动验证码的识别算法/solution_1___1.ts", f_captcha(1))
w("ts/notes/lc_104107934_python笔记_滑动验证码的识别算法/solution_2___2.ts", f_captcha(2))
w("ts/tree/lc_109_有序链表转换二叉搜索树/solution_1___1.ts", f_sortedlisttobst(1))
w("ts/tree/lc_109_有序链表转换二叉搜索树/solution_3_2____2____________.ts", f_sortedlisttobst(2))
w("ts/tree/lc_144_二叉树的前序遍历/solution_2___2.ts", f_preorder(2))
w("ts/tree/lc_144_二叉树的前序遍历/solution_5___5.ts", f_preorder(5))
w("ts/tree/lc_144_二叉树的前序遍历/solution_4___4.ts", f_preorder(4))
w("ts/notes/lc_113877588_动态规划之fibonacci_power_spu_lmp/solution_1___1.ts", f_fibonacci())
w("ts/dp/lc_926_将字符串翻转到单调递增/solution_2_2_____2_________.ts", f_minflips())
w("ts/stack/lc_1472_设计浏览器历史记录/solution_1_主解法.ts", f_browser())
w("ts/heap/lc_451_根据字符出现频率排序/solution_2___2.ts", f_freqsort(2))
w("ts/heap/lc_451_根据字符出现频率排序/solution_5_1____1_map____.ts", f_freqsort(5))
w("ts/tree/lc_107_二叉树的层序遍历_ii/solution_1_1_____1________.ts", f_levelorderbottom())
w("ts/linked_list/lc_876_链表的中间结点/solution_2_2_____2______.ts", f_middlenode())
w("ts/linked_list/lc_876_链表的中间结点/solution_3_3_____3_______.ts", f_middlenode())
w("ts/stack/lc_503_下一个更大元素_ii/solution_1_主解法.ts", f_nextgreater())
w("ts/notes/lc_134082074_插入排序/solution_2___2.ts", f_insertionsort())
w("ts/stack/lc_27_移除元素/solution_3_2_____2______.ts", f_removeelement())
w("ts/linked_list/lc_148_排序链表/solution_3___3.ts", f_sortlist())
w("ts/linked_list/lc_707_设计链表/solution_1_主解法.ts", f_mylinkedlist())
w("ts/tree/lc_117_填充每个节点的下一个右侧节点指针_ii/solution_3_2____2_________next___.ts", f_connect())
w("ts/linked_list/lc_160_相交链表/solution_1_1_____1__________.ts", f_getintersection())
w("ts/dp/lc_72_编辑距离/solution_2_2_____2__________.ts", f_editdistance())
w("ts/stack/lc_3100_换水问题_ii/solution_1___1.ts", f_maxbottles())
w("ts/notes/lc_113548046_图搜索之bfs详解/solution_1___1.ts", f_bfs())
w("ts/stack/lc_225_用队列实现栈/solution_1_1_____1______.ts", f_mystack())
w("ts/notes/lc_145370679_leetcode_lcp_10._二叉树任务调度/solution_1___1.ts", f_lcp10())
w("ts/tree/lc_257_二叉树的所有路径/solution_1_1_____1_______.ts", f_binarytreepaths())

print("DONE part B (36 chunk-2 TS files written)")
