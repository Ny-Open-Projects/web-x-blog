// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134359782
// Faithful translation of python reference. Self-check via demo().
let _pick = 6; // 把 6 存入 _pick
function guess(num: number): number {
  // 定义函数/方法 guess
  if (num > _pick) return -1; // 若 num 超过 _pick，直接返回 减 1
  if (num < _pick) return 1; // 若 num 小于 _pick，直接返回 1
  return 0; // 返回 0
}
function guessNumber(n: number): number {
  // 定义函数/方法 guessNumber
  let left = 1,
    right = n; // 把 1, 右边界 赋值为 元素个数 存入 左边界
  while (left <= right) {
    // 循环，直到不满足「左边界 不超过 右边界」
    const mid = Math.floor((left + right) / 2); // 把 向下取整((左边界 加 右边界) 除以 2) 存入 中点
    const g = guess(mid); // 把 guess(中点) 存入 g
    if (g === 0)
      return mid; // 若 g 全等于 0，直接返回 中点
    else if (g === 1)
      left = mid + 1; // 否则，若 g 全等于 1) 左边界 赋值为 中点 加 1;
    else right = mid - 1; // 否则
  }
  return -1; // 返回 减 1
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const cases = [
    [10, 6],
    [1, 1],
    [5, 3],
    [2, 2],
  ]; // 把 [[10, 6], [1, 1], [5, 3], [2, 2]] 存入 cases
  for (const [n, pick] of cases) {
    // for (const [元素个数, pick] of cases) {
    _pick = pick; // 把 pick 存入 _pick
    const got = guessNumber(n); // 把 guessNumber(元素个数) 存入 got
    if (got !== pick)
      throw new Error('FAIL n=' + n + ' pick=' + pick + ' got ' + got);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
