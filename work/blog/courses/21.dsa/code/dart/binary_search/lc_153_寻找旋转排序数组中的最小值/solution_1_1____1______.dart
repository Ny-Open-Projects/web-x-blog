// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233483
// LeetCode 153. 寻找旋转排序数组中的最小值 — Dart 版（方案1：二分查找）

int findMin(List<int> nums) {
  // 定义函数/方法 findMin
  var low = 0; // 把 0 存入 low
  var high = nums.length - 1; // 把 数组.长度 减 1 存入 high
  while (low < high) {
    // 循环，直到不满足「low 小于 high」
    final pivot = low + (high - low) ~/ 2; // 防溢出写法
    if (nums[pivot] < nums[high]) {
      // 若 数组[pivot] 小于 数组[high]
      high = pivot; // 把 pivot 存入 high
    } else {
      // 否则
      low = pivot + 1; // 把 pivot 加 1 存入 low
    }
  }
  return nums[low]; // 返回 数组[low]
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (findMin([1, 2, 3]) != 1) throw StateError('case 1 failed');
  if (findMin([3, 4, 5, 1, 2]) != 1) throw StateError('case 2 failed');
  if (findMin([4, 5, 6, 7, 0, 1, 2]) != 0) throw StateError('case 3 failed');
  if (findMin([11, 13, 15, 17]) != 11) throw StateError('case 4 failed');
  print('PASS'); // 全部用例通过，输出 PASS
}
