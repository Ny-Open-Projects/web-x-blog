// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113877588
// 动态规划之Fibonacci — Dart 版（方案2）
int fibMemo(int n) {
  // 定义函数/方法 fibMemo
  final memo = <int, int>{}; // 把 小于 int, int 超过 {} 存入 记忆化表
  int go(int k) {
    // 定义函数/方法 go
    if (k <= 1) return k; // 若 下标 k 不超过 1，直接返回 下标 k
    if (memo.containsKey(k))
      return memo[k]!; // 若 记忆化表.containsKey(下标 k)，直接返回 记忆化表[下标 k]取反
    memo[k] =
        go(k - 1) + go(k - 2); // 把 go(下标 k 减 1) 加 go(下标 k 减 2); 写入 memo[k]
    return memo[k]!; // 返回 记忆化表[下标 k]取反
  }

  return go(n); // 返回 go(元素个数)
}

void main() {
  if (fibMemo(10) != 55 || fibMemo(20) != 6765 || fibMemo(0) != 0)
    throw StateError('x');
  print('PASS');
} // 全部用例通过，输出 PASS
