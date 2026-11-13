// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133922762
// LeetCode 160. 相交链表 — Dart 版（方案1）
class LNode {
  // 定义类型
  final int val; // final int 值;
  LNode? next; // LNode? 下一个;
  LNode(this.val); // LNode(this.值);
}

LNode? getIntersectionNode(LNode? a, LNode? b) {
  // LNode? getIntersectionNode(LNode? 数组, LNode? b) {
  if (a == null || b == null) return null; // 若 数组 等于 null 或 b 等于 null，直接返回 null
  LNode? p1 = a, p2 = b; // 把 数组, p2 赋值为 b; 写入 LNode? p1
  while (!identical(p1, p2)) {
    // 循环，直到不满足「取反 identical(p1, p2」
    p1 = p1 != null ? p1.next : b; // 把 p1 不等于 null ? p1.下一个 : b 存入 p1
    p2 = p2 != null ? p2.next : a; // 把 p2 不等于 null ? p2.下一个 : 数组 存入 p2
  }
  return p1; // 返回 p1
}

void main() {
  // 程序入口：跑内嵌自测用例
  final shared = LNode(8); // 把 LNode(8) 存入 shared
  shared.next = LNode(4)
    ..next = LNode(5); // 把 LNode(4)..下一个 赋值为 LNode(5); 写入 下一个
  final a = LNode(4)
    ..next = LNode(1)
    ..next = shared; // 把 LNode(4)..下一个 赋值为 LNode(1)..下一个 赋值为 shared 存入 数组
  final b = LNode(5)
    ..next = LNode(6)
    ..next = LNode(1)
    ..next = shared;
  if (!identical(getIntersectionNode(a, b), shared)) throw StateError('c1');
  if (getIntersectionNode(LNode(1), LNode(1)) != null) throw StateError('c2');
  if (getIntersectionNode(null, null) != null) throw StateError('c3');
  print('PASS'); // 全部用例通过，输出 PASS
}
