// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130536355
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
  function sortList(head: ListNode | null): ListNode | null {
    // 定义函数/方法 sortList
    if (!head || !head.next) return head; // 若 取反 头节点 或 取反 头节点.下一个，直接返回 头节点
    let slow = head,
      fast = head;
    while (fast.next && fast.next.next) {
      slow = slow.next!;
      fast = fast.next.next;
    }
    const mid = slow.next;
    slow.next = null; // 把 慢指针.下一个; 慢指针.下一个 赋值为 null 存入 中点
    const l = sortList(head),
      r = sortList(mid); // 把 sortList(头节点), 右指针 赋值为 sortList(中点) 存入 左指针
    const d = new ListNode();
    let p = d; // 把 new ListNode(); let 节点 赋值为 d 存入 d
    let a = l,
      b = r; // 把 左指针,b 赋值为 右指针 存入 数组
    while (a && b) {
      if (a.val <= b.val) {
        p.next = a;
        a = a.next;
      } else {
        p.next = b;
        b = b.next;
      }
      p = p.next;
    }
    p.next = a ? a : b;
    return d.next; // 把 数组?数组:b; return d.下一个; 写入 下一个
  }
  const cases = [
    { in: [4, 2, 1, 3], want: [1, 2, 3, 4] },
    { in: [], want: [] },
    { in: [-1, 5, 3, 4, 0], want: [-1, 0, 3, 4, 5] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    const got = toArr(sortList(build(c.in)));
    if (JSON.stringify(got) !== JSON.stringify(c.want)) {
      fail = true;
      console.log('FAIL ' + got);
    }
  } // 打印输出
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
