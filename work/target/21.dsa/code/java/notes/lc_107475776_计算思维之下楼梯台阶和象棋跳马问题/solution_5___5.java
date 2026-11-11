// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107475776
package com.webfault.dsa; // 引入依赖

import java.util.ArrayList; // 引入依赖
import java.util.List; // 引入依赖

// 象棋跳马问题（方案5）：用结构(命名元组)表示落点坐标
class Main { // 定义类型
  static class Position { // static class Position {
    final int x, y; // final int x, y;

    Position(int x, int y) {
      this.x = x;
      this.y = y;
    } // 把 x; this.y 赋值为 y; } 写入 x
  }

  static int horseJumpCount(int gx, int gy) { // 定义函数/方法 horseJumpCount
    List<Position> moves = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Position> moves
    moves.add(new Position(1, 2)); // moves 追加 new Position(1, 2));
    moves.add(new Position(2, 1)); // moves 追加 new Position(2, 1));
    moves.add(new Position(2, -1)); // moves 追加 new Position(2, 减 1));
    moves.add(new Position(1, -2)); // moves 追加 new Position(1, 减 2));
    int[] count = {0}; // 把 {0}; 写入 int[] count
    jump(
        new Position(0, 0),
        new Position(gx, gy),
        moves,
        count); // jump(new Position(0, 0), new Position(gx, gy), moves, 计数);
    return count[0]; // 返回 计数[0]
  }

  static void jump(Position pos, Position goal, List<Position> moves, int[] count) { // 定义函数/方法 jump
    if (pos.x == goal.x && pos.y == goal.y) { // 若 pos.x 等于 goal.x 且 pos.y 等于 goal.y
      count[0]++; // 计数[0] 加一 ;
      return; // return;
    }
    for (Position mv : moves) { // for (Position mv : moves) {
      Position nxt =
          new Position(
              pos.x + mv.x,
              pos.y + mv.y); // 把 new Position(pos.x 加 mv.x, pos.y 加 mv.y); 写入 Position nxt
      if (nxt.x < 0 || nxt.x > 8 || nxt.y < 0
          || nxt.y > 4) { // 若 nxt.x 小于 0 或 nxt.x 超过 8 或 nxt.y 小于 0 或 nxt.y 超过 4
        continue; // 跳过本轮，进入下一次
      }
      jump(nxt, goal, moves, count); // jump(nxt, goal, moves, 计数);
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int normal = horseJumpCount(8, 4); // (0,0)->(8,4)
    int boundary = horseJumpCount(0, 0); // 起点即终点，只有 1 种方案
    boolean ok = true; // 把 true; 写入 boolean ok
    if (normal != 37) { // 若 normal 不等于 37
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL horseJumpCount(8,4)=" + normal + " want 37"); // 打印输出
    }
    if (boundary != 1) { // 若 boundary 不等于 1
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL horseJumpCount(0,0)=" + boundary + " want 1"); // 打印输出
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
