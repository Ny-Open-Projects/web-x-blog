// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/137295891
// LeetCode 460. LFU缓存 — Rust 版（方案1）
#[derive(Clone)]
enum Op460 {
    Put(i32, i32),
    Get(i32),
} // 定义类型
fn lfu_run(ops: Vec<Op460>, cap: usize) -> Vec<i32> {
    // 定义函数/方法 lfu_run
    // 频率最小+最久未用优先：简单 O(n) 模拟
    use std::collections::HashMap; // 引入依赖
    let mut vals: HashMap<i32, i32> = HashMap::new(); // 把 HashMap::new(); 写入 let mut vals: HashMap<i32, i32>
    let mut freq: HashMap<i32, i64> = HashMap::new(); // 把 HashMap::new(); 写入 let mut freq: HashMap<i32, i64>
    let mut stamp: HashMap<i32, i64> = HashMap::new(); // 把 HashMap::new(); 写入 let mut stamp: HashMap<i32, i64>
    let mut clock: i64 = 0; // 把 0; 写入 let mut clock: i64
    let mut out = Vec::new(); // 把 Vec::new(); 写入 let mut out
    for op in ops {
        // 逐个取出 ops 的元素（op）
        clock += 1; // clock累加 1
        match op {
            // 按情况匹配处理
            Op460::Get(k) => {
                if vals.contains_key(&k) {
                    // 若 vals.contains_key( 按位与 下标 k
                    *freq.get_mut(&k).unwrap() += 1;
                    stamp.insert(k, clock); // stamp 插入 下标 k, clock);
                    out.push(*vals.get(&k).unwrap()); // 把 乘 vals 查找 按位与 下标 k 压入栈/数组尾部
                } else {
                    out.push(-1);
                } // 否则
            }
            Op460::Put(k, v) => {
                if vals.contains_key(&k) {
                    // 若 vals.contains_key( 按位与 下标 k
                    vals.insert(k, v); // vals 插入 下标 k, 值);
                    *freq.get_mut(&k).unwrap() += 1;
                    stamp.insert(k, clock); // stamp 插入 下标 k, clock);
                } else {
                    // 否则
                    if cap > 0 && vals.len() == cap {
                        // 若 cap 超过 0 且 vals.长度() 等于 cap
                        let mut evict: Option<i32> = None; // 把 None; 写入 let mut evict: Option<i32>
                        let mut best_f = i64::MAX; // 把 i64::MAX; 写入 let mut best_f
                        let mut best_s = i64::MAX; // 把 i64::MAX; 写入 let mut best_s
                        for key in vals.keys() {
                            // 逐个取出 vals 的元素（key）
                            let f = freq[key]; // 把 频次表[key] 存入 f
                            let s = stamp[key]; // 把 stamp[key] 存入 字符串
                            if f < best_f || (f == best_f && s < best_s) {
                                // 若 f 小于 best_f 或 (f 等于 best_f 且 字符串 小于 best_s
                                best_f = f;
                                best_s = s;
                                evict = Some(*key); // 把 f; best_s 赋值为 字符串; evict 赋值为 Some( 乘 key); 写入 best_f
                            }
                        }
                        if let Some(e) = evict {
                            // 若 let Some(e) 赋值为 evict
                            vals.remove(&e);
                            freq.remove(&e);
                            stamp.remove(&e); // vals 弹出 按位与 e); 频次表 弹出 按位与 e); stamp 弹出 按位与 e);
                        }
                    }
                    if cap > 0 {
                        // 若 cap 超过 0
                        vals.insert(k, v); // vals 插入 下标 k, 值);
                        freq.insert(k, 1); // 频次表 插入 下标 k, 1);
                        stamp.insert(k, clock); // stamp 插入 下标 k, clock);
                    }
                }
            }
        }
    }
    out // out
}
fn main() {
    // 程序入口：跑内嵌自测用例
    // LC 示例：capacity=2, put(1,1), put(2,2), get(1)=1, put(3,3)逐出2, get(2)=-1, get(3)=3, put(4,4)逐出1, get(1)=-1, get(3)=3, get(4)=4
    let ops = vec![
        Op460::Put(1, 1),
        Op460::Put(2, 2),
        Op460::Get(1),
        Op460::Put(3, 3),
        Op460::Get(2),
        Op460::Get(3),
        Op460::Put(4, 4),
        Op460::Get(1),
        Op460::Get(3),
        Op460::Get(4),
    ];
    assert_eq!(lfu_run(ops, 2), vec![1, -1, 3, -1, 3, 4]); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
