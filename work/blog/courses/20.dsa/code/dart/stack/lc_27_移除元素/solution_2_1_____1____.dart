// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114689
// LeetCode 27. 移除元素 — Dart 版（方案2）
int removeElement(List<int> nums, int val) {
  // 定义函数/方法 removeElement
  var k = 0; // 把 0 存入 下标 k
  for (var i = 0; i < nums.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    if (nums[i] != val) {
      nums[k] = nums[i];
      k++;
    } // 若 数组[下标 i] 不等于 值) { 数组[下标 k] 赋值为 数组[下标 i]; 下标 k 加一 ; }
  }
  return k; // 返回 下标 k
}

void main() {
  // 程序入口：跑内嵌自测用例
  final v = [3, 2, 2, 3]; // 把 [3, 2, 2, 3] 存入 值
  if (removeElement(v, 3) != 2)
    throw StateError(
      'c1',
    ); // 若 removeElement(值, 3) 不等于 2) throw StateError('c1');
  if (v[0] != 2 || v[1] != 2)
    throw StateError(
      'c1b',
    ); // 若 值[0] 不等于 2 或 值[1] 不等于 2) throw StateError('c1b');
  if (removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) != 5) throw StateError('c2');
  print('PASS');
} // 全部用例通过，输出 PASS
