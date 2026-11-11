/**
 ** LeetCode 452. 用最少数量的箭引爆气球
 ** 方案：1 ) 方案1: 排序 + 贪心
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145244333
 */

export function findMinArrowShots(points: number[][] | null): number {
  // 定义函数/方法 findMinArrowShots
  if (!points || points.length === 0) return 0; // 若 取反 points 或 points.长度 全等于 0，直接返回 0
  points.sort((a, b) => a[1] - b[1]);
  let arrows = 1; // 把 1 存入 arrows
  let end = points[0][1]; // 把 points[0][1] 存入 终点
  for (let k = 1; k < points.length; k++) {
    // 让 下标 k 从 1 开始计数，下标 k 小于 points.长度 就继续
    const start = points[k][0]; // 把 points[下标 k][0] 存入 起点
    const endPoint = points[k][1]; // 把 points[下标 k][1] 存入 endPoint
    if (start > end) {
      // 若 起点 超过 终点
      arrows++; // arrows 加一
      end = endPoint; // 把 endPoint 存入 终点
    }
  }
  return arrows; // 返回 arrows
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  if (findMinArrowShots(null) !== 0) throw new Error('FAILED null');
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
