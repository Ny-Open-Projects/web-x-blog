// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114454
// LeetCode 26. 删除有序数组中的重复项 — Dart 版

// 方案3：快慢指针 —— fast 扫描，slow 指向已去重区间末尾
int removeDuplicates(List<int> nums) {
  // 定义函数/方法 removeDuplicates
  if (nums.isEmpty) return 0; // 若 数组.isEmpty，直接返回 0
  var slow = 0; // 把 0 存入 慢指针
  for (var fast = 1; fast < nums.length; fast++) {
    // 让 快指针 从 1 开始计数，快指针 小于 数组.长度 就继续
    if (nums[fast] != nums[slow]) {
      // 若 数组[快指针] 不等于 数组[慢指针]
      slow++; // 慢指针 加一
      nums[slow] = nums[fast]; // 把 数组[快指针]; 写入 nums[slow]
    }
  }
  return slow + 1; // 返回 慢指针 加 1
}

bool eqArr(List<int> a, List<int> b) {
  // 定义函数/方法 eqArr
  if (a.length != b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
  for (var i = 0; i < a.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    if (a[i] != b[i]) return false; // 若 数组[下标 i] 不等于 b[下标 i]，直接返回 false
  }
  return true; // 返回 true
}

class _Case {
  // 定义类型
  final List<int> input; // final List 小于 int 超过 input;
  final int k; // final int 下标 k;
  final List<int> pre; // final List 小于 int 超过 前缀和;
  _Case(
    this.input,
    this.k,
    this.pre,
  ); // _Case(this.input, this.下标 k, this.前缀和);
}

void main() {
  // 程序入口：跑内嵌自测用例
  // 与 TS 事实源内嵌用例一致
  final cases = [
    _Case([1, 1, 2], 2, [1, 2]),
    _Case([1, 2, 3], 3, [1, 2, 3]),
    _Case([], 0, []),
  ];
  for (final c in cases) {
    // for (final 字符 in cases) {
    final nums = c.input.toList(); // 把 字符.input.toList() 存入 数组
    final got = removeDuplicates(nums); // 把 removeDuplicates(数组) 存入 got
    final prefix = nums.sublist(0, got); // 把 数组.sublist(0, got) 存入 prefix
    if (got != c.k || !eqArr(prefix, c.pre)) {
      // 若 got 不等于 字符.下标 k 或 取反 eqArr(prefix, 字符.前缀和
      throw StateError(
        'FAILED removeDuplicates k=$got',
      ); // 把 $got'); 写入 throw StateError('FAILED removeDuplicates k
    }
  }
  print('PASS'); // 全部用例通过，输出 PASS
}
