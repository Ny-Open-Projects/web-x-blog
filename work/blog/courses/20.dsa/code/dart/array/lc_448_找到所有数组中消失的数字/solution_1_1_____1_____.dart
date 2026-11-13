// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134378688
// LeetCode 448. 找到所有数组中消失的数字 — Dart 版（方案1）
List<int> findDisappearedNumbers(List<int> nums) {
  // 定义函数/方法 findDisappearedNumbers
  final v = List<int>.from(nums); // 把 List 小于 int 超过 .from(数组) 存入 值
  for (var i = 0; i < v.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 值.长度 就继续
    final idx = v[i].abs() - 1; // 把 值[下标 i].取绝对值 ) 减 1 存入 idx
    if (v[idx] > 0) v[idx] = -v[idx]; // 若 值[idx] 超过 0) 值[idx] 赋值为 减 值[idx];
  }
  final out = <int>[]; // 把 小于 int 超过 [] 存入 out
  for (var i = 0; i < v.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 值.长度 就继续
    if (v[i] > 0) out.add(i + 1); // 若 值[下标 i] 超过 0) out 追加 下标 i 加 1);
  }
  return out; // 返回 out
}

void main() {
  if (findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]).toString() != '[5, 6]')
    throw StateError('c1');
  if (findDisappearedNumbers([1, 1]).toString() != '[2]')
    throw StateError('c2');
  print('PASS');
} // 全部用例通过，输出 PASS
