// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145345560
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function flatArray(arr: any[]): number[] {
    // 定义函数/方法 flatArray
    const stack: any[] = arr.slice(); // 把 数组 截取 ); 写入 const stack: any[]
    const ret: number[] = []; // 把 []; 写入 const ret: number[]
    while (stack.length > 0) {
      // 循环，直到不满足「栈.长度 超过 0」
      const next_item = stack.pop(); // 把 栈 弹出 ) 存入 next_item
      if (Array.isArray(next_item)) {
        // 若 Array.isArray(next_item
        stack.push(...next_item); // 把 next_item 压入栈/数组尾部
      } else {
        // 否则
        ret.unshift(next_item); // ret.unshift(next_item);
      }
    }
    return ret; // 返回 ret
  }
  function eqArr(a: number[], b: number[]): boolean {
    // 定义函数/方法 eqArr
    if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    return true; // 返回 true
  }
  const cases = [
    { inp: [1, 2, 3], want: [1, 2, 3] },
    { inp: [[1, [2]], 3], want: [1, 2, 3] },
    { inp: [1, [4, [6]]], want: [1, 4, 6] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = flatArray(c.inp); // 把 flatArray(字符.inp) 存入 got
    if (!eqArr(got, c.want)) {
      fail = true;
      console.log('FAIL', c, 'got', got);
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
