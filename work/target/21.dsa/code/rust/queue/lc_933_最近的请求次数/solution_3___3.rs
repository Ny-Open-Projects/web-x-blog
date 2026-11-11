// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130470370
// LeetCode 933. 最近的请求次数 — Rust 版

// 方案3：push + 真出队（等价 TS 数组 shift）
use std::collections::VecDeque; // 引入依赖

struct RecentCounter {
    // 定义类型
    q: VecDeque<i32>,
}

impl RecentCounter {
    // 实现块
    fn new() -> Self {
        // 定义函数/方法 new
        RecentCounter { q: VecDeque::new() } // RecentCounter { 节点: VecDeque::new() }
    }
    fn ping(&mut self, t: i32) -> usize {
        // 定义函数/方法 ping
        self.q.push_back(t); // self.节点 追加 另一字符串);
        while let Some(&f) = self.q.front() {
            // 边取边处理，取空即停
            if f < t - 3000 {
                // 若 f 小于 另一字符串 减 3000
                self.q.pop_front(); // self.节点.pop_front();
            } else {
                // 否则
                break; // 跳出循环
            }
        }
        self.q.len() // self.节点.长度()
    }
}

fn main() {
    // 程序入口：跑内嵌自测用例
    // 与 TS 事实源内嵌用例一致
    let mut c = RecentCounter::new(); // 把 RecentCounter::new(); 写入 let mut c
    let got = [c.ping(1), c.ping(100), c.ping(3001), c.ping(3002)];
    let want = [1usize, 2, 3, 3]; // 把 [1usize, 2, 3, 3] 存入 want
    for i in 0..got.len() {
        // 逐个取出 0 的元素（下标 i）
        assert!(
            got[i] == want[i],
            "FAIL case {} got {} want {}",
            i,
            got[i],
            want[i]
        ); // 断言校验
    }
    println!("PASS"); // 全部用例通过，输出 PASS
}
