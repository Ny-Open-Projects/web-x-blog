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

  class Status {
    // 定义类型
    val: number; // 值: number;
    ptr: ListNode; // ptr: ListNode;
    constructor(val: number, ptr: ListNode) {
      // constructor(值: number, ptr: ListNode) {
      this.val = val; // 把 值; 写入 值
      this.ptr = ptr; // 把 ptr; 写入 this.ptr
    }
  }

  class PQ {
    // 定义类型
    private heap: Status[] = []; // 把 []; 写入 private heap: Status[]
    get length(): number {
      return this.heap.length;
    } // get 长度(): number { return this.堆.长度; }
    private compare(a: Status, b: Status): number {
      return a.val - b.val;
    }
    push(item: Status): void {
      // push(item: Status): void {
      this.heap.push(item); // 把 item 压入栈/数组尾部
      this._siftUp(this.heap.length - 1); // this._siftUp(this.堆.长度 减 1);
    }
    pop(): Status | undefined {
      // pop(): Status 按位或 undefined {
      if (this.heap.length === 0) return undefined; // 若 this.堆.长度 全等于 0，直接返回 undefined
      const lastElement = this.heap.pop() as Status; // 把 this.堆 弹出 ) as Status 存入 lastElement
      if (this.heap.length === 0) return lastElement; // 若 this.堆.长度 全等于 0，直接返回 lastElement
      const returnItem = this.heap[0]; // 把 this.堆[0] 存入 returnItem
      this.heap[0] = lastElement; // 把 lastElement; 写入 this.heap[0]
      this._siftDown(0); // this._siftDown(0);
      return returnItem; // 返回 returnItem
    }
    private _siftUp(index: number): void {
      // private _siftUp(index: number): void {
      while (index > 0) {
        // 循环，直到不满足「index 超过 0」
        const parentIndex = Math.floor((index - 1) / 2); // 把 向下取整((index 减 1) 除以 2) 存入 parentIndex
        if (this.compare(this.heap[parentIndex], this.heap[index]) > 0) {
          // 若 this.compare(this.堆[parentIndex], this.堆[index]) 超过 0
          const t = this.heap[parentIndex];
          this.heap[parentIndex] = this.heap[index];
          this.heap[index] = t;
          index = parentIndex; // 把 parentIndex 存入 index
        } else break; // 否则
      }
    }
    private _siftDown(index: number): void {
      // private _siftDown(index: number): void {
      const size = this.heap.length; // 把 this.堆.长度 存入 大小
      for (;;) {
        // for (;;) {
        let smallest = index; // 把 index 存入 smallest
        const leftChild = 2 * index + 1; // 把 2 乘 index 加 1 存入 leftChild
        const rightChild = 2 * index + 2; // 把 2 乘 index 加 2 存入 rightChild
        if (
          leftChild < size &&
          this.compare(this.heap[leftChild], this.heap[smallest]) < 0
        )
          smallest = leftChild;
        if (
          rightChild < size &&
          this.compare(this.heap[rightChild], this.heap[smallest]) < 0
        )
          smallest = rightChild;
        if (smallest !== index) {
          // 若 smallest 不等于 index
          const t = this.heap[index];
          this.heap[index] = this.heap[smallest];
          this.heap[smallest] = t;
          index = smallest; // 把 smallest 存入 index
        } else break; // 否则
      }
    }
  }

  function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
    // 定义函数/方法 mergeKLists
    const queue = new PQ(); // 把 new PQ() 存入 队列
    for (const node of lists) {
      // for (const 节点 of lists) {
      if (node !== null) queue.push(new Status(node.val, node)); // 若 节点 不等于 null) 队列 追加 new Status(节点.值, 节点));
    }
    const head = new ListNode(0); // 把 new ListNode(0) 存入 头节点
    let tail = head; // 把 头节点 存入 尾节点
    while (queue.length > 0) {
      // 循环，直到不满足「队列.长度 超过 0」
      const f = queue.pop() as Status; // 把 队列 弹出 ) as Status 存入 f
      tail.next = f.ptr; // 把 f.ptr; 写入 下一个
      tail = tail.next; // 把 尾节点.下一个 存入 尾节点
      if (f.ptr.next !== null) {
        // 若 f.ptr.下一个 不等于 null
        queue.push(new Status(f.ptr.next.val, f.ptr.next)); // 把 new Status(f.ptr.下一个.值, f.ptr.下一个 压入栈/数组尾部
      }
    }
    return head.next; // 返回 头节点.下一个
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
