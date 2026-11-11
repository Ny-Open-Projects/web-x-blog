// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134359782
// Faithful translation of python reference. Self-check via demo().
let _pick = 6; // 把 6 存入 _pick
function guess(num: number): number {
  // 定义函数/方法 guess
  if (num === _pick) return 0; // 若 num 全等于 _pick，直接返回 0
  return num < _pick ? 1 : -1; // 返回 num 小于 _pick ? 1 : 减 1
}
function guessNumber(n: number): number {
  // 定义函数/方法 guessNumber
  function rec(low: number, high: number): number {
    // 定义函数/方法 rec
    if (low > high) return -1; // 若 low 超过 high，直接返回 减 1
    const mid = Math.floor((low + high) / 2); // 把 向下取整((low 加 high) 除以 2) 存入 中点
    const res = guess(mid); // 把 guess(中点) 存入 结果
    if (res === 0) return mid; // 若 结果 全等于 0，直接返回 中点
    if (res === 1) return rec(mid + 1, high); // 若 结果 全等于 1，直接返回 rec(中点 加 1, high)
    return rec(1, mid - 1); // 返回 rec(1, 中点 减 1)
  }
  return rec(1, n); // 返回 rec(1, 元素个数)
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
