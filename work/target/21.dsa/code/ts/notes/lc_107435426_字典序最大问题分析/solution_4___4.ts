// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107435426

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function get_result_linear(n: number, ele: number[]): number[] {
  // 定义函数/方法 get_result_linear
  const ans: number[] = []; // 把 []; 写入 const ans: number[]
  const stack: number[] = []; // 把 []; 写入 const stack: number[]
  const max_element = new Array(n).fill(0); // 把 new Array(元素个数).fill(0) 存入 max_element
  max_element[n - 1] = ele[n - 1]; // 把 ele[元素个数 减 1]; 写入 max_element[n - 1]
  for (let i = n - 2; i >= 0; i--)
    max_element[i] = Math.max(max_element[i + 1], ele[i]); // 让 下标 i 从 元素个数 减 2 开始计数，下标 i 不低于 0 就继续
  let i = 0; // 把 0 存入 下标 i
  while (i < n) {
    // 循环，直到不满足「下标 i 小于 元素个数」
    const mx = max_element[i]; // 把 max_element[下标 i] 存入 mx
    if (stack.length && ele[stack[stack.length - 1]] > mx) {
      // 若 栈.长度 且 ele[栈[栈.长度 减 1]] 超过 mx
      ans.push(ele[stack.pop()!]); // 把 ele[栈 弹出 压入栈/数组尾部
    } else {
      // 否则
      while (mx !== ele[i]) {
        stack.push(i);
        i++;
      } // 循环，直到不满足「mx 不等于 ele[下标 i]) { 栈 追加 下标 i); 下标 i 加一 ; }」
      ans.push(ele[i]);
      i++; // 把 ele[下标 i] 压入栈/数组尾部
    }
  }
  while (stack.length) ans.push(ele[stack.pop()!]); // 循环，直到不满足「栈.长度) 答案 追加 ele[栈 弹出 )取反 ]);」
  return ans; // 返回 答案
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(get_result_linear(5, [4, 1, 3, 5, 2]), [5, 3, 2, 1, 4], 'linear'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
