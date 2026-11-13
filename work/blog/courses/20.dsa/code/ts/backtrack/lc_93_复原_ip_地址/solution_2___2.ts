// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135037359
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function restoreIpAddresses(s: string): string[] {
    // 定义函数/方法 restoreIpAddresses
    const res: string[] = []; // 把 []; 写入 const res: string[]
    function backtrack(start: number, path: string[]): void {
      // 定义函数/方法 backtrack
      if (path.length === 4) {
        // 若 当前路径.长度 全等于 4
        if (start === s.length) res.push(path.join('.')); // 若 起点 全等于 字符串.长度) 结果 追加 当前路径.join(「.」));
        return; // return;
      }
      for (let length = 1; length <= 3; length++) {
        // 让 长度 从 1 开始计数，长度 不超过 3 就继续
        if (start + length > s.length) break; // 若 起点 加 长度 超过 字符串.长度) break;
        const segment = s.substring(start, start + length); // 把 字符串 截取 起点, 起点 加 长度) 存入 segment
        if (
          (segment[0] === '0' && segment.length > 1) ||
          parseInt(segment, 10) > 255
        )
          continue;
        backtrack(start + length, [...path, segment]); // backtrack(起点 加 长度, [...当前路径, segment]);
      }
    }
    backtrack(0, []); // backtrack(0, []);
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
    {
      in: '101023',
      want: ['1.0.10.23', '1.0.102.3', '10.1.0.23', '10.10.2.3', '101.0.2.3'],
    },
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
