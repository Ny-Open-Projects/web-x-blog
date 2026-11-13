// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function partition(arr: number[], left: number, right: number): number {
    // 定义函数/方法 partition
    const pivot = arr[right]; // 把 数组[右边界] 存入 pivot
    let i = left; // 把 左边界 存入 下标 i
    for (let j = left; j < right; j++) {
      // 让 下标 j 从 左边界 开始计数，下标 j 小于 右边界 就继续
      if (arr[j] < pivot) {
        // 若 数组[下标 j] 小于 pivot
        const t = arr[i];
        arr[i] = arr[j];
        arr[j] = t;
        i++; // 下标 i 加一
      }
    }
    const t = arr[i];
    arr[i] = arr[right];
    arr[right] = t; // 把 数组[下标 i]; 数组[下标 i] 赋值为 数组[右边界]; 数组[右边界] 赋值为 另一字符串 存入 另一字符串
    return i; // 返回 下标 i
  }

  // 快速排序：平均时间复杂度 O(n log n)
  function quickSort(
    arr: number[],
    left = 0,
    right: number | null = null,
  ): number[] {
    // 定义函数/方法 quickSort
    const r = right === null ? arr.length - 1 : right; // 把 右边界 全等于 null ? 数组.长度 减 1 : 右边界 存入 右指针
    if (left < r) {
      // 若 左边界 小于 右指针
      const pivotIndex = partition(arr, left, r); // 把 partition(数组, 左边界, 右指针) 存入 pivotIndex
      quickSort(arr, left, pivotIndex - 1); // quickSort(数组, 左边界, pivotIndex 减 1);
      quickSort(arr, pivotIndex + 1, r); // quickSort(数组, pivotIndex 加 1, 右指针);
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
    const got = quickSort(c.in.slice()); // 把 quickSort(字符.in 截取 )) 存入 got
    if (!eqArr(got, c.want)) {
      // 若 取反 eqArr(got, 字符.want
      fail = true; // 把 true 存入 fail
      console.log('FAIL quickSort(%o)=%o want %o', c.in, got, c.want); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
