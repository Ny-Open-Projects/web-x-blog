// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145634738
// LeetCode 1797. 设计一个验证系统 — Dart 版（方案1）
class AuthenticationManager {
  // 定义类型
  final int ttl; // final int ttl;
  final Map<String, int> expiresAt =
      {}; // 把 {}; 写入 final Map<String, int> expiresAt
  AuthenticationManager(this.ttl); // AuthenticationManager(this.ttl);
  void generate(String tokenId, int currentTime) {
    // 定义函数/方法 generate
    expiresAt[tokenId] =
        currentTime + ttl; // 把 currentTime 加 ttl; 写入 expiresAt[tokenId]
  }

  int renew(String tokenId, int currentTime) {
    // 定义函数/方法 renew
    final exp = expiresAt[tokenId]; // 把 expiresAt[tokenId] 存入 exp
    if (exp != null && exp > currentTime) {
      // 若 exp 不等于 null 且 exp 超过 currentTime
      expiresAt[tokenId] =
          currentTime + ttl; // 把 currentTime 加 ttl; 写入 expiresAt[tokenId]
    }
    return countValidTokens(currentTime); // 返回 countValidTokens(currentTime)
  }

  int countValidTokens(int currentTime) {
    // 定义函数/方法 countValidTokens
    var cnt = 0; // 把 0 存入 计数
    for (final e in expiresAt.values) {
      // for (final e in expiresAt.values) {
      if (e > currentTime) cnt++; // 若 e 超过 currentTime) 计数 加一 ;
    }
    return cnt; // 返回 计数
  }
}

void main() {
  // 程序入口：跑内嵌自测用例
  final auth = AuthenticationManager(5); // 把 AuthenticationManager(5) 存入 auth
  auth.generate('aaa', 1); // auth.generate('aaa', 1);
  if (auth.countValidTokens(3) != 1)
    throw StateError(
      'c1',
    ); // 若 auth.countValidTokens(3) 不等于 1) throw StateError('c1');
  if (auth.renew('aaa', 4) != 1)
    throw StateError(
      'r',
    ); // 若 auth.renew('aaa', 4) 不等于 1) throw StateError('右指针');
  if (auth.countValidTokens(6) != 1)
    throw StateError(
      'c2',
    ); // 若 auth.countValidTokens(6) 不等于 1) throw StateError('c2');
  print('PASS'); // 全部用例通过，输出 PASS
}
