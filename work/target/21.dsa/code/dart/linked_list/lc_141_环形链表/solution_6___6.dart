// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133816714
// LeetCode 141. 环形链表 — Dart 版（方案6）
class LNode {
  // 定义类型
  final int val; // final int 值;
  LNode? next; // LNode? 下一个;
  LNode(this.val); // LNode(this.值);
}

LNode? buildList(List<int> vals) {
  // LNode? buildList(List 小于 int 超过 vals) {
  LNode? head; // LNode? 头节点;
  LNode? cur; // LNode? 当前值;
  for (final v in vals) {
    // for (final 值 in vals) {
    final n = LNode(v); // 把 LNode(值) 存入 元素个数
    if (head == null) {
      // 若 头节点 等于 null
      head = n; // 把 元素个数 存入 头节点
    } else {
      // 否则
      cur!.next = n; // 把 元素个数; 写入 下一个
    }
    cur = n; // 把 元素个数 存入 当前值
  }
  return head; // 返回 头节点
}

bool hasCycle(LNode? head) {
  // 定义函数/方法 hasCycle
  LNode? slow = head, fast = head; // 把 头节点, 快指针 赋值为 头节点; 写入 LNode? slow
  while (fast != null && fast.next != null) {
    // 循环，直到不满足「快指针 不等于 null 且 快指针.下一个 不等于 null」
    slow = slow!.next; // 把 慢指针取反 .下一个 存入 慢指针
    fast = fast.next!.next; // 把 快指针.下一个取反 .下一个 存入 快指针
    if (identical(slow, fast)) return true; // 若 identical(慢指针, 快指针)，直接返回 true
  }
  return false; // 返回 false
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (hasCycle(buildList([3, 2, 0, -4]))) throw StateError('c1');
  final h = buildList([1])!; // 把 buildList([1])取反 存入 h
  h.next = h; // 把 h; 写入 下一个
  if (!hasCycle(h))
    throw StateError('c2'); // 若 取反 hasCycle(h)) throw StateError('c2');
  if (hasCycle(null))
    throw StateError('c3'); // 若 hasCycle(null)) throw StateError('c3');
  print('PASS'); // 全部用例通过，输出 PASS
}
