/**
 ** LeetCode 1047. 删除字符串中的所有相邻重复项
 ** 方案：2 ) 方案2：栈优化
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145114201
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  // removeDuplicates 忠实翻译 python ref solution_2_2_____2____.py（栈消消乐，continue 变体）
  function removeDuplicates(s: string): string {
    // 定义函数/方法 removeDuplicates
    const stack: string[] = []; // 把 []; 写入 const stack: string[]
    for (const x of s) {
      // for (const x of 字符串) {
      if (stack.length && stack[stack.length - 1] === x) {
        // 若 栈.长度 且 栈[栈.长度 减 1] 全等于 x
        stack.pop(); // 弹出栈顶元素
        continue; // 跳过本轮，进入下一次
      }
      stack.push(x); // 把 x 压入栈/数组尾部
    }
    return stack.join(''); // 返回 栈.join('')
  }

  // want 由 python ref 实跑得到
  const cases: { in: string; want: string }[] = [
    { in: 'abbaca', want: 'ca' },
    { in: 'azxxzy', want: 'ay' },
    { in: 'abc', want: 'abc' },
    { in: '', want: '' },
    { in: 'aabb', want: '' },
    { in: 'aaaa', want: '' },
    { in: 'abba', want: '' },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = removeDuplicates(c.in); // 把 removeDuplicates(字符.in) 存入 got
    if (got !== c.want) {
      // 若 got 不等于 字符.want
      fail = true; // 把 true 存入 fail
      console.log(`FAIL solve("${c.in}")="${got}" want "${c.want}"`);
    }
  }
  if (fail) {
    // 若 fail
    throw new Error('FAILED'); // throw new Error(「FAILED」);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
