// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134283831
// LeetCode 23. 合并K个升序链表 — Dart 版（方案2）
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

LNode? mergeKLists(List<LNode?> lists) {
  // LNode? mergeKLists(List 小于 LNode? 超过 lists) {
  final ptrs = List<LNode?>.from(
    lists,
  ); // 把 List 小于 LNode? 超过 .from(lists) 存入 ptrs
  final dummy = LNode(0); // 把 LNode(0) 存入 哨兵节点
  var tail = dummy; // 把 哨兵节点 存入 尾节点
  while (true) {
    // 循环，直到不满足「true」
    var bestI = -1; // 把 减 1 存入 bestI
    for (var i = 0; i < ptrs.length; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 ptrs.长度 就继续
      if (ptrs[i] != null && (bestI < 0 || ptrs[i]!.val < ptrs[bestI]!.val))
        bestI = i;
    }
    if (bestI < 0) break; // 若 bestI 小于 0) break;
    tail.next = ptrs[bestI]; // 把 ptrs[bestI]; 写入 下一个
    ptrs[bestI] = ptrs[bestI]!.next; // 把 ptrs[bestI]取反 .下一个; 写入 ptrs[bestI]
    tail = tail.next!; // 把 尾节点.下一个取反 存入 尾节点
  }
  return dummy.next; // 返回 哨兵节点.下一个
}

void main() {
  // 程序入口：跑内嵌自测用例
  final got = listToVec(
    mergeKLists([
      buildList([1, 4, 5]),
      buildList([1, 3, 4]),
      buildList([2, 6]),
    ]),
  );
  if (got.toString() != '[1, 1, 2, 3, 4, 4, 5, 6]') throw StateError('c1');
  if (mergeKLists([]) != null)
    throw StateError(
      'c2',
    ); // 若 mergeKLists([]) 不等于 null) throw StateError('c2');
  print('PASS'); // 全部用例通过，输出 PASS
}
