// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134085384
// 数据结构与算法之排序: 选择排序 — Dart 版（方案1）
List<int> selectionSort(List<int> nums) {
  // 定义函数/方法 selectionSort
  final v = List<int>.from(nums); // 把 List 小于 int 超过 .from(数组) 存入 值
  for (var i = 0; i + 1 < v.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 加 1 小于 值.长度 就继续
    var m = i; // 把 下标 i 存入 映射表
    for (var j = i + 1; j < v.length; j++) {
      if (v[j] < v[m]) m = j;
    } // 让 下标 j 从 下标 i 加 1 开始计数，下标 j 小于 值.长度 就继续
    final t = v[i]; // 把 值[下标 i] 存入 另一字符串
    v[i] = v[m]; // 把 值[映射表]; 写入 v[i]
    v[m] = t; // 把 另一字符串; 写入 v[m]
  }
  return v; // 返回 值
}

void main() {
  if (selectionSort([5, 4, 3, 2, 1]).toString() != '[1, 2, 3, 4, 5]')
    throw StateError('c1');
  print('PASS');
} // 全部用例通过，输出 PASS
