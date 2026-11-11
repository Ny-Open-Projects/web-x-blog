/**
 ** LeetCode 89. 格雷编码
 ** 方案：1 ）方案 1：递归
 ** 来源：https://blog.csdn.net/tyro_java/article/details/130456218
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  // grayCode 忠实翻译 python ref solution_1_1_____1_____.py（递归构造二进制串）
  function grayCode(n: number): number[] {
    // 定义函数/方法 grayCode
    function recursionFn(k: number): string[] {
      // 定义函数/方法 recursionFn
      if (k === 1) {
        // 若 下标 k 全等于 1
        return ['0', '1']; // 返回 ['0', '1']
      }
      const prev = recursionFn(k - 1); // 把 recursionFn(下标 k 减 1) 存入 前一个
      const result: string[] = []; // 把 []; 写入 const result: string[]
      const prefix = '1' + '0'.repeat(k - 1); // 把 '1' 加 '0'.repeat(下标 k 减 1) 存入 prefix
      for (let idx = prev.length - 1; idx >= 0; idx--) {
        // 让 idx 从 前一个.长度 减 1 开始计数，idx 不低于 0 就继续
        const item = prev[idx]; // 把 前一个[idx] 存入 item
        result.push(prefix.slice(0, prefix.length - item.length) + item); // 把 prefix 截取 0, prefix.长度 减 item.长度 压入栈/数组尾部
      }
      return [...prev, ...result]; // 返回 [...前一个, ...结果]
    }
    if (n === 0) {
      // 若 元素个数 全等于 0
      return [0]; // 返回 [0]
    }
    const codes = recursionFn(n); // 把 recursionFn(元素个数) 存入 codes
    return codes.map((x) => parseInt(x, 2));
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
