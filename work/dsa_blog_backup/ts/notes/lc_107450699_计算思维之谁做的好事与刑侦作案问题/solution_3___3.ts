/**
 ** LeetCode 107450699. 计算思维之谁做的好事与刑侦作案问题
 ** 来源：https://blog.csdn.net/tyro_java/article/details/107450699
 ** 忠实翻译自 python/notes/lc_107450699_.../solution_3___3.py（刑侦作案问题）
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  // 刑侦案件：六嫌疑人 A,B,C,D,E,F，1 表示作案，0 表示未作案
  // 线索：
  // 1) A、B 至少有一人作案            -> a or b
  // 2) A、E、F 至少两人参与          -> (a&e)|(a&f)|(e&f)
  // 3) A、D 不可能是同案犯            -> not (a and d)
  // 4) B、C 或同时作案或与本案无关    -> (b&c)|(~b&~c)
  // 5) C、D 中有且仅有一人作案        -> (c&~d)|(~c&d)
  // 6) 若 D 没作案则 E 也不可能作案   -> d or (~d and ~e)
  function cluesHold(v: number[]): boolean {
    // 定义函数/方法 cluesHold
    const a = v[0] === 1,
      b = v[1] === 1,
      c = v[2] === 1,
      d = v[3] === 1,
      e = v[4] === 1,
      f = v[5] === 1;
    return (
      (a || b) && // 返回 ((数组 或 b)
      ((a && e) || (a && f) || (e && f)) && // 且 ((数组 且 e) 或 (数组 且 f) 或 (e 且 f))
      !(a && d) && // 且 取反 (数组 且 d)
      ((b && c) || (!b && !c)) && // 且 ((b 且 字符) 或 (取反 b 且 取反 字符))
      ((c && !d) || (!c && d)) && // 且 ((字符 且 取反 d) 或 (取反 字符 且 d))
      (d || (!d && !e))
    ); // 且 (d 或 (取反 d 且 取反 e)));
  }

  function solve(): string {
    // 定义函数/方法 solve
    const found: string[] = []; // 把 []; 写入 const found: string[]
    for (let a = 0; a < 2; a++) {
      // 让 数组 从 0 开始计数，数组 小于 2 就继续
      for (let b = 0; b < 2; b++) {
        // 让 b 从 0 开始计数，b 小于 2 就继续
        for (let c = 0; c < 2; c++) {
          // 让 字符 从 0 开始计数，字符 小于 2 就继续
          for (let d = 0; d < 2; d++) {
            // 让 d 从 0 开始计数，d 小于 2 就继续
            for (let e = 0; e < 2; e++) {
              // 让 e 从 0 开始计数，e 小于 2 就继续
              for (let f = 0; f < 2; f++) {
                // 让 f 从 0 开始计数，f 小于 2 就继续
                const v = [a, b, c, d, e, f]; // 把 [数组, b, 字符, d, e, f] 存入 值
                if (cluesHold(v)) {
                  // 若 cluesHold(值
                  const names = 'ABCDEF'; // 把 'ABCDEF' 存入 names
                  let people = ''; // 把 '' 存入 people
                  for (let i = 0; i < 6; i++) {
                    // 让 下标 i 从 0 开始计数，下标 i 小于 6 就继续
                    if (v[i] === 1) people += names[i]; // 若 值[下标 i] 全等于 1) people 累加 names[下标 i];
                  }
                  found.push(people); // 把 people 压入栈/数组尾部
                }
              }
            }
          }
        }
      }
    }
    if (found.length === 0) {
      // 若 found.长度 全等于 0
      return '未找到作案人员!'; // 返回 「未找到作案人员取反 」
    }
    return found[0]; // 返回 found[0]
  }

  let fail = false; // 把 false 存入 fail
  // normal: 唯一解 ABCF
  const got = solve(); // 把 solve() 存入 got
  if (got !== 'ABCF') {
    // 若 got 不等于 「ABCF」
    fail = true; // 把 true 存入 fail
    console.log(`FAIL solve()=${got} want ABCF`);
  }
  // boundary: 唯一作案组合 6 元组为 (1,1,1,0,0,1)（A/B/C/F 作案，D/E 未作案）
  const want = [1, 1, 1, 0, 0, 1]; // 把 [1, 1, 1, 0, 0, 1] 存入 want
  if (!cluesHold(want)) {
    // 若 取反 cluesHold(want
    fail = true; // 把 true 存入 fail
    console.log('FAIL cluesHold([1,1,1,0,0,1]) should be true'); // 打印输出
  }
  // boundary: 反例组合 (1,1,1,1,0,1)（A/D 同案犯，违反线索3）应不成立
  const bad = [1, 1, 1, 1, 0, 1]; // 把 [1, 1, 1, 1, 0, 1] 存入 bad
  if (cluesHold(bad)) {
    // 若 cluesHold(bad
    fail = true; // 把 true 存入 fail
    console.log('FAIL cluesHold([1,1,1,1,0,1]) should be false'); // 打印输出
  }

  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
