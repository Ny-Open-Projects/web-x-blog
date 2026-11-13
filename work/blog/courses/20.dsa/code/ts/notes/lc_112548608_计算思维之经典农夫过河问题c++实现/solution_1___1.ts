/**
 ** LeetCode 112548608. 计算思维之经典农夫过河问题C++实现
 ** 来源：https://blog.csdn.net/tyro_java/article/details/112548608
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  // solveFarmer 忠实翻译 python ref solution_1___1.py
  // 农夫过河（狼、羊、菜）：状态 (h,w,s,v) 每位 0/1 表示是否在起点岸。
  // 农夫每次必过河，可单独或带狼/羊/菜之一；无人看管时羊吃菜、狼吃羊则非法。目标全部到达对岸。
  function solveFarmer(): string[] {
    // 定义函数/方法 solveFarmer
    function invalid(st: number[]): boolean {
      // 定义函数/方法 invalid
      const h = st[0],
        w = st[1],
        s = st[2],
        v = st[3]; // 把 st[0], 权重 赋值为 st[1], 字符串 赋值为 st[2], 值 赋值为 st[3] 存入 h
      if (h !== s && s === w) {
        // 若 h 不等于 字符串 且 字符串 全等于 权重
        return true; // 返回 true
      }
      if (h !== s && s === v) {
        // 若 h 不等于 字符串 且 字符串 全等于 值
        return true; // 返回 true
      }
      return false; // 返回 false
    }

    const itemIndex: { [key: string]: number } = { W: 1, S: 2, V: 3 };
    const path: string[] = []; // 把 []; 写入 const path: string[]
    const visited = new Set<string>(); // 把 new Set 小于 string 超过 () 存入 已访问集合

    function go(st: number[]): boolean {
      // 定义函数/方法 go
      if (st[0] === 1 && st[1] === 1 && st[2] === 1 && st[3] === 1) {
        // 若 st[0] 全等于 1 且 st[1] 全等于 1 且 st[2] 全等于 1 且 st[3] 全等于 1
        return true; // 返回 true
      }
      const key = st.join(','); // 把 st.join(',') 存入 key
      if (visited.has(key)) {
        // 若 已访问集合.has(key
        return false; // 返回 false
      }
      visited.add(key); // 已访问集合 追加 key);
      for (const role of ['-', 'W', 'S', 'V']) {
        // for (const role of [' 减 ', 'W', 'S', 'V']) {
        const ns = [...st]; // 把 复制的 st 存入 ns
        ns[0] = 1 - ns[0]; // 农夫总是过河
        if (role !== '-') {
          // 若 role 不等于 ' 减 '
          const idx = itemIndex[role]; // 把 itemIndex[role] 存入 idx
          // 农夫必须与所带物品在出发前同岸
          if (st[0] !== st[idx]) {
            // 若 st[0] 不等于 st[idx]
            continue; // 跳过本轮，进入下一次
          }
          ns[idx] = 1 - ns[idx]; // 把 1 减 ns[idx]; 写入 ns[idx]
        }
        if (invalid(ns)) {
          // 若 invalid(ns
          continue; // 跳过本轮，进入下一次
        }
        if (go(ns)) {
          // 若 go(ns
          path.push(role); // 把 role 压入栈/数组尾部
          return true; // 返回 true
        }
      }
      return false; // 返回 false
    }

    go([0, 0, 0, 0]); // go([0, 0, 0, 0]);
    path.reverse(); // 反转
    return path; // 返回 当前路径
  }

  // 模拟走 path，校验每步合法且终点为 (1,1,1,1)
  function simulate(path: string[]): boolean {
    // 定义函数/方法 simulate
    const st = [0, 0, 0, 0]; // 把 [0, 0, 0, 0] 存入 st
    const itemIndex: { [key: string]: number } = { W: 1, S: 2, V: 3 };
    for (const role of path) {
      // for (const role of 当前路径) {
      const before = [...st]; // 把 复制的 st 存入 before
      st[0] = 1 - st[0]; // 把 1 减 st[0]; 写入 st[0]
      if (role !== '-') {
        // 若 role 不等于 ' 减 '
        const idx = itemIndex[role]; // 把 itemIndex[role] 存入 idx
        if (before[0] !== before[idx]) {
          // 若 before[0] 不等于 before[idx]
          return false; // 返回 false
        }
        st[idx] = 1 - st[idx]; // 把 1 减 st[idx]; 写入 st[idx]
      }
      const h = st[0],
        w = st[1],
        s = st[2],
        v = st[3]; // 把 st[0], 权重 赋值为 st[1], 字符串 赋值为 st[2], 值 赋值为 st[3] 存入 h
      if (h !== s && s === w) {
        // 若 h 不等于 字符串 且 字符串 全等于 权重
        return false; // 返回 false
      }
      if (h !== s && s === v) {
        // 若 h 不等于 字符串 且 字符串 全等于 值
        return false; // 返回 false
      }
    }
    return st[0] === 1 && st[1] === 1 && st[2] === 1 && st[3] === 1; // 返回 st[0] 全等于 1 且 st[1] 全等于 1 且 st[2] 全等于 1 且 st[3] 全等于 1
  }

  // want 由 python ref solution_1___1.py 实跑得到
  const wantPath = ['S', '-', 'W', 'S', 'V', '-', 'S']; // 把 ['S', ' 减 ', 'W', 'S', 'V', ' 减 ', 'S'] 存入 wantPath
  const wantReadable = 'HS H HW HS HV H HS'; // 把 'HS H HW HS HV H HS' 存入 wantReadable

  let fail = false; // 把 false 存入 fail
  const gotPath = solveFarmer(); // 把 solveFarmer() 存入 gotPath

  // case1 normal: 完整路径与 python ref 一致
  if (gotPath.length !== wantPath.length) {
    // 若 gotPath.长度 不等于 wantPath.长度
    fail = true; // 把 true 存入 fail
    console.log(
      `FAIL path length got ${gotPath.length} want ${wantPath.length}`,
    );
  } else {
    // 否则
    for (let i = 0; i < gotPath.length; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 gotPath.长度 就继续
      if (gotPath[i] !== wantPath[i]) {
        // 若 gotPath[下标 i] 不等于 wantPath[下标 i]
        fail = true; // 把 true 存入 fail
        console.log(`FAIL path[${i}] got ${gotPath[i]} want ${wantPath[i]}`);
      }
    }
  }

  // case2 normal: 可读方案串与 python ref 输出一致
  const gotReadable = gotPath.map((r) => 'H' + (r !== '-' ? r : '')).join(' ');
  if (gotReadable !== wantReadable) {
    // 若 gotReadable 不等于 wantReadable
    fail = true; // 把 true 存入 fail
    console.log(`FAIL readable got "${gotReadable}" want "${wantReadable}"`);
  }

  // case3 boundary: 路径 7 步
  if (gotPath.length !== 7) {
    // 若 gotPath.长度 不等于 7
    fail = true; // 把 true 存入 fail
    console.log(`FAIL steps got ${gotPath.length} want 7`);
  }

  // case4 boundary: 模拟校验每步合法且到达终点
  if (!simulate(gotPath)) {
    // 若 取反 simulate(gotPath
    fail = true; // 把 true 存入 fail
    console.log('FAIL simulate path illegal or not reaching goal'); // 打印输出
  }

  if (fail) {
    // 若 fail
    throw new Error('FAILED'); // throw new Error(「FAILED」);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
