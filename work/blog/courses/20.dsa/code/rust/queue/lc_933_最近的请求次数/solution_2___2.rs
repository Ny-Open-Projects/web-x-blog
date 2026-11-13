// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130470370
// LeetCode 933. 最近的请求次数 — Rust 版

// 方案2：front 指针懒删除（不真正移除元素，仅移动队头下标）
struct RecentCounter {
    // 定义类型
    queue: Vec<i32>,
    front: usize,
}

impl RecentCounter {
    // 实现块
    fn new() -> Self {
        // 定义函数/方法 new
        RecentCounter {
            queue: Vec::new(),
            front: 0,
        } // RecentCounter { 队列: Vec::new(), front: 0 }
    }
    fn ping(&mut self, t: i32) -> usize {
        // 定义函数/方法 ping
        self.queue.push(t); // 把 另一字符串 压入栈/数组尾部
        while self.queue[self.front] < t - 3000 {
            // while self.队列[self.front] 小于 另一字符串 减 3000 {
            self.front += 1; // self.front累加 1
        }
        self.queue.len() - self.front // self.队列.长度() 减 self.front
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
