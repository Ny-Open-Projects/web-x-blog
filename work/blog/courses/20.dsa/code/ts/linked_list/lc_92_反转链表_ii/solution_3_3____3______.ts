// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145094075
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  class ListNode {
    val: number;
    next: ListNode | null;
    constructor(v = 0, n: ListNode | null = null) {
      this.val = v;
      this.next = n;
    }
  } // 定义类型
  function build(vals: number[]): ListNode | null {
    const d = new ListNode();
    let p = d;
    for (const v of vals) {
      p.next = new ListNode(v);
      p = p.next;
    }
    return d.next;
  } // 定义函数/方法 build
  function toArr(h: ListNode | null): number[] {
    const r: number[] = [];
    while (h) {
      r.push(h.val);
      h = h.next;
    }
    return r;
  } // 定义函数/方法 toArr
  function reverseBetween(
    head: ListNode | null,
    left: number,
    right: number,
  ): ListNode | null {
    // 定义函数/方法 reverseBetween
    const dummy = new ListNode(0);
    dummy.next = head;
    let pre = dummy;
    for (let i = 1; i < left; i++) pre = pre.next!; // 让 下标 i 从 1 开始计数，下标 i 小于 左边界 就继续
    let start = pre.next!,
      then = start.next!; // 把 前缀和.下一个取反 , then 赋值为 起点.下一个取反 存入 起点
    for (let i = left; i < right; i++) {
      start.next = then.next;
      then.next = pre.next;
      pre.next = then;
      then = start.next!;
    } // 让 下标 i 从 左边界 开始计数，下标 i 小于 右边界 就继续
    return dummy.next; // 返回 哨兵节点.下一个
  }
  const cases = [
    { in: [1, 2, 3, 4, 5], l: 2, r: 4, want: [1, 4, 3, 2, 5] },
    { in: [5], l: 1, r: 1, want: [5] },
    { in: [1, 2, 3, 4, 5], l: 1, r: 5, want: [5, 4, 3, 2, 1] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    const got = toArr(reverseBetween(build(c.in), c.l, c.r));
    if (JSON.stringify(got) !== JSON.stringify(c.want)) {
      fail = true;
      console.log('FAIL ' + got);
    }
  } // 打印输出
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
