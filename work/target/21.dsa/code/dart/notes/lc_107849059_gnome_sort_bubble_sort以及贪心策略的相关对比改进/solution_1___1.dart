// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107849059
// Gnome Sort（侏儒排序）+ Bubble Sort（冒泡排序）+ 贪心找零 对比
List<int> gnomeSort(List<int> arr) {
  // 定义函数/方法 gnomeSort
  final a = List<int>.from(arr); // 把 List 小于 int 超过 .from(数组) 存入 数组
  var i = 0; // 把 0 存入 下标 i
  while (i < a.length) {
    // 循环，直到不满足「下标 i 小于 数组.长度」
    if (i == 0 || a[i] >= a[i - 1]) {
      // 若 下标 i 等于 0 或 数组[下标 i] 不低于 数组[下标 i 减 1]
      i++; // 下标 i 加一
    } else {
      // 否则
      final t = a[i - 1]; // 把 数组[下标 i 减 1] 存入 另一字符串
      a[i - 1] = a[i]; // 把 数组[下标 i]; 写入 a[i - 1]
      a[i] = t; // 把 另一字符串; 写入 a[i]
      i--; // 下标 i 减一
    }
  }
  return a; // 返回 数组
}

List<int> bubbleSort(List<int> arr) {
  // 定义函数/方法 bubbleSort
  final a = List<int>.from(arr); // 把 List 小于 int 超过 .from(数组) 存入 数组
  var swapped = true; // 把 true 存入 swapped
  while (swapped) {
    // 循环，直到不满足「swapped」
    swapped = false; // 把 false 存入 swapped
    for (var i = 0; i < a.length - 1; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 减 1 就继续
      if (a[i] > a[i + 1]) {
        // 若 数组[下标 i] 超过 数组[下标 i 加 1]
        final t = a[i]; // 把 数组[下标 i] 存入 另一字符串
        a[i] = a[i + 1]; // 把 数组[下标 i 加 1]; 写入 a[i]
        a[i + 1] = t; // 把 另一字符串; 写入 a[i + 1]
        swapped = true; // 把 true 存入 swapped
      }
    }
  }
  return a; // 返回 数组
}

int coinChange(List<int> coins, int amount) {
  // 定义函数/方法 coinChange
  final cs = List<int>.from(coins)..sort((x, y) => y.compareTo(x));
  var remaining = amount; // 把 目标金额 存入 remaining
  var count = 0; // 把 0 存入 计数
  for (final coin in cs) {
    // for (final coin in cs) {
    while (remaining >= coin) {
      // 循环，直到不满足「remaining 不低于 coin」
      remaining -= coin; // remaining累减 coin
      count++; // 计数 加一
    }
  }
  return remaining == 0 ? count : -1; // 返回 remaining 等于 0 ? 计数 : 减 1
}

void main() {
  // 程序入口：跑内嵌自测用例
  final want = <int>[1, 2, 3]; // 把 小于 int 超过 [1, 2, 3] 存入 want
  assert(gnomeSort([3, 2, 1]).toString() == want.toString(), 'g'); // 断言校验
  assert(bubbleSort([3, 2, 1]).toString() == want.toString(), 'b'); // 断言校验
  assert(coinChange([1, 5, 10, 25], 63) == 6, 'c'); // 断言校验
  print('PASS'); // 全部用例通过，输出 PASS
}
