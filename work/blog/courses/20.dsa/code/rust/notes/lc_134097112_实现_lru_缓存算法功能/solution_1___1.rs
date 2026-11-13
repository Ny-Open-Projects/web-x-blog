// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134097112
// 实现LRU缓存算法功能 — Rust 版（方案1）
struct NoteLru {
    cap: usize,
    keys: std::collections::VecDeque<i32>,
    vals: std::collections::HashMap<i32, i32>,
} // 定义类型
impl NoteLru {
    // 实现块
    fn new(cap: usize) -> Self {
        NoteLru {
            cap,
            keys: Default::default(),
            vals: Default::default(),
        }
    } // 定义函数/方法 new
    fn get(&mut self, k: i32) -> i32 {
        // 定义函数/方法 get
        if let Some(&v) = self.vals.get(&k) {
            // 若 let Some( 按位与 值) 赋值为 self.vals 查找 按位与 下标 k
            self.keys.retain(|&x| x != k); // 把 下标 k); 写入 self.keys.retain(|&x| x !
            self.keys.push_back(k); // self.keys 追加 下标 k);
            v
        } else {
            -1
        } // 否则
    }
    fn put(&mut self, k: i32, v: i32) {
        // 定义函数/方法 put
        if self.vals.contains_key(&k) {
            // 若 self.vals.contains_key( 按位与 下标 k
            self.keys.retain(|&x| x != k); // 把 下标 k); 写入 self.keys.retain(|&x| x !
        } else if self.keys.len() == self.cap {
            // 否则，若 self.keys.长度() 等于 self.cap
            let old = self.keys.pop_front().unwrap(); // 把 self.keys.pop_front().unwrap() 存入 old
            self.vals.remove(&old); // self.vals 弹出 按位与 old);
        }
        self.keys.push_back(k); // self.keys 追加 下标 k);
        self.vals.insert(k, v); // self.vals 插入 下标 k, 值);
    }
}
fn main() {
    // 程序入口：跑内嵌自测用例
    // TS 笔记语义: cap=2, put(1,1), put(2,2), get(1)=1, put(3,3)逐出1, get(1)=-1, get(3)=3
    let mut c = NoteLru::new(2); // 把 NoteLru::new(2); 写入 let mut c
    c.put(1, 1); // 字符.put(1, 1);
    c.put(2, 2); // 字符.put(2, 2);
    assert_eq!(c.get(1), 1); // 断言校验
    c.put(3, 3); // 字符.put(3, 3);
    assert_eq!(c.get(2), -1); // 断言校验
    c.put(4, 4); // 字符.put(4, 4);
    assert_eq!(c.get(1), -1); // 断言校验
    assert_eq!(c.get(3), 3); // 断言校验
    assert_eq!(c.get(4), 4); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
