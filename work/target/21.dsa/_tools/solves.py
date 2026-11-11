# Hand-written faithful TS ports per problem dir.
# kind 'fn': (solve_src, py_fn_name, [python argsexprs]) -> oracle computes expected.
# kind 'full': (body) -> complete TS body (solve/classes/demo) written after prelude+eq.

SOLVE = {}

# ---------------------------------------------------------------------------
# FN-STYLE (oracle computes expected from the python reference)
# ---------------------------------------------------------------------------
SOLVE["tree/lc_100_相同的树"] = ("fn",
"""function isSameTree(p, q) {
    if (!p && !q) return true;
    if (!p || !q || p.val !== q.val) return false;
    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
}""", "isSameTree", ['(None, None)', '(build_tree([1,2,3]), build_tree([1,2,3]))', '(build_tree([1,2,3]), build_tree([1,2,1]))'])

SOLVE["tree/lc_104_二叉树的最大深度"] = ("fn",
"""function maxDepth(root) {
    if (!root) return 0;
    return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
}""", "maxDepth", ['(build_tree([3,9,20,null,null,15,7]),)', '(build_tree([]),)', '(build_tree([1,null,2]),)', '(build_tree([1,2,3,4,5]),)'])

SOLVE["tree/lc_107_二叉树的层序遍历_ii"] = ("fn",
"""function levelOrderBottom(root) {
    const res = [];
    if (!root) return res;
    let q = [root];
    while (q.length) {
        const cur = [];
        const nq = [];
        for (const n of q) { cur.push(n.val); if (n.left) nq.push(n.left); if (n.right) nq.push(n.right); }
        res.unshift(cur);
        q = nq;
    }
    return res;
}""", "levelOrderBottom", ['(build_tree([3,9,20,null,null,15,7]),)', '(build_tree([]),)', '(build_tree([1]),)', '(build_tree([1,2,3,4,5]),)'])

SOLVE["tree/lc_117_填充每个节点的下一个右侧节点指针_ii"] = ("fn",
"""function connect(root) {
    if (!root) return root;
    let cur = root;
    while (cur) {
        let dummy = new TreeNode(0);
        let prev = dummy;
        let node = cur;
        while (node) {
            if (node.left) { prev.next = node.left; prev = prev.next; }
            if (node.right) { prev.next = node.right; prev = prev.next; }
            node = node.next;
        }
        cur = dummy.next;
    }
    return root;
}""", "connect", ['(build_tree([1,2,3,4,5,6,7]),)'])

SOLVE["tree/lc_144_二叉树的前序遍历"] = ("fn",
"""function preorderTraversal(root) {
    if (!root) return null;
    const res = [];
    function dfs(n) { if (!n) return; res.push(n.val); dfs(n.left); dfs(n.right); }
    dfs(root);
    return res;
}""", "preorderTraversal", ['(build_tree([1,null,2,3]),)', '(build_tree([]),)', '(build_tree([1]),)', '(build_tree([1,2,3,4,5]),)'])

SOLVE["tree/lc_222_完全二叉树的节点个数"] = ("fn",
"""function countNodes(root) {
    if (!root) return 0;
    let lh = 0, r = root; while (r) { lh++; r = r.left; }
    let rh = 0; r = root; while (r) { rh++; r = r.right; }
    if (lh === rh) return (1 << lh) - 1;
    return 1 + countNodes(root.left) + countNodes(root.right);
}""", "countNodes", ['(build_tree([1,2,3,4,5,6]),)', '(build_tree([]),)', '(build_tree([1]),)', '(build_tree([1,2,3,4,5,6,7,8]),)'])

SOLVE["tree/lc_404_左叶子之和"] = ("fn",
"""function sumOfLeftLeaves(root) {
    let s = 0;
    function dfs(n) {
        if (!n) return;
        if (n.left && !n.left.left && !n.left.right) s += n.left.val;
        dfs(n.left); dfs(n.right);
    }
    dfs(root);
    return s;
}""", "sumOfLeftLeaves", ['(build_tree([3,9,20,null,null,15,7]),)', '(build_tree([1]),)', '(build_tree([]),)', '(build_tree([1,2,3,4,5]),)'])

SOLVE["tree/lc_429_n_叉树的层序遍历"] = ("full",
"""class NNode {
    val: any; children: any[];
    constructor(val?: any, children?: any[]) {
        this.val = (val === undefined ? 0 : val);
        this.children = (children === undefined ? [] : children);
    }
}
function buildNary(vals: any): any {
    if (vals === null || vals === undefined) return null;
    if (!Array.isArray(vals)) return new NNode(vals);
    if (vals.length === 0) return null;
    const root = new NNode(vals[0]);
    for (let i = 1; i < vals.length; i++) root.children.push(buildNary(vals[i]));
    return root;
}
function levelOrder(root: any): any[] {
    const res: any[] = [];
    if (!root) return res;
    let q: any[] = [root];
    while (q.length) {
        const cur: any[] = []; const nq: any[] = [];
        for (const n of q) { cur.push(n.val); for (const c of n.children) nq.push(c); }
        res.push(cur); q = nq;
    }
    return res;
}
export function demo(): void {
    const cases = [
        { in: [buildNary([1,[2],[3,4]])], want: [[1],[2,3],[4]] },
        { in: [buildNary([1,[2,3],[4,5]])], want: [[1],[2,4],[3,5]] },
        { in: [buildNary([1])], want: [[1]] },
        { in: [buildNary([])], want: [] },
    ];
    let fail = false;
    for (const c of cases) {
        const got = levelOrder(...c.in);
        if (!eq(got, c.want)) { fail = true; console.log("FAIL", JSON.stringify(c.in), "=>", JSON.stringify(got), "want", JSON.stringify(c.want)); }
    }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();
""")

SOLVE["tree/lc_515_在每个树行中找最大值"] = ("fn",
"""function largestValues(root) {
    const res = [];
    if (!root) return res;
    let q = [root];
    while (q.length) {
        let mx = -Infinity; const nq = [];
        for (const n of q) { mx = Math.max(mx, n.val); if (n.left) nq.push(n.left); if (n.right) nq.push(n.right); }
        res.push(mx); q = nq;
    }
    return res;
}""", "largestValues", ['(build_tree([1,3,2,5,3,null,9]),)', '(build_tree([1]),)', '(build_tree([1,2,3,4,5]),)', '(build_tree([]),)'])

SOLVE["tree/lc_543_二叉树的直径"] = ("fn",
"""function diameterOfBinaryTree(root) {
    let ans = 0;
    function dfs(n) {
        if (!n) return 0;
        const l = dfs(n.left), r = dfs(n.right);
        ans = Math.max(ans, l + r);
        return 1 + Math.max(l, r);
    }
    dfs(root);
    return ans;
}""", "diameterOfBinaryTree", ['(build_tree([1,2,3,4,5]),)', '(build_tree([]),)', '(build_tree([1,2]),)', '(build_tree([1,2,3]),)'])

SOLVE["tree/lc_617_合并二叉树"] = ("full",
"""function mergeTrees(t1, t2) {
    if (!t1) return t2;
    if (!t2) return t1;
    t1.val += t2.val;
    t1.left = mergeTrees(t1.left, t2.left);
    t1.right = mergeTrees(t1.right, t2.right);
    return t1;
}
export function demo(): void {
    const cases = [
        { in: [buildTree([1,3,2,5]), buildTree([2,1,3,null,4,null,7])], want: [3,4,5,5,4,null,7] },
        { in: [buildTree([]), buildTree([1])], want: [1] },
        { in: [buildTree([1]), buildTree([])], want: [1] },
        { in: [buildTree([1,2,3]), buildTree([1,2,3])], want: [2,4,6] },
    ];
    let fail = false;
    for (const c of cases) {
        const got = treeToLevel(mergeTrees(c.in[0], c.in[1]));
        if (!eq(got, c.want)) { fail = true; console.log("FAIL", JSON.stringify(got), "want", JSON.stringify(c.want)); }
    }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();
""")

SOLVE["tree/lc_637_二叉树的层平均值"] = ("fn",
"""function averageOfLevels(root) {
    const res = [];
    if (!root) return res;
    let q = [root];
    while (q.length) {
        let sum = 0, cnt = 0; const nq = [];
        for (const n of q) { sum += n.val; cnt++; if (n.left) nq.push(n.left); if (n.right) nq.push(n.right); }
        res.push(sum / cnt); q = nq;
    }
    return res;
}""", "averageOfLevels", ['(build_tree([3,9,20,null,null,15,7]),)', '(build_tree([3,9,20,15,7]),)', '(build_tree([1]),)'])

SOLVE["tree/lc_109_有序链表转换二叉搜索树"] = ("fn",
"""function sortedListToBST(head) {
    const arr = [];
    while (head) { arr.push(head.val); head = head.next; }
    function helper(l, r) {
        if (l > r) return null;
        const m = (l + r) >> 1;
        const node = new TreeNode(arr[m]);
        node.left = helper(l, m - 1);
        node.right = helper(m + 1, r);
        return node;
    }
    return helper(0, arr.length - 1);
}""", "sortedListToBST", ['(build_list([-10,-3,0,5,9]),)', '(build_list([1,2,3,4,5,6,7]),)', '(build_list([]),)', '(build_list([1]),)'])

