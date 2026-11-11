// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134120377
// LeetCode 707. 设计链表 — Dart 版（方案1）
class MyList {
  // 定义类型
  final List<int> items = []; // 把 []; 写入 final List<int> items
  void addAtHead(int x) => items.insert(0, x);
  void addAtTail(int x) => items.add(x);
  void addAtIndex(int idx, int x) {
    // 定义函数/方法 addAtIndex
    if (idx < 0) idx = 0; // 若 idx 小于 0) idx 赋值为 0;
    if (idx > items.length) return; // 若 idx 超过 items.长度) return;
    items.insert(idx, x); // items 插入 idx, x);
  }

  int get(int idx) {
    // 定义函数/方法 get
    if (idx < 0 || idx >= items.length)
      return -1; // 若 idx 小于 0 或 idx 不低于 items.长度，直接返回 减 1
    return items[idx]; // 返回 items[idx]
  }

  void deleteAtIndex(int idx) {
    // 定义函数/方法 deleteAtIndex
    if (idx < 0 || idx >= items.length)
      return; // 若 idx 小于 0 或 idx 不低于 items.长度) return;
    items.removeAt(idx); // items.removeAt(idx);
  }
}

void main() {
  // 程序入口：跑内嵌自测用例
  final l = MyList(); // 把 MyList() 存入 左指针
  l.addAtHead(1); // 左指针.addAtHead(1);
  l.addAtTail(3); // 左指针.addAtTail(3);
  l.addAtIndex(1, 2); // 左指针.addAtIndex(1, 2);
  if (l.get(1) != 2)
    throw StateError('c1'); // 若 左指针 查找 1) 不等于 2) throw StateError('c1');
  l.deleteAtIndex(1); // 左指针.deleteAtIndex(1);
  if (l.get(1) != 3)
    throw StateError('c2'); // 若 左指针 查找 1) 不等于 3) throw StateError('c2');
  print('PASS'); // 全部用例通过，输出 PASS
}
