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

  function mergeTwoLists(
    a: ListNode | null,
    b: ListNode | null,
  ): ListNode | null {
    // 定义函数/方法 mergeTwoLists
    if (a === null) return b; // 若 数组 全等于 null，直接返回 b
    if (b === null) return a; // 若 b 全等于 null，直接返回 数组
    const head = new ListNode(0); // 把 new ListNode(0) 存入 头节点
    let tail = head; // 把 头节点 存入 尾节点
    let aPtr = a; // 把 数组 存入 aPtr
    let bPtr = b; // 把 b 存入 bPtr
    while (aPtr !== null && bPtr !== null) {
      // 循环，直到不满足「aPtr 不等于 null 且 bPtr 不等于 null」
      if (aPtr.val < bPtr.val) {
        // 若 aPtr.值 小于 bPtr.值
        tail.next = aPtr; // 把 aPtr; 写入 下一个
        aPtr = aPtr.next; // 把 aPtr.下一个 存入 aPtr
      } else {
        // 否则
        tail.next = bPtr; // 把 bPtr; 写入 下一个
        bPtr = bPtr.next; // 把 bPtr.下一个 存入 bPtr
      }
      tail = tail.next; // 把 尾节点.下一个 存入 尾节点
    }
    tail.next = aPtr !== null ? aPtr : bPtr; // 把 aPtr 不等于 null ? aPtr : bPtr; 写入 下一个
    return head.next; // 返回 头节点.下一个
  }

  function merge(
    lists: Array<ListNode | null>,
    l: number,
    r: number,
  ): ListNode | null {
    // 定义函数/方法 merge
    if (l === r) return lists[l]; // 若 左指针 全等于 右指针，直接返回 lists[左指针]
    if (l > r) return null; // 若 左指针 超过 右指针，直接返回 null
    const mid = Math.floor((l + r) / 2); // 把 向下取整((左指针 加 右指针) 除以 2) 存入 中点
    return mergeTwoLists(merge(lists, l, mid), merge(lists, mid + 1, r));
  }

  function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
    // 定义函数/方法 mergeKLists
    return merge(lists, 0, lists.length - 1); // 返回 merge(lists, 0, lists.长度 减 1)
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
    const got = toList(mergeKLists(c.in.map(build))); // 把 toList(mergeKLists(字符.in.映射表(build))) 存入 got
    if (got.length !== c.want.length || got.some((v, i) => v !== c.want[i])) {
      fail = true; // 把 true 存入 fail
      console.log('FAIL mergeKLists(%o)=%o want %o', c.in, got, c.want); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
