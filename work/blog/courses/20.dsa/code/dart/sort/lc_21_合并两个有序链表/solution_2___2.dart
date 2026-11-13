// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133594090
// LeetCode 21. 合并两个有序链表 — Dart 版（方案2）
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

List<int> listToVec(LNode? head) {
  // 定义函数/方法 listToVec
  final out = <int>[]; // 把 小于 int 超过 [] 存入 out
  while (head != null) {
    // 循环，直到不满足「头节点 不等于 null」
    out.add(head.val); // out 追加 头节点.值);
    head = head.next; // 把 头节点.下一个 存入 头节点
  }
  return out; // 返回 out
}

LNode? mergeTwoLists(LNode? list1, LNode? list2) {
  // LNode? mergeTwoLists(LNode? list1, LNode? list2) {
  final dummy = LNode(0); // 把 LNode(0) 存入 哨兵节点
  var p = dummy; // 把 哨兵节点 存入 节点
  var p1 = list1, p2 = list2; // 把 list1, p2 赋值为 list2 存入 p1
  while (p1 != null && p2 != null) {
    // 循环，直到不满足「p1 不等于 null 且 p2 不等于 null」
    if (p1.val < p2.val) {
      // 若 p1.值 小于 p2.值
      p.next = p1; // 把 p1; 写入 下一个
      p1 = p1.next; // 把 p1.下一个 存入 p1
    } else {
      // 否则
      p.next = p2; // 把 p2; 写入 下一个
      p2 = p2.next; // 把 p2.下一个 存入 p2
    }
    p = p.next!; // 把 节点.下一个取反 存入 节点
  }
  p.next = p1 ?? p2; // 把 p1 ?? p2; 写入 下一个
  return dummy.next; // 返回 哨兵节点.下一个
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (listToVec(mergeTwoLists(buildList([1, 2, 4]), buildList([1, 3, 4])))
          .toString() !=
      '[1, 1, 2, 3, 4, 4]')
    throw StateError('c1');
  if (mergeTwoLists(null, null) != null) throw StateError('c2');
  if (listToVec(mergeTwoLists(null, buildList([0]))).toString() != '[0]')
    throw StateError('c3');
  print('PASS'); // 全部用例通过，输出 PASS
}
