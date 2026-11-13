// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  // 顺序查找：最坏时间复杂度 O(n)
  function linearSearch(arr: number[], target: number): number {
    // 定义函数/方法 linearSearch
    for (let i = 0; i < arr.length; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
      if (arr[i] === target) return i; // 若 数组[下标 i] 全等于 目标值，直接返回 下标 i
    }
    return -1; // 返回 减 1
  }

  const cases: { arr: number[]; target: number; want: number }[] = [
    { arr: [3, 1, 4, 1, 5, 9, 2, 6], target: 5, want: 4 },
    { arr: [3, 1, 4, 1, 5, 9, 2, 6], target: 7, want: -1 },
    { arr: [], target: 1, want: -1 },
    { arr: [9], target: 9, want: 0 },
    { arr: [9], target: 8, want: -1 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = linearSearch(c.arr, c.target); // 把 linearSearch(字符.数组, 字符.目标值) 存入 got
    if (got !== c.want) {
      // 若 got 不等于 字符.want
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL linearSearch(%o,%d)=%d want %d',
        c.arr,
        c.target,
        got,
        c.want,
      ); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
