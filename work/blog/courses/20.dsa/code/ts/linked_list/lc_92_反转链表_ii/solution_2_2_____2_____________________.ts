// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145094075
/**
 ** LeetCode 92. 反转链表 II
 ** 方案：方案2（一次遍历，头插法）
 ** 来源：python 参考忠实移植
 */

class ListNode {
  // 定义类型
  val: number; // 值: number;
  next: ListNode | null; // 下一个: ListNode 按位或 null;
  constructor(val?: number, next?: ListNode | null) {
    // constructor(值?: number, 下一个?: ListNode 按位或 null) {
    this.val = val === undefined ? 0 : val; // 把 值 全等于 undefined ? 0 : 值; 写入 值
    this.next = next === undefined ? null : next; // 把 下一个 全等于 undefined ? null : 下一个; 写入 下一个
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
  const arr: number[] = []; // 把 []; 写入 const arr: number[]
  while (head) {
    // 循环，直到不满足「头节点」
    arr.push(head.val); // 把 头节点.值 压入栈/数组尾部
    head = head.next; // 把 头节点.下一个 存入 头节点
  }
  return arr; // 返回 数组
}

function reverseBetween(
  head: ListNode | null,
  left: number,
  right: number,
): ListNode | null {
  // 定义函数/方法 reverseBetween
  const dummy = new ListNode(-1); // 把 new ListNode( 减 1) 存入 哨兵节点
  dummy.next = head; // 把 头节点; 写入 下一个
  let pre = dummy; // 把 哨兵节点 存入 前缀和
  for (let i = 0; i < left - 1; i++) pre = pre.next!; // 让 下标 i 从 0 开始计数，下标 i 小于 左边界 减 1 就继续
  let cur = pre.next!; // 把 前缀和.下一个取反 存入 当前值
  for (let i = 0; i < right - left; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 右边界 减 左边界 就继续
    const nxt = cur.next!; // 把 当前值.下一个取反 存入 nxt
    cur.next = nxt.next; // 把 nxt.下一个; 写入 下一个
    nxt.next = pre.next; // 把 前缀和.下一个; 写入 下一个
    pre.next = nxt; // 把 nxt; 写入 下一个
  }
  return dummy.next; // 返回 哨兵节点.下一个
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function eqArr(a: number[], b: number[]): boolean {
    // 定义函数/方法 eqArr
    if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    return true; // 返回 true
  }
  const cases: { in: [number[], number, number]; want: number[] }[] = [
    { in: [[1, 2, 3, 4, 5], 2, 4], want: [1, 4, 3, 2, 5] },
    { in: [[1, 2, 3], 1, 3], want: [3, 2, 1] },
    { in: [[5], 1, 1], want: [5] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = listToArr(reverseBetween(buildList(c.in[0]), c.in[1], c.in[2]));
    if (!eqArr(got, c.want)) {
      // 若 取反 eqArr(got, 字符.want
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL',
        JSON.stringify(c.in),
        'want',
        JSON.stringify(c.want),
        'got',
        JSON.stringify(got),
      ); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
