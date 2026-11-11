// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397820
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function nextGreaterElement(n: number): number {
    // 下一个更大排列：下一排列法
    const MAX = 2147483647; // 32 位上限
    const digits: number[] = []; // 逐位拆解
    let x = n;
    if (x === 0) digits.push(0);
    while (x > 0) {
      digits.unshift(x % 10);
      x = Math.floor(x / 10);
    }
    let i = digits.length - 2; // 从右找第一个降序位
    while (i >= 0 && digits[i] >= digits[i + 1]) i--;
    if (i < 0) return -1; // 整体降序，无更大排列
    let j = digits.length - 1; // 从右找第一个大于 digits[i] 的位
    while (digits[j] <= digits[i]) j--;
    const tmp = digits[i];
    digits[i] = digits[j];
    digits[j] = tmp; // 交换
    const tail = digits.splice(i + 1).sort((a, b) => a - b); // 后缀升序
    const all = digits.concat(tail);
    let result = 0; // 重拼数字
    for (const d of all) result = result * 10 + d;
    return result > MAX ? -1 : result; // 超界返回 -1
  }
  const cases = [
    { in: 12, want: 21 },
    { in: 21, want: -1 },
    { in: 321, want: -1 },
    { in: 4321, want: -1 },
    { in: 1999999999, want: -1 }, // { in: 1999999999, want: 减 1 }
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = nextGreaterElement(c.in); // 把 nextGreaterElement(字符.in) 存入 got
    if (got !== c.want) {
      fail = true;
      console.log(
        'FAIL nextGreaterElement(' + c.in + ')=' + got + ' want ' + c.want,
      );
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
