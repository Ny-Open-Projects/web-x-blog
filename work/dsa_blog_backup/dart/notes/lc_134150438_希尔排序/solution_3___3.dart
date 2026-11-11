// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134150438
// 数据结构与算法之排序: 希尔排序 — Dart 版（方案3）
List<int> shellSort(List<int> nums) {
  // 定义函数/方法 shellSort
  final v = List<int>.from(nums); // 把 List 小于 int 超过 .from(数组) 存入 值
  var gap = v.length ~/ 2; // 把 值.长度 ~ 除以 2 存入 gap
  while (gap > 0) {
    // 循环，直到不满足「gap 超过 0」
    for (var i = gap; i < v.length; i++) {
      // 让 下标 i 从 gap 开始计数，下标 i 小于 值.长度 就继续
      final key = v[i]; // 把 值[下标 i] 存入 key
      var j = i - gap; // 把 下标 i 减 gap 存入 下标 j
      while (j >= 0 && v[j] > key) {
        v[j + gap] = v[j];
        j -= gap;
      }
      v[j + gap] = key; // 把 key; 写入 v[j + gap]
    }
    gap ~/= 2; // 把 2; 写入 gap ~/
  }
  return v; // 返回 值
}

void main() {
  if (shellSort([5, 2, 4, 6, 1, 3]).toString() != '[1, 2, 3, 4, 5, 6]')
    throw StateError('c1');
  print('PASS');
} // 全部用例通过，输出 PASS
