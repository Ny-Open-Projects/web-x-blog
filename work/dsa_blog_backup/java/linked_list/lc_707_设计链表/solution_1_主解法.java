// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145347892
package com.webfault.dsa; // 引入依赖

import java.util.ArrayList; // 引入依赖
import java.util.List; // 引入依赖
import java.util.Objects; // 引入依赖

class lc707_solution1 { // 定义类型
  static class Node { // static class Node {
    int val; // int 值;
    Node prev, next; // Node 前一个, 下一个;

    Node(int v) { // Node(int 值) {
      val = v; // 把 值; 写入 值
    }
  }

  // MyLinkedList 忠实翻译 python ref solution_1_主解法.py（双向链表，head/tail/size）
  static class MyLinkedList { // static class MyLinkedList {
    Node head, tail; // Node 头节点, 尾节点;
    int size = 0; // 把 0 存入 大小

    int get(int index) { // 定义函数/方法 get
      if (index < 0 || index >= size) { // 若 index 小于 0 或 index 不低于 大小
        return -1; // 返回 减 1
      }
      Node curr = head; // 把 头节点; 写入 Node curr
      for (int i = 0; i < index; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 index 就继续
        curr = curr.next; // 把 当前值.下一个; 写入 当前值
      }
      return curr.val; // 返回 当前值.值
    }

    void addAtHead(int val) { // 定义函数/方法 addAtHead
      Node n = new Node(val); // 把 new Node(值); 写入 Node n
      n.next = head; // 把 头节点; 写入 下一个
      if (head != null) { // 若 头节点 不等于 null
        head.prev = n; // 把 元素个数; 写入 前一个
      } else { // 否则
        tail = n; // 把 元素个数; 写入 尾节点
      }
      head = n; // 把 元素个数; 写入 头节点
      size++; // 大小 加一
    }

    void addAtTail(int val) { // 定义函数/方法 addAtTail
      Node n = new Node(val); // 把 new Node(值); 写入 Node n
      if (tail != null) { // 若 尾节点 不等于 null
        tail.next = n; // 把 元素个数; 写入 下一个
        n.prev = tail; // 把 尾节点; 写入 前一个
      } else { // 否则
        head = n; // 把 元素个数; 写入 头节点
      }
      tail = n; // 把 元素个数; 写入 尾节点
      size++; // 大小 加一
    }

    void addAtIndex(int index, int val) { // 定义函数/方法 addAtIndex
      if (index < 0 || index > size) { // 若 index 小于 0 或 index 超过 大小
        return; // return;
      }
      if (index == 0) { // 若 index 等于 0
        addAtHead(val); // addAtHead(值);
        return; // return;
      }
      if (index == size) { // 若 index 等于 大小
        addAtTail(val); // addAtTail(值);
        return; // return;
      }
      Node curr = head; // 把 头节点; 写入 Node curr
      for (int i = 0; i < index; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 index 就继续
        curr = curr.next; // 把 当前值.下一个; 写入 当前值
      }
      Node n = new Node(val); // 把 new Node(值); 写入 Node n
      n.prev = curr.prev; // 把 当前值.前一个; 写入 前一个
      n.next = curr; // 把 当前值; 写入 下一个
      curr.prev.next = n; // 把 元素个数; 写入 下一个
      curr.prev = n; // 把 元素个数; 写入 前一个
      size++; // 大小 加一
    }

