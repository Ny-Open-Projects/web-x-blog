// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134073792
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function quickSort(nums: number[]): number[] {
    // 定义函数/方法 quickSort
    const a = nums.slice(); // 把 数组 截取 ) 存入 数组
    function partition(low: number, high: number): number {
      // 定义函数/方法 partition
      const pivot = a[high]; // 把 数组[high] 存入 pivot
      let i = low - 1; // 把 low 减 1 存入 下标 i
      for (let j = low; j < high; j++) {
        // 让 下标 j 从 low 开始计数，下标 j 小于 high 就继续
        if (a[j] <= pivot) {
          // 若 数组[下标 j] 不超过 pivot
          i++; // 下标 i 加一
          const t = a[i];
          a[i] = a[j];
          a[j] = t;
        }
      }
      const t = a[i + 1];
      a[i + 1] = a[high];
      a[high] = t;
      return i + 1; // 返回 下标 i 加 1
    }
    function qs(low: number, high: number): void {
      // 定义函数/方法 qs
      if (low < high) {
        // 若 low 小于 high
        const pi = partition(low, high); // 把 partition(low, high) 存入 pi
        qs(low, pi - 1); // qs(low, pi 减 1);
        qs(pi + 1, high); // qs(pi 加 1, high);
      }
    }
    qs(0, a.length - 1); // qs(0, 数组.长度 减 1);
    return a; // 返回 数组
  }
  const cases: number[][] = [
    [15, 4, 23, 52, 1],
    [3, 1, 2, 5, 4],
    [9, -20, 99, 3, 6, 8, 10, 1, 2, 1],
    [
      -2, 1, 0, -9, 1, 3, 9, 99, 9, -30, -100, 100, 88, 88, 20, 1, 0, 3, 4, 5,
      -20,
    ],
  ];
  const wants: number[][] = [
    [1, 4, 15, 23, 52],
    [1, 2, 3, 4, 5],
    [-20, 1, 1, 2, 3, 6, 8, 9, 10, 99],
    [
      -100, -30, -20, -9, -2, 0, 0, 1, 1, 1, 3, 3, 4, 5, 9, 9, 20, 88, 88, 99,
      100,
    ],
  ];
  let fail = false; // 把 false 存入 fail
  for (let i = 0; i < cases.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 cases.长度 就继续
    const got = quickSort(cases[i]); // 把 quickSort(cases[下标 i]) 存入 got
    if (got.length !== wants[i].length) {
      fail = true;
      console.log('FAIL len ' + i);
      continue;
    }
    for (let j = 0; j < got.length; j++)
      if (got[j] !== wants[i][j]) {
        fail = true;
        console.log(
          'FAIL case ' +
            i +
            ' idx ' +
            j +
            ' got ' +
            got[j] +
            ' want ' +
            wants[i][j],
        );
      } // 让 下标 j 从 0 开始计数，下标 j 小于 got.长度 就继续
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
