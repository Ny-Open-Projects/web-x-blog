// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134283831
// LeetCode 23. 合并K个升序链表 — Dart 版（方案9）
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

LNode? mergeTwo(LNode? a, LNode? b) {
  // LNode? mergeTwo(LNode? 数组, LNode? b) {
  final dummy = LNode(0); // 把 LNode(0) 存入 哨兵节点
  var cur = dummy; // 把 哨兵节点 存入 当前值
  while (a != null && b != null) {
    // 循环，直到不满足「数组 不等于 null 且 b 不等于 null」
    if (a.val <= b.val) {
      // 若 数组.值 不超过 b.值
      cur.next = a; // 把 数组; 写入 下一个
      a = a.next; // 把 数组.下一个 存入 数组
    } else {
      // 否则
      cur.next = b; // 把 b; 写入 下一个
      b = b.next; // 把 b.下一个 存入 b
    }
    cur = cur.next!; // 把 当前值.下一个取反 存入 当前值
  }
  cur.next = a ?? b; // 把 数组 ?? b; 写入 下一个
  return dummy.next; // 返回 哨兵节点.下一个
}

LNode? mergeKLists(List<LNode?> lists) {
  // LNode? mergeKLists(List 小于 LNode? 超过 lists) {
  LNode? acc; // LNode? 累加器;
  for (final l in lists) {
    // for (final 左指针 in lists) {
    acc = mergeTwo(acc, l); // 把 mergeTwo(累加器, 左指针) 存入 累加器
  }
  return acc; // 返回 累加器
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
  if (mergeKLists([buildList([])]) != null) throw StateError('c3');
  print('PASS'); // 全部用例通过，输出 PASS
}
