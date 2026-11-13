// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function merge(left: number[], right: number[]): number[] {
    // 定义函数/方法 merge
    const result: number[] = []; // 把 []; 写入 const result: number[]
    let i = 0,
      j = 0; // 把 0, 下标 j 赋值为 0 存入 下标 i
    while (i < left.length && j < right.length) {
      // 循环，直到不满足「下标 i 小于 左边界.长度 且 下标 j 小于 右边界.长度」
      if (left[i] <= right[j]) {
        // 若 左边界[下标 i] 不超过 右边界[下标 j]
        result.push(left[i]);
        i++; // 把 左边界[下标 i] 压入栈/数组尾部
      } else {
        // 否则
        result.push(right[j]);
        j++; // 把 右边界[下标 j] 压入栈/数组尾部
      }
    }
    while (i < left.length) {
      result.push(left[i]);
      i++;
    } // 循环，直到不满足「下标 i 小于 左边界.长度) { 结果 追加 左边界[下标 i]); 下标 i 加一 ; }」
    while (j < right.length) {
      result.push(right[j]);
      j++;
    } // 循环，直到不满足「下标 j 小于 右边界.长度) { 结果 追加 右边界[下标 j]); 下标 j 加一 ; }」
    return result; // 返回 结果
  }

  // 归并排序：时间复杂度 O(n log n)，空间复杂度 O(n)
  function mergeSort(arr: number[]): number[] {
    // 定义函数/方法 mergeSort
    if (arr.length <= 1) return arr; // 若 数组.长度 不超过 1，直接返回 数组
    const mid = Math.floor(arr.length / 2); // 把 向下取整(数组.长度 除以 2) 存入 中点
    const left = mergeSort(arr.slice(0, mid)); // 把 mergeSort(数组 截取 0, 中点)) 存入 左边界
    const right = mergeSort(arr.slice(mid)); // 把 mergeSort(数组 截取 中点)) 存入 右边界
    return merge(left, right); // 返回 merge(左边界, 右边界)
  }

  function eqArr(a: number[], b: number[]): boolean {
    // 定义函数/方法 eqArr
    if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    return true; // 返回 true
  }

  const cases: { in: number[]; want: number[] }[] = [
    { in: [3, 1, 4, 1, 5, 9, 2, 6], want: [1, 1, 2, 3, 4, 5, 6, 9] },
    { in: [], want: [] },
    { in: [1], want: [1] },
    { in: [5, 4, 3, 2, 1], want: [1, 2, 3, 4, 5] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = mergeSort(c.in.slice()); // 把 mergeSort(字符.in 截取 )) 存入 got
    if (!eqArr(got, c.want)) {
      // 若 取反 eqArr(got, 字符.want
      fail = true; // 把 true 存入 fail
      console.log('FAIL mergeSort(%o)=%o want %o', c.in, got, c.want); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
