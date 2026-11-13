// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145344649

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual); // 把 JSON.stringify(actual) 存入 数组
  const e = JSON.stringify(expected); // 把 JSON.stringify(expected) 存入 e
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

class Heap {
  // 定义类型
  heap: any[]; // 堆: any[];
  compareFn: (a: any, b: any) => boolean;
  constructor(compareFn: (a: any, b: any) => boolean) {
    this.heap = [];
    this.compareFn = compareFn;
  }
  size(): number {
    return this.heap.length;
  } // 大小(): number { return this.堆.长度; }
  peek(): any {
    return this.heap.length ? this.heap[0] : null;
  } // peek(): any { return this.堆.长度 ? this.堆[0] : null; }
  insert(value: any): void {
    // insert(value: any): void {
    this.heap.push(value); // 把 value 压入栈/数组尾部
    this._shiftUp(this.heap.length - 1); // this._shiftUp(this.堆.长度 减 1);
  }
  pop(): any {
    // pop(): any {
    if (this.heap.length === 1) return this.heap.pop(); // 若 this.堆.长度 全等于 1，直接返回 this.堆 弹出 )
    const first = this.heap[0]; // 把 this.堆[0] 存入 first
    this.heap[0] = this.heap.pop()!; // 弹出栈顶元素
    this._shiftDown(0); // this._shiftDown(0);
    return first; // 返回 first
  }
  _shiftUp(i: number): void {
    // _shiftUp(下标 i: number): void {
    while (i > 0 && this.compareFn(this.heap[(i - 1) >> 1], this.heap[i])) {
      const p = (i - 1) >> 1; // 把 (下标 i 减 1) 超过 超过 1 存入 节点
      [this.heap[p], this.heap[i]] = [this.heap[i], this.heap[p]];
      i = p; // 把 节点 存入 下标 i
    }
  }
  _shiftDown(pi: number): void {
    // _shiftDown(pi: number): void {
    const size = this.heap.length; // 把 this.堆.长度 存入 大小
    let largest = pi; // 把 pi 存入 largest
    const left = 2 * pi + 1,
      right = 2 * pi + 2; // 把 2 乘 pi 加 1, 右边界 赋值为 2 乘 pi 加 2 存入 左边界
    if (left < size && this.compareFn(this.heap[largest], this.heap[left]))
      largest = left;
    if (right < size && this.compareFn(this.heap[largest], this.heap[right]))
      largest = right;
    if (largest !== pi) {
      // 若 largest 不等于 pi
      [this.heap[pi], this.heap[largest]] = [this.heap[largest], this.heap[pi]];
      this._shiftDown(largest); // this._shiftDown(largest);
    }
  }
}
class MinHeap extends Heap {
  constructor() {
    super((a, b) => a > b);
  }
} // 定义类型
class MaxHeap extends Heap {
  constructor() {
    super((a, b) => a < b);
  }
} // 定义类型
class MedianFinder {
  // 定义类型
  minHeap: MinHeap; // minHeap: MinHeap;
  maxHeap: MaxHeap; // maxHeap: MaxHeap;
  constructor() {
    this.minHeap = new MinHeap();
    this.maxHeap = new MaxHeap();
  }
  addNum(num: number): void {
    // addNum(num: number): void {
    if (this.maxHeap.size() === 0 || num <= this.maxHeap.peek())
      this.maxHeap.insert(num);
    else this.minHeap.insert(num); // 否则
    if (this.maxHeap.size() > this.minHeap.size() + 1)
      this.minHeap.insert(this.maxHeap.pop());
    else if (this.minHeap.size() > this.maxHeap.size())
      this.maxHeap.insert(this.minHeap.pop());
  }
  findMedian(): number {
    // findMedian(): number {
    if (this.maxHeap.size() === this.minHeap.size())
      return (this.maxHeap.peek() + this.minHeap.peek()) / 2;
    return this.maxHeap.peek(); // 返回 this.maxHeap.peek()
  }
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const mf = new MedianFinder(); // 把 new MedianFinder() 存入 mf
  for (const x of [1, 2, 3, 4, 5]) mf.addNum(x); // for (const x of [1, 2, 3, 4, 5]) mf.addNum(x);
  assertEq(mf.findMedian(), 3, 'MedianFinder 1..5'); // 断言校验
  const mf2 = new MedianFinder(); // 把 new MedianFinder() 存入 mf2
  for (const x of [5, 2, 3, 4, 1]) mf2.addNum(x); // for (const x of [5, 2, 3, 4, 1]) mf2.addNum(x);
  assertEq(mf2.findMedian(), 3, 'MedianFinder 5,2,3,4,1'); // 断言校验
  const mf3 = new MedianFinder(); // 把 new MedianFinder() 存入 mf3
  mf3.addNum(1); // mf3.addNum(1);
  assertEq(mf3.findMedian(), 1, 'MedianFinder single'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
