// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145088458
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  class Node {
    val: number;
    children: Node[] = [];
    constructor(v: number) {
      this.val = v;
    }
  } // 定义类型
  function levelOrder(root: Node | null): number[][] {
    if (!root) return [];
    const res: number[][] = [];
    let q: Node[] = [root];
    while (q.length) {
      const lvl: number[] = [];
      const n = q.length;
      for (let k = 0; k < n; k++) {
        const x = q.shift()!;
        lvl.push(x.val);
        for (const c of x.children) q.push(c);
      }
      res.push(lvl);
    }
    return res;
  } // 定义函数/方法 levelOrder
  const c5 = new Node(5),
    c6 = new Node(6);
  const c3 = new Node(3);
  c3.children = [c5, c6];
  const c2 = new Node(2),
    c4 = new Node(4);
  const root = new Node(1);
  root.children = [c3, c2, c4];
  if (
    JSON.stringify(levelOrder(root)) !==
    JSON.stringify([[1], [3, 2, 4], [5, 6]])
  ) {
    console.log('FAIL');
    throw new Error('FAILED');
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
