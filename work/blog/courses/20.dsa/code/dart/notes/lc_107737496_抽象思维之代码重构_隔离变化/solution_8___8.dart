// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — Dart 版（方案8：Filler 状态机 + hasNext 部分填充）
class Filler {
  // 定义类型
  int rowNum, colNum; // int rowNum, colNum;
  String rule = 'ESVM'; // 把 'ESVM' 存入 rule
  int posRow = 0, posCol = 0, idx = 0; // 把 0, posCol 赋值为 0, idx 赋值为 0 存入 posRow
  int rMin = 0,
      cMin = 0,
      rMax = 0,
      cMax = 0; // 把 0, cMin 赋值为 0, rMax 赋值为 0, cMax 赋值为 0 存入 rMin

  Filler(this.rowNum, this.colNum) {
    // Filler(this.rowNum, this.colNum) {
    rMax = rowNum - 1; // 把 rowNum 减 1 存入 rMax
    cMax = colNum - 1; // 把 colNum 减 1 存入 cMax
  }

  void setRule(String r) {
    // 定义函数/方法 setRule
    rule = r; // 把 右指针 存入 rule
  }

  bool hasNext() {
    // 定义函数/方法 hasNext
    return rMin <= posRow && posRow <= rMax && cMin <= posCol && posCol <= cMax;
  }

  List<int> next() {
    // 定义函数/方法 next
    final r = posRow, c = posCol; // 把 posRow, 字符 赋值为 posCol 存入 右指针
    _advance(); // _advance();
    return [r, c]; // 返回 [右指针, 字符]
  }

  void _advance() {
    // 定义函数/方法 _advance
    final cmd = rule[idx % 4]; // 把 rule[idx 对…取模 4] 存入 cmd
    if (cmd == 'E') {
      // 若 cmd 等于 'E'
      posRow += 1; // posRow累加 1
      if (posRow == rMax) {
        // 若 posRow 等于 rMax
        idx += 1; // idx累加 1
        cMin += 1; // cMin累加 1
      }
    } else if (cmd == 'S') {
      // 否则，若 cmd 等于 'S'
      posCol += 1; // posCol累加 1
      if (posCol == cMax) {
        // 若 posCol 等于 cMax
        idx += 1; // idx累加 1
        rMax -= 1; // rMax累减 1
      }
    } else if (cmd == 'V') {
      // 否则，若 cmd 等于 'V'
      posRow -= 1; // posRow累减 1
      if (posRow == rMin) {
        // 若 posRow 等于 rMin
        idx += 1; // idx累加 1
        cMax -= 1; // cMax累减 1
      }
    } else if (cmd == 'M') {
      // 否则，若 cmd 等于 'M'
      posCol -= 1; // posCol累减 1
      if (posCol == cMin) {
        // 若 posCol 等于 cMin
        idx += 1; // idx累加 1
        rMin += 1; // rMin累加 1
      }
    }
  }
}

List<List<int>> fillMatrix(int rn, int cn, String rule) {
  // 定义函数/方法 fillMatrix
  final mat = List.generate(rn, (_) => List<int>.filled(cn, 0));
  final f = Filler(rn, cn); // 把 Filler(rn, cn) 存入 f
  f.setRule(rule); // f.setRule(rule);
  var i = 1; // 把 1 存入 下标 i
  while (f.hasNext()) {
    // 循环，直到不满足「f.hasNext(」
    final rc = f.next(); // 把 f.下一个() 存入 rc
    mat[rc[0]][rc[1]] = i; // 把 下标 i; 写入 mat[rc[0]][rc[1]]
    i++; // 下标 i 加一
  }
  return mat; // 返回 mat
}

void main() {
  // 程序入口：跑内嵌自测用例
  final want1 = <List<int>>[
    [1, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0],
    [3, 0, 0, 0, 0, 0],
    [4, 0, 0, 0, 0, 0],
    [5, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
  ];
  if (fillMatrix(6, 6, 'ESVM').toString() != want1.toString())
    throw StateError('case1 failed');
  final want2 = <List<int>>[
    [1, 0, 0],
    [2, 0, 0],
    [0, 0, 0],
  ];
  if (fillMatrix(3, 3, 'ESVM').toString() != want2.toString())
    throw StateError('case2 failed');
  print('PASS'); // 全部用例通过，输出 PASS
}
