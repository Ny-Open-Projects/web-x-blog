// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145095015

class ListNode {
  // 定义类型
  val: number; // 值: number;
  next: ListNode | null; // 下一个: ListNode 按位或 null;
  constructor(val: number = 0, next: ListNode | null = null) {
    this.val = val;
    this.next = next; // 把 值; this.下一个 赋值为 下一个; 写入 值
  }
}
function buildList(vals: number[]): ListNode | null {
  // 定义函数/方法 buildList
  const dummy = new ListNode(0);
  let cur = dummy; // 把 new ListNode(0); let 当前值 赋值为 哨兵节点 存入 哨兵节点
  for (const v of vals) {
    cur.next = new ListNode(v);
    cur = cur.next;
  } // 把 new ListNode(值); 当前值 赋值为 当前值.下一个; } 写入 下一个
  return dummy.next; // 返回 哨兵节点.下一个
}
function listToArr(head: ListNode | null): number[] {
  // 定义函数/方法 listToArr
  const res: number[] = [];
  while (head) {
    res.push(head.val);
    head = head.next;
  }
  return res; // 把 头节点.值 压入栈/数组尾部
}

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function getIntersectionNode(
  headA: ListNode | null,
  headB: ListNode | null,
): ListNode | null {
  // 定义函数/方法 getIntersectionNode
  const visited = new Set<ListNode>();
  let t = headA; // 把 new Set 小于 ListNode 超过 (); let 另一字符串 赋值为 链表 A 存入 已访问集合
  while (t) {
    visited.add(t);
    t = t.next;
  } // 循环，直到不满足「另一字符串) { 已访问集合 追加 另一字符串); 另一字符串 赋值为 另一字符串.下一个; }」
  t = headB; // 把 链表 B 存入 另一字符串
  while (t) {
    if (visited.has(t)) return t;
    t = t.next;
  }
  return null; // 返回 null
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const shared = buildList([8, 4, 5]); // 把 buildList([8, 4, 5]) 存入 shared
  const headA = buildList([4, 1]);
  let cA = headA;
  while (cA.next) cA = cA.next;
  cA.next = shared;
  const headB = buildList([5, 6, 1]);
  let cB = headB;
  while (cB.next) cB = cB.next;
  cB.next = shared;
  assertEq(listToArr(getIntersectionNode(headA, headB)), [8, 4, 5], 'inter'); // 断言校验
  assertEq(getIntersectionNode(null, null), null, 'null'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
