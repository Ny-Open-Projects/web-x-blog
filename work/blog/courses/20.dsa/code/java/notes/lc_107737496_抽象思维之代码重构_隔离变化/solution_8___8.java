// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
package com.webfault.dsa; // 引入依赖

import java.util.Arrays; // 引入依赖

// 忠实翻译 python solution_8：迭代器风格 Filler，按规则串逐格前进
class Main { // 定义类型

  static class Filler { // static class Filler {
    final int rowNum; // final int rowNum;
    final int colNum; // final int colNum;
    String rule = "ESVM"; // 把 「ESVM」 存入 rule
    int posRow; // int posRow;
    int posCol; // int posCol;
    int idx; // int idx;
    int rMin; // int rMin;
    int cMin; // int cMin;
    int rMax; // int rMax;
    int cMax; // int cMax;

    Filler(int rn, int cn) { // Filler(int rn, int cn) {
      this.rowNum = rn; // 把 rn; 写入 this.rowNum
      this.colNum = cn; // 把 cn; 写入 this.colNum
      reset(); // reset();
    }

    void reset() { // 定义函数/方法 reset
      posRow = 0; // 把 0; 写入 posRow
      posCol = 0; // 把 0; 写入 posCol
      idx = 0; // 把 0; 写入 idx
      rMin = 0; // 把 0; 写入 rMin
      cMin = 0; // 把 0; 写入 cMin
      rMax = rowNum - 1; // 把 rowNum 减 1; 写入 rMax
      cMax = colNum - 1; // 把 colNum 减 1; 写入 cMax
    }

    void setRule(String r) { // 定义函数/方法 setRule
      this.rule = r; // 把 右指针; 写入 this.rule
    }

    int[] nextPos() { // 定义函数/方法 nextPos
      if (!(rMin <= posRow && posRow <= rMax && cMin <= posCol && posCol <= cMax)) {
        return null; // 返回 null
      }
      int[] p = new int[] {posRow, posCol}; // 把 new int[] {posRow, posCol}; 写入 int[] p
      advance(); // advance();
      return p; // 返回 节点
    }

    void advance() { // 定义函数/方法 advance
      char cmd = rule.charAt(idx % 4); // 逐字符处理
      if (cmd == 'E') { // 若 cmd 等于 'E'
        posRow++; // posRow 加一
        if (posRow == rMax) { // 若 posRow 等于 rMax
          idx++; // idx 加一
          cMin++; // cMin 加一
        }
      } else if (cmd == 'S') { // 否则，若 cmd 等于 'S'
        posCol++; // posCol 加一
        if (posCol == cMax) { // 若 posCol 等于 cMax
          idx++; // idx 加一
          rMax--; // rMax 减一
        }
      } else if (cmd == 'V') { // 否则，若 cmd 等于 'V'
        posRow--; // posRow 减一
        if (posRow == rMin) { // 若 posRow 等于 rMin
          idx++; // idx 加一
          cMax--; // cMax 减一
        }
      } else if (cmd == 'M') { // 否则，若 cmd 等于 'M'
        posCol--; // posCol 减一
        if (posCol == cMin) { // 若 posCol 等于 cMin
          idx++; // idx 加一
          rMin++; // rMin 加一
        }
      }
    }
  }

  static int[][] fillMatrix(int rn, int cn, String rule) { // 定义函数/方法 fillMatrix
    int[][] mat = new int[rn][cn]; // 把 new int[rn][cn]; 写入 int[][] mat
    Filler f = new Filler(rn, cn); // 把 new Filler(rn, cn); 写入 Filler f
    f.setRule(rule); // f.setRule(rule);
    int i = 1; // 把 1 存入 下标 i
    int[] p = f.nextPos(); // 把 f.nextPos(); 写入 int[] p
    while (p != null) { // 循环，直到不满足「节点 不等于 null」
      mat[p[0]][p[1]] = i; // 把 下标 i; 写入 mat[p[0]][p[1]]
      i++; // 下标 i 加一
      p = f.nextPos(); // 把 f.nextPos(); 写入 节点
    }
    return mat; // 返回 mat
  }

  static boolean eq2(int[][] a, int[][] b) { // 定义函数/方法 eq2
    if (a.length != b.length) { // 若 数组.长度 不等于 b.长度
      return false; // 返回 false
    }
    for (int i = 0; i < a.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
      if (a[i].length != b[i].length) { // 若 数组[下标 i].长度 不等于 b[下标 i].长度
        return false; // 返回 false
      }
      for (int j = 0; j < a[i].length; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 数组[下标 i].长度 就继续
        if (a[i][j] != b[i][j]) { // 若 数组[下标 i][下标 j] 不等于 b[下标 i][下标 j]
          return false; // 返回 false
        }
      }
    }
    return true; // 返回 true
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    boolean ok = true; // 把 true; 写入 boolean ok
    int[][] g11 = fillMatrix(1, 1, "ESVM"); // 把 fillMatrix(1, 1, 「ESVM」); 写入 int[][] g11
    if (!eq2(g11, new int[][] {{1}})) { // 若 取反 eq2(g11, new int[][] {{1}}
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL fill_matrix(1,1)=" + Arrays.deepToString(g11)); // 打印输出
    }
    int[][] g33 = fillMatrix(3, 3, "ESVM"); // 把 fillMatrix(3, 3, 「ESVM」); 写入 int[][] g33
    if (!eq2(
        g33,
        new int[][] {
          {1, 0, 0}, {2, 0, 0}, {0, 0, 0}
        })) { // 若 取反 eq2(g33, new int[][] {{1, 0, 0}, {2, 0, 0}, {0, 0, 0}}
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL fill_matrix(3,3)=" + Arrays.deepToString(g33)); // 打印输出
    }
    int[][] g34 = fillMatrix(3, 4, "ESVM"); // 把 fillMatrix(3, 4, 「ESVM」); 写入 int[][] g34
    if (!eq2(g34, new int[][] {{1, 0, 0, 0}, {2, 0, 0, 0}, {0, 0, 0, 0}})) {
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL fill_matrix(3,4)=" + Arrays.deepToString(g34)); // 打印输出
    }
    int[][] g44 = fillMatrix(4, 4, "ESVM"); // 把 fillMatrix(4, 4, 「ESVM」); 写入 int[][] g44
    if (!eq2(g44, new int[][] {{1, 0, 0, 0}, {2, 0, 0, 0}, {3, 0, 0, 0}, {0, 0, 0, 0}})) {
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL fill_matrix(4,4)=" + Arrays.deepToString(g44)); // 打印输出
    }
    if (!ok) { // 若 取反 ok
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
