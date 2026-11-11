// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145347105
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function nextGreaterElement(nums1: number[], nums2: number[]): number[] {
    // 定义函数/方法 nextGreaterElement
    const stack: number[] = []; // 把 []; 写入 const stack: number[]
    const greaterMap: Map<number, number> = new Map(); // 把 new Map(); 写入 const greaterMap: Map<number, number>
    for (const num of nums2) {
      // for (const num of 数组2) {
      while (stack.length > 0 && stack[stack.length - 1] < num) {
        // 循环，直到不满足「栈.长度 超过 0 且 栈[栈.长度 减 1] 小于 num」
        greaterMap.set(stack.pop() as number, num); // 弹出栈顶元素
      }
      stack.push(num); // 把 num 压入栈/数组尾部
    }
    const result: number[] = []; // 把 []; 写入 const result: number[]
    for (const num of nums1) {
      // for (const num of 数组1) {
      result.push(greaterMap.has(num) ? (greaterMap.get(num) as number) : -1); // 把 greaterMap.has(num 压入栈/数组尾部
    }
    return result; // 返回 结果
  }

  function eqArr(a: number[], b: number[]): boolean {
    // 定义函数/方法 eqArr
    if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (let i = 0; i < a.length; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
      if (a[i] !== b[i]) return false; // 若 数组[下标 i] 不等于 b[下标 i]，直接返回 false
    }
    return true; // 返回 true
  }

  const cases = [
    { in1: [4, 1, 2], in2: [1, 3, 4, 2], want: [-1, 3, -1] },
    { in1: [2, 4], in2: [1, 2, 3, 4], want: [3, -1] },
  ];

  let fail = false; // 把 false 存入 fail
  for (let i = 0; i < cases.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 cases.长度 就继续
    const c = cases[i]; // 把 cases[下标 i] 存入 字符
    const got = nextGreaterElement(c.in1, c.in2); // 把 nextGreaterElement(字符.in1, 字符.in2) 存入 got
    if (!eqArr(c.want, got)) {
      // 若 取反 eqArr(字符.want, got
      fail = true; // 把 true 存入 fail
      console.log(
        `FAIL case${i} nextGreaterElement(${JSON.stringify(c.in1)},${JSON.stringify(c.in2)})=${JSON.stringify(got)} want ${JSON.stringify(c.want)}`,
      );
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
