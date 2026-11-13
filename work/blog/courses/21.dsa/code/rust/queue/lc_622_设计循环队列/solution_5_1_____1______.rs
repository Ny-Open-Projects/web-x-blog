// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130471048
// LeetCode 622. 设计循环队列 — Rust 版

// 方案5：数组 + front/rear/size 循环队列
struct MyCircularQueue {
    // 定义类型
    capacity: usize,
    data: Vec<i32>,
    front: usize,
    rear: usize,
    size: usize,
}

impl MyCircularQueue {
    // 实现块
    fn new(k: usize) -> Self {
        // 定义函数/方法 new
        MyCircularQueue {
            // MyCircularQueue {
            capacity: k,
            data: vec![0; k],
            front: 0,
            rear: 0,
            size: 0,
        }
    }
    fn en_queue(&mut self, value: i32) -> bool {
        // 定义函数/方法 en_queue
        if self.is_full() {
            // 若 self.is_full(
            return false; // 返回 false
        }
        self.data[self.rear] = value; // 把 value; 写入 self.data[self.rear]
        self.rear = (self.rear + 1) % self.capacity; // 把 (self.rear 加 1) 对…取模 self.capacity; 写入 self.rear
        self.size += 1; // self.size累加 1
        true // true
    }
    fn de_queue(&mut self) -> bool {
        // 定义函数/方法 de_queue
        if self.is_empty() {
            // 若 self.is_empty(
            return false; // 返回 false
        }
        self.front = (self.front + 1) % self.capacity; // 把 (self.front 加 1) 对…取模 self.capacity; 写入 self.front
        self.size -= 1; // self.size累减 1
        true // true
    }
    #[allow(dead_code)]
    fn front(&self) -> i32 {
        // 定义函数/方法 front
        if self.is_empty() {
            // 若 self.is_empty(
            return -1; // 返回 减 1
        }
        self.data[self.front] // self.data[self.front]
    }
    fn rear(&self) -> i32 {
        // 定义函数/方法 rear
        if self.is_empty() {
            // 若 self.is_empty(
            return -1; // 返回 减 1
        }
        // rear + capacity - 1 避免 usize 下溢（等价 TS 的 (rear - 1 + capacity) % capacity）
        self.data[(self.rear + self.capacity - 1) % self.capacity]
    }
    fn is_empty(&self) -> bool {
        // 定义判定函数 is_empty
        self.size == 0 // 把 赋值为 0 写入 大小
    }
    fn is_full(&self) -> bool {
        // 定义判定函数 is_full
        self.size == self.capacity // 把 赋值为 self.capacity 写入 大小
    }
}

fn main() {
    // 程序入口：跑内嵌自测用例
    // 与 TS 事实源内嵌用例一致：[true,true,true,false,3,true,true,true,4]
    // 布尔结果用 1/0 表示
    let mut q = MyCircularQueue::new(3); // 把 MyCircularQueue::new(3); 写入 let mut q
    let got: Vec<i32> = vec![
        q.en_queue(1) as i32,
        q.en_queue(2) as i32,
        q.en_queue(3) as i32,
        q.en_queue(4) as i32,
        q.rear(),
        q.is_full() as i32,
        q.de_queue() as i32,
        q.en_queue(4) as i32,
        q.rear(),
    ];
    let want: Vec<i32> = vec![1, 1, 1, 0, 3, 1, 1, 1, 4]; // 把 vec取反 [1, 1, 1, 0, 3, 1, 1, 1, 4]; 写入 let want: Vec<i32>
    for i in 0..want.len() {
        // 逐个取出 0 的元素（下标 i）
        assert!(
            got[i] == want[i],
            "FAIL idx {} got {} want {}",
            i,
            got[i],
            want[i]
        ); // 断言校验
    }
    println!("PASS"); // 全部用例通过，输出 PASS
}
