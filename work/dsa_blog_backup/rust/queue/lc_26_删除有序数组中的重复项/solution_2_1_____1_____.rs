// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114454
// LeetCode 26. 删除有序数组中的重复项 — Rust 版

// 方案2：快慢指针 —— fast 扫描，slow 指向已去重区间末尾
fn remove_duplicates(nums: &mut [i32]) -> usize {
    // 定义函数/方法 remove_duplicates
    if nums.is_empty() {
        // 若 数组.is_empty(
        return 0; // 返回 0
    }
    let mut slow = 0usize; // 把 0usize; 写入 let mut slow
    for fast in 1..nums.len() {
        // 逐个取出 1 的元素（快指针）
        if nums[fast] != nums[slow] {
            // 若 数组[快指针] 不等于 数组[慢指针]
            slow += 1; // 慢指针累加 1
            nums[slow] = nums[fast]; // 把 数组[快指针]; 写入 nums[slow]
        }
    }
    slow + 1 // 慢指针 加 1
}

fn eq_arr(a: &[i32], b: &[i32]) -> bool {
    // 定义函数/方法 eq_arr
    if a.len() != b.len() {
        // 若 数组.长度() 不等于 b.长度(
        return false; // 返回 false
    }
    for i in 0..a.len() {
        // 逐个取出 0 的元素（下标 i）
        if a[i] != b[i] {
            // 若 数组[下标 i] 不等于 b[下标 i]
            return false; // 返回 false
        }
    }
    true // true
}

fn main() {
    // 程序入口：跑内嵌自测用例
    // 与 TS 事实源内嵌用例一致
    let cases: Vec<(Vec<i32>, usize, Vec<i32>)> = vec![
        (vec![1, 1, 2], 2, vec![1, 2]),
        (vec![1, 2, 3], 3, vec![1, 2, 3]),
        (vec![], 0, vec![]),
    ];
    for (input, want_k, want_pre) in cases {
        // for (input, want_k, want_pre) in cases {
        let mut nums = input.clone(); // 把 input.clone(); 写入 let mut nums
        let got = remove_duplicates(&mut nums); // 把 remove_duplicates( 按位与 mut 数组) 存入 got
        let prefix: Vec<i32> = nums[..got].to_vec(); // 把 数组[..got].to_vec(); 写入 let prefix: Vec<i32>
        assert!(
            got == want_k && eq_arr(&prefix, &want_pre),
            "FAIL remove_duplicates({:?}) k={} prefix={:?}",
            input,
            got,
            prefix // prefix
        );
    }
    println!("PASS"); // 全部用例通过，输出 PASS
}
