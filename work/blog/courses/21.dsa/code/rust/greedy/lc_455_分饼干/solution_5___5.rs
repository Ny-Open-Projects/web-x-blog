// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135096603
// LeetCode 455. 分发饼干 — Rust 版（方案5）
fn find_content_children(mut g: Vec<i32>, mut s: Vec<i32>) -> i32 {
    // 定义函数/方法 find_content_children
    g.sort(); // 排序
    s.sort(); // 排序
    let (mut child, mut cookie) = (0usize, 0usize); // 把 (0usize, 0usize); 写入 let (mut child, mut cookie)
    while child < g.len() && cookie < s.len() {
        // while 子节点 小于 g.长度() 且 cookie 小于 字符串.长度() {
        if s[cookie] >= g[child] {
            child += 1;
        } // 若 字符串[cookie] 不低于 g[子节点] { 子节点 累加 1; }
        cookie += 1; // cookie累加 1
    }
    child as i32 // 子节点 as i32
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(find_content_children(vec![1, 2, 3], vec![1, 1]), 1); // 断言校验
    assert_eq!(find_content_children(vec![1, 2], vec![1, 2, 3]), 2); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
