// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145565975
/**
 ** LeetCode 541. 反转字符串 II
 ** 方案1: 双指针
 */

function reverseStr(s: string, k: number): string {
  // 定义函数/方法 reverseStr
  const n = s.length; // 把 字符串.长度 存入 元素个数
  const arr: string[] = Array.from(s); // 把 Array.from(字符串); 写入 const arr: string[]
  for (let i = 0; i < n; i += 2 * k) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    let left = i; // 把 下标 i 存入 左边界
    let right = Math.min(i + k - 1, n - 1); // 把 Math.取较小值 下标 i 加 下标 k 减 1, 元素个数 减 1) 存入 右边界
    while (left < right) {
      // 循环，直到不满足「左边界 小于 右边界」
      const temp = arr[left]; // 把 数组[左边界] 存入 临时变量
      arr[left] = arr[right]; // 把 数组[右边界]; 写入 arr[left]
      arr[right] = temp; // 把 临时变量; 写入 arr[right]
      left++; // 左边界 加一
      right--; // 右边界 减一
    }
  }
  return arr.join(''); // 返回 数组.join('')
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const cases: { in: [string, number]; want: string }[] = [
    { in: ['abc', 1], want: 'abc' },
    { in: ['abcdefg', 2], want: 'bacdfeg' },
    { in: ['abcd', 2], want: 'bacd' },
    { in: ['abcdefgh', 3], want: 'cbadefhg' },
    { in: ['a', 1], want: 'a' },
    { in: ['', 2], want: '' },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = reverseStr(c.in[0], c.in[1]); // 把 reverseStr(字符.in[0], 字符.in[1]) 存入 got
    if (got !== c.want) {
      // 若 got 不等于 字符.want
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL reverseStr("' +
          c.in[0] +
          '",' +
          c.in[1] +
          ')="' +
          got +
          '" want "' +
          c.want +
          '"',
      ); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
