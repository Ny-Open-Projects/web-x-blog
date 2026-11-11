/**
 ** LeetCode 1329. 将矩阵按对角线排序
 ** 方案：2 ) 方案2：优化版
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145381786
 */

export function diagonalSort(mat: number[][]): number[][] {
  // 定义函数/方法 diagonalSort
  const rows = mat.length; // 把 mat.长度 存入 行数
  const cols = mat[0].length; // 把 mat[0].长度 存入 列数
  const diags: Map<number, number[]> = new Map(); // 把 new Map(); 写入 const diags: Map<number, number[]>
  for (let r = 0; r < rows; r++) {
    // 让 右指针 从 0 开始计数，右指针 小于 行数 就继续
    for (let c = 0; c < cols; c++) {
      // 让 字符 从 0 开始计数，字符 小于 列数 就继续
      const key = r - c; // 把 右指针 减 字符 存入 key
      if (!diags.has(key)) diags.set(key, []); // 若 取反 diags.has(key)) diags.set(key, []);
      diags.get(key)!.push(mat[r][c]); // 把 mat[右指针][字符] 压入栈/数组尾部
    }
  }
  for (const arr of diags.values()) arr.sort((a, b) => a - b);
  for (let r = 0; r < rows; r++) {
    // 让 右指针 从 0 开始计数，右指针 小于 行数 就继续
    for (let c = 0; c < cols; c++) {
      // 让 字符 从 0 开始计数，字符 小于 列数 就继续
      const key = r - c; // 把 右指针 减 字符 存入 key
      mat[r][c] = diags.get(key)!.shift()!; // 取出队首元素
    }
  }
  return mat; // 返回 mat
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const m = [
    [3, 3, 1, 1],
    [2, 2, 1, 2],
    [1, 1, 1, 2],
  ]; // 把 [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]] 存入 映射表
  const got = diagonalSort(m.map((r) => r.slice()));
  const exp = [
    [1, 1, 1, 1],
    [1, 2, 2, 2],
    [1, 2, 3, 3],
  ]; // 把 [[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3]] 存入 exp
  if (JSON.stringify(got) !== JSON.stringify(exp)) {
    // 若 JSON.stringify(got) 不等于 JSON.stringify(exp
    throw new Error('FAILED: ' + JSON.stringify(got)); // throw new Error(「FAILED: 」 加 JSON.stringify(got));
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
