// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133468244

class ListNode {
  // 定义类型
  val: number; // 值: number;
  next: ListNode | null; // 下一个: ListNode 按位或 null;
  constructor(val: number = 0, next: ListNode | null = null) {
    this.val = val;
    this.next = next; // 把 值; this.下一个 赋值为 下一个; 写入 值
  }
}
function buildList(vals: number[]): ListNode | null {
  // 定义函数/方法 buildList
  const dummy = new ListNode(0);
  let cur = dummy; // 把 new ListNode(0); let 当前值 赋值为 哨兵节点 存入 哨兵节点
  for (const v of vals) {
    cur.next = new ListNode(v);
    cur = cur.next;
  } // 把 new ListNode(值); 当前值 赋值为 当前值.下一个; } 写入 下一个
  return dummy.next; // 返回 哨兵节点.下一个
}
function listToArr(head: ListNode | null): number[] {
  // 定义函数/方法 listToArr
  const res: number[] = [];
  while (head) {
    res.push(head.val);
    head = head.next;
  }
  return res; // 把 头节点.值 压入栈/数组尾部
}

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

class MinHeap {
  // 定义类型
  heap: number[]; // 堆: number[];
  constructor() {
    this.heap = [];
  } // 把 []; } 写入 堆
  getParentIndex(i: number): number {
    return (i - 1) >> 1;
  }
  getLeftIndex(i: number): number {
    return (i << 1) + 1;
  }
  getRightIndex(i: number): number {
    return (i << 1) + 2;
  }
  swap(i: number, j: number): void {
    const t = this.heap[i];
    this.heap[i] = this.heap[j];
    this.heap[j] = t;
  }
  shiftUp(i: number): void {
    if (i === 0) return;
    const pi = this.getParentIndex(i);
    if (this.heap[pi] > this.heap[i]) {
      this.swap(pi, i);
      this.shiftUp(pi);
    }
  }
  shiftDown(i: number): void {
    // shiftDown(下标 i: number): void {
    const size = this.size();
    const li = this.getLeftIndex(i);
    const ri = this.getRightIndex(i);
    let smallest = i; // 把 下标 i 存入 smallest
    if (li < size && this.heap[li] < this.heap[i]) smallest = li; // 若 li 小于 大小 且 this.堆[li] 小于 this.堆[下标 i]) smallest 赋值为 li;
    if (ri < size && this.heap[ri] < this.heap[smallest]) smallest = ri;
    if (smallest !== i) {
      this.swap(smallest, i);
      this.shiftDown(smallest);
    }
  }
  insert(value: number): void {
    this.heap.push(value);
    this.shiftUp(this.heap.length - 1);
  } // 把 value 压入栈/数组尾部
  pop(): void {
    if (this.size() === 0) return;
    this.heap[0] = this.heap.pop()!;
    this.shiftDown(0);
  } // 弹出栈顶元素
  peak(): number | null {
    return this.size() === 0 ? null : this.heap[0];
  }
  size(): number {
    return this.heap.length;
  } // 大小(): number { return this.堆.长度; }
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const heap = new MinHeap(); // 把 new MinHeap() 存入 堆
  heap.insert(3);
  heap.insert(1);
  heap.insert(6);
  heap.insert(5);
  heap.insert(2);
  heap.insert(4); // 堆 插入 3); 堆 插入 1); 堆 插入 6); 堆 插入 5); 堆 插入 2); 堆 插入 4);
  assertEq(heap.heap, [1, 2, 4, 5, 3, 6], 'afterInsert'); // 断言校验
  assertEq(heap.peak(), 1, 'peek'); // 断言校验
  heap.pop(); // 弹出栈顶元素
  assertEq(heap.heap, [2, 3, 4, 5, 6], 'afterPop'); // 断言校验
  heap.pop(); // 弹出栈顶元素
  assertEq(heap.heap, [3, 5, 4, 6], 'afterPop2'); // 断言校验
  assertEq(heap.size(), 4, 'size'); // 断言校验
  const empty = new MinHeap(); // 把 new MinHeap() 存入 empty
  assertEq(empty.peak(), null, 'emptyPeek'); // 断言校验
  empty.pop(); // 弹出栈顶元素
  assertEq(empty.size(), 0, 'emptySize'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
