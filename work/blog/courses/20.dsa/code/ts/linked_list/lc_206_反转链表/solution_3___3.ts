// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130510175
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
  function reverseList(head: ListNode | null): ListNode | null {
    let prev: ListNode | null = null,
      cur = head;
    while (cur) {
      const nx = cur.next;
      cur.next = prev;
      prev = cur;
      cur = nx;
    }
    return prev;
  } // 定义函数/方法 reverseList
  const cases = [
    { in: [1, 2, 3, 4, 5], want: [5, 4, 3, 2, 1] },
    { in: [], want: [] },
    { in: [1, 2], want: [2, 1] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    const got = toArr(reverseList(build(c.in)));
    if (JSON.stringify(got) !== JSON.stringify(c.want)) {
      fail = true;
      console.log('FAIL ' + got);
    }
  } // 打印输出
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
