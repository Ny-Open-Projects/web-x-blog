// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  // 插入排序：最坏时间复杂度 O(n^2)，最好 O(n)
  function insertionSort(arr: number[]): number[] {
    // 定义函数/方法 insertionSort
    for (let i = 1; i < arr.length; i++) {
      // 让 下标 i 从 1 开始计数，下标 i 小于 数组.长度 就继续
      const key = arr[i]; // 把 数组[下标 i] 存入 key
      let j = i - 1; // 把 下标 i 减 1 存入 下标 j
      while (j >= 0 && arr[j] > key) {
        // 循环，直到不满足「下标 j 不低于 0 且 数组[下标 j] 超过 key」
        arr[j + 1] = arr[j]; // 把 数组[下标 j]; 写入 arr[j + 1]
        j--; // 下标 j 减一
      }
      arr[j + 1] = key; // 把 key; 写入 arr[j + 1]
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
    const got = insertionSort(c.in.slice()); // 把 insertionSort(字符.in 截取 )) 存入 got
    if (!eqArr(got, c.want)) {
      // 若 取反 eqArr(got, 字符.want
      fail = true; // 把 true 存入 fail
      console.log('FAIL insertionSort(%o)=%o want %o', c.in, got, c.want); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
