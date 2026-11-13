// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134358253
/**
 ** LeetCode 21. 合并两个有序链表
 ** 方案：方案6（忠实翻译 python solution_6___6.py：迭代 + 三元接尾）
 */

class ListNode {
  // 定义类型
  val: number; // 值: number;
  next: ListNode | null; // 下一个: ListNode 按位或 null;
  constructor(val?: number, next?: ListNode | null) {
    // constructor(值?: number, 下一个?: ListNode 按位或 null) {
    this.val = val === undefined ? 0 : val; // 把 (值 全等于 undefined ? 0 : 值); 写入 值
    this.next = next === undefined ? null : next; // 把 (下一个 全等于 undefined ? null : 下一个); 写入 下一个
  }
}

function build(arr: number[]): ListNode | null {
  // 定义函数/方法 build
  const dummy = new ListNode(0); // 把 new ListNode(0) 存入 哨兵节点
  let cur = dummy; // 把 哨兵节点 存入 当前值
  for (const v of arr) {
    // for (const 值 of 数组) {
    cur.next = new ListNode(v); // 把 new ListNode(值); 写入 下一个
    cur = cur.next; // 把 当前值.下一个 存入 当前值
  }
  return dummy.next; // 返回 哨兵节点.下一个
}

function toList(node: ListNode | null): number[] {
  // 定义函数/方法 toList
  const out: number[] = []; // 把 []; 写入 const out: number[]
  while (node) {
    // 循环，直到不满足「节点」
    out.push(node.val); // 把 节点.值 压入栈/数组尾部
    node = node.next; // 把 节点.下一个 存入 节点
  }
  return out; // 返回 out
}

// faithful translation of python solution_6___6.py
function mergeTwoLists(
  list1: ListNode | null,
  list2: ListNode | null,
): ListNode | null {
  // 定义函数/方法 mergeTwoLists
  const res = new ListNode(); // 把 new ListNode() 存入 结果
  let p = res; // 把 结果 存入 节点
  let p1 = list1,
    p2 = list2; // 把 list1, p2 赋值为 list2 存入 p1
  while (p1 && p2) {
    // 循环，直到不满足「p1 且 p2」
    if (p1.val < p2.val) {
      // 若 p1.值 小于 p2.值
      p.next = p1; // 把 p1; 写入 下一个
      p1 = p1.next; // 把 p1.下一个 存入 p1
    } else {
      // 否则
      p.next = p2; // 把 p2; 写入 下一个
      p2 = p2.next; // 把 p2.下一个 存入 p2
    }
    p = p.next; // 把 节点.下一个 存入 节点
  }
  p.next = p1 ? p1 : p2; // 把 p1 ? p1 : p2; 写入 下一个
  return res.next; // 返回 结果.下一个
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const cases: { l1: number[]; l2: number[]; want: number[] }[] = [
    { l1: [1, 2, 4], l2: [1, 3, 4], want: [1, 1, 2, 3, 4, 4] },
    { l1: [], l2: [], want: [] },
    { l1: [], l2: [0], want: [0] },
    { l1: [2], l2: [1], want: [1, 2] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = toList(mergeTwoLists(build(c.l1), build(c.l2))); // 把 toList(mergeTwoLists(build(字符.l1), build(字符.l2))) 存入 got
    if (got.length !== c.want.length || got.some((v, i) => v !== c.want[i])) {
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL mergeTwoLists(' +
          JSON.stringify(c.l1) +
          ',' +
          JSON.stringify(c.l2) +
          ')=' +
          JSON.stringify(got) +
          ' want=' +
          JSON.stringify(c.want),
      ); // 打印输出
    }
  }
  if (fail) {
    throw new Error('FAILED');
  } // 若 fail) { throw new Error(「FAILED」); }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
