// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144827578
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function lengthOfLIS(nums: number[], k: number): number {
    // 定义函数/方法 lengthOfLIS
    if (nums.length === 0) return 0; // 若 数组.长度 全等于 0，直接返回 0
    const vals = Array.from(new Set(nums)).sort((a, b) => a - b);
    const comp: { [v: number]: number } = {}; // 把 {}; 写入 const comp: {[v: number]: number}
    vals.forEach((v, i) => {
      comp[v] = i;
    });
    const m = vals.length; // 把 vals.长度 存入 映射表
    let size = 1; // 把 1 存入 大小
    while (size < m) size <<= 1; // 循环，直到不满足「大小 小于 映射表) 大小 小于 不超过 1;」
    const tree = new Array(2 * size).fill(0); // 把 new Array(2 乘 大小).fill(0) 存入 tree
    function update(pos: number, val: number): void {
      // 定义函数/方法 update
      pos += size; // pos累加 大小
      if (val > tree[pos]) tree[pos] = val; // 若 值 超过 tree[pos]) tree[pos] 赋值为 值;
      pos >>= 1; // 把 1; 写入 pos >>
      while (pos) {
        // 循环，直到不满足「pos」
        tree[pos] = Math.max(tree[2 * pos], tree[2 * pos + 1]); // 把 Math.取较大值 tree[2 乘 pos], tree[2 乘 pos 加 1]); 写入 tree[pos]
        pos >>= 1; // 把 1; 写入 pos >>
      }
    }
    function query(l: number, r: number): number {
      // 定义函数/方法 query
      l += size;
      r += size; // 把 大小; 右指针 累加 大小; 写入 l +
      let res = 0; // 把 0 存入 结果
      while (l <= r) {
        // 循环，直到不满足「左指针 不超过 右指针」
        if (l & 1) {
          res = Math.max(res, tree[l]);
          l++;
        } // 若 左指针 按位与 1) { 结果 赋值为 Math.取较大值 结果, tree[左指针]); 左指针 加一 ; }
        if (!(r & 1)) {
          res = Math.max(res, tree[r]);
          r--;
        }
        l >>= 1;
        r >>= 1; // 把 1; 右指针 超过 不低于 1; 写入 l >>
      }
      return res; // 返回 结果
    }
    let ans = 0; // 把 0 存入 答案
    for (const x of nums) {
      // for (const x of 数组) {
      const ci = comp[x]; // 把 comp[x] 存入 ci
      let lo = 0,
        hi = vals.length; // 把 0, 右边界 赋值为 vals.长度 存入 左边界
      while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (vals[mid] < x - k) lo = mid + 1;
        else hi = mid;
      }
      let best = 0; // 把 0 存入 当前最优
      if (lo <= ci - 1) best = query(lo, ci - 1); // 若 左边界 不超过 ci 减 1) 当前最优 赋值为 query(左边界, ci 减 1);
      const cur = best + 1; // 把 当前最优 加 1 存入 当前值
      if (cur > ans) ans = cur; // 若 当前值 超过 答案) 答案 赋值为 当前值;
      update(ci, cur); // update(ci, 当前值);
    }
    return ans; // 返回 答案
  }
  const cases: [number[], number, number][] = [
    [[4, 2, 1, 4, 3, 4, 5, 8, 15], 3, 5],
    [[1], 1, 1],
    [[], 3, 0],
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = lengthOfLIS(c[0], c[1]); // 把 lengthOfLIS(字符[0], 字符[1]) 存入 got
    if (got !== c[2]) {
      fail = true;
      console.log(
        'FAIL lengthOfLIS(' +
          JSON.stringify(c[0]) +
          ',' +
          c[1] +
          ')=' +
          got +
          ' want ' +
          c[2],
      );
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
