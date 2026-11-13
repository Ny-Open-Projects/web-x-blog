// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134172583
// 数据结构与算法之排序: 计数排序 — Rust 版（方案6）
fn count_sort(nums: Vec<i32>) -> Vec<i32> {
    // 定义函数/方法 count_sort
    if nums.is_empty() {
        return nums;
    } // 若 数组 是否为空 { return 数组; }
    let (mut mx, mut mn) = (nums[0], nums[0]); // 把 (数组[0], 数组[0]); 写入 let (mut mx, mut mn)
    for &v in &nums {
        if v > mx {
            mx = v;
        }
        if v < mn {
            mn = v;
        }
    }
    let range = (mx - mn + 1) as usize; // 把 (mx 减 mn 加 1) as usize 存入 range
    let mut count = vec![0i32; range]; // 把 vec取反 [0i32; range]; 写入 let mut count
    let mut output = vec![0i32; nums.len()]; // 把 vec取反 [0i32; 数组.长度()]; 写入 let mut output
    for &v in &nums {
        count[(v - mn) as usize] += 1;
    } // 把 1; } 写入 for &v in &nums { count[(v - mn) as usize] +
    for i in 1..range {
        count[i] += count[i - 1];
    } // 逐个取出 1 的元素（下标 i）
    for i in (0..nums.len()).rev() {
        // for 下标 i in (0..数组.长度()).rev() {
        let idx = (nums[i] - mn) as usize; // 把 (数组[下标 i] 减 mn) as usize 存入 idx
        output[(count[idx] - 1) as usize] = nums[i]; // 把 数组[下标 i]; 写入 output[(count[idx] - 1) as usize]
        count[idx] -= 1; // count[idx]累减 1
    }
    output // 输出
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(count_sort(vec![5, 3, 8, 3, 1]), vec![1, 3, 3, 5, 8]); // 断言校验
    let big = vec![
        102, 103, 108, 107, 101, 102, 102, 102, 107, 103, 109, 108, 102, 101, 104, 102, 104, 106,
        109, 102,
    ];
    let got = count_sort(big); // 把 count_sort(big) 存入 got
    for i in 1..got.len() {
        assert!(got[i - 1] <= got[i]);
    } // 逐个取出 1 的元素（下标 i）
    assert_eq!(got.len(), 20); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
