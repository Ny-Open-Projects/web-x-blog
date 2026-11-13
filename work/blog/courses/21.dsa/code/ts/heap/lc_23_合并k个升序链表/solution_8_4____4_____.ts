// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133499836
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  class ListNode {
    // 定义类型
    val: number; // 值: number;
    next: ListNode | null; // 下一个: ListNode 按位或 null;
    constructor(val?: number, next?: ListNode | null) {
      // constructor(值?: number, 下一个?: ListNode 按位或 null) {
      this.val = val === undefined ? 0 : val; // 把 值 全等于 undefined ? 0 : 值; 写入 值
      this.next = next === undefined ? null : next; // 把 下一个 全等于 undefined ? null : 下一个; 写入 下一个
    }
  }

  function mergeTwo(a: ListNode | null, b: ListNode | null): ListNode | null {
    // 定义函数/方法 mergeTwo
    const dummy = new ListNode(0); // 把 new ListNode(0) 存入 哨兵节点
    let curr = dummy; // 把 哨兵节点 存入 当前值
    while (a !== null && b !== null) {
      // 循环，直到不满足「数组 不等于 null 且 b 不等于 null」
      if (a.val <= b.val) {
        // 若 数组.值 不超过 b.值
        curr.next = a; // 把 数组; 写入 下一个
        a = a.next; // 把 数组.下一个 存入 数组
      } else {
        // 否则
        curr.next = b; // 把 b; 写入 下一个
        b = b.next; // 把 b.下一个 存入 b
      }
      curr = curr.next; // 把 当前值.下一个 存入 当前值
    }
    curr.next = a !== null ? a : b; // 把 数组 不等于 null ? 数组 : b; 写入 下一个
    return dummy.next; // 返回 哨兵节点.下一个
  }

  // 合并 K 个升序链表 - 方案: 分治合并 (自底向上, 逐对合并)
  function merge_k_lists(lists: Array<ListNode | null>): ListNode | null {
    // 定义函数/方法 merge_k_lists
    let cur = lists.filter((l) => l !== null) as Array<ListNode | null>;
    if (cur.length === 0) return null; // 若 当前值.长度 全等于 0，直接返回 null
    while (cur.length > 1) {
      // 循环，直到不满足「当前值.长度 超过 1」
      const merged: Array<ListNode | null> = []; // 把 []; 写入 const merged: Array<ListNode | null>
      for (let i = 0; i < cur.length; i += 2) {
        // 让 下标 i 从 0 开始计数，下标 i 小于 当前值.长度 就继续
        const a = cur[i]; // 把 当前值[下标 i] 存入 数组
        const b = i + 1 < cur.length ? cur[i + 1] : null; // 把 下标 i 加 1 小于 当前值.长度 ? 当前值[下标 i 加 1] : null 存入 b
        merged.push(mergeTwo(a, b)); // 把 mergeTwo(数组, b 压入栈/数组尾部
      }
      cur = merged; // 把 merged 存入 当前值
    }
    return cur[0]; // 返回 当前值[0]
  }

  function build(vals: number[]): ListNode | null {
    // 定义函数/方法 build
    const dummy = new ListNode(0); // 把 new ListNode(0) 存入 哨兵节点
    let cur = dummy; // 把 哨兵节点 存入 当前值
    for (const v of vals) {
      cur.next = new ListNode(v);
      cur = cur.next;
    } // 把 new ListNode(值); 当前值 赋值为 当前值.下一个; } 写入 下一个
    return dummy.next; // 返回 哨兵节点.下一个
  }

  function toList(node: ListNode | null): number[] {
    // 定义函数/方法 toList
    const res: number[] = []; // 把 []; 写入 const res: number[]
    while (node) {
      res.push(node.val);
      node = node.next;
    } // 循环，直到不满足「节点) { 结果 追加 节点.值); 节点 赋值为 节点.下一个; }」
    return res; // 返回 结果
  }

  const cases: { in: number[][]; want: number[] }[] = [
    {
      in: [
        [1, 4, 5],
        [1, 3, 4],
        [2, 6],
      ],
      want: [1, 1, 2, 3, 4, 4, 5, 6],
    },
    { in: [], want: [] },
    { in: [[1]], want: [1] },
    { in: [[1], [0]], want: [0, 1] },
    {
      in: [
        [-2, -1],
        [0, 3],
      ],
      want: [-2, -1, 0, 3],
    },
    { in: [[5], [1, 2, 3], [4]], want: [1, 2, 3, 4, 5] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = toList(merge_k_lists(c.in.map(build))); // 把 toList(merge_k_lists(字符.in.映射表(build))) 存入 got
    if (got.length !== c.want.length || got.some((v, i) => v !== c.want[i])) {
      fail = true; // 把 true 存入 fail
      console.log('FAIL merge_k_lists(%o)=%o want %o', c.in, got, c.want); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
