#!/usr/bin/env python3
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LIST_NODE = '''
class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val: number = 0, next: ListNode | null = null) {
        this.val = val;
        this.next = next;
    }
}
function buildList(vals: number[]): ListNode | null {
    const dummy = new ListNode(0);
    let cur = dummy;
    for (const v of vals) { cur.next = new ListNode(v); cur = cur.next; }
    return dummy.next;
}
function listToArr(head: ListNode | null): number[] {
    const res: number[] = [];
    while (head) { res.push(head.val); head = head.next; }
    return res;
}
'''

TREE_NODE = '''
class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
    constructor(val: number, left: TreeNode | null = null, right: TreeNode | null = null) {
        this.val = val; this.left = left; this.right = right;
    }
}
function buildTree(vals: (number | null)[]): TreeNode | null {
    if (vals.length === 0 || vals[0] === null) return null;
    const root = new TreeNode(vals[0] as number);
    const q: (TreeNode | null)[] = [root];
    let i = 1;
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
    const a = JSON.stringify(actual);
    const e = JSON.stringify(expected);
    if (a !== e) throw new Error("ASSERT FAILED " + msg + " :: actual=" + a + " expected=" + e);
}
'''

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f: f.write(content)
    print("wrote", path)

# lc_714 s1 maxProfit
c = HELPERS + '''
function maxProfit(prices: number[], fee: number): number {
    let cash = 0;
    let hold = -prices[0];
    for (let i = 1; i < prices.length; i++) {
        cash = Math.max(cash, hold + prices[i] - fee);
        hold = Math.max(hold, cash - prices[i]);
    }
    return cash;
}
export function demo(): void {
    assertEq(maxProfit([1, 3, 2, 8, 4, 9], 2), 8, "maxProfit");
    assertEq(maxProfit([1], 1), 0, "maxProfit single");
    assertEq(maxProfit([1, 2, 3, 4, 5], 1), 3, "maxProfit 2");
    console.log("PASS");
}
demo();
'''
write("ts/dp/lc_714_买卖股票的最佳时机含手续费/solution_1_1_____1______.ts", c)

# lc_347 s3 topKFrequent
c = HELPERS + '''
function topKFrequent(nums: number[], k: number): number[] {
    const freq = new Map<number, number>();
    for (const num of nums) freq.set(num, (freq.get(num) || 0) + 1);
    const heap: [number, number][] = [];
    for (const [num, cnt] of freq) {
        heap.push([cnt, num]);
        heap.sort((a, b) => a[0] - b[0]); // min-heap by cnt via sort (small n)
        if (heap.length > k) heap.shift();
    }
    return heap.map(([, num]) => num);
}
export function demo(): void {
    assertEq(topKFrequent([1, 1, 1, 2, 2, 3], 2).slice().sort((a, b) => a - b), [1, 2], "topKFrequent");
    assertEq(topKFrequent([1], 1), [1], "topKFrequent single");
    console.log("PASS");
}
demo();
'''
write("ts/heap/lc_347_前k个高频元素/solution_3___3.ts", c)

# lc_151 s1 reverseWords (split)
c = HELPERS + '''
function reverseWords(s: string): string {
    return s.trim().split(/\s+/).reverse().join(" ");
}
export function demo(): void {
    assertEq(reverseWords("the sky is blue"), "blue is sky the", "reverseWords");
    assertEq(reverseWords("abc"), "abc", "reverseWords single");
    assertEq(reverseWords("  hello   world  "), "world hello", "reverseWords spaces");
    console.log("PASS");
}
demo();
'''
write("ts/stack/lc_151_反转字符串中的单词/solution_1_1_____1________.ts", c)

# lc_151 s3 reverseWords (manual)
c = HELPERS + '''
function reverseWords(s: string): string {
    let left = 0, right = s.length - 1;
    const words: string[] = [];
    let word: string[] = [];
    while (left <= right) {
        if (s[left] === ' ' && word.length) {
            words.splice(0, 0, word.join(""));
            word = [];
        } else if (s[left] !== ' ') {
            word.push(s[left]);
        }
        left++;
    }
    if (word.length) words.splice(0, 0, word.join(""));
    return words.join(" ");
}
export function demo(): void {
    assertEq(reverseWords("the sky is blue"), "blue is sky the", "reverseWords");
    assertEq(reverseWords("abc"), "abc", "reverseWords single");
    console.log("PASS");
}
demo();
'''
write("ts/stack/lc_151_反转字符串中的单词/solution_3_3_____3______.ts", c)

