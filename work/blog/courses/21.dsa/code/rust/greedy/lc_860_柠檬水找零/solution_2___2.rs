// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135167617
// LeetCode 860. 柠檬水找零 — Rust 版（方案2）
fn lemonade_change(bills: Vec<i32>) -> bool {
    // 定义函数/方法 lemonade_change
    let (mut f5, mut f10) = (0i32, 0i32); // 把 (0i32, 0i32); 写入 let (mut f5, mut f10)
    for b in bills {
        // 逐个取出 bills 的元素（b）
        if b == 5 {
            f5 += 1;
        }
        // 若 b 等于 5 { f5 累加 1; }
        else if b == 10 {
            f10 += 1;
            f5 -= 1;
        }
        // 否则，若 b 等于 10 { f10 累加 1; f5 累减 1; }
        else {
            // 否则
            if f10 > 0 {
                f10 -= 1;
                f5 -= 1;
            }
            // 若 f10 超过 0 { f10 累减 1; f5 累减 1; }
            else {
                f5 -= 3;
            } // 否则
        }
        if f5 < 0 {
            return false;
        } // 若 f5 小于 0 { return false; }
    }
    true // true
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert!(lemonade_change(vec![5, 5, 5, 10, 20])); // 断言校验
    assert!(!lemonade_change(vec![5, 5, 10, 10, 20])); // 断言校验
    assert!(lemonade_change(vec![5, 5, 5, 5, 20])); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
