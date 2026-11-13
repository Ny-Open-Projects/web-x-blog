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

function detect_edges_sobel(image: number[]): boolean[] {
  // 定义函数/方法 detect_edges_sobel
  const edges = new Array(image.length).fill(false); // 把 new Array(image.长度).fill(false) 存入 边集
  if (image.length < 2) return edges; // 若 image.长度 小于 2，直接返回 边集
  edges[0] = Math.abs(image[1] - image[0]) > 50; // 把 Math.取绝对值 image[1] 减 image[0]) 超过 50; 写入 edges[0]
  for (let i = 1; i < image.length - 1; i++)
    edges[i] = Math.abs(image[i + 1] - image[i - 1]) > 50; // 让 下标 i 从 1 开始计数，下标 i 小于 image.长度 减 1 就继续
  edges[image.length - 1] =
    Math.abs(image[image.length - 1] - image[image.length - 2]) > 50;
  return edges; // 返回 边集
}
function recognize_captcha(bg: number[], puzzle: number[]): number {
  // 定义函数/方法 recognize_captcha
  const bgEdges = detect_edges_sobel(bg);
  const puzzleEdges = detect_edges_sobel(puzzle);
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
