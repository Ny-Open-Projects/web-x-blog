// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135038527
// LeetCode 217. 存在重复元素 — Dart 版（方案2）
bool containsDuplicate(List<int> nums) => nums.toSet().length != nums.length;
void main() {
  // 程序入口：跑内嵌自测用例
  if (!containsDuplicate([1, 2, 3, 1])) throw StateError('c1');
  if (containsDuplicate([1, 2, 3, 4]))
    throw StateError(
      'c2',
    ); // 若 containsDuplicate([1, 2, 3, 4])) throw StateError('c2');
  print('PASS'); // 全部用例通过，输出 PASS
}
