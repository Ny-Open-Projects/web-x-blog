// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145238093
// LeetCode 374. 猜数字大小 — Rust 版（方案4：迭代二分）
static mut PICK: i64 = 6; // 把 6; 写入 static mut PICK: i64
fn guess(num: i64) -> i32 {
    // 定义函数/方法 guess
    unsafe {
        if num == PICK {
            0
        } else if num < PICK {
            1
        } else {
            -1
        }
    }
}
fn guess_number(n: i64) -> i64 {
    // 定义函数/方法 guess_number
    let (mut low, mut high) = (1i64, n); // 把 (1i64, 元素个数); 写入 let (mut low, mut high)
    while low <= high {
        // 把 high { 写入 while low <
        let mid = (low + high) / 2; // 把 (low 加 high) 除以 2 存入 中点
        match guess(mid) {
            // 定义函数/方法 guess
            0 => return mid,
            1 => low = mid + 1,
            _ => high = mid - 1,
        }
    }
    -1 // 减 1
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let cases: [(i64, i64); 4] = [(10, 6), (1, 1), (5, 3), (2, 2)];
    for (n, pick) in cases {
        // for (元素个数, pick) in cases {
        unsafe {
            PICK = pick;
        } // 把 pick; } 写入 unsafe { PICK
        assert_eq!(guess_number(n), pick, "n={} pick={}", n, pick); // 断言校验
    }
    println!("PASS"); // 全部用例通过，输出 PASS
}