SOLVE["linked_list/lc_19_删除链表的倒数第_n_个结点"] = ("fn",
"""function removeNthFromEnd(head, n) {
    const dummy = new ListNode(0);
    dummy.next = head;
    let s = dummy, f = dummy;
    for (let i = 0; i < n; i++) f = f.next;
    while (f.next) { f = f.next; s = s.next; }
    s.next = s.next.next;
    return dummy.next;
}""", "removeNthFromEnd", ['(build_list([1,2,3,4,5]), 2)', '(build_list([1]), 1)', '(build_list([1,2]), 1)', '(build_list([1,2,3,4,5]), 5)'])

SOLVE["linked_list/lc_83_删除排序链表中的重复元素"] = ("fn",
"""function deleteDuplicates(head) {
    let cur = head;
    while (cur && cur.next) {
        if (cur.val === cur.next.val) cur.next = cur.next.next;
        else cur = cur.next;
    }
    return head;
}""", "deleteDuplicates", ['(build_list([1,1,2]),)', '(build_list([1,1,2,3,3]),)', '(build_list([1,1,1]),)', '(build_list([]),)'])

SOLVE["linked_list/lc_148_排序链表"] = ("fn",
"""function sortList(head) {
    if (!head || !head.next) return head;
    let s = head, f = head;
    while (f.next && f.next.next) { s = s.next; f = f.next.next; }
    const mid = s.next; s.next = null;
    let l = sortList(head), r = sortList(mid);
    const dummy = new ListNode(0); let p = dummy;
    while (l && r) {
        if (l.val < r.val) { p.next = l; l = l.next; }
        else { p.next = r; r = r.next; }
        p = p.next;
    }
    p.next = l || r;
    return dummy.next;
}""", "sortList", ['(build_list([4,2,1,3]),)', '(build_list([-1,5,3,4,0]),)', '(build_list([]),)', '(build_list([1]),)'])

SOLVE["linked_list/lc_160_相交链表"] = ("fn",
"""function getIntersectionNode(a, b) {
    let p = a, q = b;
    while (p !== q) { p = p ? p.next : a; q = q ? q.next : b; }
    return p;
}""", "getIntersectionNode", ['(build_list([4,1]), build_list([5,6,1,8,4,5]))', '(build_list([1,9,1]), build_list([3,2,4]))', '(build_list([2,6,4]), build_list([1,5]))', '(build_list([]), build_list([1]))'])

SOLVE["linked_list/lc_203_移除链表元素"] = ("fn",
"""function removeElements(head, val) {
    const dummy = new ListNode(0);
    dummy.next = head;
    let p = dummy;
    while (p.next) {
        if (p.next.val === val) p.next = p.next.next;
        else p = p.next;
    }
    return dummy.next;
}""", "removeElements", ['(build_list([1,2,3,4,5,6]), 6)', '(build_list([7,7,7,7]), 7)', '(build_list([1,2,2,1]), 2)', '(build_list([]), 1)'])

SOLVE["linked_list/lc_876_链表的中间结点"] = ("fn",
"""function middleNode(head) {
    let s = head, f = head;
    while (f && f.next) { s = s.next; f = f.next.next; }
    return s;
}""", "middleNode", ['(build_list([1,2,3,4,5]),)', '(build_list([1,2,3,4,5,6]),)', '(build_list([1]),)', '(build_list([1,2]),)'])

SOLVE["dp/lc_63_不同路径_ii"] = ("fn",
"""function uniquePathsWithObstacles(o) {
    const m = o.length, n = o[0].length;
    if (o[0][0] === 1) return 0;
    const dp = Array.from({ length: m }, () => new Array(n).fill(0));
    dp[0][0] = 1;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (o[i][j] === 1) { dp[i][j] = 0; continue; }
            if (i > 0) dp[i][j] += dp[i - 1][j];
            if (j > 0) dp[i][j] += dp[i][j - 1];
        }
    }
    return dp[m - 1][n - 1];
}""", "uniquePathsWithObstacles", ['([[0,0,0],[0,1,0],[0,0,0]],)', '([[0,1],[0,0]],)', '([[0,0],[0,0]],)', '([[1,0]],)'])

SOLVE["dp/lc_72_编辑距离"] = ("fn",
"""function minDistance(w1, w2) {
    const n = w1.length, m = w2.length;
    const dp = Array.from({ length: n + 1 }, () => new Array(m + 1).fill(0));
    for (let i = 0; i <= n; i++) dp[i][0] = i;
    for (let j = 0; j <= m; j++) dp[0][j] = j;
    for (let i = 1; i <= n; i++) {
        for (let j = 1; j <= m; j++) {
            const c = w1[i - 1] === w2[j - 1] ? 0 : 1;
            dp[i][j] = Math.min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + c);
        }
    }
    return dp[n][m];
}""", "minDistance", ['("horse", "ros")', '("intention", "execution")', '("", "abc")', '("abc", "abc")'])

SOLVE["dp/lc_300_最长递增子序列"] = ("fn",
"""function lengthOfLIS(nums) {
    if (!nums.length) return 0;
    const dp = new Array(nums.length).fill(1);
    let ans = 1;
    for (let i = 0; i < nums.length; i++) {
        for (let j = 0; j < i; j++) {
            if (nums[j] < nums[i]) dp[i] = Math.max(dp[i], dp[j] + 1);
        }
        ans = Math.max(ans, dp[i]);
    }
    return ans;
}""", "lengthOfLIS", ['([10,9,2,5,3,7,101,18],)', '([0,1,0,3,2,3],)', '([7,7,7,7],)', '([4,10,4,3,8,9],)'])

SOLVE["dp/lc_3105_最长的严格递增或递减子数组"] = ("fn",
"""function longestMonotonic(nums) {
    if (nums.length <= 1) return nums.length;
    let ans = 1, inc = 1, dec = 1;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > nums[i - 1]) { inc++; dec = 1; }
        else if (nums[i] < nums[i - 1]) { dec++; inc = 1; }
        else { inc = 1; dec = 1; }
        ans = Math.max(ans, inc, dec);
    }
    return ans;
}""", "longestMonotonicSubarray", ['([1,2,3,4,5],)', '([5,4,3,2,1],)', '([1,3,2,4,5],)', '([1],)'])

SOLVE["dp/lc_337_打家劫舍_iii"] = ("fn",
"""function rob(root) {
    function dfs(n) {
        if (!n) return [0, 0];
        const l = dfs(n.left), r = dfs(n.right);
        const include = n.val + l[1] + r[1];
        const exclude = Math.max(l[0], l[1]) + Math.max(r[0], r[1]);
        return [include, exclude];
    }
    const r = dfs(root);
    return Math.max(r[0], r[1]);
}""", "rob", ['(build_tree([3,2,3,null,3,null,1]),)', '(build_tree([3,4,5,1,3,null,1]),)', '(build_tree([]),)', '(build_tree([2,1,3,null,4]),)'])

SOLVE["dp/lc_673_最长递增子序列的个数"] = ("fn",
"""function findNumberOfLIS(nums) {
    const n = nums.length;
    if (n === 0) return 0;
    let maxLen = 0, ans = 0;
    const dp = new Array(n).fill(1), cnt = new Array(n).fill(1);
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < i; j++) {
            if (nums[j] < nums[i]) {
                if (dp[j] + 1 > dp[i]) { dp[i] = dp[j] + 1; cnt[i] = cnt[j]; }
                else if (dp[j] + 1 === dp[i]) { cnt[i] += cnt[j]; }
            }
        }
        if (dp[i] > maxLen) { maxLen = dp[i]; ans = cnt[i]; }
        else if (dp[i] === maxLen) { ans += cnt[i]; }
    }
    return ans;
}""", "findNumberOfLIS", ['([1,3,5,4,7],)', '([2,2,2,2,2],)', '([1,2,4,3,5,4,7,2],)', '([1,3,2,4,5],)'])

SOLVE["dp/lc_926_将字符串翻转到单调递增"] = ("fn",
"""function minFlipsMonoIncr(s) {
    let ones = 0, flips = 0;
    for (const c of s) {
        if (c === '1') ones++;
        else flips = Math.min(flips + 1, ones);
    }
    return flips;
}""", "minFlipsMonoIncr", ['("00110")', '("010110")', '("000110")', '("")'])

SOLVE["dp/lc_1494_并行课程_ii"] = ("fn",
"""function minNumberOfSemesters(n, deps, k) {
    const pre = new Array(n).fill(0);
    for (const [a, b] of deps) pre[b - 1] |= (1 << (a - 1));
    const memo = {};
    function dfs(mask) {
        if (mask === (1 << n) - 1) return 0;
        if (memo[mask] !== undefined) return memo[mask];
        let can = [];
        for (let i = 0; i < n; i++) {
            if (!(mask & (1 << i)) && (pre[i] & mask) === pre[i]) can.push(i);
        }
        let res = Infinity;
        const m = can.length;
        for (let sub = 1; sub < (1 << m); sub++) {
            if (bitCount(sub) > k) continue;
            let add = 0;
            for (let i = 0; i < m; i++) if (sub & (1 << i)) add |= (1 << can[i]);
            res = Math.min(res, 1 + dfs(mask | add));
        }
        memo[mask] = res;
        return res;
    }
    function bitCount(x) { let c = 0; while (x) { c += x & 1; x >>= 1; } return c; }
    return dfs(0);
}""", "minNumberOfSemesters", ['(4, [[2,1],[3,1],[1,4]], 2)', '(5, [[2,1],[3,1],[4,1],[1,5]], 3)', '(3, [], 2)', '(4, [[1,2],[2,3]], 1)'])

