// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135749595
// LeetCode 295. 数据流的中位数 — Rust 版（方案1）
use std::collections::BinaryHeap; // 引入依赖
struct MedianFinder {
    max_h: BinaryHeap<i32>,
    min_h: std::collections::BinaryHeap<std::cmp::Reverse<i32>>,
} // 定义类型
impl MedianFinder {
    // 实现块
    fn new() -> Self {
        MedianFinder {
            max_h: BinaryHeap::new(),
            min_h: BinaryHeap::new(),
        }
    } // 定义函数/方法 new
    fn add_num(&mut self, num: i32) {
        // 定义函数/方法 add_num
        if self.max_h.is_empty() || num <= *self.max_h.peek().unwrap() {
            // 若 self.max_h 是否为空 或 num 不超过 乘 self.max_h.peek().unwrap(
            self.max_h.push(num); // 把 num 压入栈/数组尾部
        } else {
            // 否则
            self.min_h.push(std::cmp::Reverse(num)); // 把 std::cmp::Reverse(num 压入栈/数组尾部
        }
        // 平衡：max_h 与 min_h 最多差 1，且 max_h 可以多 1
        if self.max_h.len() > self.min_h.len() + 1 {
            // 若 self.max_h.长度() 超过 self.min_h.长度() 加 1
            let v = self.max_h.pop().unwrap(); // 把 self.max_h 弹出 ).unwrap() 存入 值
            self.min_h.push(std::cmp::Reverse(v)); // 把 std::cmp::Reverse(值 压入栈/数组尾部
        } else if self.min_h.len() > self.max_h.len() {
            // 否则，若 self.min_h.长度() 超过 self.max_h.长度(
            let std::cmp::Reverse(v) = self.min_h.pop().unwrap(); // 弹出栈顶元素
            self.max_h.push(v); // 把 值 压入栈/数组尾部
        }
    }
    fn find_median(&self) -> f64 {
        // 定义函数/方法 find_median
        if self.max_h.len() == self.min_h.len() {
            // 若 self.max_h.长度() 等于 self.min_h.长度(
            (*self.max_h.peek().unwrap() as f64 + self.min_h.peek().unwrap().0 as f64) / 2.0
        } else {
            // 否则
            *self.max_h.peek().unwrap() as f64
        }
    }
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let mut mf = MedianFinder::new(); // 把 MedianFinder::new(); 写入 let mut mf
    for x in [1, 2, 3, 4, 5] {
        mf.add_num(x);
    } // for x in [1, 2, 3, 4, 5] { mf.add_num(x); }
    assert_eq!(mf.find_median(), 3.0); // 断言校验
    let mut mf2 = MedianFinder::new(); // 把 MedianFinder::new(); 写入 let mut mf2
    mf2.add_num(1); // mf2.add_num(1);
    mf2.add_num(2); // mf2.add_num(2);
    assert_eq!(mf2.find_median(), 1.5); // 断言校验
    mf2.add_num(3); // mf2.add_num(3);
    assert_eq!(mf2.find_median(), 2.0); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
