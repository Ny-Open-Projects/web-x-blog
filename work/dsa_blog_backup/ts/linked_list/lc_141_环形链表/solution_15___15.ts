// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130514894
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  class ListNode {
    // 定义类型
    val: number; // 值: number;
    next: ListNode | null; // 下一个: ListNode 按位或 null;
    constructor(v: number) {
      // constructor(值: number) {
      this.val = v; // 把 值; 写入 值
      this.next = null; // 把 null; 写入 下一个
    }
  }
  function build(vals: number[] | null, pos: number): ListNode | null {
    // 定义函数/方法 build
    if (vals === null) return null; // 若 vals 全等于 null，直接返回 null
    const nodes: ListNode[] = vals.map((v) => new ListNode(v));
    for (let i = 0; i < nodes.length - 1; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 nodes.长度 减 1 就继续
      nodes[i].next = nodes[i + 1]; // 把 nodes[下标 i 加 1]; 写入 下一个
    }
    if (pos >= 0 && nodes.length > 0) {
      // 若 pos 不低于 0 且 nodes.长度 超过 0
      nodes[nodes.length - 1].next = nodes[pos]; // 把 nodes[pos]; 写入 下一个
    }
    return nodes.length > 0 ? nodes[0] : null; // 返回 nodes.长度 超过 0 ? nodes[0] : null
  }
  function hasCycle(head: ListNode | null): boolean {
    // 定义函数/方法 hasCycle
    let slow: ListNode | null = head; // 把 头节点; 写入 let slow: ListNode | null
    let fast: ListNode | null = head; // 把 头节点; 写入 let fast: ListNode | null
    while (fast && fast.next) {
      // 循环，直到不满足「快指针 且 快指针.下一个」
      slow = slow!.next; // 把 慢指针取反 .下一个 存入 慢指针
      fast = fast.next.next; // 把 快指针.下一个.下一个 存入 快指针
      if (slow === fast) return true; // 若 慢指针 全等于 快指针，直接返回 true
    }
    return false; // 返回 false
  }
  const cases: Array<[number[] | null, number, boolean]> = [
    [[3, 2, 0, -4], 1, true],
    [[1, 2], 0, true],
    [[1], -1, false],
    [null, 0, false],
  ];
  let fail = false; // 把 false 存入 fail
  for (const cs of cases) {
    // for (const cs of cases) {
    const got = hasCycle(build(cs[0], cs[1])); // 把 hasCycle(build(cs[0], cs[1])) 存入 got
    if (got !== cs[2]) {
      // 若 got 不等于 cs[2]
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL hasCycle case ' +
          JSON.stringify(cs[0]) +
          ',' +
          cs[1] +
          ' got ' +
          got +
          ' want ' +
          cs[2],
      ); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
