// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135949307
// LeetCode 452. 用最少数量的箭引爆气球 — Dart 版（方案2）
int findMinArrowShots(List<List<int>> points) {
  // 定义函数/方法 findMinArrowShots
  if (points.isEmpty) return 0; // 若 points.isEmpty，直接返回 0
  final arr =
      List<List<int>>.from(
          points,
        ) // 把 List 小于 List 小于 int 超过 超过 .from(points) 存入 数组
        ..sort((a, b) => a[1].compareTo(b[1]));
  var arrows = 1; // 把 1 存入 arrows
  var end = arr[0][1]; // 把 数组[0][1] 存入 终点
  for (var k = 1; k < arr.length; k++) {
    // 让 下标 k 从 1 开始计数，下标 k 小于 数组.长度 就继续
    if (arr[k][0] > end) {
      // 若 数组[下标 k][0] 超过 终点
      arrows++; // arrows 加一
      end = arr[k][1]; // 把 数组[下标 k][1] 存入 终点
    }
  }
  return arrows; // 返回 arrows
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (findMinArrowShots([
        [10, 16],
        [2, 8],
        [1, 6],
        [7, 12], // [7, 12]
      ]) !=
      2)
    throw StateError('c1'); // 把 2) throw StateError('c1'); 写入 ]) !
  if (findMinArrowShots([]) != 0)
    throw StateError(
      'c2',
    ); // 若 findMinArrowShots([]) 不等于 0) throw StateError('c2');
  if (findMinArrowShots([
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8], // [7, 8]
      ]) !=
      4)
    throw StateError('c3'); // 把 4) throw StateError('c3'); 写入 ]) !
  print('PASS'); // 全部用例通过，输出 PASS
}
