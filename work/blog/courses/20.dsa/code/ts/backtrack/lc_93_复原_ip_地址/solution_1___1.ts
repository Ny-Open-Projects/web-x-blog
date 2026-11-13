// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135037359
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function restoreIpAddresses(s: string): string[] {
    // 定义函数/方法 restoreIpAddresses
    const res: string[] = []; // 把 [] 存入 结果
    const segs: string[] = []; // 把 [] 存入 当前段
    const valid = (t: string): boolean =>
      t.length > 0 &&
      t.length <= 3 &&
      !(t.length > 1 && t[0] === '0') &&
      Number(t) <= 255; // 段合法：0 到 255 且无前导零
    const dfs = (start: number): void => {
      // 回溯：从 start 切下一段
      if (segs.length === 4) {
        // 若 已切满 4 段
        if (start === s.length) res.push(segs.join('.')); // 恰好用完整个字符串才收答案
        return; // 返回
      }
      for (let len = 1; len <= 3 && start + len <= s.length; len++) {
        // 每段取 1 到 3 个字符
        const part = s.slice(start, start + len); // 取候选段
        if (!valid(part)) continue; // 不合法直接跳过
        segs.push(part); // 追加当前段
        dfs(start + len); // 递归求解子问题
        segs.pop(); // 回溯撤销当前选择
      }
    };
    dfs(0); // 从 0 开始回溯
    return res; // 返回 结果
  }

  function eq(a: string[], b: string[]): boolean {
    // 定义函数/方法 eq
    if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    const x = [...a].sort(); // 把 复制的 数组 排序 ) 存入 x
    const y = [...b].sort(); // 把 复制的 b 排序 ) 存入 y
    for (let i = 0; i < x.length; i++) if (x[i] !== y[i]) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 x.长度 就继续
    return true; // 返回 true
  }

  const cases: { in: string; want: string[] }[] = [
    { in: '25525511135', want: ['255.255.11.135', '255.255.111.35'] },
    { in: '0000', want: ['0.0.0.0'] },
    { in: 'abc', want: [] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = restoreIpAddresses(c.in); // 把 restoreIpAddresses(字符.in) 存入 got
    if (!eq(got, c.want)) {
      // 若 取反 eq(got, 字符.want
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL in=' +
          c.in +
          ' got=' +
          JSON.stringify(got) +
          ' want=' +
          JSON.stringify(c.want),
      ); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
