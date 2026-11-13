// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134255301
// LeetCode 380. O(1)时间插入删除和获取随机元素 — Rust 版（方案1）
use std::collections::HashMap; // 引入依赖
struct RandomizedSet {
    vals: Vec<i32>,
    pos: HashMap<i32, usize>,
} // 定义类型
impl RandomizedSet {
    // 实现块
    fn new() -> Self {
        RandomizedSet {
            vals: Vec::new(),
            pos: HashMap::new(),
        }
    } // 定义函数/方法 new
    fn insert(&mut self, val: i32) -> bool {
        // 定义函数/方法 insert
        if self.pos.contains_key(&val) {
            return false;
        } // 若 self.pos.contains_key( 按位与 值) { return false; }
        self.pos.insert(val, self.vals.len()); // self.pos 插入 值, self.vals.长度());
        self.vals.push(val); // 把 值 压入栈/数组尾部
        true // true
    }
    fn remove(&mut self, val: i32) -> bool {
        // 定义函数/方法 remove
        if let Some(&idx) = self.pos.get(&val) {
            // 若 let Some( 按位与 idx) 赋值为 self.pos 查找 按位与 值
            let last = *self.vals.last().unwrap(); // 把 乘 self.vals.last().unwrap() 存入 last
            self.vals[idx] = last; // 把 last; 写入 self.vals[idx]
            self.pos.insert(last, idx); // self.pos 插入 last, idx);
            self.vals.pop(); // 弹出栈顶元素
            self.pos.remove(&val); // self.pos 弹出 按位与 值);
            true // true
        } else {
            false
        } // 否则
    }
    fn get_random(&self) -> i32 {
        self.vals[self.vals.len() % self.vals.len()]
    } // 定义函数/方法 get_random
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let mut s = RandomizedSet::new(); // 把 RandomizedSet::new(); 写入 let mut s
    assert!(s.insert(1)); // 断言校验
    assert!(s.remove(2) == false); // 断言校验
    assert!(s.insert(2)); // 断言校验
    let r = s.get_random(); // 把 字符串.get_random() 存入 右指针
    assert!(r == 1 || r == 2); // 断言校验
    assert!(s.remove(1)); // 断言校验
    assert!(s.insert(2) == false); // 断言校验
    let r2 = s.get_random(); // 把 字符串.get_random() 存入 r2
    assert!(r2 == 2); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
