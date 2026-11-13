// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133874671
// LeetCode 142. 环形链表II — Dart 版（方案1）
class LNode {
  // 定义类型
  final int val; // final int 值;
  LNode? next; // LNode? 下一个;
  LNode(this.val); // LNode(this.值);
}

LNode? buildWithCycle(List<int> vals, int pos) {
  // LNode? buildWithCycle(List 小于 int 超过 vals, int pos) {
  LNode? head; // LNode? 头节点;
  LNode? cur; // LNode? 当前值;
  LNode? tailAt; // LNode? tailAt;
  for (var i = 0; i < vals.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 vals.长度 就继续
    final n = LNode(vals[i]); // 把 LNode(vals[下标 i]) 存入 元素个数
    if (head == null) {
      // 若 头节点 等于 null
      head = n; // 把 元素个数 存入 头节点
    } else {
      // 否则
      cur!.next = n; // 把 元素个数; 写入 下一个
    }
    cur = n; // 把 元素个数 存入 当前值
    if (i + 1 == pos) tailAt = n; // 若 下标 i 加 1 等于 pos) tailAt 赋值为 元素个数;
  }
  if (tailAt != null)
    cur!.next = tailAt; // 若 tailAt 不等于 null) 当前值取反 .下一个 赋值为 tailAt;
  return head; // 返回 头节点
}

LNode? detectCycle(LNode? head) {
  // LNode? detectCycle(LNode? 头节点) {
  LNode? slow = head, fast = head; // 把 头节点, 快指针 赋值为 头节点; 写入 LNode? slow
  while (fast != null && fast.next != null) {
    // 循环，直到不满足「快指针 不等于 null 且 快指针.下一个 不等于 null」
    slow = slow!.next; // 把 慢指针取反 .下一个 存入 慢指针
    fast = fast.next!.next; // 把 快指针.下一个取反 .下一个 存入 快指针
    if (identical(slow, fast)) {
      // 若 identical(慢指针, 快指针
      LNode? p1 = head; // 把 头节点; 写入 LNode? p1
      LNode? p2 = slow; // 把 慢指针; 写入 LNode? p2
      while (!identical(p1, p2)) {
        // 循环，直到不满足「取反 identical(p1, p2」
        p1 = p1!.next; // 把 p1取反 .下一个 存入 p1
        p2 = p2!.next; // 把 p2取反 .下一个 存入 p2
      }
      return p1; // 返回 p1
    }
  }
  return null; // 返回 null
}

void main() {
  // 程序入口：跑内嵌自测用例
  final h = buildWithCycle([
    3,
    2,
    0,
    -4,
  ], 2); // 把 buildWithCycle([3, 2, 0, 减 4], 2) 存入 h
  final e = detectCycle(h); // 把 detectCycle(h) 存入 e
  if (e == null || e.val != 2)
    throw StateError('c1'); // 若 e 等于 null 或 e.值 不等于 2) throw StateError('c1');
  if (detectCycle(LNode(1)) != null)
    throw StateError(
      'c2',
    ); // 若 detectCycle(LNode(1)) 不等于 null) throw StateError('c2');
  print('PASS'); // 全部用例通过，输出 PASS
}
