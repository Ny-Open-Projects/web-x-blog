// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107475776

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function horse_jump_count(): number {
  // 定义函数/方法 horse_jump_count
  const moves = [
    [1, 2],
    [2, 1],
    [2, -1],
    [1, -2],
  ]; // 把 [[1, 2], [2, 1], [2, 减 1], [1, 减 2]] 存入 moves
  let count = 0; // 把 0 存入 计数
  function jump(x: number, y: number): void {
    // 定义函数/方法 jump
    if (x === 8 && y === 4) {
      count++;
      return;
    } // 若 x 全等于 8 且 y 全等于 4) { 计数 加一 ; return; }
    for (const mv of moves) {
      // for (const mv of moves) {
      const nx = x + mv[0],
        ny = y + mv[1]; // 把 x 加 mv[0], ny 赋值为 y 加 mv[1] 存入 nx
      if (nx < 0 || nx > 8 || ny < 0 || ny > 4) continue; // 若 nx 小于 0 或 nx 超过 8 或 ny 小于 0 或 ny 超过 4) continue;
      jump(nx, ny); // jump(nx, ny);
    }
  }
  jump(0, 0); // jump(0, 0);
  return count; // 返回 计数
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(horse_jump_count(), 37, 'horse'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
