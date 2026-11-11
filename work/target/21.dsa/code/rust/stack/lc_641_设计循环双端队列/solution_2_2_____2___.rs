// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145361774
// LeetCode 641. 设计循环双端队列 — Rust 版（方案2）
struct MyCircularDeque {
    data: Vec<i32>,
    head: usize,
    tail: usize,
    cap: usize,
    size: usize,
} // 定义类型
impl MyCircularDeque {
    // 实现块
    fn new(k: i32) -> Self {
        MyCircularDeque {
            data: vec![0; k as usize + 1],
            head: 0,
            tail: 0,
            cap: k as usize + 1,
            size: 0,
        }
    } // 定义函数/方法 new
    fn capacity(&self) -> usize {
        self.cap - 1
    } // 定义函数/方法 capacity
    fn insert_front(&mut self, v: i32) -> bool {
        // 定义函数/方法 insert_front
        if self.size == self.cap - 1 {
            return false;
        } // 若 self.大小 等于 self.cap 减 1 { return false; }
        self.head = (self.head + self.cap - 1) % self.cap; // 把 (self.头节点 加 self.cap 减 1) 对…取模 self.cap; 写入 头节点
        self.data[self.head] = v; // 把 值; 写入 self.data[self.head]
        self.size += 1; // self.size累加 1
        true // true
    }
    fn insert_last(&mut self, v: i32) -> bool {
        // 定义函数/方法 insert_last
        if self.size == self.cap - 1 {
            return false;
        } // 若 self.大小 等于 self.cap 减 1 { return false; }
        self.data[self.tail] = v; // 把 值; 写入 self.data[self.tail]
        self.tail = (self.tail + 1) % self.cap; // 把 (self.尾节点 加 1) 对…取模 self.cap; 写入 尾节点
        self.size += 1; // self.size累加 1
        true // true
    }
    fn delete_front(&mut self) -> bool {
        // 定义函数/方法 delete_front
        if self.size == 0 {
            return false;
        } // 若 self.大小 等于 0 { return false; }
        self.head = (self.head + 1) % self.cap; // 把 (self.头节点 加 1) 对…取模 self.cap; 写入 头节点
        self.size -= 1; // self.size累减 1
        true // true
    }
    fn delete_last(&mut self) -> bool {
        // 定义函数/方法 delete_last
        if self.size == 0 {
            return false;
        } // 若 self.大小 等于 0 { return false; }
        self.tail = (self.tail + self.cap - 1) % self.cap; // 把 (self.尾节点 加 self.cap 减 1) 对…取模 self.cap; 写入 尾节点
        self.size -= 1; // self.size累减 1
        true // true
    }
    fn get_front(&self) -> i32 {
        if self.size == 0 {
            -1
        } else {
            self.data[self.head]
        }
    } // 定义函数/方法 get_front
    fn get_rear(&self) -> i32 {
        if self.size == 0 {
            -1
        } else {
            self.data[(self.tail + self.cap - 1) % self.cap]
        }
    } // 定义函数/方法 get_rear
    fn is_empty(&self) -> bool {
        self.size == 0
    } // 定义判定函数 is_empty
    fn is_full(&self) -> bool {
        self.size == self.cap - 1
    } // 定义判定函数 is_full
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let mut d = MyCircularDeque::new(3); // 把 MyCircularDeque::new(3); 写入 let mut d
    assert!(d.insert_last(1)); // 断言校验
    assert!(d.insert_last(2)); // 断言校验
    assert!(d.insert_front(3)); // 断言校验
    assert!(!d.insert_front(4)); // 断言校验
    assert_eq!(d.get_rear(), 2); // 断言校验
    assert!(d.is_full()); // 断言校验
    assert!(d.delete_last()); // 断言校验
    assert!(d.insert_front(4)); // 断言校验
    assert_eq!(d.get_front(), 4); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
