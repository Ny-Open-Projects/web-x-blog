// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134537871
// LeetCode 146. LRU缓存 — Rust 版（方案2）
#[derive(Clone)]
enum Op {
    Put(i32, i32),
    Get(i32),
} // 定义类型
struct LruSim {
    cap: usize,
    keys: std::collections::VecDeque<i32>,
    vals: std::collections::HashMap<i32, i32>,
} // 定义类型
impl LruSim {
    // 实现块
    fn new(cap: usize) -> Self {
        LruSim {
            cap,
            keys: Default::default(),
            vals: Default::default(),
        }
    } // 定义函数/方法 new
    fn get(&mut self, k: i32) -> i32 {
        // 定义函数/方法 get
        if self.vals.contains_key(&k) {
            // 若 self.vals.contains_key( 按位与 下标 k
            self.keys.retain(|&x| x != k); // 把 下标 k); 写入 self.keys.retain(|&x| x !
            self.keys.push_back(k); // self.keys 追加 下标 k);
            *self.vals.get(&k).unwrap()
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
fn run_ops(ops: Vec<Op>, cap: usize) -> Vec<i32> {
    // 定义函数/方法 run_ops
    let mut lru = LruSim::new(cap); // 把 LruSim::new(cap); 写入 let mut lru
    let mut out = Vec::new(); // 把 Vec::new(); 写入 let mut out
    for op in ops {
        // 逐个取出 ops 的元素（op）
        match op {
            // 按情况匹配处理
            Op::Put(k, v) => lru.put(k, v),
            Op::Get(k) => out.push(lru.get(k)),
        }
    }
    out // out
}
fn main() {
    // 程序入口：跑内嵌自测用例
    // LC 官方示例：capacity=2, put(1,1), put(2,2), get(1)=1, put(3,3)逐出2, get(2)=-1, put(4,4)逐出1, get(1)=-1, get(3)=3, get(4)=4
    let ops = vec![
        Op::Put(1, 1),
        Op::Put(2, 2),
        Op::Get(1),
        Op::Put(3, 3),
        Op::Get(2),
        Op::Put(4, 4),
        Op::Get(1),
        Op::Get(3),
        Op::Get(4),
    ];
    assert_eq!(run_ops(ops, 2), vec![1, -1, -1, 3, 4]); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
