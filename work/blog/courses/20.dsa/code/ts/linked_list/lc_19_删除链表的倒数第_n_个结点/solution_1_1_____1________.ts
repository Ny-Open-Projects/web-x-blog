// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145093774
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
  function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
    // 定义函数/方法 removeNthFromEnd
    const dummy = new ListNode(0);
    dummy.next = head;
    let f = dummy,
      s = dummy;
    for (let i = 0; i < n; i++) f = f.next!; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    while (f.next) {
      f = f.next;
      s = s.next!;
    } // 循环，直到不满足「f.下一个){f 赋值为 f.下一个;字符串 赋值为 字符串.下一个取反 ;}」
    s.next = s.next!.next;
    return dummy.next; // 把 字符串.下一个取反 .下一个; return 哨兵节点.下一个; 写入 下一个
  }
  const cases = [
    { in: [1, 2, 3, 4, 5], n: 2, want: [1, 2, 3, 5] },
    { in: [1], n: 1, want: [] },
    { in: [1, 2], n: 2, want: [2] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    const got = toArr(removeNthFromEnd(build(c.in), c.n));
    if (JSON.stringify(got) !== JSON.stringify(c.want)) {
      fail = true;
      console.log('FAIL ' + got);
    }
  } // 打印输出
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
