// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134082074
// 数据结构与算法之排序: 插入排序 — Dart 版（方案2）
List<int> insertionSort(List<int> nums) {
  // 定义函数/方法 insertionSort
  final v = List<int>.from(nums); // 把 List 小于 int 超过 .from(数组) 存入 值
  for (var i = 1; i < v.length; i++) {
    // 让 下标 i 从 1 开始计数，下标 i 小于 值.长度 就继续
    final key = v[i]; // 把 值[下标 i] 存入 key
    var j = i - 1; // 把 下标 i 减 1 存入 下标 j
    while (j >= 0 && v[j] > key) {
      v[j + 1] = v[j];
      j--;
    }
    v[j + 1] = key; // 把 key; 写入 v[j + 1]
  }
  return v; // 返回 值
}

void main() {
  if (insertionSort([5, 4, 3, 2, 1]).toString() != '[1, 2, 3, 4, 5]')
    throw StateError('c1');
  print('PASS');
} // 全部用例通过，输出 PASS
