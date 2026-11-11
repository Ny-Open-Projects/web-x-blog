// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — Dart 版（方案9：规则串状态机，8 方向字母）
class Location {
  // 定义类型
  int row = 0, col = 0; // 把 0, col 赋值为 0 存入 row
}

class Filler {
  // 定义类型
  int rowNum, colNum; // int rowNum, colNum;
  Location pos = Location(); // 把 Location(); 写入 Location pos
  int idx = 0; // 把 0 存入 idx
  int rMin = 0,
      cMin = 0,
      rMax = 0,
      cMax = 0; // 把 0, cMin 赋值为 0, rMax 赋值为 0, cMax 赋值为 0 存入 rMin
  String rule = 'ESVM'; // 把 'ESVM' 存入 rule

  Filler(this.rowNum, this.colNum) {
    // Filler(this.rowNum, this.colNum) {
    rMax = rowNum - 1; // 把 rowNum 减 1 存入 rMax
    cMax = colNum - 1; // 把 colNum 减 1 存入 cMax
  }

  void setRule(String rule) {
    // 定义函数/方法 setRule
    rule = rule; // 把 rule 存入 rule
  }

  List<int> next() {
    // 定义函数/方法 next
    final res = [pos.row, pos.col]; // 把 [pos.row, pos.col] 存入 结果
    final ch = rule[idx % rule.length]; // 把 rule[idx 对…取模 rule.长度] 存入 字符
    if (ch == 'E') {
      // 若 字符 等于 'E'
      pos.row += 1; // pos.row累加 1
      if (pos.row == rMax) {
        // 若 pos.row 等于 rMax
        idx += 1; // idx累加 1
        cMin += 1; // cMin累加 1
      }
    } else if (ch == 'S') {
      // 否则，若 字符 等于 'S'
      pos.col += 1; // pos.col累加 1
      if (pos.col == cMax) {
        // 若 pos.col 等于 cMax
        idx += 1; // idx累加 1
        rMax -= 1; // rMax累减 1
      }
    } else if (ch == 'V') {
      // 否则，若 字符 等于 'V'
      pos.row -= 1; // pos.row累减 1
      if (pos.row == rMin) {
        // 若 pos.row 等于 rMin
        idx += 1; // idx累加 1
        cMax -= 1; // cMax累减 1
      }
    } else if (ch == 'M') {
      // 否则，若 字符 等于 'M'
      pos.col -= 1; // pos.col累减 1
      if (pos.col == cMin) {
        // 若 pos.col 等于 cMin
        idx += 1; // idx累加 1
        rMin += 1; // rMin累加 1
      }
    } else if (ch == 'e') {
      // 否则，若 字符 等于 'e'
      pos.row += 1; // pos.row累加 1
      if (pos.row == rMax) {
        // 若 pos.row 等于 rMax
        idx += 1; // idx累加 1
        cMax -= 1; // cMax累减 1
      }
    } else if (ch == 's') {
      // 否则，若 字符 等于 '字符串'
      pos.col += 1; // pos.col累加 1
      if (pos.col == cMax) {
        // 若 pos.col 等于 cMax
        idx += 1; // idx累加 1
        rMin += 1; // rMin累加 1
      }
    } else if (ch == 'v') {
      // 否则，若 字符 等于 '值'
      pos.row -= 1; // pos.row累减 1
      if (pos.row == rMin) {
        // 若 pos.row 等于 rMin
        idx += 1; // idx累加 1
        cMin += 1; // cMin累加 1
      }
    } else if (ch == 'm') {
      // 否则，若 字符 等于 '映射表'
      pos.col -= 1; // pos.col累减 1
      if (pos.col == cMin) {
        // 若 pos.col 等于 cMin
        idx += 1; // idx累加 1
        rMax -= 1; // rMax累减 1
      }
    }
    return res; // 返回 结果
  }
}

List<List<int>> testFiller(String rule, int rn, int cn) {
  // 定义函数/方法 testFiller
  final obj = Filler(rn, cn); // 把 Filler(rn, cn) 存入 obj
  obj.rule = rule; // setRule（注意 Dart 里 this.rule = rule 需要显式 this）
  final seq = <List<int>>[]; // 把 小于 List 小于 int 超过 超过 [] 存入 seq
  for (var i = 0; i < rn * cn; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 rn 乘 cn 就继续
    seq.add(obj.next()); // seq 追加 obj.下一个());
  }
  return seq; // 返回 seq
}

void main() {
  // 程序入口：跑内嵌自测用例
  final wantEsvm = <List<int>>[
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
  if (testFiller('ESVM', 4, 4).toString() != wantEsvm.toString())
    throw StateError('ESVM failed');
  final wantSemv = <List<int>>[
    [0, 0],
    [0, 1],
    [0, 2],
    [0, 3],
    [1, 3],
    [2, 3],
    [3, 3],
    [3, 2],
    [3, 1],
    [3, 0],
    [2, 0],
    [1, 0],
    [1, 1],
    [1, 2],
    [2, 2],
    [2, 1],
  ];
  if (testFiller('semv', 4, 4).toString() != wantSemv.toString())
    throw StateError('semv failed');
  print('PASS'); // 全部用例通过，输出 PASS
}
