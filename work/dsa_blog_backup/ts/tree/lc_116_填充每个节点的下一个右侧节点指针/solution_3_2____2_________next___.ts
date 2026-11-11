// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386215
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  class Node {
    val: number;
    left: Node | null = null;
    right: Node | null = null;
    next: Node | null = null;
    constructor(v: number) {
      this.val = v;
    }
  } // 定义类型
  function connect(root: Node | null): Node | null {
    if (!root) return null;
    const q: Node[] = [root];
    while (q.length) {
      const n = q.length;
      let prev: Node | null = null;
      for (let k = 0; k < n; k++) {
        const x = q.shift()!;
        if (prev) prev.next = x;
        prev = x;
        if (x.left) q.push(x.left);
        if (x.right) q.push(x.right);
      }
    }
    return root;
  } // 定义函数/方法 connect
  const n1 = new Node(1);
  n1.left = new Node(2);
  n1.right = new Node(3);
  n1.left.left = new Node(4);
  n1.left.right = new Node(5);
  n1.right.left = new Node(6);
  n1.right.right = new Node(7);
  connect(n1); // connect(n1);
  if (n1.left!.next !== n1.right) {
    console.log('FAIL lvl2');
    throw new Error('FAILED');
  }
  if (
    n1.left!.left!.next !== n1.left!.right ||
    n1.left!.right!.next !== n1.right!.left ||
    n1.right!.left!.next !== n1.right!.right
  ) {
    console.log('FAIL lvl3');
    throw new Error('FAILED');
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
