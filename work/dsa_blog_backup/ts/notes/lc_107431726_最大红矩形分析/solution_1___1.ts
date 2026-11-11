// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107431726

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function get_result(n: number, m: number, matrix: string[]): number {
  // 定义函数/方法 get_result
  let ans = 0;
  const height = new Array(m + 2).fill(0); // 把 0; const height 赋值为 new Array(映射表 加 2).fill(0) 存入 答案
  for (let k = 0; k < n; k++) {
    // 让 下标 k 从 0 开始计数，下标 k 小于 元素个数 就继续
    for (let i = 1; i <= m; i++) {
      if (matrix[k][i - 1] === '.') height[i]++;
      else height[i] = 0;
    } // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 就继续
    for (let a = 1; a <= m; a++) {
      // 让 数组 从 1 开始计数，数组 不超过 映射表 就继续
      let min_h = 50000; // 把 50000 存入 min_h
      for (let c = a; c <= m; c++) if (height[c] < min_h) min_h = height[c]; // 让 字符 从 数组 开始计数，字符 不超过 映射表 就继续
      const area = (m - a + 1) * min_h; // 把 (映射表 减 数组 加 1) 乘 min_h 存入 area
      if (area > ans) ans = area; // 若 area 超过 答案) 答案 赋值为 area;
    }
  }
  return ans; // 返回 答案
}
function get_result_card(n: number, m: number, matrix: string[]): number {
  // 定义函数/方法 get_result_card
  let ans = 0;
  const height = new Array(m + 2).fill(0); // 把 0; const height 赋值为 new Array(映射表 加 2).fill(0) 存入 答案
  for (let k = 0; k < n; k++) {
    // 让 下标 k 从 0 开始计数，下标 k 小于 元素个数 就继续
    for (let i = 1; i <= m; i++) {
      if (matrix[k][i - 1] === '.') height[i]++;
      else height[i] = 0;
    } // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 就继续
    for (let a = 1; a <= m; a++) {
      // 让 数组 从 1 开始计数，数组 不超过 映射表 就继续
      const cur_h = height[a]; // 把 height[数组] 存入 cur_h
      let lo = a - 1;
      while (lo >= 1 && height[lo] >= cur_h) lo--;
      let hi = a + 1;
      while (hi <= m && height[hi] >= cur_h) hi++;
      const area = (hi - lo - 1) * cur_h; // 把 (右边界 减 左边界 减 1) 乘 cur_h 存入 area
      if (area > ans) ans = area; // 若 area 超过 答案) 答案 赋值为 area;
    }
  }
  return ans; // 返回 答案
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const matrix = ['.....', 'XXXXX', '.X...', '.....']; // 把 [「.....」, 「.....」, 「.....」, 「.....」] 存入 矩阵
  assertEq(get_result(4, 5, matrix), 6, 'brute'); // 断言校验
  assertEq(get_result_card(4, 5, matrix), 6, 'card'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
