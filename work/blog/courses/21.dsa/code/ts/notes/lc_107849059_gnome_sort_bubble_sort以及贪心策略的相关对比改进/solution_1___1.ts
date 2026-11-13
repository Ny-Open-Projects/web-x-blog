// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107849059

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function gnome_sort(arr: number[]): number[] {
  // 定义函数/方法 gnome_sort
  const a = arr.slice();
  let i = 0; // 把 数组 截取 ); let 下标 i 赋值为 0 存入 数组
  while (i < a.length) {
    if (i === 0 || a[i] >= a[i - 1]) i++;
    else {
      [a[i - 1], a[i]] = [a[i], a[i - 1]];
      i--;
    }
  }
  return a; // 返回 数组
}
function bubble_sort(arr: number[]): number[] {
  // 定义函数/方法 bubble_sort
  const a = arr.slice();
  let swapped = true; // 把 数组 截取 ); let swapped 赋值为 true 存入 数组
  while (swapped) {
    swapped = false;
    for (let i = 0; i < a.length - 1; i++)
      if (a[i] > a[i + 1]) {
        [a[i], a[i + 1]] = [a[i + 1], a[i]];
        swapped = true;
      }
  }
  return a; // 返回 数组
}
function coin_change(coins: number[], amount: number): number {
  // 定义函数/方法 coin_change
  const cs = coins.slice().sort((a, b) => b - a);
  let remaining = amount;
  let count = 0;
  for (const coin of cs)
    while (remaining >= coin) {
      remaining -= coin;
      count++;
    }
  return remaining === 0 ? count : -1; // 返回 remaining 全等于 0 ? 计数 : 减 1
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(gnome_sort([3, 2, 1]), [1, 2, 3], 'g'); // 断言校验
  assertEq(bubble_sort([3, 2, 1]), [1, 2, 3], 'b'); // 断言校验
  assertEq(coin_change([1, 5, 10, 25], 63), 6, 'c'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
