// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134394571
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function sortArrayByParityII(nums: number[]): number[] {
    // 定义函数/方法 sortArrayByParityII
    const n = nums.length;
    const res = new Array(n);
    let e = 0,
      o = 1;
    for (const v of nums) {
      if (v % 2 === 0) {
        res[e] = v;
        e += 2;
      } else {
        res[o] = v;
        o += 2;
      }
    }
    return res; // 返回 结果
  }
  function validParity(a: number[], src: number[]): boolean {
    // 定义函数/方法 validParity
    if (a.length !== src.length) return false; // 若 数组.长度 不等于 src.长度，直接返回 false
    const ca: Record<number, number> = {},
      cb: Record<number, number> = {};
    for (const v of a) ca[v] = (ca[v] || 0) + 1; // 把 (ca[值] 或 0) 加 1; 写入 for (const v of a) ca[v]
    for (const v of src) cb[v] = (cb[v] || 0) + 1; // 把 (cb[值] 或 0) 加 1; 写入 for (const v of src) cb[v]
    for (const k in ca) if (ca[k] !== cb[k]) return false;
    for (let i = 0; i < a.length; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
      if (i % 2 === 0 && a[i] % 2 !== 0) return false; // 若 下标 i 对…取模 2 全等于 0 且 数组[下标 i] 对…取模 2 不等于 0，直接返回 false
      if (i % 2 === 1 && a[i] % 2 === 0) return false; // 若 下标 i 对…取模 2 全等于 1 且 数组[下标 i] 对…取模 2 全等于 0，直接返回 false
    }
    return true; // 返回 true
  }
  const cases = [
    [4, 2, 5, 7],
    [2, 3],
    [1, 2, 3, 4],
  ]; // 把 [[4,2,5,7],[2,3],[1,2,3,4]] 存入 cases
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    if (!validParity(sortArrayByParityII(c), c)) {
      fail = true;
      console.log('FAIL ' + c);
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
