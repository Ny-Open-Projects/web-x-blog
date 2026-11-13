// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — Dart 版（方案11：Rule 循环游标）
class Rule {
  // 定义类型
  String data; // String data;
  int idx = 0; // 把 0 存入 idx
  Rule(this.data); // Rule(this.data);

  String next() {
    // 定义函数/方法 next
    final ch = data[idx]; // 把 data[idx] 存入 字符
    idx = (idx + 1) % data.length; // 把 (idx 加 1) 对…取模 data.长度 存入 idx
    return ch; // 返回 字符
  }

  String peek() {
    // 定义函数/方法 peek
    return data[idx]; // 返回 data[idx]
  }
}

void main() {
  // 程序入口：跑内嵌自测用例
  final r = Rule('ESVM'); // 把 Rule('ESVM') 存入 右指针
  final s1 = List.generate(10, (_) => r.next()).join('');
  final r2 = Rule('semv'); // 把 Rule('semv') 存入 r2
  final s2 = List.generate(6, (_) => r2.next()).join('');
  if (s1 != 'ESVMESVMES')
    throw StateError(
      'rule1 failed',
    ); // 若 s1 不等于 'ESVMESVMES') throw StateError('rule1 failed');
  if (s2 != 'semvse')
    throw StateError(
      'rule2 failed',
    ); // 若 s2 不等于 'semvse') throw StateError('rule2 failed');
  print('PASS'); // 全部用例通过，输出 PASS
}
