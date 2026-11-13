// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386215
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  class Node {
    // 定义类型
    val: number; // 值: number;
    left: Node | null; // 左边界: Node 按位或 null;
    right: Node | null; // 右边界: Node 按位或 null;
    next: Node | null; // 下一个: Node 按位或 null;
    constructor(
      v: number,
      left: Node | null = null,
      right: Node | null = null,
      next: Node | null = null,
    ) {
      this.val = v;
      this.left = left;
      this.right = right;
      this.next = next;
    }
  }
  function buildPerfect(): Node {
    // 定义函数/方法 buildPerfect
    const n1 = new Node(1); // 把 new Node(1) 存入 n1
    n1.left = new Node(2);
    n1.right = new Node(3); // 把 new Node(2); n1.右边界 赋值为 new Node(3); 写入 左边界
    n1.left.left = new Node(4);
    n1.left.right = new Node(5); // 把 new Node(4); n1.左边界.右边界 赋值为 new Node(5); 写入 左边界
    n1.right.left = new Node(6);
    n1.right.right = new Node(7); // 把 new Node(6); n1.右边界.右边界 赋值为 new Node(7); 写入 左边界
    return n1; // 返回 n1
  }
  function connect(root: Node | null): Node | null {
    // 定义函数/方法 connect
    if (!root) return root; // 若 取反 根节点，直接返回 根节点
    const queue: (Node | null)[] = [root]; // 把 [根节点]; 写入 const queue: (Node | null)[]
    while (queue.length) {
      // 循环，直到不满足「队列.长度」
      const size = queue.length; // 把 队列.长度 存入 大小
      let prev: Node | null = null; // 把 null; 写入 let prev: Node | null
      for (let i = 0; i < size; i++) {
        // 让 下标 i 从 0 开始计数，下标 i 小于 大小 就继续
        const node = queue.shift() as Node; // 把 队列.shift() as Node 存入 节点
        if (prev) prev.next = node; // 若 前一个) 前一个.下一个 赋值为 节点;
        prev = node; // 把 节点 存入 前一个
        if (node.left) queue.push(node.left); // 若 节点.左边界) 队列 追加 节点.左边界);
        if (node.right) queue.push(node.right); // 若 节点.右边界) 队列 追加 节点.右边界);
      }
    }
    return root; // 返回 根节点
  }
  let fail = false; // 把 false 存入 fail
  const gotNull = connect(null); // 把 connect(null) 存入 gotNull
  if (gotNull !== null) {
    fail = true;
    console.log('FAIL connect(null)=' + JSON.stringify(gotNull) + ' want null');
  }
  const root = connect(buildPerfect()); // 把 connect(buildPerfect()) 存入 根节点
  const levels: string[][] = []; // 把 []; 写入 const levels: string[][]
  let cur: Node | null = root; // 把 根节点; 写入 let cur: Node | null
  while (cur) {
    // 循环，直到不满足「当前值」
    const vals: string[] = []; // 把 []; 写入 const vals: string[]
    let node: Node | null = cur; // 把 当前值; 写入 let node: Node | null
    while (node) {
      vals.push(String(node.val));
      node = node.next;
    } // 循环，直到不满足「节点) { vals 追加 String(节点.值)); 节点 赋值为 节点.下一个; }」
    levels.push(vals); // 把 vals 压入栈/数组尾部
    cur = cur.left; // 把 当前值.左边界 存入 当前值
  }
  const want = [['1'], ['2', '3'], ['4', '5', '6', '7']]; // 把 [[「1」], [「1」, 「1」], [「1」, 「1」, 「1」, 「1」]] 存入 want
  if (JSON.stringify(levels) !== JSON.stringify(want)) {
    fail = true;
    console.log(
      'FAIL connect levels=' +
        JSON.stringify(levels) +
        ' want ' +
        JSON.stringify(want),
    );
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
