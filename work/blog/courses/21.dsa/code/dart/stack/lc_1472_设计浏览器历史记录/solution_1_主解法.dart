// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145338856
// LeetCode 1472. 设计浏览器历史记录 — Dart 版（方案1）
class BrowserHistory {
  // 定义类型
  final List<String> history; // final List 小于 String 超过 history;
  int cur = 0; // 把 0 存入 当前值
  BrowserHistory(String homepage)
    : history = [
        homepage,
      ]; // 把 [homepage]; 写入 BrowserHistory(String homepage) : history
  void visit(String url) {
    // 定义函数/方法 visit
    history.removeRange(
      cur + 1,
      history.length,
    ); // history.removeRange(当前值 加 1, history.长度);
    history.add(url); // history 追加 url);
    cur = history.length - 1; // 把 history.长度 减 1 存入 当前值
  }

  String back(int steps) {
    // 定义函数/方法 back
    cur = cur - steps < 0
        ? 0
        : cur - steps; // 把 当前值 减 steps 小于 0 ? 0 : 当前值 减 steps 存入 当前值
    return history[cur]; // 返回 history[当前值]
  }

  String forward(int steps) {
    // 定义函数/方法 forward
    cur = (cur + steps > history.length - 1) ? history.length - 1 : cur + steps;
    return history[cur]; // 返回 history[当前值]
  }
}

void main() {
  // 程序入口：跑内嵌自测用例
  final b = BrowserHistory(
    'leetcode.com',
  ); // 把 BrowserHistory('leetcode.com') 存入 b
  b.visit('google.com'); // b.visit('google.com');
  b.visit('facebook.com'); // b.visit('facebook.com');
  b.visit('youtube.com'); // b.visit('youtube.com');
  if (b.back(1) != 'facebook.com')
    throw StateError(
      'c1',
    ); // 若 b.back(1) 不等于 'facebook.com') throw StateError('c1');
  if (b.back(1) != 'google.com')
    throw StateError(
      'c2',
    ); // 若 b.back(1) 不等于 'google.com') throw StateError('c2');
  if (b.forward(1) != 'facebook.com')
    throw StateError(
      'c3',
    ); // 若 b.forward(1) 不等于 'facebook.com') throw StateError('c3');
  b.visit('linkedin.com'); // b.visit('linkedin.com');
  if (b.forward(2) != 'linkedin.com')
    throw StateError(
      'c4',
    ); // 若 b.forward(2) 不等于 'linkedin.com') throw StateError('c4');
  if (b.back(2) != 'google.com')
    throw StateError(
      'c5',
    ); // 若 b.back(2) 不等于 'google.com') throw StateError('c5');
  if (b.back(7) != 'leetcode.com')
    throw StateError(
      'c6',
    ); // 若 b.back(7) 不等于 'leetcode.com') throw StateError('c6');
  print('PASS');
} // 全部用例通过，输出 PASS
