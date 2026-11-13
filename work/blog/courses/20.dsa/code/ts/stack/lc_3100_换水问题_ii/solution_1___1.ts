// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386116

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function maxBottlesDrunk(numBottles: number, numExchange: number): number {
  // 定义函数/方法 maxBottlesDrunk
  let total = numBottles,
    nb = numBottles,
    ne = numExchange; // 把 numBottles, nb 赋值为 numBottles, ne 赋值为 numExchange 存入 总和
  while (nb >= ne) {
    nb += 1 - ne;
    ne += 1;
    total += 1;
  } // 循环，直到不满足「nb 不低于 ne) { nb 累加 1 减 ne; ne 累加 1; 总和 累加 1; }」
  return total; // 返回 总和
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(maxBottlesDrunk(10, 3), 13, 'mbd'); // 断言校验
  assertEq(maxBottlesDrunk(1, 2), 1, 'one'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
