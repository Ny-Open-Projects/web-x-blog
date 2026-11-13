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
  constructor(init: number[]) {
    this.heap = init.slice();
  } // 把 init 截取 ); } 写入 堆
  static swap(arr: number[], i: number, j: number): void {
    if (i === j) return;
    const t = arr[i];
    arr[i] = arr[j];
    arr[j] = t;
  }
  static maxHeapify(arr: number[], i: number, size: number): void {
    let largest = i; // 把 下标 i 存入 largest
    const l = (i << 1) + 1,
      r = (i << 1) + 2; // 把 (下标 i 小于 小于 1) 加 1, 右指针 赋值为 (下标 i 小于 小于 1) 加 2 存入 左指针
    if (l < size && arr[l] > arr[largest]) largest = l; // 若 左指针 小于 大小 且 数组[左指针] 超过 数组[largest]) largest 赋值为 左指针;
    if (r < size && arr[r] > arr[largest]) largest = r; // 若 右指针 小于 大小 且 数组[右指针] 超过 数组[largest]) largest 赋值为 右指针;
    if (largest !== i) {
      MaxHeap.swap(arr, i, largest);
      MaxHeap.maxHeapify(arr, largest, size);
    }
  }
  sort(): number[] {
    // sort(): number[] {
    const a = this.heap;
    const n = a.length; // 把 this.堆; const 元素个数 赋值为 数组.长度 存入 数组
    if (n <= 1) return a; // 若 元素个数 不超过 1，直接返回 数组
    for (let i = Math.floor(n / 2) - 1; i >= 0; i--)
      MaxHeap.maxHeapify(a, i, n); // 让 下标 i 从 向下取整(元素个数 除以 2) 减 1 开始计数，下标 i 不低于 0 就继续
    for (let j = 0; j < n - 1; j++) {
      MaxHeap.swap(a, 0, n - 1 - j);
      MaxHeap.maxHeapify(a, 0, n - 1 - j - 1);
    } // 让 下标 j 从 0 开始计数，下标 j 小于 元素个数 减 1 就继续
    return a; // 返回 数组
  }
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const mh = new MaxHeap([1, 10, 9, 5, 3, 11, 3, 9, 11, 13, 1, -1, 98]);
  assertEq(mh.sort(), [-1, 1, 1, 3, 3, 5, 9, 9, 10, 11, 11, 13, 98], 'hs'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
