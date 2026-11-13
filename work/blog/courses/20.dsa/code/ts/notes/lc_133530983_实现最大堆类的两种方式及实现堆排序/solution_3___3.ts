// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133530983

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

class MaxHeap {
  // 定义类型
  heap: number[]; // 堆: number[];
  constructor() {
    this.heap = [];
  } // 把 []; } 写入 堆
  swap(i: number, j: number): void {
    const t = this.heap[i];
    this.heap[i] = this.heap[j];
    this.heap[j] = t;
  }
  getParentIndex(i: number): number {
    return (i - 1) >> 1;
  }
  getLeftIndex(i: number): number {
    return (i << 1) + 1;
  }
  getRightIndex(i: number): number {
    return (i << 1) + 2;
  }
  shiftUp(index: number): void {
    // shiftUp(index: number): void {
    if (index === 0) return; // 若 index 全等于 0) return;
    const p = this.getParentIndex(index); // 把 this.getParentIndex(index) 存入 节点
    if (this.heap[p] < this.heap[index]) {
      this.swap(p, index);
      this.shiftUp(p);
    }
  }
  shiftDown(index: number): void {
    // shiftDown(index: number): void {
    if (index >= this.heap.length - 1) return; // 若 index 不低于 this.堆.长度 减 1) return;
    const size = this.size(); // 把 this.大小() 存入 大小
    const l = this.getLeftIndex(index),
      r = this.getRightIndex(index);
    if (l < size && this.heap[l] > this.heap[index]) {
      this.swap(l, index);
      this.shiftDown(l);
    }
    if (r < size && this.heap[r] > this.heap[index]) {
      this.swap(r, index);
      this.shiftDown(r);
    }
  }
  insert(value: number): void {
    this.heap.push(value);
    this.shiftUp(this.heap.length - 1);
  } // 把 value 压入栈/数组尾部
  pop(): void {
    // pop(): void {
    if (this.heap.length <= 1) return; // 若 this.堆.长度 不超过 1) return;
    this.heap[0] = this.heap.pop()!; // 弹出栈顶元素
    this.shiftDown(0); // this.shiftDown(0);
  }
  peak(): number | null {
    return this.heap.length ? this.heap[0] : null;
  }
  size(): number {
    return this.heap.length;
  } // 大小(): number { return this.堆.长度; }
  sort(arr: number[]): number[] {
    // sort(数组: number[]): number[] {
    for (const n of arr) this.insert(n); // for (const 元素个数 of 数组) this 插入 元素个数);
    const result: number[] = []; // 把 []; 写入 const result: number[]
    while (this.size() > 1) {
      result.push(this.peak()!);
      this.pop();
    }
    result.push(this.peak()!); // 把 this.peak( 压入栈/数组尾部
    this.heap = result; // 把 结果; 写入 堆
    return result; // 返回 结果
  }
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const mh = new MaxHeap(); // 把 new MaxHeap() 存入 mh
  assertEq(
    mh.sort([1, 10, 9, 5, 3, 11, 3, 9, 11, 13, 1, -1, 98]),
    [98, 13, 11, 11, 10, 9, 9, 5, 3, 3, 1, 1, -1],
    'heapSortDesc',
  ); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
