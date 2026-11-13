// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145095646

class ListNode {
  // 定义类型
  val: number; // 值: number;
  next: ListNode | null; // 下一个: ListNode 按位或 null;
  constructor(val: number = 0, next: ListNode | null = null) {
    this.val = val; // 把 值; 写入 值
    this.next = next; // 把 下一个; 写入 下一个
  }
}

function buildList(vals: number[]): ListNode | null {
  // 定义函数/方法 buildList
  const dummy = new ListNode(0); // 把 new ListNode(0) 存入 哨兵节点
  let cur = dummy; // 把 哨兵节点 存入 当前值
  for (const v of vals) {
    // for (const 值 of vals) {
    cur.next = new ListNode(v); // 把 new ListNode(值); 写入 下一个
    cur = cur.next; // 把 当前值.下一个 存入 当前值
  }
  return dummy.next; // 返回 哨兵节点.下一个
}

function listToArr(head: ListNode | null): number[] {
  // 定义函数/方法 listToArr
  const res: number[] = []; // 把 []; 写入 const res: number[]
  while (head) {
    // 循环，直到不满足「头节点」
    res.push(head.val); // 把 头节点.值 压入栈/数组尾部
    head = head.next; // 把 头节点.下一个 存入 头节点
  }
  return res; // 返回 结果
}

function listToStr(head: ListNode | null): string {
  // 定义函数/方法 listToStr
  const parts: string[] = []; // 把 []; 写入 const parts: string[]
  while (head) {
    // 循环，直到不满足「头节点」
    parts.push(String(head.val)); // 把 String(头节点.值 压入栈/数组尾部
    head = head.next; // 把 头节点.下一个 存入 头节点
  }
  return parts.join('->'); // 返回 parts.join(「 减 超过 」)
}

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual); // 把 JSON.stringify(actual) 存入 数组
  const e = JSON.stringify(expected); // 把 JSON.stringify(expected) 存入 e
  if (a !== e) {
    // 若 数组 不等于 e
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
  }
}

function removeElements(head: ListNode | null, val: number): ListNode | null {
  // 定义函数/方法 removeElements
  const dummy = new ListNode(0, head); // 把 new ListNode(0, 头节点) 存入 哨兵节点
  let temp = dummy; // 把 哨兵节点 存入 临时变量
  while (temp.next) {
    // 循环，直到不满足「临时变量.下一个」
    if (temp.next.val === val) {
      // 若 临时变量.下一个.值 全等于 值
      temp.next = temp.next.next; // 把 临时变量.下一个.下一个; 写入 下一个
    } else {
      // 否则
      temp = temp.next; // 把 临时变量.下一个 存入 临时变量
    }
  }
  return dummy.next; // 返回 哨兵节点.下一个
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const h = buildList([1, 2, 6, 3, 4, 5, 6]); // 把 buildList([1, 2, 6, 3, 4, 5, 6]) 存入 h
  assertEq(listToStr(removeElements(h, 6)), '1->2->3->4->5', 'removeElements'); // 断言校验
  const h2 = buildList([6, 6, 6]); // 把 buildList([6, 6, 6]) 存入 h2
  assertEq(listToStr(removeElements(h2, 6)), '', 'removeElements all'); // 断言校验
  const h3 = buildList([1, 2, 3]); // 把 buildList([1, 2, 3]) 存入 h3
  assertEq(listToStr(removeElements(h3, 9)), '1->2->3', 'removeElements none'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
