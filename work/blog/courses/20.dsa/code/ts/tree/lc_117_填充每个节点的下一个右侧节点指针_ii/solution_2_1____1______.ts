// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385760
/**
 ** LeetCode 117. 填充每个节点的下一个右侧节点指针 II
 ** 方案：方案2（层序连接，使用已建立的 next 指针）
 ** 来源：python 参考忠实移植
 */

class Node {
  // 定义类型
  val: number; // 值: number;
  left: Node | null; // 左边界: Node 按位或 null;
  right: Node | null; // 右边界: Node 按位或 null;
  next: Node | null; // 下一个: Node 按位或 null;
  constructor(
    val?: number,
    left?: Node | null,
    right?: Node | null,
    next?: Node | null,
  ) {
    this.val = val === undefined ? 0 : val; // 把 值 全等于 undefined ? 0 : 值; 写入 值
    this.left = left === undefined ? null : left; // 把 左边界 全等于 undefined ? null : 左边界; 写入 左边界
    this.right = right === undefined ? null : right; // 把 右边界 全等于 undefined ? null : 右边界; 写入 右边界
    this.next = next === undefined ? null : next; // 把 下一个 全等于 undefined ? null : 下一个; 写入 下一个
  }
}

function buildNode(vals: (number | null)[]): Node | null {
  // 定义函数/方法 buildNode
  if (!vals.length) return null; // 若 取反 vals.长度，直接返回 null
  const root = new Node(vals[0]); // 把 new Node(vals[0]) 存入 根节点
  const q: Node[] = [root]; // 把 [根节点]; 写入 const q: Node[]
  let i = 1; // 把 1 存入 下标 i
  while (i < vals.length && q.length) {
    // 循环，直到不满足「下标 i 小于 vals.长度 且 节点.长度」
    const node = q.shift()!; // 把 节点.shift()取反 存入 节点
    if (i < vals.length && vals[i] !== null) {
      // 若 下标 i 小于 vals.长度 且 vals[下标 i] 不等于 null
      node.left = new Node(vals[i] as number); // 把 new Node(vals[下标 i] as number); 写入 左边界
      q.push(node.left); // 把 节点.左边界 压入栈/数组尾部
    }
    i++; // 下标 i 加一
    if (i < vals.length && vals[i] !== null) {
      // 若 下标 i 小于 vals.长度 且 vals[下标 i] 不等于 null
      node.right = new Node(vals[i] as number); // 把 new Node(vals[下标 i] as number); 写入 右边界
      q.push(node.right); // 把 节点.右边界 压入栈/数组尾部
    }
    i++; // 下标 i 加一
  }
  return root; // 返回 根节点
}

function levelOrderVals(root: Node | null): (number | null)[] {
  // 定义函数/方法 levelOrderVals
  if (!root) return []; // 若 取反 根节点，直接返回 []
  const res: (number | null)[] = []; // 把 []; 写入 const res: (number | null)[]
  const q: Node[] = [root]; // 把 [根节点]; 写入 const q: Node[]
  while (q.length) {
    // 循环，直到不满足「节点.长度」
    const node = q.shift()!; // 把 节点.shift()取反 存入 节点
    if (node === null) {
      // 若 节点 全等于 null
      res.push(null); // 把 null 压入栈/数组尾部
      continue; // 跳过本轮，进入下一次
    }
    res.push(node.val); // 把 节点.值 压入栈/数组尾部
    q.push(node.left as Node); // 把 节点.左边界 as Node 压入栈/数组尾部
    q.push(node.right as Node); // 把 节点.右边界 as Node 压入栈/数组尾部
  }
  while (res.length && res[res.length - 1] === null) res.pop(); // 循环，直到不满足「结果.长度 且 结果[结果.长度 减 1] 全等于 null) 结果 弹出 );」
  return res; // 返回 结果
}

function connect(root: Node | null): Node | null {
  // 定义函数/方法 connect
  if (!root) return root; // 若 取反 根节点，直接返回 根节点
  let head: Node | null = root; // 把 根节点; 写入 let head: Node | null
  while (head) {
    // 循环，直到不满足「头节点」
    const dummy = new Node(); // 把 new Node() 存入 哨兵节点
    let tail = dummy; // 把 哨兵节点 存入 尾节点
    let cur: Node | null = head; // 把 头节点; 写入 let cur: Node | null
    while (cur) {
      // 循环，直到不满足「当前值」
      if (cur.left) {
        // 若 当前值.左边界
        tail.next = cur.left; // 把 当前值.左边界; 写入 下一个
        tail = tail.next; // 把 尾节点.下一个 存入 尾节点
      }
      if (cur.right) {
        // 若 当前值.右边界
        tail.next = cur.right; // 把 当前值.右边界; 写入 下一个
        tail = tail.next; // 把 尾节点.下一个 存入 尾节点
      }
      cur = cur.next; // 把 当前值.下一个 存入 当前值
    }
    head = dummy.next; // 把 哨兵节点.下一个 存入 头节点
  }
  return root; // 返回 根节点
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function eqArrN(a: (number | null)[], b: (number | null)[]): boolean {
    // 定义函数/方法 eqArrN
    if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    return true; // 返回 true
  }
  const cases: { in: (number | null)[]; want: (number | null)[] }[] = [
    { in: [1, 2, 3, 4, 5, null, 7], want: [1, 2, 3, 4, 5, null, 7] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = levelOrderVals(connect(buildNode(c.in))); // 把 levelOrderVals(connect(buildNode(字符.in))) 存入 got
    if (!eqArrN(got, c.want)) {
      // 若 取反 eqArrN(got, 字符.want
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL',
        JSON.stringify(c.in),
        'want',
        JSON.stringify(c.want),
        'got',
        JSON.stringify(got),
      ); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
