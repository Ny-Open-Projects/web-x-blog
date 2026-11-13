// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145338856
// LeetCode 1472. 设计浏览器历史记录 — Rust 版（方案1）
struct BrowserHistory {
    history: Vec<String>,
    cur: usize,
} // 定义类型
impl BrowserHistory {
    // 实现块
    fn new(homepage: &str) -> Self {
        BrowserHistory {
            history: vec![homepage.to_string()],
            cur: 0,
        }
    } // 定义函数/方法 new
    fn visit(&mut self, url: &str) {
        // 定义函数/方法 visit
        self.history.truncate(self.cur + 1); // self.history.truncate(self.当前值 加 1);
        self.history.push(url.to_string()); // 把 url.to_string( 压入栈/数组尾部
        self.cur = self.history.len() - 1; // 把 self.history.长度() 减 1; 写入 当前值
    }
    fn back(&mut self, steps: i32) -> String {
        // 定义函数/方法 back
        self.cur = self.cur.saturating_sub(steps as usize); // 把 self.当前值.saturating_sub(steps as usize); 写入 当前值
        self.history[self.cur].clone() // self.history[self.当前值].clone()
    }
    fn forward(&mut self, steps: i32) -> String {
        // 定义函数/方法 forward
        self.cur = (self.cur + steps as usize).min(self.history.len() - 1);
        self.history[self.cur].clone() // self.history[self.当前值].clone()
    }
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let mut b = BrowserHistory::new("leetcode.com"); // 把 BrowserHistory::new(「leetcode.com」); 写入 let mut b
    b.visit("google.com"); // b.visit(「google.com」);
    b.visit("facebook.com"); // b.visit(「facebook.com」);
    b.visit("youtube.com"); // b.visit(「youtube.com」);
    assert_eq!(b.back(1), "facebook.com".to_string()); // 断言校验
    assert_eq!(b.back(1), "google.com".to_string()); // 断言校验
    assert_eq!(b.forward(1), "facebook.com".to_string()); // 断言校验
    b.visit("linkedin.com"); // b.visit(「linkedin.com」);
    assert_eq!(b.forward(2), "linkedin.com".to_string()); // 断言校验
    assert_eq!(b.back(2), "google.com".to_string()); // 断言校验
    assert_eq!(b.back(7), "leetcode.com".to_string()); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
