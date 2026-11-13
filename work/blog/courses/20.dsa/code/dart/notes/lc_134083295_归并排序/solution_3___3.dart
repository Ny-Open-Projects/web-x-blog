// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134083295
// 数据结构与算法之排序: 归并排序 — Dart 版（方案3）
List<int> mergeSort(List<int> nums) {
  // 定义函数/方法 mergeSort
  if (nums.length <= 1) return nums; // 若 数组.长度 不超过 1，直接返回 数组
  final mid = nums.length ~/ 2; // 把 数组.长度 ~ 除以 2 存入 中点
  final left = mergeSort(
    nums.sublist(0, mid),
  ); // 把 mergeSort(数组.sublist(0, 中点)) 存入 左边界
  final right = mergeSort(
    nums.sublist(mid),
  ); // 把 mergeSort(数组.sublist(中点)) 存入 右边界
  final out = <int>[]; // 把 小于 int 超过 [] 存入 out
  var i = 0, j = 0; // 把 0, 下标 j 赋值为 0 存入 下标 i
  while (i < left.length && j < right.length) {
    // 循环，直到不满足「下标 i 小于 左边界.长度 且 下标 j 小于 右边界.长度」
    if (left[i] <= right[j]) {
      out.add(left[i++]);
    } else {
      out.add(right[j++]);
    }
  }
  while (i < left.length) {
    out.add(left[i++]);
  } // 循环，直到不满足「下标 i 小于 左边界.长度) { out 追加 左边界[下标 i 加一 ]); }」
  while (j < right.length) {
    out.add(right[j++]);
  } // 循环，直到不满足「下标 j 小于 右边界.长度) { out 追加 右边界[下标 j 加一 ]); }」
  return out; // 返回 out
}

void main() {
  if (mergeSort([5, 4, 3, 2, 1]).toString() != '[1, 2, 3, 4, 5]')
    throw StateError('c1');
  print('PASS');
} // 全部用例通过，输出 PASS
