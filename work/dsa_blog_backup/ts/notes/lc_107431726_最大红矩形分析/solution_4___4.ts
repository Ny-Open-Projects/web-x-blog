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

function max_red_rectangle(matrix: string[]): number {
  // 定义函数/方法 max_red_rectangle
  const n = matrix.length,
    m = matrix[0].length; // 把 矩阵.长度, 映射表 赋值为 矩阵[0].长度 存入 元素个数
  let ans = 0; // 把 0 存入 答案
  const height = new Array(m + 2).fill(0); // 把 new Array(映射表 加 2).fill(0) 存入 height
  for (let k = 0; k < n; k++) {
    // 让 下标 k 从 0 开始计数，下标 k 小于 元素个数 就继续
    for (let i = 1; i <= m; i++) {
      if (matrix[k][i - 1] === '.') height[i]++;
      else height[i] = 0;
    } // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 就继续
    const stack: number[] = [0]; // 把 [0]; 写入 const stack: number[]
    for (let i = 1; i <= m + 1; i++) {
      // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 加 1 就继续
      while (height[stack[stack.length - 1]] > height[i]) {
        // 循环，直到不满足「height[栈[栈.长度 减 1]] 超过 height[下标 i]」
        const now_h = height[stack.pop() as number]; // 把 height[栈 弹出 ) as number] 存入 now_h
        const width = i - stack[stack.length - 1] - 1; // 把 下标 i 减 栈[栈.长度 减 1] 减 1 存入 width
        ans = Math.max(ans, now_h * width); // 把 Math.取较大值 答案, now_h 乘 width) 存入 答案
      }
      stack.push(i); // 把 下标 i 压入栈/数组尾部
    }
  }
  return ans; // 返回 答案
}
function get_result_brute(n: number, m: number, matrix: string[]): number {
  // 定义函数/方法 get_result_brute
  let ans = 0;
  const height = new Array(m + 2).fill(0); // 把 0; const height 赋值为 new Array(映射表 加 2).fill(0) 存入 答案
  for (let k = 0; k < n; k++) {
    // 让 下标 k 从 0 开始计数，下标 k 小于 元素个数 就继续
    for (let i = 1; i <= m; i++) {
      if (matrix[k][i - 1] === '.') height[i]++;
      else height[i] = 0;
    } // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 就继续
    for (let a = 1; a <= m; a++) {
      let min_h = 50000;
      for (let c = a; c <= m; c++) if (height[c] < min_h) min_h = height[c];
      const area = (m - a + 1) * 0 + (a > 0 ? 0 : 0);
      const ar = c_index(a, m, height);
      if (ar > ans) ans = ar;
    } // 让 数组 从 1 开始计数，数组 不超过 映射表 就继续
  }
  return ans; // 返回 答案
}
function c_index(a: number, m: number, height: number[]): number {
  let min_h = 50000;
  for (let c = a; c <= m; c++) if (height[c] < min_h) min_h = height[c];
  return (m - a + 1) * min_h;
} // 定义函数/方法 c_index
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const matrix = ['.....', 'XXXXX', '.X...', '.....']; // 把 [「.....」, 「.....」, 「.....」, 「.....」] 存入 矩阵
  assertEq(max_red_rectangle(matrix), 6, 'mono'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
