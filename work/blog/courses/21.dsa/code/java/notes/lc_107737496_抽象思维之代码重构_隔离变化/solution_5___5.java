// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
package com.webfault.dsa; // 引入依赖

// 忠实翻译 python solution_5：矩阵类，m(r, c) 取值，set(r, c, v) 赋值
class Main { // 定义类型

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

    String str() { // 定义函数/方法 str
      StringBuilder sb = new StringBuilder(); // 把 new StringBuilder(); 写入 StringBuilder sb
      for (int i = 0; i < row; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 row 就继续
        if (i > 0) { // 若 下标 i 超过 0
          sb.append('\n'); // 把 '\元素个数' 追加到列表尾部
        }
        for (int j = 0; j < col; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 col 就继续
          if (j > 0) { // 若 下标 j 超过 0
            sb.append(' '); // 把 ' ' 追加到列表尾部
          }
          sb.append(
              String.format(
                  "%2d", buf[i][j])); // 把 String.format(「 对…取模 2d」, buf[下标 i][下标 j] 追加到列表尾部
        }
      }
      return sb.toString(); // 返回 sb.toString()
    }
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
    Matrix m = new Matrix(2, 3); // 把 new Matrix(2, 3); 写入 Matrix m
    for (int i = 0; i < 2; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 2 就继续
      for (int j = 0; j < 3; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 3 就继续
        m.set(i, j, i * 10 + j); // 映射表.set(下标 i, 下标 j, 下标 i 乘 10 加 下标 j);
      }
    }
    int[][] want =
        new int[][] {
          {0, 1, 2}, {10, 11, 12}
        }; // 把 new int[][] {{0, 1, 2}, {10, 11, 12}}; 写入 int[][] want
    boolean ok = true; // 把 true; 写入 boolean ok
    if (!eq2(m.buf, want)) { // 若 取反 eq2(映射表.buf, want
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL buf=" + java.util.Arrays.deepToString(m.buf)); // 打印输出
    }
    if (m.get(1, 2) != 12) { // 若 映射表 查找 1, 2) 不等于 12
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL m(1,2)=" + m.get(1, 2) + " want 12"); // 打印输出
    }
    String wantStr = " 0  1  2\n10 11 12"; // 把 「 0 1 2 10 11 12」 存入 wantStr
    if (!m.str().equals(wantStr)) { // 若 取反 映射表.str().equals(wantStr
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL str=[" + m.str() + "] want [" + wantStr + "]"); // 打印输出
    }
    Matrix one = new Matrix(1, 1); // 把 new Matrix(1, 1); 写入 Matrix one
    one.set(0, 0, 7); // one.set(0, 0, 7);
    if (one.get(0, 0) != 7) { // 若 one 查找 0, 0) 不等于 7
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL 1x1 get=" + one.get(0, 0) + " want 7"); // 打印输出
    }
    if (!ok) { // 若 取反 ok
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
