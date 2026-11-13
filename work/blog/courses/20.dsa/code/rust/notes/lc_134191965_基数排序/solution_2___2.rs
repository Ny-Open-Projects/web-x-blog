// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134191965
// 数据结构与算法之排序: 基数排序 — Rust 版（方案2）
fn radix_sort(nums: Vec<i32>) -> Vec<i32> {
    // 定义函数/方法 radix_sort
    if nums.is_empty() {
        return nums;
    } // 若 数组 是否为空 { return 数组; }
    let (mut mn, mut mx) = (nums[0], nums[0]); // 把 (数组[0], 数组[0]); 写入 let (mut mn, mut mx)
    for &v in &nums {
        if v < mn {
            mn = v;
        }
        if v > mx {
            mx = v;
        }
    }
    let offset = if mn < 0 { -mn } else { 0 }; // 把 if mn 小于 0 { 减 mn } else { 0 } 存入 offset
    let mut adj: Vec<i64> = nums.iter().map(|&x| (x + offset) as i64).collect();
    let mut max_adj: i64 = adj[0]; // 把 邻接表[0]; 写入 let mut max_adj: i64
    for &x in &adj {
        if x > max_adj {
            max_adj = x;
        }
    } // 把 x; } } 写入 for &x in &adj { if x > max_adj { max_adj
    let mut radix: i64 = 1; // 把 1; 写入 let mut radix: i64
    let mut tmp = vec![0i64; adj.len()]; // 把 vec取反 [0i64; 邻接表.长度()]; 写入 let mut tmp
    while max_adj >= radix {
        // 把 radix { 写入 while max_adj >
        let mut bucket = [0i64; 10]; // 把 [0i64; 10]; 写入 let mut bucket
        for &x in &adj {
            bucket[((x / radix) % 10) as usize] += 1;
        }
        for i in 1..10 {
            bucket[i] += bucket[i - 1];
        } // 逐个取出 1 的元素（下标 i）
        for i in (0..adj.len()).rev() {
            // for 下标 i in (0..邻接表.长度()).rev() {
            let d = ((adj[i] / radix) % 10) as usize; // 把 ((邻接表[下标 i] 除以 radix) 对…取模 10) as usize 存入 d
            bucket[d] -= 1; // bucket[d]累减 1
            tmp[bucket[d] as usize] = adj[i]; // 把 邻接表[下标 i]; 写入 tmp[bucket[d] as usize]
        }
        adj.copy_from_slice(&tmp); // 邻接表.copy_from_slice( 按位与 临时变量);
        radix *= 10; // 把 10; 写入 radix *
    }
    adj.into_iter()
        .map(|x| (x - offset as i64) as i32)
        .collect()
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(radix_sort(vec![1, 2, 3]), vec![1, 2, 3]); // 断言校验
    assert_eq!(radix_sort(vec![5, 4, 3, 2, 1]), vec![1, 2, 3, 4, 5]); // 断言校验
    assert_eq!(
        radix_sort(vec![3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]),
        vec![1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    ); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
