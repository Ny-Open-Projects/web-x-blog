// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108673483
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function binarySearch(arr: number[], target: number): number {
    // 定义函数/方法 binarySearch
    let left = 0,
      right = arr.length - 1; // 把 0, 右边界 赋值为 数组.长度 减 1 存入 左边界
    while (left <= right) {
      // 循环，直到不满足「左边界 不超过 右边界」
      const mid = Math.floor((left + right) / 2); // 把 向下取整((左边界 加 右边界) 除以 2) 存入 中点
      if (arr[mid] === target) return mid; // 若 数组[中点] 全等于 目标值，直接返回 中点
      if (arr[mid] < target)
        left = mid + 1; // 若 数组[中点] 小于 目标值) 左边界 赋值为 中点 加 1;
      else right = mid - 1; // 否则
    }
    return -1; // 返回 减 1
  }
  const cases = [
    { a: [1, 3, 5, 7, 9], t: 5, want: 2 },
    { a: [1, 3, 5, 7, 9], t: 4, want: -1 },
    { a: [], t: 5, want: -1 },
    { a: [1, 3, 5, 7, 9], t: 1, want: 0 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = binarySearch(c.a, c.t); // 把 binarySearch(字符.数组, 字符.另一字符串) 存入 got
    if (got !== c.want) {
      fail = true;
      console.log('FAIL', c, 'got', got);
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