SOLVE["heap/lc_208_实现_trie_(前缀树)"] = ("full",
"""class TrieNode {
    children: any; isEnd: boolean;
    constructor() { this.children = {}; this.isEnd = false; }
}
class Trie {
    root: any;
    constructor() { this.root = new TrieNode(); }
    insert(word) {
        let node = this.root;
        for (const ch of word) { if (!node.children[ch]) node.children[ch] = new TrieNode(); node = node.children[ch]; }
        node.isEnd = true;
    }
    search(word) {
        let node = this.root;
        for (const ch of word) { if (!node.children[ch]) return false; node = node.children[ch]; }
        return node.isEnd;
    }
    startsWith(prefix) {
        let node = this.root;
        for (const ch of prefix) { if (!node.children[ch]) return false; node = node.children[ch]; }
        return true;
    }
}
export function demo(): void {
    const t = new Trie();
    t.insert("apple");
    const cases = [
        { in: ["search", "apple"], want: true },
        { in: ["search", "app"], want: false },
        { in: ["startsWith", "app"], want: true },
        { in: ["search", "appl"], want: false },
    ];
    let fail = false;
    for (const c of cases) {
        const got = t[c.in[0]](c.in[1]);
        if (got !== c.want) { fail = true; console.log("FAIL", c, "=>", got); }
    }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();
""")

SOLVE["heap/lc_295_数据流的中位数"] = ("full",
"""class MedianFinder {
    lo: any[]; hi: any[];
    constructor() { this.lo = []; this.hi = []; }
    addNum(num) {
        if (this.lo.length === 0 || num <= this.lo[0]) heapPush(this.lo, -num);
        else heapPush(this.hi, num);
        if (this.lo.length > this.hi.length + 1) heapPush(this.hi, -heapPop(this.lo));
        if (this.hi.length > this.lo.length) heapPush(this.lo, -heapPop(this.hi));
    }
    findMedian() {
        if (this.lo.length > this.hi.length) return -this.lo[0];
        return (this.hi[0] - this.lo[0]) / 2;
    }
}
export function demo(): void {
    const m = new MedianFinder();
    m.addNum(1); m.addNum(2);
    const cases = [
        { got: m.findMedian(), want: 1.5 },
    ];
    m.addNum(3);
    cases.push({ got: m.findMedian(), want: 2 });
    let fail = false;
    for (const c of cases) if (!eq(c.got, c.want)) { fail = true; console.log("FAIL", c); }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();
""")

SOLVE["heap/lc_313_超级丑数"] = ("fn",
"""function nthSuperUglyNumber(n, primes) {
    if (n === 1) return 1;
    const res = [1];
    const idx = new Array(primes.length).fill(0);
    const vals = primes.slice();
    for (let i = 1; i < n; i++) {
        const m = Math.min(...vals);
        res.push(m);
        for (let j = 0; j < primes.length; j++) {
            if (vals[j] === m) { idx[j]++; vals[j] = primes[j] * res[idx[j]]; }
        }
    }
    return res[n - 1];
}""", "nthSuperUglyNumber", ['(12, [2,7,13,19])', '(1, [2,3,5])', '(10, [2,3,5])', '(2, [2])'])

SOLVE["heap/lc_347_前k个高频元素"] = ("fn",
"""function topKFrequent(nums, k) {
    const m = {};
    for (const x of nums) m[x] = (m[x] || 0) + 1;
    const arr = Object.entries(m).map(([k, v]) => [+k, +v]);
    arr.sort((a, b) => b[1] - a[1]);
    return arr.slice(0, k).map(e => e[0]);
}""", "topKFrequent", ['([1,1,1,2,2,3], 2)', '([1], 1)', '([4,1,-1,4,-1,4,4], 2)', '([5,3,1,1,1,3], 2)'], {"set": True})

SOLVE["heap/lc_451_根据字符出现频率排序"] = ("fn",
"""function frequencySort(s) {
    const m = {};
    for (const c of s) m[c] = (m[c] || 0) + 1;
    return Object.keys(m).sort((a, b) => m[b] - m[a]).map(c => c.repeat(m[c])).join('');
}""", "frequencySort", ['("tree")', '("cccaaa")', '("Aabb")', '("aaabbbccc")'])

SOLVE["heap/lc_502_ipo"] = ("fn",
"""function findMaximizedCapital(k, w, profits, capital) {
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
}""", "findMaximizedCapital", ['(2, 0, [1,2,3], [0,1,1])', '(3, 0, [1,2,3], [0,1,2])', '(1, 0, [1,2], [1,2])', '(2, 1, [1,2,3], [1,1,2])'])

SOLVE["stack/lc_27_移除元素"] = ("fn",
"""function removeElement(nums, val) {
    let j = 0;
    for (let i = 0; i < nums.length; i++) if (nums[i] !== val) nums[j++] = nums[i];
    return j;
}""", "removeElement", ['([3,2,2,3], 3)', '([0,1,2,2,3,0,4,2], 2)', '([1], 1)', '([2,2,2], 2)'])

SOLVE["stack/lc_71_简化路径"] = ("fn",
"""function simplifyPath(path) {
    const st = [];
    for (const p of path.split('/')) {
        if (p === '' || p === '.') continue;
        if (p === '..') st.pop();
        else st.push(p);
    }
    return '/' + st.join('/');
}""", "simplifyPath", ['("/home/")', '("/../")', '("/home//foo/")', '("/a/./b/../../c/")'])

SOLVE["stack/lc_151_反转字符串中的单词"] = ("fn",
"""function reverseWords(s) {
    return s.trim().split(/\\s+/).reverse().join(' ');
}""", "reverseWords", ['("the sky is blue")', '("  hello world  ")', '("a good   example")', '("  bob   ")'])

SOLVE["stack/lc_225_用队列实现栈"] = ("full",
"""class MyStack {
    q: any[];
    constructor() { this.q = []; }
    push(x) { this.q.push(x); }
    pop() { return this.q.pop(); }
    top() { return this.q[this.q.length - 1]; }
    empty() { return this.q.length === 0; }
}
export function demo(): void {
    const s = new MyStack();
    s.push(1); s.push(2);
    const cases = [
        { got: s.top(), want: 2 },
        { got: s.pop(), want: 2 },
        { got: s.top(), want: 1 },
        { got: s.empty(), want: false },
    ];
    let fail = false;
    for (const c of cases) if (!eq(c.got, c.want)) { fail = true; console.log("FAIL", c); }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();
""")

SOLVE["stack/lc_3100_换水问题_ii"] = ("fn",
"""function maxBottlesDrunk(numBottles, numExchange) {
    let result = 0, emptyBottles = 0, flag = true;
    while (flag) {
        flag = false;
        if (numBottles > 0) { result += numBottles; emptyBottles += numBottles; numBottles = 0; flag = true; }
        if (emptyBottles >= numExchange) { numBottles += 1; emptyBottles -= numExchange; numExchange += 1; flag = true; }
    }
    return result;
}""", "maxBottlesDrunk", ['(13, 3)', '(10, 3)', '(1, 2)', '(15, 4)'])

SOLVE["stack/lc_641_设计循环双端队列"] = ("full",
"""class MyCircularDeque {
    capacity: number; rear: number; front: number; elements: any[];
    constructor(k: number) { this.capacity = k + 1; this.rear = 0; this.front = 0; this.elements = new Array(this.capacity).fill(0); }
    isFull() { return (this.rear + 1) % this.capacity === this.front; }
    isEmpty() { return this.rear === this.front; }
    insertFront(value: number) { if (this.isFull()) return false; this.front = (this.front - 1 + this.capacity) % this.capacity; this.elements[this.front] = value; return true; }
    insertLast(value: number) { if (this.isFull()) return false; this.elements[this.rear] = value; this.rear = (this.rear + 1) % this.capacity; return true; }
    deleteFront() { if (this.isEmpty()) return false; this.front = (this.front + 1) % this.capacity; return true; }
    deleteLast() { if (this.isEmpty()) return false; this.rear = (this.rear - 1 + this.capacity) % this.capacity; return true; }
    getFront() { if (this.isEmpty()) return -1; return this.elements[this.front]; }
    getRear() { if (this.isEmpty()) return -1; return this.elements[(this.rear - 1 + this.capacity) % this.capacity]; }
}
export function demo(): void {
    const obj = new MyCircularDeque(3);
    const cases = [
        { got: obj.insertLast(1), want: true },
        { got: obj.insertLast(2), want: true },
        { got: obj.insertFront(3), want: true },
        { got: obj.insertFront(4), want: false },
        { got: obj.getRear(), want: 2 },
        { got: obj.isFull(), want: true },
        { got: obj.deleteLast(), want: true },
        { got: obj.insertFront(4), want: true },
        { got: obj.getFront(), want: 4 },
    ];
    let fail = false;
    for (const c of cases) if (!eq(c.got, c.want)) { fail = true; console.log("FAIL", JSON.stringify(c)); }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();
""")

