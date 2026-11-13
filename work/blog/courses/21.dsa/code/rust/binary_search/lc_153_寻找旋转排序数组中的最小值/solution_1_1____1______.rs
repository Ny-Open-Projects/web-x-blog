// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233483
// LeetCode 153. 寻找旋转排序数组中的最小值 — Rust 版（方案1：二分查找）

fn find_min(nums: &[i32]) -> i32 {
    // 定义函数/方法 find_min
    let mut low: i32 = 0; // 把 0; 写入 let mut low: i32
    let mut high: i32 = nums.len() as i32 - 1; // 把 数组.长度() as i32 减 1; 写入 let mut high: i32
    while low < high {
        // while low 小于 high {
        let pivot = low + (high - low) / 2; // 防溢出写法
        let p = pivot as usize; // 把 pivot as usize 存入 节点
        if nums[p] < nums[high as usize] {
            // 若 数组[节点] 小于 数组[high as usize]
            high = pivot; // 把 pivot; 写入 high
        } else {
            // 否则
            low = pivot + 1; // 把 pivot 加 1; 写入 low
        }
    }
    nums[low as usize] // 数组[low as usize]
}

fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(find_min(&[1, 2, 3]), 1); // 断言校验
    assert_eq!(find_min(&[3, 4, 5, 1, 2]), 1); // 断言校验
    assert_eq!(find_min(&[4, 5, 6, 7, 0, 1, 2]), 0); // 断言校验
    assert_eq!(find_min(&[11, 13, 15, 17]), 11); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
