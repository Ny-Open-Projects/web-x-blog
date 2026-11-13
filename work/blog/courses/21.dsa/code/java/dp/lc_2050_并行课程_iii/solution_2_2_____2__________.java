// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145380834
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Lc2050 { // 定义类型
  int minimumTime(int n, int[][] relations, int[] time) { // 定义函数/方法 minimumTime
    Map<Integer, List<Integer>> graph =
        new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 Map<Integer,List<Integer>> graph
    int[] indeg = new int[n + 1]; // 把 new int[元素个数 加 1]; 写入 int[] indeg
    for (int[] r : relations) {
      graph.computeIfAbsent(r[0], k -> new ArrayList<>()).add(r[1]);
      indeg[r[1]]++;
    }
    int[] dp = new int[n + 1]; // 把 new int[元素个数 加 1]; 写入 int[] dp
    for (int i = 1; i <= n; i++) dp[i] = time[i - 1]; // 让 下标 i 从 1 开始计数，下标 i 不超过 元素个数 就继续
    Deque<Integer> q = new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<Integer> q
    for (int i = 1; i <= n; i++) if (indeg[i] == 0) q.offer(i); // 让 下标 i 从 1 开始计数，下标 i 不超过 元素个数 就继续
    while (!q.isEmpty()) { // 循环，直到不满足「取反 节点.isEmpty(」
      int u = q.poll(); // 把 节点.poll() 存入 节点 u
      for (int v :
          graph.getOrDefault(
              u,
              new ArrayList<>())) { // for(int 值: graph.getOrDefault(节点 u,new ArrayList 小于 超过 ())){
        dp[v] =
            Math.max(
                dp[v],
                dp[u] + time[v - 1]); // 把 Math.取较大值 DP 表[值], DP 表[节点 u] 加 time[值 减 1]); 写入 dp[v]
        indeg[v]--; // indeg[值] 减一 ;
        if (indeg[v] == 0) q.offer(v); // 若 indeg[值] 等于 0) 节点.offer(值);
      }
    }
    int mx = 0;
    for (int i = 1; i <= n; i++) mx = Math.max(mx, dp[i]);
    return mx; // 返回 mx
  }

  public static void main(String[] args) { // public static void main(String[] args){
    Lc2050 s = new Lc2050(); // 把 new Lc2050(); 写入 Lc2050 s
    int ans = s.minimumTime(3, new int[][] {{1, 3}, {2, 3}}, new int[] {3, 2, 5});
    if (ans != 8) throw new RuntimeException("FAILED got=" + ans);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
