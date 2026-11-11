// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108673483
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function quickSelect(arr: number[], k: number): number {
    // 定义函数/方法 quickSelect
    const a = arr.slice(); // 把 数组 截取 ) 存入 数组
    function select(lo: number, hi: number, k: number): number {
      // 定义函数/方法 select
      if (lo === hi) return a[lo]; // 若 左边界 全等于 右边界，直接返回 数组[左边界]
      const pivot = a[hi]; // 把 数组[右边界] 存入 pivot
      let i = lo; // 把 左边界 存入 下标 i
      for (let j = lo; j < hi; j++) {
        // 让 下标 j 从 左边界 开始计数，下标 j 小于 右边界 就继续
        if (a[j] <= pivot) {
          // 若 数组[下标 j] 不超过 pivot
          const tmp = a[i];
          a[i] = a[j];
          a[j] = tmp; // 把 数组[下标 i]; 数组[下标 i] 赋值为 数组[下标 j]; 数组[下标 j] 赋值为 临时变量 存入 临时变量
          i++; // 下标 i 加一
        }
      }
      const tmp = a[i];
      a[i] = a[hi];
      a[hi] = tmp; // 把 数组[下标 i]; 数组[下标 i] 赋值为 数组[右边界]; 数组[右边界] 赋值为 临时变量 存入 临时变量
      if (i === k)
        return a[i]; // 若 下标 i 全等于 下标 k，直接返回 数组[下标 i]
      else if (i > k)
        return select(lo, i - 1, k); // 否则，若 下标 i 超过 下标 k) return select(左边界, 下标 i 减 1, 下标 k);
      else return select(i + 1, hi, k); // 否则
    }
    return select(0, a.length - 1, k); // 返回 select(0, 数组.长度 减 1, 下标 k)
  }
  const cases = [
    { a: [3, 1, 4, 1, 5, 9, 2, 6], k: 2, want: 2 },
    { a: [3, 1, 4, 1, 5, 9, 2, 6], k: 3, want: 3 },
    { a: [3, 1, 4, 1, 5, 9, 2, 6], k: 0, want: 1 },
    { a: [3, 1, 4, 1, 5, 9, 2, 6], k: 7, want: 9 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = quickSelect(c.a, c.k); // 把 quickSelect(字符.数组, 字符.下标 k) 存入 got
    if (got !== c.want) {
      fail = true;
      console.log('FAIL', c, 'got', got);
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
