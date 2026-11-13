// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130536355

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

function sortList(head: ListNode | null): ListNode | null {
  // 定义函数/方法 sortList
  if (!head || !head.next) return head; // 若 取反 头节点 或 取反 头节点.下一个，直接返回 头节点
  let slow = head,
    fast = head.next; // 把 头节点, 快指针 赋值为 头节点.下一个 存入 慢指针
  while (fast && fast.next) {
    slow = slow.next!;
    fast = fast.next.next;
  }
  const mid = slow.next;
  slow.next = null; // 把 慢指针.下一个; 慢指针.下一个 赋值为 null 存入 中点
  const left = sortList(head);
  const right = sortList(mid); // 把 sortList(头节点); const 右边界 赋值为 sortList(中点) 存入 左边界
  const dummy = new ListNode(0);
  let curr = dummy; // 把 new ListNode(0); let 当前值 赋值为 哨兵节点 存入 哨兵节点
  let l = left,
    r = right; // 把 左边界, 右指针 赋值为 右边界 存入 左指针
  while (l && r) {
    if (l.val <= r.val) {
      curr.next = l;
      l = l.next;
    } else {
      curr.next = r;
      r = r.next;
    }
    curr = curr.next;
  }
  curr.next = l || r; // 把 左指针 或 右指针; 写入 下一个
  return dummy.next; // 返回 哨兵节点.下一个
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(listToArr(sortList(null)), [], 'null'); // 断言校验
  assertEq(listToArr(sortList(buildList([4, 2, 1, 3]))), [1, 2, 3, 4], 'sort'); // 断言校验
  assertEq(listToArr(sortList(buildList([1]))), [1], 'single'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
