// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145344649

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

class Heap {
  // 定义类型
  heap: any[];
  compareFn: (a: any, b: any) => boolean;
  constructor(c: (a: any, b: any) => boolean) {
    this.heap = [];
    this.compareFn = c;
  }
  size(): number {
    return this.heap.length;
  } // 大小(): number { return this.堆.长度; }
  peek(): any {
    return this.heap.length ? this.heap[0] : null;
  } // peek(): any { return this.堆.长度 ? this.堆[0] : null; }
  insert(v: any): void {
    this.heap.push(v);
    this.su(this.heap.length - 1);
  } // 把 值 压入栈/数组尾部
  pop(): any {
    if (this.heap.length === 1) return this.heap.pop();
    const f = this.heap[0];
    this.heap[0] = this.heap.pop()!;
    this.sd(0);
    return f;
  } // 弹出栈顶元素
  su(i: number): void {
    while (i > 0 && this.compareFn(this.heap[(i - 1) >> 1], this.heap[i])) {
      const p = (i - 1) >> 1;
      [this.heap[p], this.heap[i]] = [this.heap[i], this.heap[p]];
      i = p;
    }
  }
  sd(pi: number): void {
    const s = this.heap.length;
    let lg = pi;
    const l = 2 * pi + 1,
      r = 2 * pi + 2;
    if (l < s && this.compareFn(this.heap[lg], this.heap[l])) lg = l;
    if (r < s && this.compareFn(this.heap[lg], this.heap[r])) lg = r;
    if (lg !== pi) {
      [this.heap[pi], this.heap[lg]] = [this.heap[lg], this.heap[pi]];
      this.sd(lg);
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
  minH: MinHeap;
  maxH: MaxHeap; // minH: MinHeap; maxH: MaxHeap;
  constructor() {
    this.minH = new MinHeap();
    this.maxH = new MaxHeap();
  }
  addNum(num: number): void {
    // addNum(num: number): void {
    if (this.maxH.size() === 0 || num <= this.maxH.peek())
      this.maxH.insert(num);
    else this.minH.insert(num);
    if (this.maxH.size() > this.minH.size() + 1)
      this.minH.insert(this.maxH.pop());
    else if (this.minH.size() > this.maxH.size())
      this.maxH.insert(this.minH.pop());
  }
  findMedian(): number {
    if (this.maxH.size() === this.minH.size())
      return (this.maxH.peek() + this.minH.peek()) / 2;
    return this.maxH.peek();
  }
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const mf = new MedianFinder(); // 把 new MedianFinder() 存入 mf
  for (const x of [1, 2, 3, 4, 5]) mf.addNum(x); // for (const x of [1, 2, 3, 4, 5]) mf.addNum(x);
  assertEq(mf.findMedian(), 3, 'm1'); // 断言校验
  const mf2 = new MedianFinder(); // 把 new MedianFinder() 存入 mf2
  for (const x of [5, 2, 3, 4, 1]) mf2.addNum(x); // for (const x of [5, 2, 3, 4, 1]) mf2.addNum(x);
  assertEq(mf2.findMedian(), 3, 'm2'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
