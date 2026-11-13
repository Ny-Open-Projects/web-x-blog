// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134368624
// LeetCode 71. 简化路径 — Rust 版（方案2）
fn simplify_path(path: String) -> String {
    // 定义函数/方法 simplify_path
    let mut st: Vec<&str> = Vec::new(); // 把 Vec::new(); 写入 let mut st: Vec<&str>
    for part in path.split('/') {
        // 逐个取出 当前路径 的元素（part）
        match part {
            // 按情况匹配处理
            "" | "." => {}
            ".." => {
                st.pop();
            }
            _ => st.push(part),
        }
    }
    format!("/{}", st.join("/")) // 拼接为字符串
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(simplify_path("/home/".into()), "/home"); // 断言校验
    assert_eq!(simplify_path("/../".into()), "/"); // 断言校验
    assert_eq!(simplify_path("/home//foo/".into()), "/home/foo"); // 断言校验
    assert_eq!(simplify_path("/a/./b/../../c/".into()), "/c"); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
