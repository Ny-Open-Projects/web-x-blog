// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107573690

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function climb_stairs_refactored(h: number): number {
  // 定义函数/方法 climb_stairs_refactored
  const goal = h;
  let count = 0; // 把 h; let 计数 赋值为 0 存入 goal
  function is_done(pos: number): boolean {
    return pos === goal;
  } // 定义判定函数 is_done
  function is_valid(pos: number): boolean {
    return 0 <= pos && pos <= goal;
  } // 定义判定函数 is_valid
  function get_new_pos(pos: number, k: number): number {
    return pos + (k + 1);
  } // 定义函数/方法 get_new_pos
  function dfs(pos: number): void {
    // 定义函数/方法 dfs
    if (is_done(pos)) {
      count++;
      return;
    } // 若 is_done(pos)) { 计数 加一 ; return; }
    for (let k = 0; k < 3; k++) {
      const nxt = get_new_pos(pos, k);
      if (!is_valid(nxt)) continue;
      dfs(nxt);
    } // 让 下标 k 从 0 开始计数，下标 k 小于 3 就继续
  }
  dfs(0); // dfs(0);
  return count; // 返回 计数
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(climb_stairs_refactored(10), 274, 'sr'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
