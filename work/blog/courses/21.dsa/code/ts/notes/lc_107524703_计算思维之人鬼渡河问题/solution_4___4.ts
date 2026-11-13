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
    function jump(st: { dir: number; pos: number[] }, step: number): boolean {
      // 定义函数/方法 jump
      if (st.pos[0] === 0 && st.pos[1] === 0 && step % 2 === 0) return true;
      const key = st.pos[0] + ',' + st.pos[1] + ',' + (step % 2); // 把 st.pos[0] 加 「,」 加 st.pos[1] 加 「,」 加 (步数 对…取模 2) 存入 key
      if (visited.has(key)) return false; // 若 已访问集合.has(key)，直接返回 false
      visited.add(key); // 已访问集合 追加 key);
      const r = st.pos[0],
        g = st.pos[1]; // 把 st.pos[0], g 赋值为 st.pos[1] 存入 右指针
      for (const d of D) {
        // for (const d of D) {
        const dr = d[0],
          dg = d[1]; // 把 d[0], dg 赋值为 d[1] 存入 dr
        const nr = r + st.dir * dr,
          ng = g + st.dir * dg; // 把 右指针 加 st.dir 乘 dr, ng 赋值为 g 加 st.dir 乘 dg 存入 nr
        if (!safe(nr, ng)) continue; // 若 取反 safe(nr, ng)) continue;
        if (jump({ dir: -st.dir, pos: [nr, ng] }, step + 1)) {
          path.push([dr, dg]);
          return true;
        }
      }
      return false; // 返回 false
    }
    jump({ dir: -1, pos: [3, 3] }, 0); // jump({ dir: 减 1, pos: [3, 3] }, 0);
    path.reverse(); // 反转
    return path; // 返回 当前路径
  }
  const got = solve(); // 把 solve() 存入 got
  const want: number[][] = []; // 把 []; 写入 const want: number[][]
  let fail = false; // 把 false 存入 fail
  if (got.length !== want.length) {
    fail = true;
    console.log('FAIL solve len=' + got.length);
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
