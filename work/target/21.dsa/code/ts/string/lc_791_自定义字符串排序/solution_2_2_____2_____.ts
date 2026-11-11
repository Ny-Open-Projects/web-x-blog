/**
 ** LeetCode 791. 自定义字符串排序
 ** 方案：2 ) 方案2：计数重排
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145385760
 */

export function customSortString(order: string, s: string): string {
  // 定义函数/方法 customSortString
  const count: { [c: string]: number } = {}; // 把 {}; 写入 const count: { [c: string]: number }
  for (const c of s) count[c] = (count[c] || 0) + 1; // 把 (计数[字符] 或 0) 加 1; 写入 for (const c of s) count[c]
  const result: string[] = []; // 把 []; 写入 const result: string[]
  for (const c of order) {
    // for (const 字符 of order) {
    if (c in count) {
      // 若 字符 in 计数
      result.push(c.repeat(count[c])); // 把 字符.repeat(计数[字符] 压入栈/数组尾部
      delete count[c]; // delete 计数[字符];
    }
  }
  for (const c in count) result.push(c.repeat(count[c])); // 把 字符.repeat(计数[字符] 压入栈/数组尾部
  return result.join(''); // 返回 结果.join('')
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  if (customSortString('cba', 'abcd') !== 'cbad')
    throw new Error('FAILED 1: ' + customSortString('cba', 'abcd'));
  if (customSortString('cbafg', 'abcd') !== 'cbad') throw new Error('FAILED 2');
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
