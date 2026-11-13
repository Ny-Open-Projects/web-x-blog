// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133547933
// LeetCode 313. 超级丑数 — Dart 版（方案4）
int nthSuperUglyNumber(int n, List<int> primes) {
  // 定义函数/方法 nthSuperUglyNumber
  final ugly = List<int>.filled(
    n,
    1,
  ); // 把 List 小于 int 超过 .filled(元素个数, 1) 存入 ugly
  final idx = List<int>.filled(
    primes.length,
    0,
  ); // 把 List 小于 int 超过 .filled(primes.长度, 0) 存入 idx
  final val = List<int>.from(primes); // 把 List 小于 int 超过 .from(primes) 存入 值
  for (var i = 1; i < n; i++) {
    // 让 下标 i 从 1 开始计数，下标 i 小于 元素个数 就继续
    var next = 0x7fffffffffffffff; // 把 0x7fffffffffffffff 存入 下一个
    for (final v in val) {
      // for (final 值 in 值) {
      if (v < next) next = v; // 若 值 小于 下一个) 下一个 赋值为 值;
    }
    ugly[i] = next; // 把 下一个; 写入 ugly[i]
    for (var k = 0; k < primes.length; k++) {
      // 让 下标 k 从 0 开始计数，下标 k 小于 primes.长度 就继续
      if (val[k] == next) {
        // 若 值[下标 k] 等于 下一个
        idx[k]++; // idx[下标 k] 加一 ;
        val[k] =
            ugly[idx[k]] *
            primes[k]; // 把 ugly[idx[下标 k]] 乘 primes[下标 k]; 写入 val[k]
      }
    }
  }
  return ugly[n - 1]; // 返回 ugly[元素个数 减 1]
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (nthSuperUglyNumber(12, [2, 7, 13, 19]) != 32) throw StateError('c1');
  if (nthSuperUglyNumber(1, [2, 7, 13, 19]) != 1) throw StateError('c2');
  print('PASS'); // 全部用例通过，输出 PASS
}
