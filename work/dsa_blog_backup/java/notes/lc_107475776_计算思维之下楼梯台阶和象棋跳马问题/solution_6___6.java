// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107475776
package com.webfault.dsa; // 引入依赖

import java.util.ArrayList; // 引入依赖
import java.util.List; // 引入依赖

// 象棋跳马问题（方案6）：将合法性/终止判断隔离为辅助函数
class Main { // 定义类型
  static class Position { // static class Position {
    final int x, y; // final int x, y;

    Position(int x, int y) {
      this.x = x;
      this.y = y;
    } // 把 x; this.y 赋值为 y; } 写入 x
  }

  static final List<Position> MOVES = new ArrayList<>();

  static { // static {
    MOVES.add(new Position(1, 2)); // MOVES 追加 new Position(1, 2));
    MOVES.add(new Position(2, 1)); // MOVES 追加 new Position(2, 1));
    MOVES.add(new Position(2, -1)); // MOVES 追加 new Position(2, 减 1));
    MOVES.add(new Position(1, -2)); // MOVES 追加 new Position(1, 减 2));
  }

  static boolean isValid(Position pos) { // 定义判定函数 isValid
    return 0 <= pos.x
        && pos.x <= 8
        && 0 <= pos.y
        && pos.y <= 4; // 返回 0 不超过 pos.x 且 pos.x 不超过 8 且 0 不超过 pos.y 且 pos.y 不超过 4
  }

  static boolean isGoal(Position pos, Position goal) { // 定义判定函数 isGoal
    return pos.x == goal.x && pos.y == goal.y; // 返回 pos.x 等于 goal.x 且 pos.y 等于 goal.y
  }

  static int horseJumpCount(int gx, int gy) { // 定义函数/方法 horseJumpCount
    int[] count = {0}; // 把 {0}; 写入 int[] count
    jump(
        new Position(0, 0),
        new Position(gx, gy),
        count); // jump(new Position(0, 0), new Position(gx, gy), 计数);
    return count[0]; // 返回 计数[0]
  }

  static void jump(Position pos, Position goal, int[] count) { // 定义函数/方法 jump
    if (isGoal(pos, goal)) { // 若 isGoal(pos, goal
      count[0]++; // 计数[0] 加一 ;
      return; // return;
    }
    for (Position mv : MOVES) { // for (Position mv : MOVES) {
      Position nxt =
          new Position(
              pos.x + mv.x,
              pos.y + mv.y); // 把 new Position(pos.x 加 mv.x, pos.y 加 mv.y); 写入 Position nxt
      if (!isValid(nxt)) { // 若 取反 isValid(nxt
        continue; // 跳过本轮，进入下一次
      }
      jump(nxt, goal, count); // jump(nxt, goal, 计数);
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
