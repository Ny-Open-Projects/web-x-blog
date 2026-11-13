// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107450699
// 计算思维之谁做的好事 — Rust 版（方案2）
fn find_good_man() -> char {
    // 定义函数/方法 find_good_man
    // 谁做的好事: 甲乙丙丁四人中恰1人做好事。陈述: 甲说不是我; 乙说是C; 丙说是D; 丁说C胡说。3人说真话
    for thisman in ['A', 'B', 'C', 'D'] {
        // for thisman in ['A', 'B', 'C', 'D'] {
        let truth_count = (thisman != 'A') as i32  // 把 (thisman 不等于 'A') as i32 存入 truth_count
            + (thisman == 'C') as i32  // 把 赋值为 'C') as i32 写入 + (thisman
            + (thisman == 'D') as i32  // 把 赋值为 'D') as i32 写入 + (thisman
            + (thisman != 'D') as i32; // 把 'D') as i32; 写入 + (thisman !
        if truth_count == 3 {
            return thisman;
        } // 若 truth_count 等于 3 { return thisman; }
    }
    '?' // '?'
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(find_good_man(), 'C'); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
