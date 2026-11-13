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

function detect_edges(image: number[]): boolean[] {
  // 定义函数/方法 detect_edges
  const edges = new Array(image.length).fill(false); // 把 new Array(image.长度).fill(false) 存入 边集
  for (let i = 1; i < image.length; i++)
    edges[i] = Math.abs(image[i] - image[i - 1]) > 50; // 让 下标 i 从 1 开始计数，下标 i 小于 image.长度 就继续
  return edges; // 返回 边集
}
function recognize_captcha(bg: number[], puzzle: number[]): number {
  // 定义函数/方法 recognize_captcha
  const bgEdges = detect_edges(bg);
  const puzzleEdges = detect_edges(puzzle);
  let best_x = 0,
    best_score = -1; // 把 0, best_score 赋值为 减 1 存入 best_x
  for (let x = 0; x <= bg.length - puzzle.length; x++) {
    // 让 x 从 0 开始计数，x 不超过 bg.长度 减 puzzle.长度 就继续
    let score = 0; // 把 0 存入 score
    for (let y = 0; y < puzzle.length; y++)
      if (bgEdges[x + y] && puzzleEdges[y]) score++; // 让 y 从 0 开始计数，y 小于 puzzle.长度 就继续
    if (score > best_score) {
      best_score = score;
      best_x = x;
    }
  }
  return best_x; // 返回 best_x
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const bg = [10, 10, 10, 10, 200, 200, 200, 200]; // 把 [10, 10, 10, 10, 200, 200, 200, 200] 存入 bg
  const puzzle = [10, 200, 200, 200]; // 把 [10, 200, 200, 200] 存入 puzzle
  assertEq(recognize_captcha(bg, puzzle), 3, 'gap'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
