// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385578

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

class CNode {
  val: number;
  prev: CNode | null;
  next: CNode | null;
  constructor(v: number) {
    this.val = v;
    this.prev = null;
    this.next = null;
  }
} // 定义类型
class MyCircularDeque {
  // 定义类型
  head: CNode | null;
  tail: CNode | null;
  capacity: number;
  size: number;
  constructor(k: number) {
    this.head = null;
    this.tail = null;
    this.capacity = k;
    this.size = 0;
  }
  insertFront(v: number): boolean {
    // insertFront(值: number): boolean {
    if (this.isFull()) return false; // 若 this.isFull()，直接返回 false
    const n = new CNode(v); // 把 new CNode(值) 存入 元素个数
    if (this.isEmpty()) {
      this.head = n;
      this.tail = n;
    } // 若 this.isEmpty()) { this.头节点 赋值为 元素个数; this.尾节点 赋值为 元素个数; }
    else {
      n.next = this.head;
      if (this.head) this.head.prev = n;
      this.head = n;
    } // 否则
    this.size++;
    return true; // this.大小 加一 ; return true;
  }
  insertLast(v: number): boolean {
    // insertLast(值: number): boolean {
    if (this.isFull()) return false; // 若 this.isFull()，直接返回 false
    const n = new CNode(v); // 把 new CNode(值) 存入 元素个数
    if (this.isEmpty()) {
      this.head = n;
      this.tail = n;
    } // 若 this.isEmpty()) { this.头节点 赋值为 元素个数; this.尾节点 赋值为 元素个数; }
    else {
      if (this.tail) {
        this.tail.next = n;
        n.prev = this.tail;
      }
      this.tail = n;
    } // 否则
    this.size++;
    return true; // this.大小 加一 ; return true;
  }
  deleteFront(): boolean {
    // deleteFront(): boolean {
    if (this.isEmpty()) return false; // 若 this.isEmpty()，直接返回 false
    if (this.head) {
      this.head = this.head.next;
      if (this.head) this.head.prev = null;
      else this.tail = null;
    }
    this.size--;
    return true; // this.大小 减一 ; return true;
  }
  deleteLast(): boolean {
    // deleteLast(): boolean {
    if (this.isEmpty()) return false; // 若 this.isEmpty()，直接返回 false
    if (this.tail) {
      this.tail = this.tail.prev;
      if (this.tail) this.tail.next = null;
      else this.head = null;
    }
    this.size--;
    return true; // this.大小 减一 ; return true;
  }
  getFront(): number {
    if (this.isEmpty()) return -1;
    return this.head ? this.head.val : -1;
  }
  getRear(): number {
    if (this.isEmpty()) return -1;
    return this.tail ? this.tail.val : -1;
  }
  isEmpty(): boolean {
    return this.size === 0;
  } // 把 等于 0; } 写入 大小
  isFull(): boolean {
    return this.size === this.capacity;
  } // 把 等于 this.capacity; } 写入 大小
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const obj = new MyCircularDeque(3); // 把 new MyCircularDeque(3) 存入 obj
  assertEq(obj.insertLast(1), true, 'i1'); // 断言校验
  assertEq(obj.insertLast(2), true, 'i2'); // 断言校验
  assertEq(obj.insertFront(3), true, 'i3'); // 断言校验
  assertEq(obj.insertFront(4), false, 'i4'); // 断言校验
  assertEq(obj.getRear(), 2, 'rear'); // 断言校验
  assertEq(obj.isFull(), true, 'full'); // 断言校验
  assertEq(obj.deleteLast(), true, 'dl'); // 断言校验
  assertEq(obj.insertFront(4), true, 'i4b'); // 断言校验
  assertEq(obj.getFront(), 4, 'front'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
