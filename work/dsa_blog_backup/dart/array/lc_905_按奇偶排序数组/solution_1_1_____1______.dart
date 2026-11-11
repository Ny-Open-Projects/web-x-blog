// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134893847
// LeetCode 905. 按奇偶排序数组 — Dart 版（方案1）
List<int> sortArrayByParity(List<int> nums) {
  // 定义函数/方法 sortArrayByParity
  final v = List<int>.from(nums); // 把 List 小于 int 超过 .from(数组) 存入 值
  var pos = 0; // 把 0 存入 pos
  for (var i = 0; i < v.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 值.长度 就继续
    if (v[i] % 2 == 0) {
      // 若 值[下标 i] 对…取模 2 等于 0
      final t = v[pos]; // 把 值[pos] 存入 另一字符串
      v[pos] = v[i]; // 把 值[下标 i]; 写入 v[pos]
      v[i] = t; // 把 另一字符串; 写入 v[i]
      pos++; // pos 加一
    }
  }
  return v; // 返回 值
}

void main() {
  // 程序入口：跑内嵌自测用例
  final g1 = sortArrayByParity([
    3,
    1,
    2,
    4,
  ]); // 把 sortArrayByParity([3, 1, 2, 4]) 存入 g1
  if (g1.length != 4 || g1[0] % 2 != 0 || g1[1] % 2 != 0 || g1[2] % 2 != 1)
    throw StateError('c1');
  if (sortArrayByParity([1, 2, 3]).toString() != '[2, 1, 3]')
    throw StateError('c2');
  print('PASS');
} // 全部用例通过，输出 PASS
