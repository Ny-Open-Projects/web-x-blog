// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134205361
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function bucketSort(lst: number[], n: number): number[] {
    // 定义函数/方法 bucketSort
    if (lst.length < 2) return lst.slice(); // 若 lst.长度 小于 2，直接返回 lst 截取 )
    const max_val = Math.max.apply(null, lst),
      min_val = Math.min.apply(null, lst);
    const dist = max_val - min_val; // 把 max_val 减 min_val 存入 dist
    if (dist === 0) return lst.slice(); // 若 dist 全等于 0，直接返回 lst 截取 )
    const buckets: number[][] = []; // 把 []; 写入 const buckets: number[][]
    for (let i = 0; i < n; i++) buckets.push([]); // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    const width = Math.floor((dist + 1) / n); // 把 向下取整((dist 加 1) 除以 元素个数) 存入 width
    for (const current of lst) {
      // for (const current of lst) {
      let index = Math.floor((current - min_val) / width); // 把 向下取整((current 减 min_val) 除以 width) 存入 index
      if (index >= n) index = n - 1; // 若 index 不低于 元素个数) index 赋值为 元素个数 减 1;
      buckets[index].push(current); // 把 current 压入栈/数组尾部
    }
    for (const bucket of buckets) bucket.sort((x, y) => x - y);
    const result: number[] = []; // 把 []; 写入 const result: number[]
    for (const bucket of buckets) for (const item of bucket) result.push(item); // 把 item 压入栈/数组尾部
    return result; // 返回 结果
  }
  function eqArr(a: number[], b: number[]): boolean {
    // 定义函数/方法 eqArr
    if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    return true; // 返回 true
  }
  const cases = [
    { a: [5, 4, 3, 2, 1], want: [1, 2, 3, 4, 5] },
    { a: [1, 2, 3, 4, 5], want: [1, 2, 3, 4, 5] },
    { a: [], want: [] },
    { a: [1], want: [1] },
    {
      a: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],
      want: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9],
    },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = bucketSort(c.a.slice(), 5); // 把 bucketSort(字符.数组 截取 ), 5) 存入 got
    if (!eqArr(got, c.want)) {
      fail = true;
      console.log('FAIL', c, 'got', JSON.stringify(got));
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
