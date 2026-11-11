// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107524703
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function solve(): number[][] {
    // 定义函数/方法 solve
    const D: number[][] = [
      [2, 0],
      [1, 0],
      [1, 1],
      [0, 1],
      [0, 2],
    ];
    function safe(r: number, g: number): boolean {
      // 定义函数/方法 safe
      return (
        0 <= r && r <= 3 && 0 <= g && g <= 3 && (r === 0 || r === 3 || r === g)
      );
    }
    const path: number[][] = []; // 把 []; 写入 const path: number[][]
    const visited = new Set<string>(); // 把 new Set 小于 string 超过 () 存入 已访问集合
    function dfs(state: number[], step: number): boolean {
      // 定义函数/方法 dfs
      if (state[0] === 0 && state[1] === 0) return true; // 若 state[0] 全等于 0 且 state[1] 全等于 0，直接返回 true
      const key = state[0] + ',' + state[1] + ',' + (step % 2); // 把 state[0] 加 「,」 加 state[1] 加 「,」 加 (步数 对…取模 2) 存入 key
      if (visited.has(key)) return false; // 若 已访问集合.has(key)，直接返回 false
      visited.add(key); // 已访问集合 追加 key);
      const r = state[0],
        g = state[1]; // 把 state[0], g 赋值为 state[1] 存入 右指针
      const odd = step % 2 === 1; // 把 (步数 对…取模 2 全等于 1) 存入 odd
      for (const d of D) {
        // for (const d of D) {
        const dr = d[0],
          dg = d[1]; // 把 d[0], dg 赋值为 d[1] 存入 dr
        let nr: number, ng: number; // let nr: number, ng: number;
        if (odd) {
          // 若 odd
          if (r < dr || g < dg) continue; // 若 右指针 小于 dr 或 g 小于 dg) continue;
          nr = r - dr;
          ng = g - dg; // 把 右指针 减 dr; ng 赋值为 g 减 dg 存入 nr
        } else {
          // 否则
          if (3 - r < dr || 3 - g < dg) continue; // 若 (3 减 右指针) 小于 dr 或 (3 减 g) 小于 dg) continue;
          nr = r + dr;
          ng = g + dg; // 把 右指针 加 dr; ng 赋值为 g 加 dg 存入 nr
        }
        if (!safe(nr, ng)) continue; // 若 取反 safe(nr, ng)) continue;
        if (dfs([nr, ng], step + 1)) {
          path.push([dr, dg]);
          return true;
        } // 若 dfs([nr, ng], 步数 加 1)) { 当前路径 追加 [dr, dg]); return true; }
      }
      return false; // 返回 false
    }
    dfs([3, 3], 1); // dfs([3, 3], 1);
    path.reverse(); // 反转
    return path; // 返回 当前路径
  }
  const got = solve(); // 把 solve() 存入 got
  const want = [
    [1, 1],
    [1, 0],
    [0, 2],
    [0, 1],
    [2, 0],
    [1, 1],
    [2, 0],
    [0, 1],
    [0, 2],
    [1, 0],
    [1, 1],
  ];
  let fail = false; // 把 false 存入 fail
  if (got.length !== want.length) {
    fail = true;
    console.log('FAIL solve len=' + got.length);
  } else {
    // 否则
    for (let i = 0; i < want.length; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 want.长度 就继续
      if (got[i][0] !== want[i][0] || got[i][1] !== want[i][1]) {
        fail = true;
        console.log('FAIL solve at ' + i);
        break;
      }
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