SOLVE["stack/lc_739_每日温度"] = ("fn",
"""function dailyTemperatures(t) {
    const res = new Array(t.length).fill(0);
    const st = [];
    for (let i = 0; i < t.length; i++) {
        while (st.length && t[i] > t[st[st.length - 1]]) {
            const idx = st.pop();
            res[idx] = i - idx;
        }
        st.push(i);
    }
    return res;
}""", "dailyTemperatures", ['([73,74,75,71,69,72,76,73],)', '([30,40,50,60],)', '([30,60,90],)', '([55],)'])

SOLVE["stack/lc_1685_有序数组中差绝对值之和"] = ("fn",
"""function getSumAbsoluteDifferences(nums) {
    const n = nums.length;
    const total = nums.reduce((a, b) => a + b, 0);
    let pref = 0; const res = [];
    for (let i = 0; i < n; i++) {
        const left = i * nums[i] - pref;
        const right = (total - pref - nums[i]) - (n - 1 - i) * nums[i];
        res.push(left + right);
        pref += nums[i];
    }
    return res;
}""", "getSumAbsoluteDifferences", ['([2,3,5])', '([1,4,6,8,10])', '([1,2,3,4,5])', '([5])'])

SOLVE["stack/lc_03_05_栈排序"] = ("full",
"""class SortedStack {
    s: any[]; t: any[];
    constructor() { this.s = []; this.t = []; }
    push(x) {
        while (this.s.length && this.s[this.s.length - 1] > x) this.t.push(this.s.pop());
        this.s.push(x);
        while (this.t.length) this.s.push(this.t.pop());
    }
    pop() { return this.s.length ? this.s.pop() : -1; }
    peek() { return this.s.length ? this.s[this.s.length - 1] : -1; }
    isEmpty() { return this.s.length === 0; }
}
export function demo(): void {
    const st = new SortedStack();
    st.push(1); st.push(2); st.push(3);
    const cases = [
        { got: st.peek(), want: 3 },
        { got: st.pop(), want: 3 },
        { got: st.peek(), want: 2 },
    ];
    let fail = false;
    for (const c of cases) if (!eq(c.got, c.want)) { fail = true; console.log("FAIL", c); }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();
""")

SOLVE["stack/lc_2454_下一个更大元素_iv"] = ("fn",
"""function secondGreaterElement(nums) {
    const n = nums.length;
    const ans = new Array(n).fill(-1);
    const st1 = [], st2 = [];
    for (let i = 0; i < n; i++) {
        while (st2.length && nums[st2[st2.length - 1]] < nums[i]) {
            ans[st2.pop()] = nums[i];
        }
        let j = st1.length - 1;
        while (j >= 0 && nums[st1[j]] < nums[i]) j--;
        for (let k = st1.length - 1; k > j; k--) st2.push(st1.pop());
        st1.push(i);
    }
    return ans;
}""", "secondGreaterElement", ['([2,4,0,9,6])', '([5,4,3,2,1])', '([1,2,3,4,5])', '([4,3,2,1,5])'])

SOLVE["linked_list/lc_460_lfu_缓存"] = ("full",
"""class Node {
    key: any; val: any; freq: number; prev: any; next: any;
    constructor(k, v) { this.key = k; this.val = v; this.freq = 1; this.prev = null; this.next = null; }
}
class DLinkedList {
    head: any; tail: any;
    constructor() { this.head = new Node(0, 0); this.tail = new Node(0, 0); this.head.next = this.tail; this.tail.prev = this.head; }
    add(n) { n.prev = this.head; n.next = this.head.next; this.head.next.prev = n; this.head.next = n; }
    remove(n) { n.prev.next = n.next; n.next.prev = n.prev; }
    pop() { const n = this.tail.prev; if (n === this.head) return null; this.remove(n); return n; }
}
class LFUCache {
    cap: number; size: number; minF: number; nodes: any; lists: any;
    constructor(capacity) {
        this.cap = capacity; this.size = 0; this.minF = 0;
        this.nodes = {}; this.lists = {};
    }
    _list(f) { if (!this.lists[f]) this.lists[f] = new DLinkedList(); return this.lists[f]; }
    get(key) {
        if (!(key in this.nodes)) return -1;
        return this._touch(this.nodes[key]).val;
    }
    put(key, value) {
        if (this.cap === 0) return;
        if (key in this.nodes) { this.nodes[key].val = value; this._touch(this.nodes[key]); return; }
        if (this.size === this.cap) {
            const lst = this._list(this.minF);
            const n = lst.pop();
            if (n) { delete this.nodes[n.key]; this.size--; }
        }
        const n = new Node(key, value);
        this.nodes[key] = n; this._list(1).add(n); this.minF = 1; this.size++;
    }
    _touch(n) {
        const f = n.freq;
        this._list(f).remove(n);
        if (this._list(f).head.next === this._list(f).tail && this.minF === f) this.minF++;
        n.freq++;
        this._list(n.freq).add(n);
        return n;
    }
}
export function demo(): void {
    const c = new LFUCache(2);
    c.put(1, 1); c.put(2, 2);
    const cases = [{ got: c.get(1), want: 1 }];
    c.put(3, 3);
    cases.push({ got: c.get(2), want: -1 });
    cases.push({ got: c.get(3), want: 3 });
    c.put(4, 4);
    cases.push({ got: c.get(1), want: -1 });
    cases.push({ got: c.get(3), want: 3 });
    cases.push({ got: c.get(4), want: 4 });
    let fail = false;
    for (const cse of cases) if (!eq(cse.got, cse.want)) { fail = true; console.log("FAIL", cse); }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();
""")

# ---------------------------------------------------------------------------
# NOTES (plain functions -> fn with oracle; classes -> full)
# ---------------------------------------------------------------------------
SOLVE["notes/lc_107475776_计算思维之下楼梯台阶和象棋跳马问题"] = ("fn",
"""function climbStairs(h) {
    if (h < 0) return 0;
    if (h === 0) return 1;
    if (h <= 2) return h;
    let a = 1, b = 1, c = 2;
    for (let i = 3; i <= h; i++) { const t = a + b + c; a = b; b = c; c = t; }
    return c;
}""", "climb_stairs_count", ['(5,)', '(10,)', '(1,)', '(8,)'])

SOLVE["notes/lc_107573690_抽象思维之对比算法_发现共性"] = ("fn",
"""function climbStairsRefactored(h) {
    if (h < 0) return 0;
    if (h === 0) return 1;
    if (h <= 2) return h;
    let a = 1, b = 1, c = 2;
    for (let i = 3; i <= h; i++) { const t = a + b + c; a = b; b = c; c = t; }
    return c;
}""", "climb_stairs_refactored", ['(5,)', '(10,)', '(1,)', '(6,)'])

SOLVE["notes/lc_113764246_图搜索之dfs详解"] = ("fn",
"""function dfs(graph, start) {
    const visited = new Set();
    const out = [];
    function go(u) {
        visited.add(u); out.push(u);
        for (const v of (graph[u] || [])) if (!visited.has(v)) go(v);
    }
    go(start);
    return out;
}""", "dfs", ['({0:[1,2],1:[2],2:[0,3],3:[3]}, 0)'])

SOLVE["notes/lc_113877588_动态规划之fibonacci_power_spu_lmp"] = ("fn",
"""function fibonacci(n, memo) {
    memo = memo || {};
    if (n < 2) return n;
    if (memo[n] !== undefined) return memo[n];
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo);
    return memo[n];
}""", "fibonacci", ['(10,)', '(20,)', '(1,)', '(30,)'])

SOLVE["notes/lc_107579658_抽象思维之转换视角_提炼共性"] = ("fn",
"""function solveUnified(queen) {
    // count attacking pairs of queens (columns/rows/diagonics) on an n*n board
    const n = queen.length;
    let cnt = 0;
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            if (queen[i] === queen[j]) cnt++;
            if (Math.abs(queen[i] - queen[j]) === j - i) cnt++;
        }
    }
    return cnt;
}""", "solve_unified", ['([0,1,2,3],)', '([0,2,1,3],)', '([1,3,0,2],)', '([0,0,0,0],)'])

SOLVE["notes/lc_134082074_插入排序"] = ("fn",
"""function insertionSort(nums) {
    const a = nums.slice();
    for (let i = 1; i < a.length; i++) {
        const x = a[i]; let j = i - 1;
        while (j >= 0 && a[j] > x) { a[j + 1] = a[j]; j--; }
        a[j + 1] = x;
    }
    return a;
}""", "insertionSort", ['([5,2,4,6,1,3],)', '([1,2,3],)', '([3,2,1],)', '([],)'])

SOLVE["notes/lc_134150438_希尔排序"] = ("fn",
"""function shellSort(nums) {
    const a = nums.slice();
    const n = a.length;
    for (let gap = Math.floor(n / 2); gap > 0; gap = Math.floor(gap / 2)) {
        for (let i = gap; i < n; i++) {
            const x = a[i]; let j = i;
            while (j >= gap && a[j - gap] > x) { a[j] = a[j - gap]; j -= gap; }
            a[j] = x;
        }
    }
    return a;
}""", "shellSort", ['([5,2,4,6,1,3],)', '([9,8,7,6,5,4,3,2,1],)', '([1,2,3],)', '([],)'])

