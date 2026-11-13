// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133886377
// LeetCode 237. 删除链表中的节点 — Dart 版（方案4）
class LNode {
  // 定义类型
  int val; // int 值;
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

void deleteNode(LNode node) {
  // 定义函数/方法 deleteNode
  final next = node.next!; // 把 节点.下一个取反 存入 下一个
  node.val = next.val; // 把 下一个.值; 写入 值
  node.next = next.next; // 把 下一个.下一个; 写入 下一个
}

void main() {
  // 程序入口：跑内嵌自测用例
  final l = buildList([4, 5, 1, 9])!; // 把 buildList([4, 5, 1, 9])取反 存入 左指针
  deleteNode(l.next!); // deleteNode(左指针.下一个取反 );
  if (toVec(l).toString() != '[4, 1, 9]') throw StateError('c1');
  final l2 = buildList([1, 2, 3])!; // 把 buildList([1, 2, 3])取反 存入 l2
  deleteNode(l2.next!); // deleteNode(l2.下一个取反 );
  if (toVec(l2).toString() != '[1, 3]')
    throw StateError(
      'c2',
    ); // 若 toVec(l2).toString() 不等于 '[1, 3]') throw StateError('c2');
  print('PASS'); // 全部用例通过，输出 PASS
}
