/**
 ** LeetCode 89. 格雷编码
 ** 方案：3 ）方案3：利用已有的格雷编码来生成新的格雷编码
 ** 来源：https://blog.csdn.net/tyro_java/article/details/130456218
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  // grayCode 忠实翻译 python ref solution_3_3____3___________________.py（从 [0] 起镜像追加）
  function grayCode(n: number): number[] {
    // 定义函数/方法 grayCode
    const ret: number[] = [0]; // 把 [0]; 写入 const ret: number[]
    for (let i = 1; i <= n; i++) {
      // 让 下标 i 从 1 开始计数，下标 i 不超过 元素个数 就继续
      for (let j = ret.length - 1; j >= 0; j--) {
        // 让 下标 j 从 ret.长度 减 1 开始计数，下标 j 不低于 0 就继续
        ret.push(ret[j] | (1 << (i - 1))); // 把 ret[下标 j] 按位或 (1 小于 小于 (下标 i 减 1 压入栈/数组尾部
      }
    }
    return ret; // 返回 ret
  }

  function eqArr(a: number[], b: number[]): boolean {
    // 定义函数/方法 eqArr
    if (a.length !== b.length) {
      // 若 数组.长度 不等于 b.长度
      return false; // 返回 false
    }
    for (let i = 0; i < a.length; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
      if (a[i] !== b[i]) {
        // 若 数组[下标 i] 不等于 b[下标 i]
        return false; // 返回 false
      }
    }
    return true; // 返回 true
  }

  // want 由 python ref 实跑得到
  const cases: { n: number; want: number[] }[] = [
    { n: 0, want: [0] },
    { n: 1, want: [0, 1] },
    { n: 2, want: [0, 1, 3, 2] },
    { n: 3, want: [0, 1, 3, 2, 6, 7, 5, 4] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = grayCode(c.n); // 把 grayCode(字符.元素个数) 存入 got
    if (!eqArr(got, c.want)) {
      // 若 取反 eqArr(got, 字符.want
      fail = true; // 把 true 存入 fail
      console.log(
        `FAIL grayCode(${c.n})=${JSON.stringify(got)} want ${JSON.stringify(c.want)}`,
      );
    }
  }
  if (fail) {
    // 若 fail
    throw new Error('FAILED'); // throw new Error(「FAILED」);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
