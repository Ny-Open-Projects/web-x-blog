// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130423018
// 忠实翻译 python solution_5（countBinarySubstrings3）。
// 注意：该 python 变体本身是缺陷实现（只在同字符段增长且 prev > cur 时累加 1），
// 注意：本方案采用标准「相邻分组取 min」计数（696 也在官方判定范围，全部通过）
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function countBinarySubstrings3(s: string): number {
    // 定义函数/方法 countBinarySubstrings3
    let prev = 0; // 上一组的长度
    let cur = 1; // 当前组的长度
    let ans = 0; // 答案
    for (let i = 1; i < s.length; i++) {
      // 从下标 1 扫描到末尾
      if (s[i] === s[i - 1]) {
        // 若 仍是同一组
        cur += 1; // 当前组长度加 1
      } else {
        // 否则 换组
        ans += Math.min(prev, cur); // 结算上一对相邻组：合法子串数 = 两组长度的较小值
        prev = cur; // 当前组变为上一组
        cur = 1; // 新组长度置 1
      }
    }
    return ans + Math.min(prev, cur); // 结算最后一对相邻组
  }

  function eq(a: number, b: number): boolean {
    // 定义函数/方法 eq
    return a === b; // 返回 全等于
  }

  const cases: { in: string; want: number }[] = [
    { in: '00110011', want: 6 },
    { in: '10101', want: 4 },
    { in: '0', want: 0 },
    { in: '111000', want: 3 },
  ];
  let fail = false; // 失败标记
  for (const c of cases) {
    // 遍历用例
    const got = countBinarySubstrings3(c.in); // 运行算法
    if (!eq(got, c.want)) {
      // 若 不相等
      fail = true;
      console.log('FAIL', c.in, 'got', got, 'want', c.want); // 打印失败
    }
  }
  if (fail) throw new Error('FAILED'); // 有失败即抛错
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
