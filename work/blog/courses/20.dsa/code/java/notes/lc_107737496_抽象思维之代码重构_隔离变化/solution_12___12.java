// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
package com.webfault.dsa; // 引入依赖

import java.util.Arrays; // 引入依赖

// 忠实翻译 python solution_12：Rule 对象供 Filler 读取/推进当前命令。
// 注意：python 参考只处理大写 E/S/V/M，小写 'semv' 不命中任何分支，
// 位置恒为 (0,0)；此处忠实保持该行为并作为边界断言。
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

  static class Rule { // static class Rule {
    final char[] data; // final char[] data;
    int idx; // int idx;
    final int length; // final int 长度;

    Rule(String r) { // Rule(String 右指针) {
      this.data = r.toCharArray(); // 把 右指针.toCharArray(); 写入 this.data
      this.idx = 0; // 把 0; 写入 this.idx
      this.length = this.data.length; // 把 this.data.长度; 写入 长度
    }

    char current() { // 定义函数/方法 current
      return data[idx]; // 返回 data[idx]
    }

    void advance() { // 定义函数/方法 advance
      idx = (idx + 1) % length; // 把 (idx 加 1) 对…取模 长度; 写入 idx
    }
  }

  static class Filler { // static class Filler {
    final int rowNum; // final int rowNum;
    final int colNum; // final int colNum;
    Location pos = new Location(0, 0); // 把 new Location(0, 0); 写入 Location pos
    int rMin = 0; // 把 0 存入 rMin
    int cMin = 0; // 把 0 存入 cMin
    int rMax; // int rMax;
    int cMax; // int cMax;
    Rule cmd = null; // 把 null; 写入 Rule cmd

    Filler(int rn, int cn) { // Filler(int rn, int cn) {
      this.rowNum = rn; // 把 rn; 写入 this.rowNum
      this.colNum = cn; // 把 cn; 写入 this.colNum
      this.rMax = rn - 1; // 把 rn 减 1; 写入 this.rMax
      this.cMax = cn - 1; // 把 cn 减 1; 写入 this.cMax
    }

    void setRule(Rule rule) { // 定义函数/方法 setRule
      this.cmd = rule; // 把 rule; 写入 this.cmd
    }

    Location next() { // 定义函数/方法 next
      Location res =
          new Location(pos.row, pos.col); // 把 new Location(pos.row, pos.col); 写入 Location res
      char ch = cmd.current(); // 把 cmd.current(); 写入 char ch
      if (ch == 'E') { // 若 字符 等于 'E'
        pos.row++; // pos.row 加一 ;
        if (pos.row == rMax) { // 若 pos.row 等于 rMax
          cmd.advance(); // cmd.advance();
          cMin++; // cMin 加一
        }
      } else if (ch == 'S') { // 否则，若 字符 等于 'S'
        pos.col++; // pos.col 加一 ;
        if (pos.col == cMax) { // 若 pos.col 等于 cMax
          cmd.advance(); // cmd.advance();
          rMax--; // rMax 减一
        }
      } else if (ch == 'V') { // 否则，若 字符 等于 'V'
        pos.row--; // pos.row 减一 ;
        if (pos.row == rMin) { // 若 pos.row 等于 rMin
          cmd.advance(); // cmd.advance();
          cMax--; // cMax 减一
        }
      } else if (ch == 'M') { // 否则，若 字符 等于 'M'
        pos.col--; // pos.col 减一 ;
        if (pos.col == cMin) { // 若 pos.col 等于 cMin
          cmd.advance(); // cmd.advance();
          rMin++; // rMin 加一
        }
      }
      return res; // 返回 结果
    }
  }

  static int[][] test(String rule, int rn, int cn) { // 定义函数/方法 test
    Filler obj = new Filler(rn, cn); // 把 new Filler(rn, cn); 写入 Filler obj
    obj.setRule(new Rule(rule)); // obj.setRule(new Rule(rule));
    int[][] out = new int[rn * cn][2]; // 把 new int[rn 乘 cn][2]; 写入 int[][] out
    for (int i = 0; i < rn * cn; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 rn 乘 cn 就继续
      Location p = obj.next(); // 把 obj.下一个(); 写入 Location p
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

    int[][] want3 =
        new int[][] {{0, 0}, {1, 0}, {2, 0}, {2, 1}, {2, 2}, {1, 2}, {0, 2}, {0, 1}, {1, 1}};
    int[][] got3 = test("ESVM", 3, 3); // 把 test(「ESVM」, 3, 3); 写入 int[][] got3
    if (!eq2(got3, want3)) { // 若 取反 eq2(got3, want3
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL test(ESVM,3,3)=" + Arrays.deepToString(got3)); // 打印输出
    }

    int[][] got1 = test("ESVM", 1, 1); // 把 test(「ESVM」, 1, 1); 写入 int[][] got1
    if (!eq2(got1, new int[][] {{0, 0}})) { // 若 取反 eq2(got1, new int[][] {{0, 0}}
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL test(ESVM,1,1)=" + Arrays.deepToString(got1)); // 打印输出
    }

    int[][] wantSemv = new int[9][2]; // 把 new int[9][2]; 写入 int[][] wantSemv
    int[][] gotSemv = test("semv", 3, 3); // 把 test(「semv」, 3, 3); 写入 int[][] gotSemv
    if (!eq2(gotSemv, wantSemv)) { // 若 取反 eq2(gotSemv, wantSemv
      ok = false; // 把 false; 写入 ok
      System.out.println(
          "FAIL test(semv,3,3)=" + Arrays.deepToString(gotSemv) + " want 全部(0,0)"); // 打印输出
    }

    if (!ok) { // 若 取反 ok
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
