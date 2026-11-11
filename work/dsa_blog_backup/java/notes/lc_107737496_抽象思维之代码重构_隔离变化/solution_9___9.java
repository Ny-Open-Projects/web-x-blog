// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
package com.webfault.dsa; // 引入依赖

import java.util.Arrays; // 引入依赖

// 忠实翻译 python solution_9：Location + Filler（ESVM 逆时针 / semv 顺时针）
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

    void setRule(String r) { // 定义函数/方法 setRule
      this.rule = r; // 把 右指针; 写入 this.rule
    }

    Location current() { // 定义函数/方法 current
      return pos; // 返回 pos
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
      } else if (ch == 'e') { // 否则，若 字符 等于 'e'
        pos.row++; // pos.row 加一 ;
        if (pos.row == rMax) { // 若 pos.row 等于 rMax
          idx++; // idx 加一
          cMax--; // cMax 减一
        }
      } else if (ch == 's') { // 否则，若 字符 等于 '字符串'
        pos.col++; // pos.col 加一 ;
        if (pos.col == cMax) { // 若 pos.col 等于 cMax
          idx++; // idx 加一
          rMin++; // rMin 加一
        }
      } else if (ch == 'v') { // 否则，若 字符 等于 '值'
        pos.row--; // pos.row 减一 ;
        if (pos.row == rMin) { // 若 pos.row 等于 rMin
          idx++; // idx 加一
          cMin++; // cMin 加一
        }
      } else if (ch == 'm') { // 否则，若 字符 等于 '映射表'
        pos.col--; // pos.col 减一 ;
        if (pos.col == cMin) { // 若 pos.col 等于 cMin
          idx++; // idx 加一
          rMax--; // rMax 减一
        }
      }
      return res; // 返回 结果
    }
  }

  static int[][] seq(Filler f, int n) { // 定义函数/方法 seq
    int[][] out = new int[n][2]; // 把 new int[元素个数][2]; 写入 int[][] out
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      Location p = f.next(); // 把 f.下一个(); 写入 Location p
      out[i][0] = p.row; // 把 节点.row; 写入 out[i][0]
      out[i][1] = p.col; // 把 节点.col; 写入 out[i][1]
    }
    return out; // 返回 out
  }

  static boolean eq2(int[][] a, int[][] b) { // 定义函数/方法 eq2
    if (a.length != b.length) { // 若 数组.长度 不等于 b.长度
      return false; // 返回 false
    }
    for (int i = 0; i < a.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
      for (int j = 0; j < 2; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 2 就继续
        if (a[i][j] != b[i][j]) { // 若 数组[下标 i][下标 j] 不等于 b[下标 i][下标 j]
          return false; // 返回 false
        }
      }
    }
    return true; // 返回 true
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    boolean ok = true; // 把 true; 写入 boolean ok

    Filler a1 = new Filler(1, 1); // 把 new Filler(1, 1); 写入 Filler a1
    if (!eq2(seq(a1, 1), new int[][] {{0, 0}})) { // 若 取反 eq2(seq(a1, 1), new int[][] {{0, 0}}
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL Filler(1,1)=" + Arrays.deepToString(seq(a1, 1))); // 打印输出
    }

    Filler a2 = new Filler(2, 2); // 把 new Filler(2, 2); 写入 Filler a2
    a2.setRule("ESVM"); // a2.setRule(「ESVM」);
    int[][] want22 = new int[][] {{0, 0}, {1, 0}, {1, 1}, {0, 1}};
    if (!eq2(seq(a2, 4), want22)) { // 若 取反 eq2(seq(a2, 4), want22
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL Filler(2,2,ESVM)=" + Arrays.deepToString(seq(a2, 4))); // 打印输出
    }

    Filler b = new Filler(3, 3); // 把 new Filler(3, 3); 写入 Filler b
    b.setRule("ESVM"); // b.setRule(「ESVM」);
    int[][] want3ESVM =
        new int[][] {{0, 0}, {1, 0}, {2, 0}, {2, 1}, {2, 2}, {1, 2}, {0, 2}, {0, 1}, {1, 1}};
    if (!eq2(seq(b, 9), want3ESVM)) { // 若 取反 eq2(seq(b, 9), want3ESVM
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL Filler(3,3,ESVM)=" + Arrays.deepToString(seq(b, 9))); // 打印输出
    }

    Filler c = new Filler(3, 3); // 把 new Filler(3, 3); 写入 Filler c
    c.setRule("semv"); // 字符.setRule(「semv」);
    int[][] want3semv =
        new int[][] {{0, 0}, {0, 1}, {0, 2}, {1, 2}, {2, 2}, {2, 1}, {2, 0}, {1, 0}, {1, 1}};
    if (!eq2(seq(c, 9), want3semv)) { // 若 取反 eq2(seq(字符, 9), want3semv
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL Filler(3,3,semv)=" + Arrays.deepToString(seq(c, 9))); // 打印输出
    }

    if (!ok) { // 若 取反 ok
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
