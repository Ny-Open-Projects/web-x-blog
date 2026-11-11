// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — Dart 版（方案12：Location/Rule/Filler 组合）
class Rule {
  // 定义类型
  String data; // String data;
  int idx = 0; // 把 0 存入 idx
  Rule(this.data); // Rule(this.data);

  String current() {
    // 定义函数/方法 current
    return data[idx]; // 返回 data[idx]
  }

  void advance() {
    // 定义函数/方法 advance
    idx = (idx + 1) % data.length; // 把 (idx 加 1) 对…取模 data.长度 存入 idx
  }
}

class Filler {
  // 定义类型
  int posRow = 0, posCol = 0; // 把 0, posCol 赋值为 0 存入 posRow
  int rMin = 0,
      cMin = 0,
      rMax = 0,
      cMax = 0; // 把 0, cMin 赋值为 0, rMax 赋值为 0, cMax 赋值为 0 存入 rMin
  Rule cmd; // Rule cmd;
  Filler(int rn, int cn, this.cmd) {
    // Filler(int rn, int cn, this.cmd) {
    rMax = rn - 1; // 把 rn 减 1 存入 rMax
    cMax = cn - 1; // 把 cn 减 1 存入 cMax
  }

  List<int> next() {
    // 定义函数/方法 next
    final res = [posRow, posCol]; // 把 [posRow, posCol] 存入 结果
    final ch = cmd.current(); // 把 cmd.current() 存入 字符
    if (ch == 'E') {
      // 若 字符 等于 'E'
      posRow += 1; // posRow累加 1
      if (posRow == rMax) {
        // 若 posRow 等于 rMax
        cmd.advance(); // cmd.advance();
        cMin += 1; // cMin累加 1
      }
    } else if (ch == 'S') {
      // 否则，若 字符 等于 'S'
      posCol += 1; // posCol累加 1
      if (posCol == cMax) {
        // 若 posCol 等于 cMax
        cmd.advance(); // cmd.advance();
        rMax -= 1; // rMax累减 1
      }
    } else if (ch == 'V') {
      // 否则，若 字符 等于 'V'
      posRow -= 1; // posRow累减 1
      if (posRow == rMin) {
        // 若 posRow 等于 rMin
        cmd.advance(); // cmd.advance();
        cMax -= 1; // cMax累减 1
      }
    } else if (ch == 'M') {
      // 否则，若 字符 等于 'M'
      posCol -= 1; // posCol累减 1
      if (posCol == cMin) {
        // 若 posCol 等于 cMin
        cmd.advance(); // cmd.advance();
        rMin += 1; // rMin累加 1
      }
    }
    return res; // 返回 结果
  }
}

void main() {
  // 程序入口：跑内嵌自测用例
  final obj = Filler(4, 4, Rule('ESVM')); // 把 Filler(4, 4, Rule('ESVM')) 存入 obj
  final want = <List<int>>[
    [0, 0],
    [1, 0],
    [2, 0],
    [3, 0],
    [3, 1],
    [3, 2],
    [3, 3],
    [2, 3],
    [1, 3],
    [0, 3],
    [0, 2],
    [0, 1],
    [1, 1],
    [2, 1],
    [2, 2],
    [1, 2],
  ];
  for (final w in want) {
    // for (final 权重 in want) {
    final rc = obj.next(); // 把 obj.下一个() 存入 rc
    if (rc[0] != w[0] || rc[1] != w[1]) throw StateError('filler4 failed');
  }
  print('PASS'); // 全部用例通过，输出 PASS
}
