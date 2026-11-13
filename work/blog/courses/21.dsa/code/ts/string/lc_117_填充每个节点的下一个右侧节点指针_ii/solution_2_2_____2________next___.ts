/**
 ** LeetCode 117. 填充每个节点的下一个右侧节点指针 II
 ** 方案：2 ) 方案2：使用已建立的 next 指针（O(1) 额外空间）
 ** 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386298
 */

class Node2 {
  // 定义类型
  val: number; // 值: number;
  left: Node2 | null; // 左边界: Node2 按位或 null;
  right: Node2 | null; // 右边界: Node2 按位或 null;
  next: Node2 | null; // 下一个: Node2 按位或 null;
  constructor(
    val?: number,
    left: Node2 | null = null,
    right: Node2 | null = null,
  ) {
    this.val = val === undefined ? 0 : val; // 把 (值 全等于 undefined ? 0 : 值); 写入 值
    this.left = left; // 把 左边界; 写入 左边界
    this.right = right; // 把 右边界; 写入 右边界
    this.next = null; // 把 null; 写入 下一个
  }
}

function buildNode(vals: (number | null)[]): Node2 | null {
  // 定义函数/方法 buildNode
  if (vals.length === 0 || vals[0] === null || vals[0] === undefined)
    return null;
  const root = new Node2(vals[0] as number); // 把 new Node2(vals[0] as number) 存入 根节点
  const q: Node2[] = [root]; // 把 [根节点]; 写入 const q: Node2[]
  let i = 1; // 把 1 存入 下标 i
  while (i < vals.length) {
    // 循环，直到不满足「下标 i 小于 vals.长度」
    const node = q.shift() as Node2; // 把 节点.shift() as Node2 存入 节点
    if (i < vals.length && vals[i] !== null && vals[i] !== undefined) {
      node.left = new Node2(vals[i] as number); // 把 new Node2(vals[下标 i] as number); 写入 左边界
      q.push(node.left); // 把 节点.左边界 压入栈/数组尾部
    }
    i++; // 下标 i 加一
    if (i < vals.length && vals[i] !== null && vals[i] !== undefined) {
      node.right = new Node2(vals[i] as number); // 把 new Node2(vals[下标 i] as number); 写入 右边界
      q.push(node.right); // 把 节点.右边界 压入栈/数组尾部
    }
    i++; // 下标 i 加一
  }
  return root; // 返回 根节点
}

function connect(root: Node2 | null): Node2 | null {
  // 定义函数/方法 connect
  if (root === null) return null; // 若 根节点 全等于 null，直接返回 null
  let leftmost: Node2 | null = root; // 把 根节点; 写入 let leftmost: Node2 | null
  while (leftmost !== null) {
    // 循环，直到不满足「leftmost 不等于 null」
    let cur: Node2 | null = leftmost; // 把 leftmost; 写入 let cur: Node2 | null
    let nextStart: Node2 | null = null; // 把 null; 写入 let nextStart: Node2 | null
    let prev: Node2 | null = null; // 把 null; 写入 let prev: Node2 | null
    while (cur !== null) {
      // 循环，直到不满足「当前值 不等于 null」
      for (const ch of [cur.left, cur.right]) {
        // for (const 字符 of [当前值.左边界, 当前值.右边界]) {
        if (ch !== null) {
          // 若 字符 不等于 null
          if (prev === null) {
            // 若 前一个 全等于 null
            nextStart = ch; // 把 字符 存入 nextStart
          } else {
            // 否则
            prev.next = ch; // 把 字符; 写入 下一个
          }
          prev = ch; // 把 字符 存入 前一个
        }
      }
      cur = cur.next; // 把 当前值.下一个 存入 当前值
    }
    leftmost = nextStart; // 把 nextStart 存入 leftmost
  }
  return root; // 返回 根节点
}

function collectLevels(root: Node2 | null): number[][] {
  // 定义函数/方法 collectLevels
  const res: number[][] = []; // 把 []; 写入 const res: number[][]
  for (
    let leftmost: Node2 | null = root;
    leftmost !== null;
    leftmost = leftmost.left
  ) {
    const level: number[] = []; // 把 []; 写入 const level: number[]
    for (let cur: Node2 | null = leftmost; cur !== null; cur = cur.next) {
      level.push(cur.val); // 把 当前值.值 压入栈/数组尾部
    }
    res.push(level); // 把 level 压入栈/数组尾部
  }
  return res; // 返回 结果
}

function eqLevels(a: number[][], b: number[][]): boolean {
  // 定义函数/方法 eqLevels
  if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
  for (let i = 0; i < a.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    if (a[i].length !== b[i].length) return false; // 若 数组[下标 i].长度 不等于 b[下标 i].长度，直接返回 false
    for (let j = 0; j < a[i].length; j++) if (a[i][j] !== b[i][j]) return false; // 让 下标 j 从 0 开始计数，下标 j 小于 数组[下标 i].长度 就继续
  }
  return true; // 返回 true
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const root = buildNode([1, 2, 3, 4, 5, null, 7]); // 把 buildNode([1, 2, 3, 4, 5, null, 7]) 存入 根节点
  connect(root); // connect(根节点);
  const got = collectLevels(root); // 把 collectLevels(根节点) 存入 got
  const want: number[][] = [[1], [2, 3], [4, 5, 7]]; // 把 [[1], [2, 3], [4, 5, 7]]; 写入 const want: number[][]
  if (!eqLevels(got, want)) {
    // 若 取反 eqLevels(got, want
    throw new Error(
      'FAILED connect=' + JSON.stringify(got) + ' want ' + JSON.stringify(want),
    );
  }
  if (connect(null) !== null) throw new Error('FAILED connect(null) != null');
  const single = new Node2(9); // 把 new Node2(9) 存入 single
  connect(single); // connect(single);
  if (!eqLevels(collectLevels(single), [[9]])) throw new Error('FAILED single');
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
