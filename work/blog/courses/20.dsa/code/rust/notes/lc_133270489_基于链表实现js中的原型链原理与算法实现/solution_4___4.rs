// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
// LeetCode 133270489. 原型链原理 — Rust 版（方案4：null/undefined 边界：instanceOf 均返回 false）
struct FakeObj {
    // 定义类型
    proto: Option<*const u8>, // 模拟 __proto__ 指针
}

struct FakeCtor {
    // 定义类型
    prototype: Option<*const u8>,
}

fn instance_of(a: Option<&FakeObj>, b: &FakeCtor) -> bool {
    // 定义函数/方法 instance_of
    // 与 JS 语义对齐：null/undefined 沿链必为 false
    let mut p = match a {
        // 把 match 数组 { 写入 let mut p
        None => return false,
        Some(o) => o.proto,
    };
    while let Some(ptr) = p {
        // 边取边处理，取空即停
        if Some(ptr) == b.prototype {
            // 若 Some(ptr) 等于 b.prototype
            return true; // 返回 true
        }
        // 演示用：无法继续向上（无真实对象头），直接终止
        p = None; // 把 None; 写入 节点
    }
    false // false
}

fn main() {
    // 程序入口：跑内嵌自测用例
    // case: null / undefined 视为 None —— instanceOf 均为 false
    let ctor = FakeCtor { prototype: None }; // 把 FakeCtor { prototype: None } 存入 ctor
    assert!(!instance_of(None, &ctor), "null case failed"); // 断言校验
    assert!(!instance_of(None, &ctor), "undefined case failed"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
