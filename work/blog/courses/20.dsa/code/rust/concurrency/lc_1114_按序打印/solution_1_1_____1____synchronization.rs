// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385760
// LeetCode 1114. 按序打印 — Rust 版（方案1）
use std::sync::{Arc, Condvar, Mutex}; // 引入依赖
struct Foo {
    // 定义类型
    step: Mutex<u32>,
    cv: Condvar,
}
impl Foo {
    // 实现块
    fn new() -> Self {
        Foo {
            step: Mutex::new(1),
            cv: Condvar::new(),
        }
    } // 定义函数/方法 new
    fn first(&self, out: &mut String) {
        // 定义函数/方法 first
        out.push_str("first"); // out.push_str(「first」);
        let mut s = self.step.lock().unwrap(); // 把 self.步数.lock().unwrap(); 写入 let mut s
        *s = 2;
        self.cv.notify_all(); // self.cv.notify_all();
    }
    fn second(&self, out: &mut String) {
        // 定义函数/方法 second
        let mut s = self.step.lock().unwrap(); // 把 self.步数.lock().unwrap(); 写入 let mut s
        while *s < 2 {
            s = self.cv.wait(s).unwrap();
        } // 把 self.cv.wait(字符串).unwrap(); } 写入 while *s < 2 { s
        out.push_str("second"); // out.push_str(「second」);
        *s = 3;
        self.cv.notify_all(); // self.cv.notify_all();
    }
    fn third(&self, out: &mut String) {
        // 定义函数/方法 third
        let mut s = self.step.lock().unwrap(); // 把 self.步数.lock().unwrap(); 写入 let mut s
        while *s < 3 {
            s = self.cv.wait(s).unwrap();
        } // 把 self.cv.wait(字符串).unwrap(); } 写入 while *s < 3 { s
        out.push_str("third"); // out.push_str(「third」);
    }
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let foo = Foo::new(); // 把 Foo::new() 存入 foo
    let mut out = String::new(); // 把 String::new(); 写入 let mut out
    foo.first(&mut out); // foo.first( 按位与 mut out);
    foo.second(&mut out); // foo.second( 按位与 mut out);
    foo.third(&mut out); // foo.third( 按位与 mut out);
    assert_eq!(out, "firstsecondthird"); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
