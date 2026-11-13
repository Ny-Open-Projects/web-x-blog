// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145012016
// LeetCode 496. 下一个更大元素 I — Dart 版（方案1）
List<int> nextGreaterElement(List<int> nums1, List<int> nums2) {
  // 定义函数/方法 nextGreaterElement
  final next = <int, int>{}; // 把 小于 int, int 超过 {} 存入 下一个
  final st = <int>[]; // 把 小于 int 超过 [] 存入 st
  for (final v in nums2) {
    // for (final 值 in 数组2) {
    while (st.isNotEmpty && st.last < v) {
      // 循环，直到不满足「st.isNotEmpty 且 st.last 小于 值」
      next[st.removeLast()] = v; // 把 值; 写入 next[st.removeLast()]
    }
    st.add(v); // st 追加 值);
  }
  return nums1.map((v) => next[v] ?? -1).toList();
}

void main() {
  if (nextGreaterElement([4, 1, 2], [1, 3, 4, 2]).toString() != '[-1, 3, -1]')
    throw StateError('c1');
  if (nextGreaterElement([2, 4], [1, 2, 3, 4]).toString() != '[3, -1]')
    throw StateError('c2');
  print('PASS');
} // 全部用例通过，输出 PASS
