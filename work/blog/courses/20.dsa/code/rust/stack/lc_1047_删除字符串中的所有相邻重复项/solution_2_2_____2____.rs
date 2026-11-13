// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145295630
// LeetCode 1047. 删除字符串中的所有相邻重复项 — Rust 版（方案2）
fn remove_duplicates(s: String) -> String {
    // 定义函数/方法 remove_duplicates
    let mut st: Vec<char> = Vec::new(); // 把 Vec::new(); 写入 let mut st: Vec<char>
    for c in s.chars() {
        // 逐个取出 字符串 的元素（字符）
        if st.last() == Some(&c) {
            st.pop();
        } else {
            st.push(c);
        }
    }
    st.into_iter().collect() // st.into_iter().collect()
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(remove_duplicates("abbaca".into()), "ca"); // 断言校验
    assert_eq!(remove_duplicates("azxxzy".into()), "ay"); // 断言校验
    assert_eq!(remove_duplicates("".into()), ""); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
