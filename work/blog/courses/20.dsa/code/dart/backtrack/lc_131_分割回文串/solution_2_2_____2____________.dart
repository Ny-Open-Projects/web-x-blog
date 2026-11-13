// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133772625
// LeetCode 131. 分割回文串 — Dart 版（方案2）
bool isPal(String s) {
  // 定义判定函数 isPal
  var i = 0, j = s.length - 1; // 把 0, 下标 j 赋值为 字符串.长度 减 1 存入 下标 i
  while (i < j) {
    // 循环，直到不满足「下标 i 小于 下标 j」
    if (s[i] != s[j]) return false; // 若 字符串[下标 i] 不等于 字符串[下标 j]，直接返回 false
    i++; // 下标 i 加一
    j--; // 下标 j 减一
  }
  return true; // 返回 true
}

List<List<String>> partition(String s) {
  // 定义函数/方法 partition
  final res = <List<String>>[]; // 把 小于 List 小于 String 超过 超过 [] 存入 结果
  final path = <String>[]; // 把 小于 String 超过 [] 存入 当前路径
  void dfs(int start) {
    // 定义函数/方法 dfs
    if (start == s.length) {
      // 若 起点 等于 字符串.长度
      res.add(List<String>.from(path)); // 结果 追加 List 小于 String 超过 .from(当前路径));
      return; // return;
    }
    for (var e = start + 1; e <= s.length; e++) {
      // 让 e 从 起点 加 1 开始计数，e 不超过 字符串.长度 就继续
      final sub = s.substring(start, e); // 把 字符串 截取 起点, e) 存入 sub
      if (isPal(sub)) {
        // 若 isPal(sub
        path.add(sub); // 当前路径 追加 sub);
        dfs(e); // dfs(e);
        path.removeLast(); // 当前路径.removeLast();
      }
    }
  }

  dfs(0); // dfs(0);
  return res; // 返回 结果
}

void main() {
  // 程序入口：跑内嵌自测用例
  final got = partition('aab'); // 把 partition('aab') 存入 got
  if (got.length != 2)
    throw StateError('cnt'); // 若 got.长度 不等于 2) throw StateError('计数');
  if (got[0].toString() != '[a, a, b]' || got[1].toString() != '[aa, b]')
    throw StateError('p');
  print('PASS'); // 全部用例通过，输出 PASS
}