    void deleteAtIndex(int index) { // 定义函数/方法 deleteAtIndex
      if (index < 0 || index >= size) { // 若 index 小于 0 或 index 不低于 大小
        return; // return;
      }
      if (index == 0) { // 若 index 等于 0
        head = head.next; // 把 头节点.下一个; 写入 头节点
        if (head != null) { // 若 头节点 不等于 null
          head.prev = null; // 把 null; 写入 前一个
        } else { // 否则
          tail = null; // 把 null; 写入 尾节点
        }
      } else if (index == size - 1) { // 否则，若 index 等于 大小 减 1
        tail = tail.prev; // 把 尾节点.前一个; 写入 尾节点
        if (tail != null) { // 若 尾节点 不等于 null
          tail.next = null; // 把 null; 写入 下一个
        } else { // 否则
          head = null; // 把 null; 写入 头节点
        }
      } else { // 否则
        Node curr = head; // 把 头节点; 写入 Node curr
        for (int i = 0; i < index; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 index 就继续
          curr = curr.next; // 把 当前值.下一个; 写入 当前值
        }
        curr.prev.next = curr.next; // 把 当前值.下一个; 写入 下一个
        curr.next.prev = curr.prev; // 把 当前值.前一个; 写入 前一个
      }
      size--; // 大小 减一
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    // 操作编码: AH=addAtHead, AT=addAtTail, AI=addAtIndex, DI=deleteAtIndex, G=get
    // want 由 python ref solution_1_主解法.py 实跑操作序列得到
    String[][][] caseOps = { // 把 { 写入 String[][][] caseOps
      {
        {"AH", "1"},
        {"AT", "3"},
        {"AI", "1", "2"},
        {"G", "1"},
        {"G", "0"},
        {"G", "2"},
        {"DI", "1"},
        {"G", "1"}
      },
      {
        {"G", "0"},
        {"AH", "1"},
        {"G", "0"},
        {"AT", "2"},
        {"AI", "2", "3"},
        {"G", "2"},
        {"DI", "0"},
        {"G", "0"},
        {"DI", "1"},
        {"G", "1"},
        {"DI", "1"},
        {"G", "0"}
      },
      {
        {"AI", "1", "5"},
        {"G", "0"},
        {"AT", "1"},
        {"AH", "0"},
        {"AI", "2", "2"},
        {"AI", "0", "-1"},
        {"G", "3"},
        {"DI", "3"},
        {"G", "3"},
        {"AI", "-1", "9"},
        {"G", "0"}
      },
    };
    Integer[][] wants = { // 把 { 写入 Integer[][] wants
      {null, null, null, 2, 1, 3, null, 3},
      {-1, null, 1, null, null, 3, null, 2, null, -1, null, 2},
      {null, -1, null, null, null, null, 2, null, -1, null, -1},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int ci = 0; ci < caseOps.length; ci++) { // 让 ci 从 0 开始计数，ci 小于 caseOps.长度 就继续
      MyLinkedList obj = new MyLinkedList(); // 把 new MyLinkedList(); 写入 MyLinkedList obj
      List<Integer> got = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> got
      for (String[] op : caseOps[ci]) { // for (String[] op : caseOps[ci]) {
        switch (op[0]) { // switch (op[0]) {
          case "AH": // case 「AH」:
            obj.addAtHead(Integer.parseInt(op[1])); // obj.addAtHead(Integer.转整数(op[1]));
            got.add(null); // got 追加 null);
            break; // 跳出循环
          case "AT": // case 「AT」:
            obj.addAtTail(Integer.parseInt(op[1])); // obj.addAtTail(Integer.转整数(op[1]));
            got.add(null); // got 追加 null);
            break; // 跳出循环
          case "AI": // case 「AI」:
            obj.addAtIndex(
                Integer.parseInt(op[1]),
                Integer.parseInt(op[2])); // obj.addAtIndex(Integer.转整数(op[1]), Integer.转整数(op[2]));
            got.add(null); // got 追加 null);
            break; // 跳出循环
          case "DI": // case 「DI」:
            obj.deleteAtIndex(Integer.parseInt(op[1])); // obj.deleteAtIndex(Integer.转整数(op[1]));
            got.add(null); // got 追加 null);
            break; // 跳出循环
          case "G": // case 「G」:
            got.add(obj.get(Integer.parseInt(op[1]))); // got 追加 obj 查找 Integer.转整数(op[1])));
            break; // 跳出循环
          default: // default:
            break; // 跳出循环
        }
      }
      for (int i = 0; i < wants[ci].length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 wants[ci].长度 就继续
        if (!Objects.equals(
            got.get(i), wants[ci][i])) { // 若 取反 Objects.equals(got 查找 下标 i), wants[ci][下标 i]
          ok = false; // 把 false; 写入 ok
          System.out.println(
              "FAIL case"
                  + ci
                  + " step"
                  + i
                  + " got "
                  + got.get(i)
                  + " want "
                  + wants[ci][i]); // 打印输出
        }
      }
    }
    if (!ok) { // 若 取反 ok
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
