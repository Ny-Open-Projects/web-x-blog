/**
 * LeetCode 237. 删除链表中的节点
 * 方案：方案2
 * 来源：https://blog.csdn.net/tyro_java/article/details/130508569
 * 忠实翻译 python/linked_list/lc_237_删除链表中的节点/solution_2___2.py
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  class ListNode {
    // 定义类型
    val: number; // 值: number;
    next: ListNode | null; // 下一个: ListNode 按位或 null;
    constructor(val: number = 0, next: ListNode | null = null) {
      this.val = val; // 把 值; 写入 值
      this.next = next; // 把 下一个; 写入 下一个
    }
  }

  function build(nums: number[]): ListNode | null {
    // 定义函数/方法 build
    const dummy = new ListNode(0); // 把 new ListNode(0) 存入 哨兵节点
    let cur: ListNode = dummy; // 把 哨兵节点; 写入 let cur: ListNode
    for (const n of nums) {
      // for (const 元素个数 of 数组) {
      cur.next = new ListNode(n); // 把 new ListNode(元素个数); 写入 下一个
      cur = cur.next; // 把 当前值.下一个 存入 当前值
    }
    return dummy.next; // 返回 哨兵节点.下一个
  }

  function toList(head: ListNode | null): number[] {
    // 定义函数/方法 toList
    const res: number[] = []; // 把 []; 写入 const res: number[]
    let h = head; // 把 头节点 存入 h
    while (h) {
      // 循环，直到不满足「h」
      res.push(h.val); // 把 h.值 压入栈/数组尾部
      h = h.next; // 把 h.下一个 存入 h
    }
    return res; // 返回 结果
  }

  function deleteNode(node: ListNode): void {
    // 定义函数/方法 deleteNode
    // 将本节点值替换为下一个节点的值，再连到下下一个节点
    node.val = node.next!.val; // 把 节点.下一个取反 .值; 写入 值
    node.next = node.next!.next; // 把 节点.下一个取反 .下一个; 写入 下一个
  }

  // case: [nums, 目标下标, 期望结果]
  const cases: { nums: number[]; idx: number; want: number[] }[] = [
    { nums: [4, 5, 1, 9], idx: 2, want: [4, 5, 9] },
    { nums: [4, 5, 1, 9], idx: 1, want: [4, 1, 9] },
    { nums: [1, 2, 3, 4], idx: 2, want: [1, 2, 4] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const head = build(c.nums); // 把 build(字符.数组) 存入 头节点
    let target: ListNode | null = head; // 把 头节点; 写入 let target: ListNode | null
    for (let i = 0; i < c.idx; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 字符.idx 就继续
      target = target!.next; // 把 目标值取反 .下一个 存入 目标值
    }
    deleteNode(target!); // deleteNode(目标值取反 );
    const got = toList(head); // 把 toList(头节点) 存入 got
    if (got.length !== c.want.length || got.some((v, i) => v !== c.want[i])) {
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL deleteNode(%o,%d)=%o want %o',
        c.nums,
        c.idx,
        got,
        c.want,
      ); // 打印输出
    }
  }
  if (fail) {
    // 若 fail
    throw new Error('FAILED'); // throw new Error(「FAILED」);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
