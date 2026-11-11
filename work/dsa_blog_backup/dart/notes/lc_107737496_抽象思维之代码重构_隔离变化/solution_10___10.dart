// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — Dart 版（方案10：Filler+Matrix 组合 9x9 全螺旋）
class Filler {
  // 定义类型
  int posRow = 0, posCol = 0, idx = 0; // 把 0, posCol 赋值为 0, idx 赋值为 0 存入 posRow
  int rMin = 0,
      cMin = 0,
      rMax = 0,
      cMax = 0; // 把 0, cMin 赋值为 0, rMax 赋值为 0, cMax 赋值为 0 存入 rMin
  Filler(int rn, int cn) {
    // Filler(int rn, int cn) {
    rMax = rn - 1; // 把 rn 减 1 存入 rMax
    cMax = cn - 1; // 把 cn 减 1 存入 cMax
  }

  List<int> next() {
    // 定义函数/方法 next
    final res = [posRow, posCol]; // 把 [posRow, posCol] 存入 结果
    final cmd = 'ESVM'[idx % 4]; // 把 'ESVM'[idx 对…取模 4] 存入 cmd
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
    return res; // 返回 结果
  }
}

String fmtRow(List<int> row) =>
    row.map((x) => x.toString().padLeft(2)).join(' ');

void main() {
  // 程序入口：跑内嵌自测用例
  const rn = 9, cn = 9; // 把 9, cn 赋值为 9 存入 rn
  final obj = Filler(rn, cn); // 把 Filler(rn, cn) 存入 obj
  final m = List.generate(rn, (_) => List<int>.filled(cn, 0));
  for (var i = 0; i < rn * cn; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 rn 乘 cn 就继续
    final rc = obj.next(); // 把 obj.下一个() 存入 rc
    m[rc[0]][rc[1]] = i + 1; // 把 下标 i 加 1; 写入 m[rc[0]][rc[1]]
  }
  const want = <String>[
    ' 1 32 31 30 29 28 27 26 25',
    ' 2 33 56 55 54 53 52 51 24',
    ' 3 34 57 72 71 70 69 50 23',
    ' 4 35 58 73 80 79 68 49 22',
    ' 5 36 59 74 81 78 67 48 21',
    ' 6 37 60 75 76 77 66 47 20',
    ' 7 38 61 62 63 64 65 46 19',
    ' 8 39 40 41 42 43 44 45 18',
    ' 9 10 11 12 13 14 15 16 17',
  ];
  for (var i = 0; i < rn; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 rn 就继续
    if (fmtRow(m[i]) != want[i]) throw StateError('matrix9 row $i failed');
  }
  print('PASS'); // 全部用例通过，输出 PASS
}
