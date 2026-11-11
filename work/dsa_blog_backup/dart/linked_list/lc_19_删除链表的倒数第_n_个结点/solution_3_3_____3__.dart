// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133746567
// LeetCode 19. 删除链表的倒数第N个结点 — Dart 版（方案3）
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

List<int> toVec(LNode? h) {
  // 定义函数/方法 toVec
  final out = <int>[]; // 把 小于 int 超过 [] 存入 out
  while (h != null) {
    // 循环，直到不满足「h 不等于 null」
    out.add(h.val); // out 追加 h.值);
    h = h.next; // 把 h.下一个 存入 h
  }
  return out; // 返回 out
}

LNode? removeNthFromEnd(LNode? head, int n) {
  // LNode? removeNthFromEnd(LNode? 头节点, int 元素个数) {
  final dummy = LNode(0); // 把 LNode(0) 存入 哨兵节点
  dummy.next = head; // 把 头节点; 写入 下一个
  LNode? fast = dummy, slow = dummy; // 把 哨兵节点, 慢指针 赋值为 哨兵节点; 写入 LNode? fast
  for (var i = 0; i <= n; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 不超过 元素个数 就继续
    fast = fast!.next; // 把 快指针取反 .下一个 存入 快指针
  }
  while (fast != null) {
    // 循环，直到不满足「快指针 不等于 null」
    fast = fast.next; // 把 快指针.下一个 存入 快指针
    slow = slow!.next; // 把 慢指针取反 .下一个 存入 慢指针
  }
  slow!.next = slow.next!.next; // 把 慢指针.下一个取反 .下一个; 写入 下一个
  return dummy.next; // 返回 哨兵节点.下一个
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (toVec(removeNthFromEnd(buildList([1, 2, 3, 4, 5]), 2)).toString() !=
      '[1, 2, 3, 5]')
    throw StateError('c1');
  if (removeNthFromEnd(buildList([1]), 1) != null) throw StateError('c2');
  if (toVec(removeNthFromEnd(buildList([1, 2]), 2)).toString() != '[2]')
    throw StateError('c3');
  print('PASS'); // 全部用例通过，输出 PASS
}
