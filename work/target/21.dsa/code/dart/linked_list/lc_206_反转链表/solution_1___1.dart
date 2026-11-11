// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133785568
// LeetCode 206. 反转链表 — Dart 版（方案1）
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

LNode? reverseList(LNode? head) {
  // LNode? reverseList(LNode? 头节点) {
  LNode? prev; // LNode? 前一个;
  var cur = head; // 把 头节点 存入 当前值
  while (cur != null) {
    // 循环，直到不满足「当前值 不等于 null」
    final nxt = cur.next; // 把 当前值.下一个 存入 nxt
    cur.next = prev; // 把 前一个; 写入 下一个
    prev = cur; // 把 当前值 存入 前一个
    cur = nxt; // 把 nxt 存入 当前值
  }
  return prev; // 返回 前一个
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (toVec(reverseList(buildList([1, 2, 3, 4, 5]))).toString() !=
      '[5, 4, 3, 2, 1]')
    throw StateError('c1');
  if (toVec(reverseList(null)).isNotEmpty) throw StateError('c2');
  if (toVec(reverseList(buildList([1]))).toString() != '[1]')
    throw StateError('c3');
  print('PASS'); // 全部用例通过，输出 PASS
}