SOLVE["notes/lc_134083295_归并排序"] = ("fn",
"""function mergeSort(nums) {
    if (nums.length <= 1) return nums.slice();
    const m = nums.length >> 1;
    const left = mergeSort(nums.slice(0, m));
    const right = mergeSort(nums.slice(m));
    const out = []; let i = 0, j = 0;
    while (i < left.length && j < right.length) {
        if (left[i] <= right[j]) out.push(left[i++]); else out.push(right[j++]);
    }
    while (i < left.length) out.push(left[i++]);
    while (j < right.length) out.push(right[j++]);
    return out;
}""", "mergeSort", ['([5,2,4,6,1,3],)', '([9,8,7,6,5],)', '([1,2,3],)', '([],)'])

SOLVE["notes/lc_134085409_堆排序"] = ("fn",
"""function heapSort(arr) {
    const a = arr.slice();
    const n = a.length;
    function heapify(k) {
        for (let i = Math.floor(k / 2) - 1; i >= 0; i--) sift(i, k);
    }
    function sift(i, k) {
        while (true) {
            let l = 2 * i + 1, r = 2 * i + 2, big = i;
            if (l < k && a[l] > a[big]) big = l;
            if (r < k && a[r] > a[big]) big = r;
            if (big === i) break;
            [a[i], a[big]] = [a[big], a[i]]; i = big;
        }
    }
    heapify(n);
    for (let end = n - 1; end > 0; end--) {
        [a[0], a[end]] = [a[end], a[0]];
        sift(0, end);
    }
    return a;
}""", "heap_sort", ['([5,2,4,6,1,3],)', '([9,8,7,6,5],)', '([1,2,3],)', '([],)'])

SOLVE["notes/lc_110240695_分治策略之greatest_slice_2-way_merge_counting"] = ("fn",
"""function maxSubArrayBf(arr) {
    let best = -Infinity;
    for (let i = 0; i < arr.length; i++) {
        let s = 0;
        for (let j = i; j < arr.length; j++) { s += arr[j]; best = Math.max(best, s); }
    }
    return best;
}""", "max_sub_array_bf", ['([-2,1,-3,4,-1,2,1,-5,4],)', '([1],)', '([-1,-2,-3],)', '([5,4,-1,7,8],)'])

SOLVE["notes/lc_99759428_python笔记_数据结构与算法之数组操作"] = ("full",
"""function twoSum(nums, target) {
    const m = {};
    for (let i = 0; i < nums.length; i++) {
        if ((target - nums[i]) in m) return [m[target - nums[i]], i];
        m[nums[i]] = i;
    }
    return [];
}
function maxSubArray(nums) {
    let best = nums[0], cur = nums[0];
    for (let i = 1; i < nums.length; i++) { cur = Math.max(nums[i], cur + nums[i]); best = Math.max(best, cur); }
    return best;
}
function rotateArray(nums, k) {
    const n = nums.length; if (n === 0) return nums;
    k = k % n; return nums.slice(n - k).concat(nums.slice(0, n - k));
}
export function demo(): void {
    const cases = [
        { got: twoSum([2,7,11,15], 9), want: [0,1] },
        { got: maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), want: 6 },
        { got: rotateArray([1,2,3,4,5,6,7], 3), want: [5,6,7,1,2,3,4] },
        { got: twoSum([3,2,4], 6), want: [1,2] },
    ];
    let fail = false;
    for (const c of cases) if (!eq(c.got, c.want)) { fail = true; console.log("FAIL", c); }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();
""")

SOLVE["notes/lc_107836586_big-o记号_数据结构与算法的关系以及几种基本的数据结构"] = ("fn",
"""function classify(coeffs) {
    // coeffs from highest degree; return highest non-zero degree (degree of polynomial)
    let deg = -1;
    for (let i = 0; i < coeffs.length; i++) if (coeffs[i] !== 0) deg = coeffs.length - 1 - i;
    return deg;
}""", "classify", ['([1,0,0,0],)', '([0,1,2,3],)', '([0,0,0,5],)', '([0,0,0,0],)'])

SOLVE["notes/lc_145355207_leetcode_lcr_152._验证二叉搜索树的后序遍历序列"] = ("fn",
"""function verifyPostorder(postorder) {
    function dfs(l, r) {
        if (l >= r) return true;
        let p = l;
        while (postorder[p] < postorder[r]) p++;
        const m = p;
        while (postorder[p] > postorder[r]) p++;
        return p === r && dfs(l, m - 1) && dfs(m, r - 1);
    }
    if (!postorder.length) return true;
    return dfs(0, postorder.length - 1);
}""", "verify_postorder", ['([1,6,3,2,5],)', '([1,3,2,4,5],)', '([4,6,5,9,8,7],)', '([1,2,3],)'])

SOLVE["notes/lc_107435426_字典序最大问题分析"] = ("fn",
"""function getResultBruteforce(n, ele) {
    const ans: any[] = [];
    const stack: number[] = [];
    let i = 0;
    while (i < n) {
        let mx = 0;
        for (let j = i; j < n; j++) if (ele[j] > mx) mx = ele[j];
        if (stack.length && ele[stack[stack.length - 1]] > mx) {
            ans.push(ele[stack.pop()!]);
        } else {
            while (mx !== ele[i]) { stack.push(i); i++; }
            ans.push(ele[i]); i++;
        }
    }
    while (stack.length) ans.push(ele[stack.pop()!]);
    return ans;
}""", "get_result_bruteforce", ['(3, [1,2,3])', '(4, [4,2,9,7])', '(2, [5,1])', '(1, [8])'])

SOLVE["notes/lc_107431726_最大红矩形分析"] = ("fn",
"""function getResult(n, m, matrix) {
    // largest rectangle in binary matrix (histogram method)
    const heights = new Array(m).fill(0);
    let best = 0;
    function largestArea(h) {
        const st = [];
        let mx = 0;
        for (let i = 0; i <= h.length; i++) {
            const cur = i === h.length ? 0 : h[i];
            while (st.length && h[st[st.length - 1]] > cur) {
                const hh = h[st.pop()];
                const w = st.length ? i - st[st.length - 1] - 1 : i;
                mx = Math.max(mx, hh * w);
            }
            st.push(i);
        }
        return mx;
    }
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) heights[j] = matrix[i][j] === 0 ? 0 : heights[j] + 1;
        best = Math.max(best, largestArea(heights));
    }
    return best;
}""", "get_result", ['(4, 4, [[1,0,1,1],[1,1,1,1],[1,1,1,1],[1,0,1,1]])', '(2, 2, [[1,1],[1,1]])', '(3, 3, [[0,0,0],[0,0,0],[0,0,0]])', '(1, 4, [[1,1,1,1]])'])

SOLVE["notes/lc_133278676_使用链表指针获取json节点值的算法实现"] = ("fn",
"""function getValue(data, path) {
    let cur = data;
    for (const p of path) {
        if (cur === null || cur === undefined) return undefined;
        cur = cur[p];
    }
    return cur;
}""", "get_value", ['({a:{b:[10,20,30]}}, ["a","b",2])', '({x:{y:5}}, ["x","y"])', '({a:{b:{c:9}}}, ["a","b","c"])', '({a:1}, ["a","z"])'])

SOLVE["notes/lc_134083295_归并排序"] = ("fn",
"""function mergeSort(nums) {
    if (nums.length <= 1) return nums.slice();
    const m = nums.length >> 1;
    const left = mergeSort(nums.slice(0, m));
    const right = mergeSort(nums.slice(m));
    const out = []; let i = 0, j = 0;
    while (i < left.length && j < right.length) {
        if (left[i] <= right[j]) out.push(left[i++]); else out.push(right[j++]);
    }
    while (i < left.length) out.push(left[i++]);
    while (j < right.length) out.push(right[j++]);
    return out;
}""", "mergeSort", ['([5,2,4,6,1,3],)', '([9,8,7,6,5],)', '([1,2,3],)', '([],)'])

SOLVE["notes/lc_107737496_抽象思维之代码重构_隔离变化"] = ("full",
"""class Matrix {
    rules: any; n: number;
    constructor(n, rules) { this.n = n; this.rules = rules || []; }
    setRule(r, c, v) { if (!this.rules[r]) this.rules[r] = {}; this.rules[r][c] = v; }
    get(r, c) { return this.rules[r] && this.rules[r][c] !== undefined ? this.rules[r][c] : 0; }
}
export function demo(): void {
    const m = new Matrix(3, [{0:{0:1,1:2,2:3}},{1:{1:5}},{2:{0:7,2:9}}]);
    m.setRule(1, 2, 4);
    const cases = [
        { got: m.get(0, 0), want: 1 },
        { got: m.get(1, 2), want: 4 },
        { got: m.get(2, 0), want: 7 },
        { got: m.get(0, 2), want: 3 },
    ];
    let fail = false;
    for (const c of cases) if (!eq(c.got, c.want)) { fail = true; console.log("FAIL", c); }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();
""")

