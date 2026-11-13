// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145381943
package com.webfault.dsa; // 引入依赖

class Solution { // 定义类型
  public String multiply(String num1, String num2) { // 定义函数/方法 multiply
    if (num1.equals("0") || num2.equals("0"))
      return "0"; // 若 num1.equals(「0」) 或 num2.equals(「0」)，直接返回 「0」
    int m = num1.length(), n = num2.length(); // 把 num1.长度(), 元素个数 赋值为 num2.长度() 存入 映射表
    int[] result = new int[m + n]; // 把 new int[映射表 加 元素个数]; 写入 int[] result
    for (int i = m - 1; i >= 0; i--) { // 让 下标 i 从 映射表 减 1 开始计数，下标 i 不低于 0 就继续
      for (int j = n - 1; j >= 0; j--) { // 让 下标 j 从 元素个数 减 1 开始计数，下标 j 不低于 0 就继续
        int mul =
            (num1.charAt(i) - '0')
                * (num2.charAt(j)
                    - '0'); // 把 (num1 取字符 下标 i) 减 '0') 乘 (num2 取字符 下标 j) 减 '0') 存入 mul
        int p1 = i + j, p2 = i + j + 1; // 把 下标 i 加 下标 j, p2 赋值为 下标 i 加 下标 j 加 1 存入 p1
        int total = mul + result[p2]; // 把 mul 加 结果[p2] 存入 总和
        result[p2] = total % 10; // 把 总和 对…取模 10; 写入 result[p2]
        result[p1] += total / 10; // result[p1]累加 总和 除以 10
      }
    }
    StringBuilder sb = new StringBuilder(); // 把 new StringBuilder(); 写入 StringBuilder sb
    for (int d : result) sb.append(d); // 把 d 追加到列表尾部
    String r = sb.toString().replaceFirst("^0+(?=.)", "");
    return r.isEmpty() ? "0" : r; // 返回 右指针.isEmpty() ? 「0」 : 右指针
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Solution s = new Solution(); // 把 new Solution(); 写入 Solution s
    String[][] ins = {{"2", "3"}, {"123", "456"}}; // 把 {{「2」,「2」},{「2」,「2」}}; 写入 String[][] ins
    String[] wants = {"6", "56088"}; // 把 {「6」,「6」}; 写入 String[] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < ins.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 ins.长度 就继续
      String got =
          s.multiply(ins[i][0], ins[i][1]); // 把 字符串.multiply(ins[下标 i][0], ins[下标 i][1]) 存入 got
      if (!got.equals(wants[i])) {
        ok = false;
        System.out.println("FAIL " + ins[i][0] + "x" + ins[i][1] + "=" + got + " want " + wants[i]);
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
