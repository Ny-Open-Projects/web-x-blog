// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145370422
package com.webfault.dsa; // 引入依赖

class lc2166_solution111 { // 定义类型
  // Bitset 忠实翻译 python ref（32 位分 words + reverse 懒翻转）
  static class Bitset { // static class Bitset {
    int n; // int 元素个数;
    int[] words; // int[] 单词列表;
    int ones; // int ones;
    int reverse; // int reverse;

    Bitset(int size) { // Bitset(int 大小) {
      this.n = size; // 把 大小; 写入 元素个数
      this.words = new int[(size + 31) / 32]; // 把 new int[(大小 加 31) 除以 32]; 写入 单词列表
      this.ones = 0; // 把 0; 写入 this.ones
      this.reverse = 0; // 把 0; 写入 this.reverse
    }

    int realFlag(int idx) { // 定义函数/方法 realFlag
      int index = idx / 32; // 把 idx 除以 32 存入 index
      int bit = idx % 32; // 把 idx 对…取模 32 存入 bit
      return ((words[index] >> bit) & 1)
          ^ reverse; // 返回 ((单词列表[index] 超过 超过 bit) 按位与 1) 按位异或 reverse
    }

    void setFlag(int idx, int v) { // 定义函数/方法 setFlag
      int index = idx / 32; // 把 idx 除以 32 存入 index
      int bit = idx % 32; // 把 idx 对…取模 32 存入 bit
      int old = realFlag(idx); // 把 realFlag(idx) 存入 old
      if (old != v) { // 若 old 不等于 值
        ones += (v - old); // ones累加 (值 减 old)
        int physical = v ^ reverse; // 把 值 按位异或 reverse 存入 physical
        if (physical == 1) { // 若 physical 等于 1
          words[index] |= (1 << bit); // 把 (1 小于 小于 bit); 写入 words[index] |
        } else { // 否则
          words[index] &= ~(1 << bit); // 把 ~(1 小于 小于 bit); 写入 words[index] &
        }
      }
    }

    void fix(int idx) { // 定义函数/方法 fix
      setFlag(idx, 1); // setFlag(idx, 1);
    }

    void unfix(int idx) { // 定义函数/方法 unfix
      setFlag(idx, 0); // setFlag(idx, 0);
    }

    void flip() { // 定义函数/方法 flip
      reverse ^= 1; // 把 1; 写入 reverse ^
      ones = n - ones; // 把 元素个数 减 ones; 写入 ones
    }

    boolean all() { // 定义函数/方法 all
      return ones == n; // 返回 ones 等于 元素个数
    }

    boolean one() { // 定义函数/方法 one
      return ones > 0; // 返回 ones 超过 0
    }

    int count() { // 定义函数/方法 count
      return ones; // 返回 ones
    }

    String str() { // 定义函数/方法 str
      StringBuilder sb = new StringBuilder(); // 把 new StringBuilder(); 写入 StringBuilder sb
      for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        sb.append(realFlag(i)); // 把 realFlag(下标 i 追加到列表尾部
      }
      return sb.toString(); // 返回 sb.toString()
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    boolean ok = true; // 把 true; 写入 boolean ok

    // case A normal: 对应 python ref __main__
    Bitset a = new Bitset(5); // 把 new Bitset(5); 写入 Bitset a
    a.fix(0); // 数组.fix(0);
    a.fix(3); // 数组.fix(3);
    if (!a.str().equals("10010")
        || a.count() != 2) { // 若 取反 数组.str().equals(「10010」) 或 数组.计数() 不等于 2
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL A1 got " + a.str() + " count " + a.count()); // 打印输出
    }
    a.flip(); // 数组.flip();
    if (!a.str().equals("01101")
        || a.count() != 3) { // 若 取反 数组.str().equals(「01101」) 或 数组.计数() 不等于 3
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL A2 got " + a.str() + " count " + a.count()); // 打印输出
    }
    a.unfix(0); // 数组.unfix(0);
    if (!a.str().equals("01101")
        || a.all()
        || !a.one()) { // 若 取反 数组.str().equals(「01101」) 或 数组.all() 或 取反 数组.one(
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL A3 got " + a.str()); // 打印输出
    }

    // case B boundary: size=1 全边界
    Bitset b = new Bitset(1); // 把 new Bitset(1); 写入 Bitset b
    if (!b.str().equals("0")
        || b.all()
        || b.one()
        || b.count() != 0) { // 若 取反 b.str().equals(「0」) 或 b.all() 或 b.one() 或 b.计数() 不等于 0
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL B0"); // 打印输出
    }
    b.fix(0); // b.fix(0);
    if (!b.str().equals("1") || !b.all() || !b.one() || b.count() != 1) {
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL B1"); // 打印输出
    }
    b.unfix(0); // b.unfix(0);
    if (!b.str().equals("0")
        || b.all()
        || b.one()
        || b.count() != 0) { // 若 取反 b.str().equals(「0」) 或 b.all() 或 b.one() 或 b.计数() 不等于 0
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL B2"); // 打印输出
    }
    b.flip(); // b.flip();
    if (!b.str().equals("1") || !b.all() || !b.one() || b.count() != 1) {
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL B3"); // 打印输出
    }

    // case C boundary: size=33 跨 32 位 words 边界
    Bitset c = new Bitset(33); // 把 new Bitset(33); 写入 Bitset c
    c.fix(0); // 字符.fix(0);
    c.fix(32); // 字符.fix(32);
    c.flip(); // 字符.flip();
    c.fix(16); // 字符.fix(16);
    if (!c.str().equals("011111111111111111111111111111110")
        || c.count() != 31
        || c.all()
        || !c.one()) {
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL C1 got " + c.str() + " count " + c.count()); // 打印输出
    }

    if (!ok) { // 若 取反 ok
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
