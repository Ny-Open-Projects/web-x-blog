// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145634738
// LeetCode 1797. 设计一个验证系统 — Rust 版（方案1）
use std::collections::HashMap; // 引入依赖
struct AuthenticationManager {
    ttl: i64,
    expires_at: HashMap<String, i64>,
} // 定义类型
impl AuthenticationManager {
    // 实现块
    fn new(time_to_live: i64) -> Self {
        AuthenticationManager {
            ttl: time_to_live,
            expires_at: HashMap::new(),
        }
    } // 定义函数/方法 new
    fn generate(&mut self, token_id: &str, current_time: i64) {
        self.expires_at
            .insert(token_id.to_string(), current_time + self.ttl);
    } // 定义函数/方法 generate
    fn renew(&mut self, token_id: &str, current_time: i64) -> usize {
        // 定义函数/方法 renew
        if let Some(&exp) = self.expires_at.get(token_id) {
            // 若 let Some( 按位与 exp) 赋值为 self.expires_at 查找 token_id
            if exp > current_time {
                // 若 exp 超过 current_time
                self.expires_at
                    .insert(token_id.to_string(), current_time + self.ttl);
            }
        }
        self.count_valid_tokens(current_time) // self.count_valid_tokens(current_time)
    }
    fn count_valid_tokens(&self, current_time: i64) -> usize {
        // 定义函数/方法 count_valid_tokens
        self.expires_at
            .values()
            .filter(|&&e| e > current_time)
            .count()
    }
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let mut auth = AuthenticationManager::new(5); // 把 AuthenticationManager::new(5); 写入 let mut auth
    auth.generate("aaa", 1); // auth.generate(「aaa」, 1);
    assert_eq!(auth.count_valid_tokens(3), 1); // 断言校验
    assert_eq!(auth.renew("aaa", 4), 1); // 断言校验
    assert_eq!(auth.count_valid_tokens(6), 1); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
