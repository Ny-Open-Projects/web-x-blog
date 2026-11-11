// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/98685358
// 忠实翻译 python solution_1：BFS 求农夫过河最短路径
// 状态四元组 (农夫, 狼, 羊, 菜)，0=左岸，1=右岸
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function isSafe(state: number[]): boolean {
    // 定义判定函数 isSafe
    const farmer = state[0]; // 把 state[0] 存入 farmer
    const wolf = state[1]; // 把 state[1] 存入 wolf
    const goat = state[2]; // 把 state[2] 存入 goat
    const cabbage = state[3]; // 把 state[3] 存入 cabbage
    if (wolf === goat && farmer !== wolf) {
      // 若 wolf 全等于 goat 且 farmer 不等于 wolf
      return false; // 返回 false
    }
    if (goat === cabbage && farmer !== goat) {
      // 若 goat 全等于 cabbage 且 farmer 不等于 goat
      return false; // 返回 false
    }
    return true; // 返回 true
  }
  function solve(): number[][] | null {
    // 定义函数/方法 solve
    const start = [0, 0, 0, 0]; // 把 [0, 0, 0, 0] 存入 起点
    const goal = [1, 1, 1, 1]; // 把 [1, 1, 1, 1] 存入 goal
    const prev: Map<string, number[] | null> = new Map(); // 把 new Map(); 写入 const prev: Map<string, number[] | null>
    prev.set(start.join(','), null); // 拼接为字符串
    const q: number[][] = [start]; // 把 [起点]; 写入 const q: number[][]
    while (q.length > 0) {
      // 循环，直到不满足「节点.长度 超过 0」
      const cur = q.shift() as number[]; // 把 节点.shift() as number[] 存入 当前值
      const curKey = cur.join(','); // 把 当前值.join(「,」) 存入 curKey
      if (curKey === goal.join(',')) {
        // 若 curKey 全等于 goal.join(「,」
        const path: number[][] = []; // 把 []; 写入 const path: number[][]
        let k: number[] | null = cur; // 把 当前值; 写入 let k: number[] | null
        while (k !== null) {
          // 循环，直到不满足「下标 k 不等于 null」
          path.push(k); // 把 下标 k 压入栈/数组尾部
          k = prev.get(k.join(',')) || null; // 把 前一个 查找 下标 k.join(「,」)) 或 null 存入 下标 k
        }
        path.reverse(); // 反转
        return path; // 返回 当前路径
      }
      const farmer = cur[0]; // 把 当前值[0] 存入 farmer
      for (let i = 0; i < 4; i++) {
        // 让 下标 i 从 0 开始计数，下标 i 小于 4 就继续
        if (i !== 0 && cur[i] !== farmer) {
          // 若 下标 i 不等于 0 且 当前值[下标 i] 不等于 farmer
          continue; // 跳过本轮，进入下一次
        }
        const nxt = cur.slice(); // 把 当前值 截取 ) 存入 nxt
        nxt[0] = 1 - farmer; // 把 1 减 farmer; 写入 nxt[0]
        if (i !== 0) {
          // 若 下标 i 不等于 0
          nxt[i] = 1 - farmer; // 把 1 减 farmer; 写入 nxt[i]
        }
        const nk = nxt.join(','); // 把 nxt.join(「,」) 存入 nk
        if (prev.has(nk)) {
          // 若 前一个.has(nk
          continue; // 跳过本轮，进入下一次
        }
        if (!isSafe(nxt)) {
          // 若 取反 isSafe(nxt
          continue; // 跳过本轮，进入下一次
        }
        prev.set(nk, cur); // 前一个.set(nk, 当前值);
        q.push(nxt); // 把 nxt 压入栈/数组尾部
      }
    }
    return null; // 返回 null
  }
  const want: number[][] = [
    [0, 0, 0, 0],
    [1, 0, 1, 0],
    [0, 0, 1, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 1],
    [1, 1, 1, 1],
  ];
  const path = solve(); // 把 solve() 存入 当前路径
  if (path === null) {
    // 若 当前路径 全等于 null
    throw new Error('FAILED: 无解'); // throw new Error(「FAILED: 无解」);
  }
  let ok = path.length === want.length; // 把 当前路径.长度 全等于 want.长度 存入 ok
  for (let i = 0; ok && i < want.length; i++) {
    // 让 下标 i 从 0 开始计数，ok 且 下标 i 小于 want.长度 就继续
    for (let j = 0; j < 4; j++) {
      // 让 下标 j 从 0 开始计数，下标 j 小于 4 就继续
      if (path[i][j] !== want[i][j]) {
        // 若 当前路径[下标 i][下标 j] 不等于 want[下标 i][下标 j]
        ok = false; // 把 false 存入 ok
      }
    }
  }
  if (!ok) {
    // 若 取反 ok
    console.log(
      'FAIL path=' + JSON.stringify(path) + ' want=' + JSON.stringify(want),
    ); // 打印输出
    throw new Error('FAILED'); // throw new Error(「FAILED」);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