# lc_71 s1 simplifyPath
c = HELPERS + '''
function simplifyPath(path: string): string {
    const stk: string[] = [];
    for (const s of path.split('/')) {
        if (!s || s === '.') continue;
        if (s !== '..') stk.push(s);
        else if (stk.length) stk.pop();
    }
    return '/' + stk.join('/');
}
export function demo(): void {
    assertEq(simplifyPath("/home/"), "/home", "simplifyPath");
    assertEq(simplifyPath("/a/./b/../../c/"), "/c", "simplifyPath2");
    assertEq(simplifyPath("/../"), "/", "simplifyPath3");
    console.log("PASS");
}
demo();
'''
write("ts/stack/lc_71_简化路径/solution_1_1_____1____.ts", c)

# lc_100 s4 isSameTree
c = TREE_NODE + HELPERS + '''
function isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {
    if (!p && !q) return true;
    if (p!.val !== q!.val) return false;
    const q1: (TreeNode | null)[] = [p];
    const q2: (TreeNode | null)[] = [q];
    while (q1.length && q2.length) {
        const pTop = q1.shift()!;
        const qTop = q2.shift()!;
        if (pTop.val !== qTop.val) return false;
        const pL = pTop.left, pR = pTop.right, qL = qTop.left, qR = qTop.right;
        if ((pL && !qL) || (!pL && qL)) return false;
        if ((pR && !qR) || (!pR && qR)) return false;
        if (pL) q1.push(pL);
        if (pR) q1.push(pR);
        if (qL) q2.push(qL);
        if (qR) q2.push(qR);
    }
    return !q1.length && !q2.length;
}
export function demo(): void {
    assertEq(isSameTree(null, null), true, "isSameTree null");
    assertEq(isSameTree(buildTree([1, 2, 3]), buildTree([1, 2, 3])), true, "isSameTree same");
    assertEq(isSameTree(buildTree([1, 2]), buildTree([1, null, 2])), false, "isSameTree diff");
    console.log("PASS");
}
demo();
'''
write("ts/tree/lc_100_相同的树/solution_4___4.ts", c)

# lc_230 s1 kthSmallest
c = TREE_NODE + HELPERS + '''
function kthSmallest(root: TreeNode | null, k: number): number {
    const stack: TreeNode[] = [];
    let cur: TreeNode | null = root;
    while (cur !== null || stack.length) {
        while (cur !== null) { stack.push(cur); cur = cur.left; }
        cur = stack.pop()!;
        k -= 1;
        if (k === 0) break;
        cur = cur.right;
    }
    return cur!.val;
}
export function demo(): void {
    const root = buildTree([3, 1, 4, null, 2]);
    assertEq(kthSmallest(root, 1), 1, "kth 1");
    assertEq(kthSmallest(root, 2), 2, "kth 2");
    assertEq(kthSmallest(root, 3), 3, "kth 3");
    assertEq(kthSmallest(root, 4), 4, "kth 4");
    console.log("PASS");
}
demo();
'''
write("ts/tree/lc_230_二叉搜索树中第_k_小的元素/solution_1_1_____1_____.ts", c)

# lc_404 s1 sumOfLeftLeaves
c = TREE_NODE + HELPERS + '''
function isLeafNode(node: TreeNode | null): boolean {
    return node !== null && node.left === null && node.right === null;
}
function sumOfLeftLeaves(root: TreeNode | null): number {
    if (!root) return 0;
    let total = 0;
    const stack: TreeNode[] = [root];
    while (stack.length) {
        const node = stack.pop()!;
        if (node.left) {
            if (isLeafNode(node.left)) total += node.left.val;
            else stack.push(node.left);
        }
        if (node.right) stack.push(node.right);
    }
    return total;
}
export function demo(): void {
    assertEq(sumOfLeftLeaves(buildTree([3, 9, 20, null, null, 15, 7])), 24, "sumOfLeftLeaves");
    assertEq(sumOfLeftLeaves(null), 0, "sumOfLeftLeaves null");
    console.log("PASS");
}
demo();
'''
write("ts/tree/lc_404_左叶子之和/solution_1_1_____1_______.ts", c)

