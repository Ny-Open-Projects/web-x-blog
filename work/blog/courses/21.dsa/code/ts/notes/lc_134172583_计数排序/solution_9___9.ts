// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134172583
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function countSort(lst: number[]): void {
    // 定义函数/方法 countSort
    const length = lst.length; // 把 lst.长度 存入 长度
    if (length < 2) return; // 若 长度 小于 2) return;
    let maxVal = lst[0],
      minVal = lst[0]; // 把 lst[0], minVal 赋值为 lst[0] 存入 maxVal
    for (const v of lst) {
      if (v > maxVal) maxVal = v;
      if (v < minVal) minVal = v;
    }
    const countList = new Array(maxVal - minVal + 1).fill(0); // 把 new Array(maxVal 减 minVal 加 1).fill(0) 存入 countList
    for (const num of lst) countList[num - minVal]++; // for (const num of lst) countList[num 减 minVal] 加一 ;
    let i = 0; // 把 0 存入 下标 i
    for (let j = 0; j < maxVal - minVal + 1; j++) {
      for (let k = 0; k < countList[j]; k++) {
        lst[i++] = j + minVal;
      }
    } // 让 下标 j 从 0 开始计数，下标 j 小于 maxVal 减 minVal 加 1 就继续
  }
  let fail = false; // 把 false 存入 fail
  const c1 = [
    2, 3, 8, 7, 1, 2, 2, 2, 7, 3, 9, 8, 2, 1, 4, 2, 4, 6, 9, 2,
  ].slice();
  countSort(c1); // countSort(c1);
  if (
    JSON.stringify(c1) !==
    JSON.stringify([1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 6, 7, 7, 8, 8, 9, 9])
  ) {
    fail = true;
    console.log('FAIL countSort in-place A=' + JSON.stringify(c1));
  }
  const c2 = [4, 2, 4, 3].slice(); // 把 [4,2,4,3] 截取 ) 存入 c2
  countSort(c2); // countSort(c2);
  if (JSON.stringify(c2) !== JSON.stringify([2, 3, 4, 4])) {
    fail = true;
    console.log('FAIL countSort in-place [4,2,4,3]=' + JSON.stringify(c2));
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
