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
  static swap(arr: number[], i: number, j: number): void {
    // static 交换 数组: number[], 下标 i: number, 下标 j: number): void {
    if (i === j) return; // 若 下标 i 全等于 下标 j) return;
    const t = arr[i];
    arr[i] = arr[j];
    arr[j] = t;
  }
  static maxHeapify(arr: number[], i: number, size: number): void {
    const l = (i << 1) + 1,
      r = (i << 1) + 2; // 把 (下标 i 小于 小于 1) 加 1, 右指针 赋值为 (下标 i 小于 小于 1) 加 2 存入 左指针
    let largest = i; // 把 下标 i 存入 largest
    if (l < size && arr[l] > arr[largest]) largest = l; // 若 左指针 小于 大小 且 数组[左指针] 超过 数组[largest]) largest 赋值为 左指针;
    if (r < size && arr[r] > arr[largest]) largest = r; // 若 右指针 小于 大小 且 数组[右指针] 超过 数组[largest]) largest 赋值为 右指针;
    if (largest !== i) {
      MaxHeap.swap(arr, i, largest);
      MaxHeap.maxHeapify(arr, largest, size);
    }
  }
  sort(): number[] {
    // sort(): number[] {
    const i_arr = this.heap; // 把 this.堆 存入 i_arr
    const n = i_arr.length; // 把 i_arr.长度 存入 元素个数
    if (n <= 1) return i_arr; // 若 元素个数 不超过 1，直接返回 i_arr
    for (let i = Math.floor(n / 2) - 1; i >= 0; i--)
      MaxHeap.maxHeapify(i_arr, i, n); // 让 下标 i 从 向下取整(元素个数 除以 2) 减 1 开始计数，下标 i 不低于 0 就继续
    for (let j = 0; j < n - 1; j++) {
      // 让 下标 j 从 0 开始计数，下标 j 小于 元素个数 减 1 就继续
      MaxHeap.swap(i_arr, 0, n - 1 - j); // MaxHeap.交换 i_arr, 0, 元素个数 减 1 减 下标 j);
      MaxHeap.maxHeapify(i_arr, 0, n - 1 - j - 1); // MaxHeap.maxHeapify(i_arr, 0, 元素个数 减 1 减 下标 j 减 1);
    }
    return i_arr; // 返回 i_arr
  }
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const mh = new MaxHeap(); // 把 new MaxHeap() 存入 mh
  mh.heap = [1, 10, 9, 5, 3, 11, 3, 9, 11, 13, 1, -1, 98]; // 把 [1, 10, 9, 5, 3, 11, 3, 9, 11, 13, 1, 减 1, 98]; 写入 堆
  assertEq(
    mh.sort(),
    [-1, 1, 1, 3, 3, 5, 9, 9, 10, 11, 11, 13, 98],
    'heapSort',
  ); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
