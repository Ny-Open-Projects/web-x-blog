// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145096505

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

function middleNode(head: ListNode | null): ListNode | null {
  // 定义函数/方法 middleNode
  let slow = head,
    fast = head; // 把 头节点, 快指针 赋值为 头节点 存入 慢指针
  while (fast && fast.next) {
    slow = slow!.next;
    fast = fast.next.next;
  }
  return slow; // 返回 慢指针
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(middleNode(null), null, 'null'); // 断言校验
  assertEq(middleNode(buildList([1, 2, 3, 4, 5]))!.val, 3, 'odd'); // 断言校验
  assertEq(middleNode(buildList([1, 2, 3, 4, 5, 6]))!.val, 4, 'even'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