# lc_295 s2 MedianFinder
c = HELPERS + '''
class Heap {
    heap: any[];
    compareFn: (a: any, b: any) => boolean;
    constructor(compareFn: (a: any, b: any) => boolean) { this.heap = []; this.compareFn = compareFn; }
    size(): number { return this.heap.length; }
    peek(): any { return this.heap.length ? this.heap[0] : null; }
    insert(value: any): void {
        this.heap.push(value);
        this._shiftUp(this.heap.length - 1);
    }
    pop(): any {
        if (this.heap.length === 1) return this.heap.pop();
        const first = this.heap[0];
        this.heap[0] = this.heap.pop()!;
        this._shiftDown(0);
        return first;
    }
    _shiftUp(i: number): void {
        while (i > 0 && this.compareFn(this.heap[(i - 1) >> 1], this.heap[i])) {
            const p = (i - 1) >> 1;
            [this.heap[p], this.heap[i]] = [this.heap[i], this.heap[p]];
            i = p;
        }
    }
    _shiftDown(pi: number): void {
        const size = this.heap.length;
        let largest = pi;
        const left = 2 * pi + 1, right = 2 * pi + 2;
        if (left < size && this.compareFn(this.heap[largest], this.heap[left])) largest = left;
        if (right < size && this.compareFn(this.heap[largest], this.heap[right])) largest = right;
        if (largest !== pi) {
            [this.heap[pi], this.heap[largest]] = [this.heap[largest], this.heap[pi]];
            this._shiftDown(largest);
        }
    }
}
class MinHeap extends Heap { constructor() { super((a, b) => a > b); } }
class MaxHeap extends Heap { constructor() { super((a, b) => a < b); } }
class MedianFinder {
    minHeap: MinHeap;
    maxHeap: MaxHeap;
    constructor() { this.minHeap = new MinHeap(); this.maxHeap = new MaxHeap(); }
    addNum(num: number): void {
        if (this.maxHeap.size() === 0 || num <= this.maxHeap.peek()) this.maxHeap.insert(num);
        else this.minHeap.insert(num);
        if (this.maxHeap.size() > this.minHeap.size() + 1) this.minHeap.insert(this.maxHeap.pop());
        else if (this.minHeap.size() > this.maxHeap.size()) this.maxHeap.insert(this.minHeap.pop());
    }
    findMedian(): number {
        if (this.maxHeap.size() === this.minHeap.size()) return (this.maxHeap.peek() + this.minHeap.peek()) / 2;
        return this.maxHeap.peek();
    }
}
export function demo(): void {
    const mf = new MedianFinder();
    for (const x of [1, 2, 3, 4, 5]) mf.addNum(x);
    assertEq(mf.findMedian(), 3, "MedianFinder 1..5");
    const mf2 = new MedianFinder();
    for (const x of [5, 2, 3, 4, 1]) mf2.addNum(x);
    assertEq(mf2.findMedian(), 3, "MedianFinder 5,2,3,4,1");
    const mf3 = new MedianFinder();
    mf3.addNum(1);
    assertEq(mf3.findMedian(), 1, "MedianFinder single");
    console.log("PASS");
}
demo();
'''
write("ts/heap/lc_295_数据流的中位数/solution_2_2_____2_____-___.ts", c)

# lc_208 s2 Trie
c = HELPERS + '''
class Trie {
    root: Record<string, any>;
    constructor() { this.root = {}; }
    insert(word: string): void {
        let node = this.root;
        for (const ch of word) {
            if (!(ch in node)) node[ch] = {};
            node = node[ch];
        }
        node['end'] = true;
    }
    search(word: string): boolean {
        const node = this.startsWith(word);
        return node !== false && 'end' in node && node['end'] === true;
    }
    startsWith(prefix: string): any {
        let node = this.root;
        for (const ch of prefix) {
            if (!(ch in node)) return false;
            node = node[ch];
        }
        return node;
    }
}
export function demo(): void {
    const trie = new Trie();
    trie.insert("apple");
    assertEq(trie.search("apple"), true, "search apple");
    assertEq(trie.search("app"), false, "search app");
    assertEq(trie.startsWith("app"), { l: { e: { end: true } } }, "startsWith app");
    trie.insert("app");
    assertEq(trie.search("app"), true, "search app after insert");
    console.log("PASS");
}
demo();
'''
write("ts/heap/lc_208_实现_trie_(前缀树)/solution_2_2_____2_______.ts", c)

print("DONE batch2")
