// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107431726
/**
 ** 笔记：最大红矩形分析
 ** 方案：方案5（单调栈求最大全 '.' 矩形）
 ** 来源：python 参考忠实移植
 */

function maxRedRectangle(matrix: string[]): number {
  // 定义函数/方法 maxRedRectangle
  const n = matrix.length; // 把 矩阵.长度 存入 元素个数
  const m = matrix[0].length; // 把 矩阵[0].长度 存入 映射表
  let ans = 0; // 把 0 存入 答案
  const height: number[] = new Array(m + 2).fill(0); // 把 new Array(映射表 加 2).fill(0); 写入 const height: number[]
  for (let k = 0; k < n; k++) {
    // 让 下标 k 从 0 开始计数，下标 k 小于 元素个数 就继续
    for (let i = 1; i <= m; i++) {
      // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 就继续
      if (matrix[k][i - 1] === '.')
        height[i] += 1; // 若 矩阵[下标 k][下标 i 减 1] 全等于 '.') height[下标 i] 累加 1;
      else height[i] = 0; // 否则
    }
    const stack: number[] = [0]; // 把 [0]; 写入 const stack: number[]
    for (let i = 1; i <= m + 1; i++) {
      // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 加 1 就继续
      while (height[stack[stack.length - 1]] > height[i]) {
        // 循环，直到不满足「height[栈[栈.长度 减 1]] 超过 height[下标 i]」
        const nowH = height[stack.pop()!]; // 把 height[栈 弹出 )取反 ] 存入 nowH
        const width = i - stack[stack.length - 1] - 1; // 把 下标 i 减 栈[栈.长度 减 1] 减 1 存入 width
        ans = Math.max(ans, nowH * width); // 把 Math.取较大值 答案, nowH 乘 width) 存入 答案
      }
      stack.push(i); // 把 下标 i 压入栈/数组尾部
    }
  }
  return ans; // 返回 答案
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const cases: { in: string[]; want: number }[] = [
    { in: ['.....', 'XXXXX', '.X...', '.....'], want: 6 },
    { in: ['...', '...', '...'], want: 9 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = maxRedRectangle(c.in); // 把 maxRedRectangle(字符.in) 存入 got
    if (got !== c.want) {
      // 若 got 不等于 字符.want
      fail = true; // 把 true 存入 fail
      console.log('FAIL', JSON.stringify(c.in), 'want', c.want, 'got', got); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
