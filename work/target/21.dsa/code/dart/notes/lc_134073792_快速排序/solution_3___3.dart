// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134073792
// 数据结构与算法之排序: 快速排序 — Dart 版（方案3）
List<int> quickSort(List<int> nums) {
  // 定义函数/方法 quickSort
  if (nums.length <= 1) return nums; // 若 数组.长度 不超过 1，直接返回 数组
  final pivot = nums[nums.length ~/ 2]; // 把 数组[数组.长度 ~ 除以 2] 存入 pivot
  final lt = <int>[], eq = <int>[], gt = <int>[];
  for (final x in nums) {
    // for (final x in 数组) {
    if (x < pivot) {
      lt.add(x);
    } else if (x == pivot) {
      eq.add(x);
    } else {
      gt.add(x);
    }
  }
  return [
    ...quickSort(lt),
    ...eq,
    ...quickSort(gt),
  ]; // 返回 [...quickSort(lt), ...eq, ...quickSort(gt)]
}

void main() {
  if (quickSort([5, 4, 3, 2, 1]).toString() != '[1, 2, 3, 4, 5]')
    throw StateError('c1');
  if (quickSort([3, 1, 4, 1, 5]).toString() != '[1, 1, 3, 4, 5]')
    throw StateError('c2');
  print('PASS');
} // 全部用例通过，输出 PASS
