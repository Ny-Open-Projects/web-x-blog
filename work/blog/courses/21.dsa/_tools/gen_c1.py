#!/usr/bin/env python3
# Generator for chunk 1 TS files. Writes faithful ports with demo() + PASS gate.
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---- common scaffolding pieces ----
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
    for (const v of vals) {
        cur.next = new ListNode(v);
        cur = cur.next;
    }
    return dummy.next;
}

function listToArr(head: ListNode | null): number[] {
    const res: number[] = [];
    while (head) {
        res.push(head.val);
        head = head.next;
    }
    return res;
}

function listToStr(head: ListNode | null): string {
    const parts: string[] = [];
    while (head) {
        parts.push(String(head.val));
        head = head.next;
    }
    return parts.join("->");
}
'''

TREE_NODE = '''
class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
    constructor(val: number, left: TreeNode | null = null, right: TreeNode | null = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

function buildTree(vals: (number | null)[]): TreeNode | null {
    if (vals.length === 0 || vals[0] === null) return null;
    const root = new TreeNode(vals[0] as number);
    const q: (TreeNode | null)[] = [root];
    let i = 1;
    while (i < vals.length) {
        const node = q.shift() as TreeNode;
        if (i < vals.length && vals[i] !== null) {
            node.left = new TreeNode(vals[i] as number);
            q.push(node.left);
        }
        i++;
        if (i < vals.length && vals[i] !== null) {
            node.right = new TreeNode(vals[i] as number);
            q.push(node.right);
        }
        i++;
    }
    return root;
}
'''

HELPERS = '''
function assertEq(actual: any, expected: any, msg: string = ""): void {
    const a = JSON.stringify(actual);
    const e = JSON.stringify(expected);
    if (a !== e) {
        throw new Error("ASSERT FAILED " + msg + " :: actual=" + a + " expected=" + e);
    }
}
'''

def write(path: str, content: str):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(content)
    print("wrote", path)

# ---- file 1: lc_206 reverseList ----
c = LIST_NODE + HELPERS + '''
function reverseList(head: ListNode | null): ListNode | null {
    let result: ListNode | null = null;
    while (head) {
        const temp = head.next;
        head.next = result;
        result = head;
        head = temp;
    }
    return result;
}

export function demo(): void {
    const h1 = buildList([1, 2, 3]);
    assertEq(listToArr(reverseList(h1)!), [3, 2, 1], "reverseList [1,2,3]");
    const h2 = buildList([1]);
    assertEq(listToArr(reverseList(h2)!), [1], "reverseList [1]");
    const h3 = buildList([5, 4, 3, 2, 1]);
    assertEq(listToArr(reverseList(h3)!), [1, 2, 3, 4, 5], "reverseList [5,4,3,2,1]");
    console.log("PASS");
}
demo();
'''
write("ts/linked_list/lc_206_反转链表/solution_2___2.ts", c)

# ---- file 2: lc_203 removeElements ----
c = LIST_NODE + HELPERS + '''
function removeElements(head: ListNode | null, val: number): ListNode | null {
    const dummy = new ListNode(0, head);
    let temp = dummy;
    while (temp.next) {
        if (temp.next.val === val) {
            temp.next = temp.next.next;
        } else {
            temp = temp.next;
        }
    }
    return dummy.next;
}

export function demo(): void {
    const h = buildList([1, 2, 6, 3, 4, 5, 6]);
    assertEq(listToStr(removeElements(h, 6)), "1->2->3->4->5", "removeElements");
    const h2 = buildList([6, 6, 6]);
    assertEq(listToStr(removeElements(h2, 6)), "", "removeElements all");
    const h3 = buildList([1, 2, 3]);
    assertEq(listToStr(removeElements(h3, 9)), "1->2->3", "removeElements none");
    console.log("PASS");
}
demo();
'''
write("ts/linked_list/lc_203_移除链表元素/solution_2_2_____2____.ts", c)

# ---- file 3: selectionSort ----
c = HELPERS + '''
function selectionSort(nums: number[]): number[] {
    for (let i = 0; i < nums.length; i++) {
        let minIdx = i;
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[j] < nums[minIdx]) minIdx = j;
        }
        [nums[i], nums[minIdx]] = [nums[minIdx], nums[i]];
    }
    return nums;
}

export function demo(): void {
    assertEq(selectionSort([1, 2, 3].slice()), [1, 2, 3], "sel [1,2,3]");
    assertEq(selectionSort([3, 2, 1].slice()), [1, 2, 3], "sel [3,2,1]");
    assertEq(selectionSort([5, 2, 4, 1, 3].slice()), [1, 2, 3, 4, 5], "sel [5,2,4,1,3]");
    console.log("PASS");
}
demo();
'''
write("ts/notes/lc_134085384_选择排序/solution_1___1.ts", c)

# ---- file 4: seqSearch ----
c = HELPERS + '''
function seqSearch(arr: number[], target: number): number {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === target) return i;
    }
    return -1;
}

export function demo(): void {
    assertEq(seqSearch([1, 2, 3], 1), 0, "seqSearch hit");
    assertEq(seqSearch([1, 2, 3], 2), 1, "seqSearch hit2");
    assertEq(seqSearch([1, 2, 3], 4), -1, "seqSearch miss");
    console.log("PASS");
}
demo();
'''
write("ts/notes/lc_134217002_顺序查找/solution_1___1.ts", c)

# ---- file 5: maxDepth ----
c = TREE_NODE + HELPERS + '''
function maxDepth(root: TreeNode | null): number {
    let dep = 0;
    function dfs(n: TreeNode | null, l: number): void {
        if (!n) return;
        if (!n.left && !n.right) dep = Math.max(dep, l);
        dfs(n.left, l + 1);
        dfs(n.right, l + 1);
    }
    dfs(root, 1);
    return dep;
}

export function demo(): void {
    assertEq(maxDepth(null), 0, "maxDepth null");
    assertEq(maxDepth(buildTree([1])), 1, "maxDepth [1]");
    assertEq(maxDepth(buildTree([3, 9, 20, null, null, 15, 7])), 3, "maxDepth 3");
    console.log("PASS");
}
demo();
'''
write("ts/tree/lc_104_二叉树的最大深度/solution_1___1.ts", c)

# ---- file 6: isBalanced ----
c = TREE_NODE + HELPERS + '''
function isBalanced(root: TreeNode | null): boolean {
    if (!root) return true;
    function height(node: TreeNode | null): number {
        if (!node) return 0;
        return Math.max(height(node.left), height(node.right)) + 1;
    }
    const leftHeight = height(root.left);
    const rightHeight = height(root.right);
    return Math.abs(leftHeight - rightHeight) <= 1 && isBalanced(root.left) && isBalanced(root.right);
}

export function demo(): void {
    assertEq(isBalanced(null), true, "isBalanced null");
    assertEq(isBalanced(buildTree([3, 9, 20, null, null, 15, 7])), true, "isBalanced balanced");
    assertEq(isBalanced(buildTree([1, 2, 2, 3, 3, null, null, 4, 4])), false, "isBalanced unbalanced");
    console.log("PASS");
}
demo();
'''
write("ts/tree/lc_110_平衡二叉树/solution_1_1_____1_________.ts", c)

print("DONE batch1")
