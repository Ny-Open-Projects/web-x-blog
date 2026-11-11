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

  interface HeapItem {
    val: number;
    id: number;
    node: ListNode;
  } // 定义类型

  class MinHeap {
    // 定义类型
    private heap: HeapItem[] = []; // 把 []; 写入 private heap: HeapItem[]
    private counter = 0; // 把 0; 写入 private counter

    size(): number {
      return this.heap.length;
    } // 大小(): number { return this.堆.长度; }

    // 插入（对应 python heapq.heappush((val, id(node), node))，id 用自增计数充当 tiebreak）
    insert(val: number, node: ListNode): void {
      // insert(值: number, 节点: ListNode): void {
      this.heap.push({ val: val, id: this.counter++, node: node }); // 把 { 值: 值, id: this.counter 加一 , 节点: 节点 } 压入栈/数组尾部
      this.shiftUp(this.heap.length - 1); // this.shiftUp(this.堆.长度 减 1);
    }

    pop(): ListNode | null {
      // pop(): ListNode 按位或 null {
      if (this.heap.length === 0) return null; // 若 this.堆.长度 全等于 0，直接返回 null
      const first = this.heap[0]; // 把 this.堆[0] 存入 first
      const last = this.heap.pop() as HeapItem; // 把 this.堆 弹出 ) as HeapItem 存入 last
      if (this.heap.length > 0) {
        // 若 this.堆.长度 超过 0
        this.heap[0] = last; // 把 last; 写入 this.heap[0]
        this.shiftDown(0); // this.shiftDown(0);
      }
      return first.node; // 返回 first.节点
    }

    private less(a: HeapItem, b: HeapItem): boolean {
      // private less(数组: HeapItem, b: HeapItem): boolean {
      if (a.val !== b.val) return a.val < b.val; // 若 数组.值 不等于 b.值，直接返回 数组.值 小于 b.值
      return a.id < b.id; // 返回 数组.id 小于 b.id
    }

    private swap(i: number, j: number): void {
      // private 交换 下标 i: number, 下标 j: number): void {
      const t = this.heap[i];
      this.heap[i] = this.heap[j];
      this.heap[j] = t;
    }

    private shiftUp(i: number): void {
      // private shiftUp(下标 i: number): void {
      while (i > 0) {
        // 循环，直到不满足「下标 i 超过 0」
        const pi = (i - 1) >> 1; // 把 (下标 i 减 1) 超过 超过 1 存入 pi
        if (this.less(this.heap[i], this.heap[pi])) {
          this.swap(pi, i);
          i = pi;
        } else break; // 否则
      }
    }

    private shiftDown(i: number): void {
      // private shiftDown(下标 i: number): void {
      const n = this.heap.length; // 把 this.堆.长度 存入 元素个数
      for (;;) {
        // for (;;) {
        let smallest = i; // 把 下标 i 存入 smallest
        const li = 2 * i + 1,
          ri = 2 * i + 2; // 把 2 乘 下标 i 加 1, ri 赋值为 2 乘 下标 i 加 2 存入 li
        if (li < n && this.less(this.heap[li], this.heap[smallest]))
          smallest = li;
        if (ri < n && this.less(this.heap[ri], this.heap[smallest]))
          smallest = ri;
        if (smallest === i) break; // 若 smallest 全等于 下标 i) break;
        this.swap(i, smallest); // this.交换 下标 i, smallest);
        i = smallest; // 把 smallest 存入 下标 i
      }
    }
  }

  function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
    // 定义函数/方法 mergeKLists
    const res = new ListNode(0); // 把 new ListNode(0) 存入 结果
    let p = res; // 把 结果 存入 节点
    const h = new MinHeap(); // 把 new MinHeap() 存入 h
    for (const l of lists) {
      // for (const 左指针 of lists) {
      if (l) h.insert(l.val, l); // 若 左指针) h 插入 左指针.值, 左指针);
    }
    while (h.size() > 0) {
      // 循环，直到不满足「h.大小() 超过 0」
      const n = h.pop() as ListNode; // 把 h 弹出 ) as ListNode 存入 元素个数
      p.next = n; // 把 元素个数; 写入 下一个
      p = p.next; // 把 节点.下一个 存入 节点
      if (n.next) h.insert(n.next.val, n.next); // 若 元素个数.下一个) h 插入 元素个数.下一个.值, 元素个数.下一个);
    }
    return res.next; // 返回 结果.下一个
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