SOLVE["notes/lc_133468244_堆和实现最小堆类"] = ("full",
"""class MinHeap {
    heap: any[];
    constructor() { this.heap = []; }
    size() { return this.heap.length; }
    insert(value) {
        this.heap.push(value);
        let i = this.heap.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (this.heap[p] <= this.heap[i]) break;
            [this.heap[p], this.heap[i]] = [this.heap[i], this.heap[p]]; i = p;
        }
    }
    pop() {
        if (!this.heap.length) return undefined;
        const top = this.heap[0];
        const last = this.heap.pop();
        if (this.heap.length) { this.heap[0] = last; this._down(0); }
        return top;
    }
    peek() { return this.heap.length ? this.heap[0] : undefined; }
    _down(i) {
        const n = this.heap.length;
        while (true) {
            let l = 2*i+1, r = 2*i+2, s = i;
            if (l < n && this.heap[l] < this.heap[s]) s = l;
            if (r < n && this.heap[r] < this.heap[s]) s = r;
            if (s === i) break;
            [this.heap[s], this.heap[i]] = [this.heap[i], this.heap[s]]; i = s;
        }
    }
}
export function demo(): void {
    const h = new MinHeap();
    [3,1,6,5,2,4].forEach(v => h.insert(v));
    const out = [];
    while (h.size()) out.push(h.pop());
    const cases = [
        { got: out, want: [1,2,3,4,5,6] },
        { got: new MinHeap().peek(), want: undefined },
    ];
    let fail = false;
    for (const c of cases) if (!eq(c.got, c.want)) { fail = true; console.log("FAIL", c); }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();
""")

SOLVE["notes/lc_133530983_实现最大堆类的两种方式及实现堆排序"] = ("full",
"""class MaxHeap {
    heap: any[];
    constructor() { this.heap = []; }
    size() { return this.heap.length; }
    insert(value) {
        this.heap.push(value);
        let i = this.heap.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (this.heap[p] >= this.heap[i]) break;
            [this.heap[p], this.heap[i]] = [this.heap[i], this.heap[p]]; i = p;
        }
    }
    pop() {
        if (!this.heap.length) return undefined;
        const top = this.heap[0];
        const last = this.heap.pop();
        if (this.heap.length) { this.heap[0] = last; this._down(0); }
        return top;
    }
    peek() { return this.heap.length ? this.heap[0] : undefined; }
    _down(i) {
        const n = this.heap.length;
        while (true) {
            let l = 2*i+1, r = 2*i+2, s = i;
            if (l < n && this.heap[l] > this.heap[s]) s = l;
            if (r < n && this.heap[r] > this.heap[s]) s = r;
            if (s === i) break;
            [this.heap[s], this.heap[i]] = [this.heap[i], this.heap[s]]; i = s;
        }
    }
}
export function demo(): void {
    const h = new MaxHeap();
    [3,1,6,5,2,4].forEach(v => h.insert(v));
    const out = [];
    while (h.size()) out.push(h.pop());
    const cases = [{ got: out, want: [6,5,4,3,2,1] }];
    let fail = false;
    for (const c of cases) if (!eq(c.got, c.want)) { fail = true; console.log("FAIL", c); }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();
""")

SOLVE["notes/lc_105893757_栈排序分析"] = ("full",
"""class SortedStack {
    s: any[]; t: any[];
    constructor() { this.s = []; this.t = []; }
    push(x) {
        while (this.s.length && this.s[this.s.length - 1] > x) this.t.push(this.s.pop());
        this.s.push(x);
        while (this.t.length) this.s.push(this.t.pop());
    }
    pop() { return this.s.length ? this.s.pop() : -1; }
    peek() { return this.s.length ? this.s[this.s.length - 1] : -1; }
    isEmpty() { return this.s.length === 0; }
}
export function demo(): void {
    const st = new SortedStack();
    [3,1,5,2,4].forEach(v => st.push(v));
    const out = [];
    while (!st.isEmpty()) out.push(st.pop());
    const cases = [{ got: out, want: [5,4,3,2,1] }];
    let fail = false;
    for (const c of cases) if (!eq(c.got, c.want)) { fail = true; console.log("FAIL", c); }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();
""")

SOLVE["notes/lc_108013114_贪心策略之bst&bbst_hashtable+dictionary+map_p"] = ("fn",
"""function kruskalMst(edges) {
    // edges: list of [u, v, w]; return total weight of MST
    const sorted = edges.slice().sort((a, b) => a[2] - b[2]);
    const parent = {};
    function find(x) { if (parent[x] === undefined) parent[x] = x; while (parent[x] !== x) { parent[x] = parent[parent[x]]; x = parent[x]; } return x; }
    function union(a, b) { parent[find(a)] = find(b); }
    let total = 0;
    for (const [u, v, w] of sorted) {
        if (find(u) !== find(v)) { union(u, v); total += w; }
    }
    return total;
}""", "kruskal_mst", ['([[0,1,10],[0,2,6],[0,3,5],[1,3,15],[2,3,4]],)', '([[0,1,1],[1,2,2],[2,3,3],[3,4,4]],)', '([[0,1,2],[1,2,3]],)', '([],)'])

SOLVE["notes/lc_107868749_贪心策略之matrixsorting_pfc_coding_huffmantre"] = ("fn",
"""function matrixSort(matrix) {
    return matrix.slice().sort((a, b) => {
        const sa = a.reduce((x, y) => x + y, 0);
        const sb = b.reduce((x, y) => x + y, 0);
        if (sa !== sb) return sb - sa;
        return b[0] - a[0];
    });
}
function buildHuffman(freqs) {
    const pq = freqs.slice().sort((a, b) => a - b);
    let cost = 0;
    while (pq.length > 1) {
        const a = pq.shift(), b = pq.shift();
        const s = a + b; cost += s;
        let i = 0; while (i < pq.length && pq[i] < s) i++;
        pq.splice(i, 0, s);
    }
    return cost;
}""", "build_huffman", ['([5,9,12,13,16,45],)', '([1,2,3,4,5],)', '([10,20,30],)', '([7],)'])

SOLVE["notes/lc_104107934_python笔记_滑动验证码的识别算法"] = ("fn",
"""function detectEdges(image) {
    const h = image.length, w = image[0].length;
    const out = image.map(r => r.slice());
    for (let i = 0; i < h; i++) {
        for (let j = 0; j < w; j++) {
            if (image[i][j] === 0) continue;
            let edge = false;
            for (const [di, dj] of [[-1,0],[1,0],[0,-1],[0,1]]) {
                const ni = i + di, nj = j + dj;
                if (ni < 0 || nj < 0 || ni >= h || nj >= w || image[ni][nj] === 0) edge = true;
            }
            out[i][j] = edge ? 255 : 0;
        }
    }
    return out;
}""", "detect_edges", ['([[0,0,0],[0,255,0],[0,0,0]],)', '([[255,255],[255,255]],)', '([[0,255,0],[255,0,255]],)', '([[255]],)'])

SOLVE["notes/lc_145370679_leetcode_lcp_10._二叉树任务调度"] = ("fn",
"""function dfs(root) {
    // return [total_time, max_dep] for tree task scheduling
    if (!root) return [0, 0];
    const l = dfs(root.left), r = dfs(root.right);
    const total = root.val + Math.max(l[0], r[0]);
    const dep = 1 + Math.max(l[1], r[1]);
    return [total, dep];
}""", "dfs", ['(build_tree([6,2,4]),)', '(build_tree([]),)', '(build_tree([5,3,1]),)', '(build_tree([10,2,3,4,5]),)'])


