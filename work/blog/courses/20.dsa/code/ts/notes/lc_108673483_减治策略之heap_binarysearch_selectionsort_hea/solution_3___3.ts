// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108673483
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function majorityElement(arr: number[]): number {
    // 定义函数/方法 majorityElement
    let candidate: number | null = null; // 把 null; 写入 let candidate: number | null
    let count = 0; // 把 0 存入 计数
    for (const num of arr) {
      // for (const num of 数组) {
      if (count === 0) candidate = num; // 若 计数 全等于 0) candidate 赋值为 num;
      if (num === candidate)
        count++; // 若 num 全等于 candidate) 计数 加一 ;
      else count--; // 否则
    }
    let cnt = 0; // 把 0 存入 计数
    for (const num of arr) if (num === candidate) cnt++; // 把 等于 candidate) 计数 加一 ; 写入 for (const num of arr) if (num
    if (cnt > Math.floor(arr.length / 2)) return candidate as number; // 若 计数 超过 向下取整(数组.长度 除以 2)，直接返回 candidate as number
    return -1; // 返回 减 1
  }
  const cases = [
    { a: [2, 2, 1, 1, 1, 1, 1], want: 1 },
    { a: [1, 2, 3], want: -1 },
    { a: [3, 3, 4], want: 3 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = majorityElement(c.a); // 把 majorityElement(字符.数组) 存入 got
    if (got !== c.want) {
      fail = true;
      console.log('FAIL', c, 'got', got);
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
