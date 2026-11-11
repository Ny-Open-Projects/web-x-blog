// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145568435
// LeetCode 350. 两个数组的交集 II — Dart 版（方案2）
List<int> intersect(List<int> nums1, List<int> nums2) {
  // 定义函数/方法 intersect
  final a = nums1.length <= nums2.length
      ? nums1
      : nums2; // 把 数组1.长度 不超过 数组2.长度 ? 数组1 : 数组2 存入 数组
  final b = nums1.length <= nums2.length
      ? nums2
      : nums1; // 把 数组1.长度 不超过 数组2.长度 ? 数组2 : 数组1 存入 b
  final mp = <int, int>{}; // 把 小于 int, int 超过 {} 存入 mp
  for (final v in a) {
    // for (final 值 in 数组) {
    mp[v] = (mp[v] ?? 0) + 1; // 把 (mp[值] ?? 0) 加 1; 写入 mp[v]
  }
  final res = <int>[]; // 把 小于 int 超过 [] 存入 结果
  for (final v in b) {
    // for (final 值 in b) {
    final c = mp[v] ?? 0; // 把 mp[值] ?? 0 存入 字符
    if (c > 0) {
      // 若 字符 超过 0
      res.add(v); // 结果 追加 值);
      mp[v] = c - 1; // 把 字符 减 1; 写入 mp[v]
    }
  }
  return res; // 返回 结果
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (intersect([1, 2, 2, 1], [2, 2]).toString() != '[2, 2]')
    throw StateError('c1');
  if (intersect([4, 9, 5], [9, 4, 9, 8, 4]).toString() != '[9, 4]')
    throw StateError('c2');
  print('PASS'); // 全部用例通过，输出 PASS
}