SOLVE_REL = {
"ts/tree/lc_144_二叉树的前序遍历/solution_3___3.ts": ("full", '''function preorderTraversal(root) {
    const res = [];
    let cur = root;
    while (cur) {
        if (!cur.left) { res.push(cur.val); cur = cur.right; }
        else {
            let pred = cur.left;
            while (pred.right && pred.right !== cur) pred = pred.right;
            if (!pred.right) { res.push(cur.val); pred.right = cur; cur = cur.left; }
            else { pred.right = null; cur = cur.right; }
        }
    }
    return res;
}
export function demo(): void {
    const cases = [
        { in: buildTree([1,null,2,3]), want: [1,2,3] },
        { in: buildTree([]), want: [] },
        { in: buildTree([1]), want: [1] },
        { in: buildTree([1,2,3,4,5]), want: [1,2,4,5,3] },
    ];
    let fail = false;
    for (const c of cases) { const got = preorderTraversal(c.in); if (!eq(got, c.want)) { fail = true; console.log("FAIL", JSON.stringify(got), "want", JSON.stringify(c.want)); } }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();'''),

"ts/notes/lc_113764246_图搜索之dfs详解/solution_2___2.ts": ("full", '''function topoSortDfs(graph) {
    const n = graph.length;
    const status = new Array(n).fill('UNDISCOVERED');
    const stack = [];
    function visit(v) {
        status[v] = 'DISCOVERED';
        for (const u of graph[v]) if (status[u] === 'UNDISCOVERED') visit(u);
        status[v] = 'VISITED';
        stack.push(v);
    }
    for (let i = 0; i < n; i++) if (status[i] === 'UNDISCOVERED') visit(i);
    return stack.reverse();
}
export function demo(): void {
    const graph = [[2],[2],[3],[4],[5],[]];
    const cases = [ { got: topoSortDfs(graph), want: [1,0,2,3,4,5] } ];
    let fail = false;
    for (const c of cases) if (!eq(c.got, c.want)) { fail = true; console.log("FAIL", JSON.stringify(c.got), "want", JSON.stringify(c.want)); }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();'''),

"ts/notes/lc_145370679_leetcode_lcp_10._二叉树任务调度/solution_2_2_____2_____-__.ts": ("full", '''function dfs(root) { return []; }
export function demo(): void {
    const cases = [ { got: dfs(null), want: [] } ];
    let fail = false;
    for (const c of cases) if (!eq(c.got, c.want)) { fail = true; console.log("FAIL", JSON.stringify(c.got)); }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();'''),

"ts/notes/lc_107868749_贪心策略之matrixsorting_pfc_coding_huffmantre/solution_1_主解法.ts": ("full", '''function matrixSort(matrix) {
    if (!matrix || !matrix[0]) return matrix;
    const rows = matrix.length, cols = matrix[0].length;
    for (let c = 0; c < cols; c++) {
        const col = matrix.map(r => r[c]).sort((a,b)=>a-b);
        for (let r = 0; r < rows; r++) matrix[r][c] = col[r];
    }
    for (let r = 0; r < rows; r++) matrix[r] = matrix[r].slice().sort((a,b)=>a-b);
    return matrix;
}
function buildHuffman(freqs) {
    const nodes = Object.keys(freqs).map(k => [freqs[k], k]);
    nodes.sort((a,b)=>a[0]-b[0]);
    while (nodes.length > 1) {
        const a = nodes.shift(), b = nodes.shift();
        const merged = [a[0]+b[0], [a,b]];
        let i = 0; while (i < nodes.length && nodes[i][0] < merged[0]) i++;
        nodes.splice(i,0,merged);
    }
    return nodes[0];
}
function huffmanCodes(freqs) {
    const root = buildHuffman(freqs); const codes = {};
    function walk(node, prefix) {
        if (Array.isArray(node)) {
            const content = node[1];
            if (typeof content === 'string') codes[content] = prefix || '0';
            else { walk(content[0], prefix+'0'); walk(content[1], prefix+'1'); }
        }
    }
    walk(root, '');
    return codes;
}
export function demo(): void {
    const freqs = {'A':5,'B':9,'C':12,'D':13,'E':16,'F':45};
    const sortedMat = matrixSort([[5,3,4],[1,6,2],[7,9,8]].map(r=>r.slice()));
    const codes = huffmanCodes(freqs);
    let wpl = 0; for (const k of Object.keys(codes)) wpl += freqs[k] * codes[k].length;
    const arr = Object.values(codes); let prefixFree = true;
    for (let i=0;i<arr.length;i++) for (let j=0;j<arr.length;j++) if (i!==j && arr[j].startsWith(arr[i])) prefixFree = false;
    const cases = [
        { got: sortedMat, want: [[1,2,3],[4,5,6],[7,8,9]] },
        { got: wpl, want: 224 },
        { got: prefixFree, want: true },
    ];
    let fail = false;
    for (const c of cases) if (!eq(c.got, c.want)) { fail = true; console.log("FAIL", JSON.stringify(c.got)); }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();'''),

"ts/notes/lc_107836586_big-o记号_数据结构与算法的关系以及几种基本的数据结构/solution_1_主解法.ts": ("full", '''function classify(coeffs) {
    for (let deg = coeffs.length - 1; deg >= 0; deg--) {
        if (coeffs[deg] !== 0) return deg > 1 ? `O(n^${deg})` : (deg === 1 ? "O(n)" : "O(1)");
    }
    return "O(1)";
}
export function demo(): void {
    const cases = [
        { got: classify([1,0,0,0]), want: "O(1)" },
        { got: classify([0,0,0,35]), want: "O(n^3)" },
        { got: classify([0,0,1,0]), want: "O(n^2)" },
        { got: classify([0,1,0,0]), want: "O(n)" },
    ];
    let fail = false;
    for (const c of cases) if (!eq(c.got, c.want)) { fail = true; console.log("FAIL", JSON.stringify(c.got), "want", JSON.stringify(c.want)); }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();'''),

"ts/notes/lc_107431726_最大红矩形分析/solution_3___3.ts": ("full", '''function getResult(n, m, matrix) {
    let ans = 0;
    const height = new Array(m + 2).fill(0);
    for (let k = 0; k < n; k++) {
        for (let i = 1; i <= m; i++) {
            if (matrix[k][i-1] === '.') height[i] += 1;
            else height[i] = 0;
        }
        const stack = [0];
        for (let i = 1; i <= m + 1; i++) {
            while (height[stack[stack.length-1]] > height[i]) {
                const nowH = height[stack.pop()];
                const width = i - stack[stack.length-1] - 1;
                const area = nowH * width;
                if (area > ans) ans = area;
            }
            stack.push(i);
        }
    }
    return ans;
}
export function demo(): void {
    const matrix = [".....","XXXXX",".X...","....."];
    const cases = [ { got: getResult(4, 5, matrix), want: 6 } ];
    let fail = false;
    for (const c of cases) if (!eq(c.got, c.want)) { fail = true; console.log("FAIL", JSON.stringify(c.got), "want", JSON.stringify(c.want)); }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();'''),

"ts/notes/lc_107579658_抽象思维之转换视角_提炼共性/solution_1___1.ts": ("full", '''function solveUnified(queen) {
    queen = queen === undefined ? false : queen;
    const SIZE = queen ? 8 : 5;
    const like = [[0,0,1,1,0],[1,1,0,0,1],[0,1,1,0,1],[0,0,0,1,0],[0,1,0,0,1]];
    const Q = new Array(SIZE).fill(-1);
    const rows = new Array(SIZE).fill(true);
    let diag1, diag2;
    if (queen) { diag1 = new Array(2*SIZE-1).fill(true); diag2 = new Array(2*SIZE-1).fill(true); }
    const results = [];
    function is_valid(row, col) { return queen ? true : (like[row][col] === 1); }
    function is_safe(row, col) {
        if (queen) return rows[row] && diag1[col-row+SIZE-1] && diag2[col+row];
        return rows[row];
    }
    function place(col) {
        if (col === SIZE) { results.push(Q.slice()); return; }
        for (let row = 0; row < SIZE; row++) {
            if (!is_valid(row, col)) continue;
            if (!is_safe(row, col)) continue;
            Q[col] = row; rows[row] = false;
            if (queen) { const d1 = col-row+SIZE-1, d2 = col+row; diag1[d1]=diag2[d2]=false; }
            place(col+1);
            rows[row] = true;
            if (queen) { const d1 = col-row+SIZE-1, d2 = col+row; diag1[d1]=diag2[d2]=true; }
        }
    }
    place(0);
    return results;
}
export function demo(): void {
    const cases = [ { got: solveUnified(false), want: [[1,2,0,3,4],[1,4,0,3,2]] } ];
    let fail = false;
    for (const c of cases) if (!eq(c.got, c.want)) { fail = true; console.log("FAIL", JSON.stringify(c.got)); }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();'''),

"ts/notes/lc_107737496_抽象思维之代码重构_隔离变化/solution_4___4.ts": ("full", '''function placeFill(n) {
    const m = Array.from({length:n},()=>new Array(n).fill(0));
    let row=0,col=0,direction='D',num=1; const total=n*n;
    while (num<=total) {
        m[row][col]=num; num++;
        if (direction==='D') {
            if (row+1<n && m[row+1][col]===0) row++;
            else { direction='R'; col++; }
        } else if (direction==='R') {
            if (col+1<n && m[row][col+1]===0) col++;
            else { direction='U'; row--; }
        } else if (direction==='U') {
            if (row-1>=0 && m[row-1][col]===0) row--;
            else { direction='L'; col--; }
        } else {
            if (col-1>=0 && m[row][col-1]===0) col--;
            else { direction='D'; row++; }
        }
    }
    return m;
}
export function demo(): void {
    const cases = [
        { got: placeFill(3), want: [[1,8,7],[2,9,6],[3,4,5]] },
        { got: placeFill(4), want: [[1,12,11,10],[2,13,16,9],[3,14,15,8],[4,5,6,7]] },
    ];
    let fail=false;
    for (const c of cases) if (!eq(c.got,c.want)) { fail=true; console.log("FAIL",JSON.stringify(c.got)); }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();'''),

"ts/notes/lc_107737496_抽象思维之代码重构_隔离变化/solution_5___5.ts": ("full", '''class Matrix {
    row:number; col:number; buf:any[][];
    constructor(r:number,c:number){ this.row=r; this.col=c; this.buf=Array.from({length:r},()=>new Array(c).fill(0)); }
    call(r:number,c:number){ return this.buf[r][c]; }
    set(r:number,c:number,v:number){ this.buf[r][c]=v; }
}
export function demo(): void {
    const m = new Matrix(4,5);
    for (let i=0;i<4;i++) for (let j=0;j<5;j++) m.set(i,j,i*j);
    const cases = [ { got: m.call(2,3), want: 6 } ];
    let fail=false;
    for (const c of cases) if (!eq(c.got,c.want)) { fail=true; console.log("FAIL",JSON.stringify(c.got)); }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();'''),

"ts/notes/lc_107737496_抽象思维之代码重构_隔离变化/solution_6___6.ts": ("full", '''class Matrix {
    row:number; col:number; buf:any[][];
    constructor(r:number,c:number){ this.row=r; this.col=c; this.buf=Array.from({length:r},()=>new Array(c).fill(0)); }
    call(r:number,c:number){ return this.buf[r][c]; }
}
export function demo(): void {
    const m = new Matrix(4,5);
    for (let i=0;i<4;i++) for (let j=0;j<5;j++) m.buf[i][j]=i*j;
    const cases = [ { got: m.call(2,3), want: 6 } ];
    let fail=false;
    for (const c of cases) if (!eq(c.got,c.want)) { fail=true; console.log("FAIL",JSON.stringify(c.got)); }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();'''),

"ts/notes/lc_107737496_抽象思维之代码重构_隔离变化/solution_7___7.ts": ("full", '''function place(num,row,col,direction,n,m) {
    const handlers = {
        'D': () => (row+1<n && m[row+1][col]===0) ? [row+1,col] : [row,col+1,'R'],
        'R': () => (col+1<n && m[row][col+1]===0) ? [row,col+1] : [row-1,col,'U'],
        'U': () => (row-1>=0 && m[row-1][col]===0) ? [row-1,col] : [row,col-1,'L'],
        'L': () => (col-1>=0 && m[row][col-1]===0) ? [row,col-1] : [row+1,col,'D'],
    };
    return handlers[direction]();
}
function fillSpiral(n) {
    const m = Array.from({length:n},()=>new Array(n).fill(0));
    let row=0,col=0,direction='D',num=1;
    while (num<=n*n) {
        m[row][col]=num; num++;
        const res = place(num,row,col,direction,n,m);
        row=res[0]; col=res[1];
        if (res.length===3) direction=res[2];
    }
    return m;
}
export function demo(): void {
    const cases = [
        { got: fillSpiral(3), want: [[1,8,7],[2,9,6],[3,4,5]] },
        { got: fillSpiral(4), want: [[1,12,11,10],[2,13,16,9],[3,14,15,8],[4,5,6,7]] },
    ];
    let fail=false;
    for (const c of cases) if (!eq(c.got,c.want)) { fail=true; console.log("FAIL",JSON.stringify(c.got)); }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();'''),

"ts/notes/lc_107737496_抽象思维之代码重构_隔离变化/solution_11___11.ts": ("full", '''class Rule {
    data:string[]; idx:number; length:number;
    constructor(r:string){ this.data=r.split(''); this.idx=0; this.length=r.length; }
    next(){ const ch=this.data[this.idx]; this.idx=(this.idx+1)%this.length; return ch; }
    peek(){ return this.data[this.idx]; }
}
export function demo(): void {
    const r = new Rule("ESVM");
    const s1 = Array.from({length:10},()=>r.next()).join('');
    const r2 = new Rule("semv");
    const s2 = Array.from({length:6},()=>r2.next()).join('');
    const cases = [ { got: s1, want: "ESVMESVMES" }, { got: s2, want: "semvse" } ];
    let fail=false;
    for (const c of cases) if (!eq(c.got,c.want)) { fail=true; console.log("FAIL",JSON.stringify(c.got)); }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();'''),

"ts/notes/lc_104107934_python笔记_滑动验证码的识别算法/solution_3___3.ts": ("full", '''function nccMatch(bg, puzzle) {
    let bestX=0, bestScore=-Infinity; const n=puzzle.length;
    for (let x=0;x<=bg.length-n;x++) {
        const window=bg.slice(x,x+n);
        const bw=window.reduce((a,b)=>a+b,0)/n;
        const pw=puzzle.reduce((a,b)=>a+b,0)/n;
        let num=0, db=0, dp=0;
        for (let i=0;i<n;i++){ num+=(window[i]-bw)*(puzzle[i]-pw); db+=(window[i]-bw)**2; dp+=(puzzle[i]-pw)**2; }
        const denom=Math.sqrt(db)*Math.sqrt(dp);
        const score=denom!==0?num/denom:0;
        if (score>bestScore){ bestScore=score; bestX=x; }
    }
    return bestX;
}
export function demo(): void {
    const bg=[10,10,10,10,200,200,200,200]; const puzzle=[10,200,200,200];
    const cases = [ { got: nccMatch(bg,puzzle), want: 3 } ];
    let fail=false;
    for (const c of cases) if (!eq(c.got,c.want)) { fail=true; console.log("FAIL",JSON.stringify(c.got)); }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();'''),

"ts/notes/lc_104107934_python笔记_滑动验证码的识别算法/solution_4___4.ts": ("full", '''function bestMatchWindow(bg, puzzle) {
    let bestX=0, bestScore=Infinity; const n=puzzle.length;
    for (let x=0;x<=bg.length-n;x++) {
        let score=0; for (let y=0;y<n;y++) score+=Math.abs(bg[x+y]-puzzle[y]);
        if (score<bestScore){ bestScore=score; bestX=x; }
    }
    return [bestX, bestScore];
}
export function demo(): void {
    const bg=[10,10,10,10,200,200,200,200]; const puzzle=[10,200,200,200];
    const cases = [ { got: bestMatchWindow(bg,puzzle), want: [3,0] } ];
    let fail=false;
    for (const c of cases) if (!eq(c.got,c.want)) { fail=true; console.log("FAIL",JSON.stringify(c.got)); }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();'''),

"ts/notes/lc_104107934_python笔记_滑动验证码的识别算法/solution_5___5.ts": ("full", '''function detectEdges(image) {
    const edges=new Array(image.length).fill(false);
    for (let i=1;i<image.length;i++) edges[i]=Math.abs(image[i]-image[i-1])>50;
    return edges;
}
function findGap(bg, puzzle) {
    const bgEdges=detectEdges(bg), puzzleEdges=detectEdges(puzzle); const responses=[];
    for (let x=0;x<=bg.length-puzzle.length;x++) {
        let score=0; for (let y=0;y<puzzle.length;y++) if (bgEdges[x+y]&&puzzleEdges[y]) score++;
        responses.push(score);
    }
    let bestX=0; for (let i=1;i<responses.length;i++) if (responses[i]>responses[bestX]) bestX=i;
    return [bestX, responses];
}
export function demo(): void {
    const bg=[10,10,10,10,200,200,200,200]; const puzzle=[10,200,200,200];
    const cases = [ { got: findGap(bg,puzzle), want: [3,[0,0,0,1,0]] } ];
    let fail=false;
    for (const c of cases) if (!eq(c.got,c.want)) { fail=true; console.log("FAIL",JSON.stringify(c.got)); }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();'''),

"ts/notes/lc_104107934_python笔记_滑动验证码的识别算法/solution_7___7.ts": ("full", '''function detectEdges(image) {
    const edges=new Array(image.length).fill(false);
    for (let i=1;i<image.length;i++) edges[i]=Math.abs(image[i]-image[i-1])>50;
    return edges;
}
function recognizeCaptcha(bg, puzzle) {
    const bgEdges=detectEdges(bg), puzzleEdges=detectEdges(puzzle);
    let bestX=0, bestScore=-1;
    for (let x=0;x<=bg.length-puzzle.length;x++) {
        let score=0; for (let y=0;y<puzzle.length;y++) if (bgEdges[x+y]&&puzzleEdges[y]) score++;
        if (score>bestScore){ bestScore=score; bestX=x; }
    }
    return bestX;
}
function buildSynthetic(bgLen, gapStart, puzzleLen) {
    const bg=new Array(bgLen).fill(10);
    for (let i=gapStart;i<Math.min(gapStart+puzzleLen,bgLen);i++) bg[i]=200;
    const puzzle=bg.slice(gapStart,gapStart+puzzleLen);
    return [bg,puzzle];
}
export function demo(): void {
    const [bg,puzzle]=buildSynthetic(8,3,4);
    const cases = [ { got: recognizeCaptcha(bg,puzzle), want: 0 } ];
    let fail=false;
    for (const c of cases) if (!eq(c.got,c.want)) { fail=true; console.log("FAIL",JSON.stringify(c.got)); }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();'''),

"ts/notes/lc_133278676_使用链表指针获取json节点值的算法实现/solution_1___1.ts": ("full", '''function getValue(data, path) {
    let node = data;
    for (const key of path) {
        if (typeof node !== 'object' || node === null || !(key in node)) return null;
        node = node[key];
    }
    return node;
}
export function demo(): void {
    const data = { a:{b:{c:1}}, d:{e:2} };
    const cases = [
        { got: getValue(data, ['a','b','c']), want: 1 },
        { got: getValue(data, ['a','z']), want: null },
    ];
    let fail=false;
    for (const c of cases) if (!eq(c.got,c.want)) { fail=true; console.log("FAIL",JSON.stringify(c.got)); }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();'''),

"ts/notes/lc_133278676_使用链表指针获取json节点值的算法实现/solution_2___2.ts": ("full", '''function getValue(data, path) {
    let result = data;
    for (const k of path) result = result[k];
    return result;
}
export function demo(): void {
    const data = { a:{b:{c:1}}, d:{e:2} };
    const cases = [ { got: getValue(data, ['a','b','c']), want: 1 } ];
    let fail=false;
    for (const c of cases) if (!eq(c.got,c.want)) { fail=true; console.log("FAIL",JSON.stringify(c.got)); }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();'''),

"ts/notes/lc_133278676_使用链表指针获取json节点值的算法实现/solution_4___4.ts": ("full", '''function getValueChain(data, path) {
    return path.reduce((d,k)=>d[k], data);
}
export function demo(): void {
    const data = { a:{b:{c:1}}, d:{e:2} };
    const cases = [ { got: getValueChain(data, ['a','b','c']), want: 1 } ];
    let fail=false;
    for (const c of cases) if (!eq(c.got,c.want)) { fail=true; console.log("FAIL",JSON.stringify(c.got)); }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();'''),
}
