/**
 ** LeetCode 107450699. 计算思维之谁做的好事与刑侦作案问题
 ** 来源：https://blog.csdn.net/tyro_java/article/details/107450699
 ** 忠实翻译自 python/notes/lc_107450699_.../solution_1___1.py（思路一：字符表示人）
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  // 思路一：通过字符表示人 (A/B/C/D)
  // A说:不是我  -> thisman != 'A'
  // B说:是C     -> thisman == 'C'
  // C说:是D     -> thisman == 'D'
  // D说:他胡说  -> thisman != 'D'
  // 已知三人说真话一人说假话：sum == 3
  function truthCount(thisman: string): number {
    // 定义函数/方法 truthCount
    return (
      (thisman !== 'A' ? 1 : 0) + // 返回 (thisman 不等于 'A' ? 1 : 0)
      (thisman === 'C' ? 1 : 0) + // 把 等于 'C' ? 1 : 0) 写入 + (thisman
      (thisman === 'D' ? 1 : 0) + // 把 等于 'D' ? 1 : 0) 写入 + (thisman
      (thisman !== 'D' ? 1 : 0)
    ); // 把 赋值为 'D' ? 1 : 0); 写入 + (thisman !
  }

  function solve(): string {
    // 定义函数/方法 solve
    const found: string[] = []; // 把 []; 写入 const found: string[]
    for (let k = 0; k < 4; k++) {
      // 让 下标 k 从 0 开始计数，下标 k 小于 4 就继续
      const thisman = String.fromCharCode('A'.charCodeAt(0) + k); // 把 String.fromCharCode('A'.charCodeAt(0) 加 下标 k) 存入 thisman
      if (truthCount(thisman) === 3) {
        // 若 truthCount(thisman) 全等于 3
        found.push(thisman); // 把 thisman 压入栈/数组尾部
      }
    }
    if (found.length === 0) {
      // 若 found.长度 全等于 0
      return '找不出做好事者'; // 返回 「找不出做好事者」
    }
    return found[0]; // 返回 found[0]
  }

  // 每个候选人的真话计数（边界覆盖：A/B/C/D 全部候选）
  const counts: number[] = []; // 把 []; 写入 const counts: number[]
  for (let k = 0; k < 4; k++) {
    // 让 下标 k 从 0 开始计数，下标 k 小于 4 就继续
    counts.push(truthCount(String.fromCharCode('A'.charCodeAt(0) + k))); // 把 truthCount(String.fromCharCode('A'.charCodeAt(0 压入栈/数组尾部
  }

  let fail = false; // 把 false 存入 fail
  // normal: 唯一解为 C
  const got = solve(); // 把 solve() 存入 got
  if (got !== 'C') {
    // 若 got 不等于 「C」
    fail = true; // 把 true 存入 fail
    console.log(`FAIL solve()=${got} want C`);
  }
  // boundary: 各候选真话计数 [1,2,3,2]（仅 C 为 3）
  const wantCounts = [1, 2, 3, 2]; // 把 [1, 2, 3, 2] 存入 wantCounts
  if (
    counts.length !== wantCounts.length ||
    counts.some((v, i) => v !== wantCounts[i])
  ) {
    fail = true; // 把 true 存入 fail
    console.log(
      `FAIL truthCounts=${JSON.stringify(counts)} want ${JSON.stringify(wantCounts)}`,
    );
  }

  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
