/**
 ** LeetCode 344. 反转字符串
 ** 方案：1 ) 方案1：双指针
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145116781
 */

function reverseString(s: string[]): void {
  // 定义函数/方法 reverseString
  let left = 0,
    right = s.length - 1; // 把 0, 右边界 赋值为 字符串.长度 减 1 存入 左边界
  while (left <= right) {
    // 循环，直到不满足「左边界 不超过 右边界」
    const tmp = s[left]; // 把 字符串[左边界] 存入 临时变量
    s[left] = s[right]; // 把 字符串[右边界]; 写入 s[left]
    s[right] = tmp; // 把 临时变量; 写入 s[right]
    left++; // 左边界 加一
    right--; // 右边界 减一
  }
}

function eqStr(a: string[], b: string[]): boolean {
  // 定义函数/方法 eqStr
  if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
  for (let i = 0; i < a.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    if (a[i] !== b[i]) return false; // 若 数组[下标 i] 不等于 b[下标 i]，直接返回 false
  }
  return true; // 返回 true
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const cases: [string[], string[]][] = [
    [
      ['h', 'e', 'l', 'l', 'o'],
      ['o', 'l', 'l', 'e', 'h'],
    ],
    [
      ['H', 'a', 'n', 'n', 'a', 'h'],
      ['h', 'a', 'n', 'n', 'a', 'H'],
    ],
  ];
  for (const [input, expected] of cases) {
    // for (const [input, expected] of cases) {
    reverseString(input); // reverseString(input);
    if (!eqStr(input, expected)) {
      // 若 取反 eqStr(input, expected
      throw new Error('FAIL: got ' + input + ' expected ' + expected);
    }
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
