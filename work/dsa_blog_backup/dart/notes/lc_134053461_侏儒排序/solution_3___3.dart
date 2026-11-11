// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134053461
// 数据结构与算法之排序: 侏儒排序 — Dart 版（方案3）
List<int> gnomeSort(List<int> nums) {
  // 定义函数/方法 gnomeSort
  final v = List<int>.from(nums); // 把 List 小于 int 超过 .from(数组) 存入 值
  var i = 0; // 把 0 存入 下标 i
  while (i < v.length) {
    // 循环，直到不满足「下标 i 小于 值.长度」
    if (i == 0 || v[i - 1] <= v[i]) {
      i++;
    } // 若 下标 i 等于 0 或 值[下标 i 减 1] 不超过 值[下标 i]) { 下标 i 加一 ; }
    else {
      // 否则
      final t = v[i - 1]; // 把 值[下标 i 减 1] 存入 另一字符串
      v[i - 1] = v[i]; // 把 值[下标 i]; 写入 v[i - 1]
      v[i] = t; // 把 另一字符串; 写入 v[i]
      i--; // 下标 i 减一
    }
  }
  return v; // 返回 值
}

void main() {
  if (gnomeSort([5, 4, 3, 2, 1]).toString() != '[1, 2, 3, 4, 5]')
    throw StateError('c1');
  print('PASS');
} // 全部用例通过，输出 PASS
