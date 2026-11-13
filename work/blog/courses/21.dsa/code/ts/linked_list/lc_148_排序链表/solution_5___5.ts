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
  const nodes: ListNode[] = [];
  let curr = head; // 把 []; let 当前值 赋值为 头节点; 写入 const nodes: ListNode[]
  while (curr) {
    nodes.push(curr);
    curr = curr.next;
  } // 循环，直到不满足「当前值) { nodes 追加 当前值); 当前值 赋值为 当前值.下一个; }」
  nodes.sort((a, b) => a.val - b.val);
  for (let i = 0; i < nodes.length - 1; i++) nodes[i].next = nodes[i + 1]; // 让 下标 i 从 0 开始计数，下标 i 小于 nodes.长度 减 1 就继续
  if (nodes.length) nodes[nodes.length - 1].next = null; // 若 nodes.长度) nodes[nodes.长度 减 1].下一个 赋值为 null;
  return nodes.length ? nodes[0] : null; // 返回 nodes.长度 ? nodes[0] : null
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(
    listToArr(sortList(buildList([4, 2, 1, 3, 5]))!),
    [1, 2, 3, 4, 5],
    'sort1',
  ); // 断言校验
  assertEq(listToArr(sortList(buildList([1]))!), [1], 'sort2'); // 断言校验
  assertEq(sortList(null), null, 'sort null'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
