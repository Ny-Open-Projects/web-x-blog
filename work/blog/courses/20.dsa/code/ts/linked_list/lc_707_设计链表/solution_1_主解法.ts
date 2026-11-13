// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145347892

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

class DNode {
  val: number;
  prev: DNode | null;
  next: DNode | null;
  constructor(val: number) {
    this.val = val;
    this.prev = null;
    this.next = null;
  }
} // 定义类型
class MyLinkedList {
  // 定义类型
  head: DNode | null;
  tail: DNode | null;
  size: number; // 头节点: DNode 按位或 null; 尾节点: DNode 按位或 null; 大小: number;
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  } // 把 null; this.尾节点 赋值为 null; this.大小 赋值为 0; } 写入 头节点
  get(index: number): number {
    if (index < 0 || index >= this.size) return -1;
    let curr = this.head;
    for (let i = 0; i < index; i++) curr = curr!.next;
    return curr!.val;
  }
  addAtHead(val: number): void {
    const n = new DNode(val);
    n.next = this.head;
    if (this.head) this.head.prev = n;
    else this.tail = n;
    this.head = n;
    this.size++;
  }
  addAtTail(val: number): void {
    const n = new DNode(val);
    if (this.tail) {
      this.tail.next = n;
      n.prev = this.tail;
    } else this.head = n;
    this.tail = n;
    this.size++;
  }
  addAtIndex(index: number, val: number): void {
    // addAtIndex(index: number, 值: number): void {
    if (index < 0 || index > this.size) return; // 若 index 小于 0 或 index 超过 this.大小) return;
    if (index === 0)
      this.addAtHead(val); // 若 index 全等于 0) this.addAtHead(值);
    else if (index === this.size)
      this.addAtTail(val); // 否则，若 index 全等于 this.大小) this.addAtTail(值);
    else {
      let curr = this.head;
      for (let i = 0; i < index; i++) curr = curr!.next;
      const n = new DNode(val);
      n.prev = curr!.prev;
      n.next = curr;
      curr!.prev!.next = n;
      curr!.prev = n;
      this.size++;
    } // 否则
  }
  deleteAtIndex(index: number): void {
    // deleteAtIndex(index: number): void {
    if (index < 0 || index >= this.size) return; // 若 index 小于 0 或 index 不低于 this.大小) return;
    if (index === 0) {
      this.head = this.head!.next;
      if (this.head) this.head.prev = null;
      else this.tail = null;
    } else if (index === this.size - 1) {
      this.tail = this.tail!.prev;
      if (this.tail) this.tail.next = null;
      else this.head = null;
    } else {
      let curr = this.head;
      for (let i = 0; i < index; i++) curr = curr!.next;
      curr!.prev!.next = curr.next;
      curr!.next!.prev = curr.prev;
    } // 否则
    this.size--; // this.大小 减一 ;
  }
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const obj = new MyLinkedList(); // 把 new MyLinkedList() 存入 obj
  obj.addAtHead(1);
  obj.addAtTail(3);
  obj.addAtIndex(1, 2); // obj.addAtHead(1); obj.addAtTail(3); obj.addAtIndex(1, 2);
  assertEq(obj.get(1), 2, 'g1'); // 断言校验
  assertEq(obj.get(0), 1, 'g0'); // 断言校验
  assertEq(obj.get(2), 3, 'g2'); // 断言校验
  obj.deleteAtIndex(1); // obj.deleteAtIndex(1);
  assertEq(obj.get(1), 3, 'g1b'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
