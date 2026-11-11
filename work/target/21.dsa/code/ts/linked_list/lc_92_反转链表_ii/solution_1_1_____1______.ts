// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145094075

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

function reverseLinkedList(head: ListNode | null): ListNode | null {
  // 定义函数/方法 reverseLinkedList
  let prev: ListNode | null = null;
  let curr = head; // 把 null; let 当前值 赋值为 头节点; 写入 let prev: ListNode | null
  while (curr) {
    const nxt = curr.next;
    curr.next = prev;
    prev = curr;
    curr = nxt;
  }
  return prev; // 返回 前一个
}
function reverseBetween(
  head: ListNode | null,
  left: number,
  right: number,
): ListNode | null {
  // 定义函数/方法 reverseBetween
  const dummy = new ListNode(-1);
  dummy.next = head; // 把 new ListNode( 减 1); 哨兵节点.下一个 赋值为 头节点 存入 哨兵节点
  let pre: ListNode = dummy; // 把 哨兵节点; 写入 let pre: ListNode
  for (let k = 0; k < left - 1; k++) pre = pre.next!; // 让 下标 k 从 0 开始计数，下标 k 小于 左边界 减 1 就继续
  const left_node = pre.next!; // 把 前缀和.下一个取反 存入 left_node
  let right_node: ListNode = pre; // 把 前缀和; 写入 let right_node: ListNode
  for (let k = 0; k < right - left; k++) right_node = right_node.next!; // 让 下标 k 从 0 开始计数，下标 k 小于 右边界 减 左边界 就继续
  const curr = right_node.next; // 把 right_node.下一个 存入 当前值
  pre.next = null; // 把 null; 写入 下一个
  right_node.next = null; // 把 null; 写入 下一个
  reverseLinkedList(left_node); // reverseLinkedList(left_node);
  pre.next = right_node; // 把 right_node; 写入 下一个
  left_node.next = curr; // 把 当前值; 写入 下一个
  return dummy.next; // 返回 哨兵节点.下一个
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(
    listToArr(reverseBetween(buildList([1, 2, 3, 4, 5]), 2, 4)!),
    [1, 3, 2, 4, 5],
    'rev1',
  ); // 断言校验
  assertEq(
    listToArr(reverseBetween(buildList([1, 2, 3, 4, 5]), 1, 4)!),
    [3, 2, 1, 4, 5],
    'rev2',
  ); // 断言校验
  assertEq(
    listToArr(reverseBetween(buildList([1, 2, 3, 4, 5]), 3, 4)!),
    [1, 2, 3, 4, 5],
    'rev3',
  ); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
