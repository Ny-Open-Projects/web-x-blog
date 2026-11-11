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
    102, 103, 108, 107, 101, 102, 102, 102, 107, 103, 109, 108, 102, 101, 104,
    102, 104, 106, 109, 102,
  ].slice();
  countSort(c1); // countSort(c1);
  if (
    JSON.stringify(c1) !==
    JSON.stringify([
      101, 101, 102, 102, 102, 102, 102, 102, 102, 103, 103, 104, 104, 106, 107,
      107, 108, 108, 109, 109,
    ])
  ) {
    fail = true;
    console.log('FAIL countSort in-place B=' + JSON.stringify(c1));
  }
  const c2 = [5, 3, 8, 3, 1].slice(); // 把 [5,3,8,3,1] 截取 ) 存入 c2
  countSort(c2); // countSort(c2);
  if (JSON.stringify(c2) !== JSON.stringify([1, 3, 3, 5, 8])) {
    fail = true;
    console.log('FAIL countSort in-place [5,3,8,3,1]=' + JSON.stringify(c2));
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
