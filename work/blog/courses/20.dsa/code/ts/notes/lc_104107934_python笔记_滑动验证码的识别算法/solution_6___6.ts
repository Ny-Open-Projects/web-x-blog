// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function buildSynthetic(
  bgLen: number = 8,
  gapStart: number = 3,
  puzzleLen: number = 4,
): [number[], number[]] {
  // 定义函数/方法 buildSynthetic
  const bg = new Array(bgLen).fill(10); // 把 new Array(bgLen).fill(10) 存入 bg
  for (let i = gapStart; i < Math.min(gapStart + puzzleLen, bgLen); i++)
    bg[i] = 200;
  const puzzle = bg.slice(gapStart, gapStart + puzzleLen); // 把 bg 截取 gapStart, gapStart 加 puzzleLen) 存入 puzzle
  return [bg, puzzle]; // 返回 [bg, puzzle]
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const [bg, puzzle] = buildSynthetic(); // 把 buildSynthetic(); 写入 const [bg, puzzle]
  assertEq(
    ['背景:', bg],
    ['背景:', [10, 10, 10, 200, 200, 200, 200, 10]],
    'bg',
  ); // 断言校验
  assertEq(['拼图:', puzzle], ['拼图:', [200, 200, 200, 200]], 'puzzle'); // 断言校验
  assertEq(
    ['拼图长度:', 4, ' 背景长度:', 8],
    ['拼图长度:', 4, ' 背景长度:', 8],
    'lens',
  ); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
