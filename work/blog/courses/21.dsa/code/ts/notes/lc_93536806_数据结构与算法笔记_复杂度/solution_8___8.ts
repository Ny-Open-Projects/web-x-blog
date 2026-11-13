// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  // 堆排序：时间复杂度 O(n log n)，原地排序
  function heapSort(arr: number[]): number[] {
    // 定义函数/方法 heapSort
    const n = arr.length; // 把 数组.长度 存入 元素个数

    function heapify(size: number, root: number): void {
      // 定义函数/方法 heapify
      let largest = root; // 把 根节点 存入 largest
      const left = 2 * root + 1; // 把 2 乘 根节点 加 1 存入 左边界
      const right = 2 * root + 2; // 把 2 乘 根节点 加 2 存入 右边界
      if (left < size && arr[left] > arr[largest]) largest = left; // 若 左边界 小于 大小 且 数组[左边界] 超过 数组[largest]) largest 赋值为 左边界;
      if (right < size && arr[right] > arr[largest]) largest = right; // 若 右边界 小于 大小 且 数组[右边界] 超过 数组[largest]) largest 赋值为 右边界;
      if (largest !== root) {
        // 若 largest 不等于 根节点
        const t = arr[root];
        arr[root] = arr[largest];
        arr[largest] = t;
        heapify(size, largest); // heapify(大小, largest);
      }
    }

    for (let i = Math.floor(n / 2) - 1; i >= 0; i--) heapify(n, i); // 让 下标 i 从 向下取整(元素个数 除以 2) 减 1 开始计数，下标 i 不低于 0 就继续
    for (let i = n - 1; i > 0; i--) {
      // 让 下标 i 从 元素个数 减 1 开始计数，下标 i 超过 0 就继续
      const t = arr[0];
      arr[0] = arr[i];
      arr[i] = t; // 把 数组[0]; 数组[0] 赋值为 数组[下标 i]; 数组[下标 i] 赋值为 另一字符串 存入 另一字符串
      heapify(i, 0); // heapify(下标 i, 0);
    }
    return arr; // 返回 数组
  }

  function eqArr(a: number[], b: number[]): boolean {
    // 定义函数/方法 eqArr
    if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    return true; // 返回 true
  }

  const cases: { in: number[]; want: number[] }[] = [
    { in: [3, 1, 4, 1, 5, 9, 2, 6], want: [1, 1, 2, 3, 4, 5, 6, 9] },
    { in: [], want: [] },
    { in: [1], want: [1] },
    { in: [5, 4, 3, 2, 1], want: [1, 2, 3, 4, 5] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = heapSort(c.in.slice()); // 把 heapSort(字符.in 截取 )) 存入 got
    if (!eqArr(got, c.want)) {
      // 若 取反 eqArr(got, 字符.want
      fail = true; // 把 true 存入 fail
      console.log('FAIL heapSort(%o)=%o want %o', c.in, got, c.want); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
