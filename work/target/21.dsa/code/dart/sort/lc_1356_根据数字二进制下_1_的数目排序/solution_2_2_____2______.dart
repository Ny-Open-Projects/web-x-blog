// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138671078
// LeetCode 1356. 根据数字二进制下1的数目排序 — Dart 版（方案2）
int countBits(int n) {
  // 定义函数/方法 countBits
  var c = 0; // 把 0 存入 字符
  while (n > 0) {
    // 循环，直到不满足「元素个数 超过 0」
    c += n & 1; // 字符累加 元素个数 按位与 1
    n >>= 1; // 把 1; 写入 n >>
  }
  return c; // 返回 字符
}

List<int> sortByBits(List<int> nums) {
  // 定义函数/方法 sortByBits
  final arr =
      List<int>.from(nums) // 把 List 小于 int 超过 .from(数组) 存入 数组
        ..sort((a, b) {
          // 排序
          final ba = countBits(a),
              bb = countBits(b); // 把 countBits(数组), bb 赋值为 countBits(b) 存入 ba
          if (ba != bb)
            return ba.compareTo(bb); // 若 ba 不等于 bb，直接返回 ba.compareTo(bb)
          return a.compareTo(b); // 返回 数组.compareTo(b)
        }); // });
  return arr; // 返回 数组
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8]).toString() !=
      '[0, 1, 2, 4, 8, 3, 5, 6, 7]')
    throw StateError('c1');
  print('PASS'); // 全部用例通过，输出 PASS
}
