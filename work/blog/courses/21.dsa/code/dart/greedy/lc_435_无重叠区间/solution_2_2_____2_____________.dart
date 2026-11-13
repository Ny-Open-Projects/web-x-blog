// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135941089
// LeetCode 435. 无重叠区间 — Dart 版（方案2）
int eraseOverlapIntervals(List<List<int>> intervals) {
  // 定义函数/方法 eraseOverlapIntervals
  if (intervals.isEmpty) return 0; // 若 intervals.isEmpty，直接返回 0
  final arr =
      List<List<int>>.from(
          intervals,
        ) // 把 List 小于 List 小于 int 超过 超过 .from(intervals) 存入 数组
        ..sort((a, b) => a[1].compareTo(b[1]));
  var count = 1; // 把 1 存入 计数
  var end = arr[0][1]; // 把 数组[0][1] 存入 终点
  for (var i = 1; i < arr.length; i++) {
    // 让 下标 i 从 1 开始计数，下标 i 小于 数组.长度 就继续
    if (arr[i][0] >= end) {
      // 若 数组[下标 i][0] 不低于 终点
      count++; // 计数 加一
      end = arr[i][1]; // 把 数组[下标 i][1] 存入 终点
    }
  }
  return arr.length - count; // 返回 数组.长度 减 计数
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (eraseOverlapIntervals([
        [1, 2],
        [2, 3],
        [3, 4],
        [1, 3], // [1, 3]
      ]) !=
      1)
    throw StateError('c1'); // 把 1) throw StateError('c1'); 写入 ]) !
  if (eraseOverlapIntervals([]) != 0)
    throw StateError(
      'c2',
    ); // 若 eraseOverlapIntervals([]) 不等于 0) throw StateError('c2');
  if (eraseOverlapIntervals([
        [1, 2],
        [1, 2],
        [1, 2], // [1, 2]
      ]) !=
      2)
    throw StateError('c3'); // 把 2) throw StateError('c3'); 写入 ]) !
  print('PASS'); // 全部用例通过，输出 PASS
}
