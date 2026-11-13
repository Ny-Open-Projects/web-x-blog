// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
package com.webfault.dsa; // 引入依赖

import java.util.Arrays; // 引入依赖

// 忠实翻译 python solution_10：Location + Filler + Matrix（operator() 风格访问）
class Main { // 定义类型

  static class Location { // static class Location {
    int row; // int row;
    int col; // int col;

    Location() { // Location() {
      this(0, 0); // this(0, 0);
    }

    Location(int r, int c) { // Location(int 右指针, int 字符) {
      this.row = r; // 把 右指针; 写入 this.row
      this.col = c; // 把 字符; 写入 this.col
    }
  }

  static class Filler { // static class Filler {
    final int rowNum; // final int rowNum;
    final int colNum; // final int colNum;
    Location pos = new Location(0, 0); // 把 new Location(0, 0); 写入 Location pos
    int idx = 0; // 把 0 存入 idx
    int rMin = 0; // 把 0 存入 rMin
    int cMin = 0; // 把 0 存入 cMin
    int rMax; // int rMax;
    int cMax; // int cMax;
    String rule = "ESVM"; // 把 「ESVM」 存入 rule

    Filler(int rn, int cn) { // Filler(int rn, int cn) {
      this.rowNum = rn; // 把 rn; 写入 this.rowNum
      this.colNum = cn; // 把 cn; 写入 this.colNum
      this.rMax = rn - 1; // 把 rn 减 1; 写入 this.rMax
      this.cMax = cn - 1; // 把 cn 减 1; 写入 this.cMax
    }

    void reset() { // 定义函数/方法 reset
      pos = new Location(0, 0); // 把 new Location(0, 0); 写入 pos
      idx = 0; // 把 0; 写入 idx
      rMin = 0; // 把 0; 写入 rMin
      cMin = 0; // 把 0; 写入 cMin
      rMax = rowNum - 1; // 把 rowNum 减 1; 写入 rMax
      cMax = colNum - 1; // 把 colNum 减 1; 写入 cMax
      rule = "ESVM"; // 把 「ESVM」; 写入 rule
    }

    void setRule(String r) { // 定义函数/方法 setRule
      this.rule = r; // 把 右指针; 写入 this.rule
    }

    Location next() { // 定义函数/方法 next
      Location res =
          new Location(pos.row, pos.col); // 把 new Location(pos.row, pos.col); 写入 Location res
      char ch = rule.charAt(idx % rule.length()); // 逐字符处理
      if (ch == 'E') { // 若 字符 等于 'E'
        pos.row++; // pos.row 加一 ;
        if (pos.row == rMax) { // 若 pos.row 等于 rMax
          idx++; // idx 加一
          cMin++; // cMin 加一
        }
      } else if (ch == 'S') { // 否则，若 字符 等于 'S'
        pos.col++; // pos.col 加一 ;
        if (pos.col == cMax) { // 若 pos.col 等于 cMax
          idx++; // idx 加一
          rMax--; // rMax 减一
        }
      } else if (ch == 'V') { // 否则，若 字符 等于 'V'
        pos.row--; // pos.row 减一 ;
        if (pos.row == rMin) { // 若 pos.row 等于 rMin
          idx++; // idx 加一
          cMax--; // cMax 减一
        }
      } else if (ch == 'M') { // 否则，若 字符 等于 'M'
        pos.col--; // pos.col 减一 ;
        if (pos.col == cMin) { // 若 pos.col 等于 cMin
          idx++; // idx 加一
          rMin++; // rMin 加一
        }
      }
      return res; // 返回 结果
    }
  }

  static class Matrix { // static class Matrix {
    final int row; // final int row;
    final int col; // final int col;
    final int[][] buf; // final int[][] buf;

    Matrix(int r, int c) { // Matrix(int 右指针, int 字符) {
      this.row = r; // 把 右指针; 写入 this.row
      this.col = c; // 把 字符; 写入 this.col
      this.buf = new int[r][c]; // 把 new int[右指针][字符]; 写入 this.buf
    }

    int get(int r, int c) { // 定义函数/方法 get
      return buf[r][c]; // 返回 buf[右指针][字符]
    }

    void set(int r, int c, int v) { // 定义函数/方法 set
      buf[r][c] = v; // 把 值; 写入 buf[r][c]
    }
  }

  static Matrix fill(int rn, int cn) { // 定义函数/方法 fill
    Filler obj = new Filler(rn, cn); // 把 new Filler(rn, cn); 写入 Filler obj
    obj.setRule("ESVM"); // obj.setRule(「ESVM」);
    Matrix m = new Matrix(rn, cn); // 把 new Matrix(rn, cn); 写入 Matrix m
    for (int i = 0; i < rn * cn; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 rn 乘 cn 就继续
      Location p = obj.next(); // 把 obj.下一个(); 写入 Location p
      m.set(p.row, p.col, i + 1); // 映射表.set(节点.row, 节点.col, 下标 i 加 1);
    }
    return m; // 返回 映射表
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

    Matrix m4 = fill(4, 4); // 把 fill(4, 4); 写入 Matrix m4
    int[][] want4 = new int[][] {{1, 12, 11, 10}, {2, 13, 16, 9}, {3, 14, 15, 8}, {4, 5, 6, 7}};
    if (!eq2(m4.buf, want4)) { // 若 取反 eq2(m4.buf, want4
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL 4x4=" + Arrays.deepToString(m4.buf)); // 打印输出
    }

    Matrix m9 = fill(9, 9); // 把 fill(9, 9); 写入 Matrix m9
    int[] wantRow0 = {
      1, 32, 31, 30, 29, 28, 27, 26, 25
    }; // 把 {1, 32, 31, 30, 29, 28, 27, 26, 25}; 写入 int[] wantRow0
    int[] wantRow1 = {
      2, 33, 56, 55, 54, 53, 52, 51, 24
    }; // 把 {2, 33, 56, 55, 54, 53, 52, 51, 24}; 写入 int[] wantRow1
    int[] wantRow8 = {
      9, 10, 11, 12, 13, 14, 15, 16, 17
    }; // 把 {9, 10, 11, 12, 13, 14, 15, 16, 17}; 写入 int[] wantRow8
    if (!Arrays.equals(m9.buf[0], wantRow0)) { // 若 取反 Arrays.equals(m9.buf[0], wantRow0
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL 9x9 row0=" + Arrays.toString(m9.buf[0])); // 打印输出
    }
    if (!Arrays.equals(m9.buf[1], wantRow1)) { // 若 取反 Arrays.equals(m9.buf[1], wantRow1
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL 9x9 row1=" + Arrays.toString(m9.buf[1])); // 打印输出
    }
    if (!Arrays.equals(m9.buf[8], wantRow8)) { // 若 取反 Arrays.equals(m9.buf[8], wantRow8
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL 9x9 row8=" + Arrays.toString(m9.buf[8])); // 打印输出
    }
    if (!ok) { // 若 取反 ok
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
