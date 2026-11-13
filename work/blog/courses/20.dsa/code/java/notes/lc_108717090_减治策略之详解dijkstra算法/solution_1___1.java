// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108717090
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc108717090_solution11 { // 定义类型
  static class Edge { // static class Edge {
    int to, w; // int to, 权重;

    Edge(int to, int w) {
      this.to = to;
      this.w = w;
    } // 把 to; this.权重 赋值为 权重; } 写入 Edge(int to, int w) { this.to
  }

  static class DResult { // static class DResult {
    int[] dist; // int[] dist;
    int[] parent; // int[] parent;
  }

  static DResult dijkstra(List<List<Edge>> graph, int src) { // 定义函数/方法 dijkstra
    int n = graph.size(); // 把 graph.大小() 存入 元素个数
    int[] dist = new int[n]; // 把 new int[元素个数]; 写入 int[] dist
    Arrays.fill(dist, Integer.MAX_VALUE); // Arrays.fill(dist, Integer.MAX_VALUE);
    dist[src] = 0; // 把 0; 写入 dist[src]
    int[] parent = new int[n]; // 把 new int[元素个数]; 写入 int[] parent
    Arrays.fill(parent, -1); // Arrays.fill(parent, 减 1);
    PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
    pq.add(new int[] {0, src}); // 优先队列 追加 new int[]{0, src});
    while (!pq.isEmpty()) { // 循环，直到不满足「取反 优先队列.isEmpty(」
      int[] cur = pq.poll(); // 把 优先队列.poll(); 写入 int[] cur
      int d = cur[0], u = cur[1]; // 把 当前值[0], 节点 u 赋值为 当前值[1] 存入 d
      if (d > dist[u]) continue; // 若 d 超过 dist[节点 u]) continue;
      for (Edge e : graph.get(u)) { // for (Edge e : graph 查找 节点 u)) {
        if (dist[u] + e.w < dist[e.to]) { // 若 dist[节点 u] 加 e.权重 小于 dist[e.to]
          dist[e.to] = dist[u] + e.w; // 把 dist[节点 u] 加 e.权重; 写入 dist[e.to]
          parent[e.to] = u; // 把 节点 u; 写入 parent[e.to]
          pq.add(new int[] {dist[e.to], e.to}); // 优先队列 追加 new int[]{dist[e.to], e.to});
        }
      }
    }
    DResult r = new DResult(); // 把 new DResult(); 写入 DResult r
    r.dist = dist; // 把 dist; 写入 r.dist
    r.parent = parent; // 把 parent; 写入 r.parent
    return r; // 返回 右指针
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    List<List<Edge>> graph =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<List<Edge>> graph
    for (int i = 0; i < 5; i++) graph.add(new ArrayList<>()); // 让 下标 i 从 0 开始计数，下标 i 小于 5 就继续
    graph.get(0).add(new Edge(1, 4)); // graph 查找 0) 追加 new Edge(1, 4));
    graph.get(0).add(new Edge(2, 1)); // graph 查找 0) 追加 new Edge(2, 1));
    graph.get(1).add(new Edge(3, 1)); // graph 查找 1) 追加 new Edge(3, 1));
    graph.get(2).add(new Edge(1, 2)); // graph 查找 2) 追加 new Edge(1, 2));
    graph.get(2).add(new Edge(3, 5)); // graph 查找 2) 追加 new Edge(3, 5));
    graph.get(3).add(new Edge(4, 3)); // graph 查找 3) 追加 new Edge(4, 3));
    DResult res = dijkstra(graph, 0); // 把 dijkstra(graph, 0); 写入 DResult res
    int[] expectDist = {0, 3, 1, 4, 7}; // 把 {0, 3, 1, 4, 7}; 写入 int[] expectDist
    int[] expectParent = {-1, 2, 0, 1, 3}; // 把 { 减 1, 2, 0, 1, 3}; 写入 int[] expectParent
    for (int i = 0; i < 5; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 5 就继续
      if (res.dist[i] != expectDist[i]) { // 若 结果.dist[下标 i] 不等于 expectDist[下标 i]
        System.out.println("FAIL dist[" + i + "]=" + res.dist[i]); // 打印输出
        throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
      }
      if (res.parent[i] != expectParent[i]) { // 若 结果.parent[下标 i] 不等于 expectParent[下标 i]
        System.out.println("FAIL parent[" + i + "]=" + res.parent[i]); // 打印输出
        throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
      }
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
