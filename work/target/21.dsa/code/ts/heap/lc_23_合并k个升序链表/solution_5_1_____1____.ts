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
    idx: number;
    node: ListNode;
  } // 定义类型

  // 小顶堆（heapq 风格）：元组 (val, i, node) 比较，val 相同时按链表序号 i
  class MinHeap {
    // 定义类型
    private heap: HeapItem[] = []; // 把 []; 写入 private heap: HeapItem[]

    push(item: HeapItem): void {
      // push(item: HeapItem): void {
      this.heap.push(item); // 把 item 压入栈/数组尾部
      let i = this.heap.length - 1; // 把 this.堆.长度 减 1 存入 下标 i
      while (i > 0) {
        // 循环，直到不满足「下标 i 超过 0」
        const p = (i - 1) >> 1; // 把 (下标 i 减 1) 超过 超过 1 存入 节点
        if (this.less(this.heap[i], this.heap[p])) {
          // 若 this.less(this.堆[下标 i], this.堆[节点]
          const t = this.heap[i];
          this.heap[i] = this.heap[p];
          this.heap[p] = t;
          i = p; // 把 节点 存入 下标 i
        } else break; // 否则
      }
    }

    pop(): HeapItem | undefined {
      // pop(): HeapItem 按位或 undefined {
      if (this.heap.length === 0) return undefined; // 若 this.堆.长度 全等于 0，直接返回 undefined
      const top = this.heap[0]; // 把 this.堆[0] 存入 top
      const last = this.heap.pop() as HeapItem; // 把 this.堆 弹出 ) as HeapItem 存入 last
      if (this.heap.length > 0) {
        // 若 this.堆.长度 超过 0
        this.heap[0] = last; // 把 last; 写入 this.heap[0]
        let i = 0; // 把 0 存入 下标 i
        const n = this.heap.length; // 把 this.堆.长度 存入 元素个数
        for (;;) {
          // for (;;) {
          let smallest = i; // 把 下标 i 存入 smallest
          const l = 2 * i + 1,
            r = 2 * i + 2; // 把 2 乘 下标 i 加 1, 右指针 赋值为 2 乘 下标 i 加 2 存入 左指针
          if (l < n && this.less(this.heap[l], this.heap[smallest]))
            smallest = l;
          if (r < n && this.less(this.heap[r], this.heap[smallest]))
            smallest = r;
          if (smallest === i) break; // 若 smallest 全等于 下标 i) break;
          const t = this.heap[i];
          this.heap[i] = this.heap[smallest];
          this.heap[smallest] = t;
          i = smallest; // 把 smallest 存入 下标 i
        }
      }
      return top; // 返回 top
    }

    get length(): number {
      return this.heap.length;
    } // get 长度(): number { return this.堆.长度; }

    private less(a: HeapItem, b: HeapItem): boolean {
      // private less(数组: HeapItem, b: HeapItem): boolean {
      if (a.val !== b.val) return a.val < b.val; // 若 数组.值 不等于 b.值，直接返回 数组.值 小于 b.值
      return a.idx < b.idx; // 返回 数组.idx 小于 b.idx
    }
  }

  // 合并 K 个升序链表 - 方案: 小顶堆 (heapq)
  function merge_k_lists(lists: Array<ListNode | null>): ListNode | null {
    // 定义函数/方法 merge_k_lists
    const heap = new MinHeap(); // 把 new MinHeap() 存入 堆
    for (let i = 0; i < lists.length; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 lists.长度 就继续
      const node = lists[i]; // 把 lists[下标 i] 存入 节点
      if (node) heap.push({ val: node.val, idx: i, node: node }); // 若 节点) 堆 追加 { 值: 节点.值, idx: 下标 i, 节点: 节点 });
    }
    const dummy = new ListNode(0); // 把 new ListNode(0) 存入 哨兵节点
    let curr = dummy; // 把 哨兵节点 存入 当前值
    while (heap.length > 0) {
      // 循环，直到不满足「堆.长度 超过 0」
      const item = heap.pop() as HeapItem; // 把 堆 弹出 ) as HeapItem 存入 item
      const node = item.node; // 把 item.节点 存入 节点
      curr.next = node; // 把 节点; 写入 下一个
      curr = curr.next; // 把 当前值.下一个 存入 当前值
      if (node.next)
        heap.push({ val: node.next.val, idx: item.idx, node: node.next }); // 若 节点.下一个) 堆 追加 { 值: 节点.下一个.值, idx: item.idx, 节点: 节点.下一个 });
    }
    return dummy.next; // 返回 哨兵节点.下一个
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
