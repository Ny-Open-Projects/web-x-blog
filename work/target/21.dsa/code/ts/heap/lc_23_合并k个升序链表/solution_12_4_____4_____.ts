// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133499836
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
  function mergeKLists(lists: (ListNode | null)[]): ListNode | null {
    // 定义函数/方法 mergeKLists
    const pq: ListNode[] = []; // 把 []; 写入 const pq: ListNode[]
    const push = (n: ListNode) => {
      pq.push(n);
      pq.sort((a, b) => a.val - b.val);
    };
    for (const l of lists) if (l) push(l); // for(const 左指针 of lists) if(左指针) push(左指针);
    const d = new ListNode();
    let p = d; // 把 new ListNode(); let 节点 赋值为 d 存入 d
    while (pq.length) {
      const n = pq.shift()!;
      p.next = n;
      p = p.next!;
      if (n.next) push(n.next);
    }
    return d.next; // 返回 d.下一个
  }
  const cases = [
    {
      in: [
        [1, 4, 5],
        [1, 3, 4],
        [2, 6],
      ],
      want: [1, 1, 2, 3, 4, 4, 5, 6],
    },
    { in: [[]], want: [] },
    { in: [[1]], want: [1] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    const ls = c.in.map((x) => (x.length ? build(x) : null));
    const got = toArr(mergeKLists(ls));
    if (JSON.stringify(got) !== JSON.stringify(c.want)) {
      fail = true;
      console.log('FAIL ' + got);
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
