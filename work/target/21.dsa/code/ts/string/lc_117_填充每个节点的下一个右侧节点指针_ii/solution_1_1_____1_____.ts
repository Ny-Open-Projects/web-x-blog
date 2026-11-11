/**
 ** LeetCode 117. 填充每个节点的下一个右侧节点指针 II
 ** 方案：1 ) 方案1：层序遍历 (BFS)
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145385760
 */

class Node {
  // 定义类型
  val: number; // 值: number;
  left: Node | null; // 左边界: Node 按位或 null;
  right: Node | null; // 右边界: Node 按位或 null;
  next: Node | null; // 下一个: Node 按位或 null;
  constructor(
    val: number,
    left: Node | null = null,
    right: Node | null = null,
    next: Node | null = null,
  ) {
    this.val = val; // 把 值; 写入 值
    this.left = left; // 把 左边界; 写入 左边界
    this.right = right; // 把 右边界; 写入 右边界
    this.next = next; // 把 下一个; 写入 下一个
  }
}

export function connect(root: Node | null): Node | null {
  // 定义函数/方法 connect
  if (!root) return null; // 若 取反 根节点，直接返回 null
  const queue: Node[] = [root]; // 把 [根节点]; 写入 const queue: Node[]
  while (queue.length) {
    // 循环，直到不满足「队列.长度」
    const n = queue.length; // 把 队列.长度 存入 元素个数
    let prev: Node | null = null; // 把 null; 写入 let prev: Node | null
    for (let k = 0; k < n; k++) {
      // 让 下标 k 从 0 开始计数，下标 k 小于 元素个数 就继续
      const node = queue.shift()!; // 把 队列.shift()取反 存入 节点
      if (prev) prev.next = node; // 若 前一个) 前一个.下一个 赋值为 节点;
      prev = node; // 把 节点 存入 前一个
      if (node.left) queue.push(node.left); // 若 节点.左边界) 队列 追加 节点.左边界);
      if (node.right) queue.push(node.right); // 若 节点.右边界) 队列 追加 节点.右边界);
    }
  }
  return root; // 返回 根节点
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const root = new Node(
    1,
    new Node(2, new Node(4), new Node(5)),
    new Node(3, null, new Node(7)),
  );
  connect(root); // connect(根节点);
  if (!(root.left && root.left.next && root.left.next.val === 3))
    throw new Error('FAILED level1');
  if (!(
    root.left.left &&
    root.left.left.next &&
    root.left.left.next.val === 5 &&
    root.left.left.next.next &&
    root.left.left.next.next.val === 7
  )) {
    // 把 等于 7)) { 写入 值
    throw new Error('FAILED level2'); // throw new Error(「FAILED level2」);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
