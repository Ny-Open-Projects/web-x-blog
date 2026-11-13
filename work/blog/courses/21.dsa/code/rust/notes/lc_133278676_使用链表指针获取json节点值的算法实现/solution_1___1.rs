// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133278676
// LeetCode 133278676. 使用链表（指针链）获取 JSON 节点值 — Rust 版（方案A：安全遍历，缺失返回 None）
use std::collections::HashMap; // 引入依赖

#[derive(Debug, Clone, PartialEq)]
enum Json {
    // 定义类型
    Obj(HashMap<String, Json>),
    Num(i64),
}

fn get_value(data: &Json, path: &[&str]) -> Option<i64> {
    // 定义函数/方法 get_value
    let mut node = data; // 把 data; 写入 let mut node
    for key in path {
        // 逐个取出 当前路径 的元素（key）
        match node {
            // 按情况匹配处理
            Json::Obj(map) => match map.get(*key) {
                Some(next) => node = next,
                None => return None,
            },
            _ => return None,
        }
    }
    match node {
        // 按情况匹配处理
        Json::Num(v) => Some(*v),
        _ => None,
    }
}

fn sample() -> Json {
    // 定义函数/方法 sample
    let mut c = HashMap::new(); // 把 HashMap::new(); 写入 let mut c
    c.insert("c".to_string(), Json::Num(1)); // 字符 插入 「字符」.to_string(), Json::Num(1));
    let mut b = HashMap::new(); // 把 HashMap::new(); 写入 let mut b
    b.insert("b".to_string(), Json::Obj(c)); // b 插入 「b」.to_string(), Json::Obj(字符));
    let mut a = HashMap::new(); // 把 HashMap::new(); 写入 let mut a
    a.insert("a".to_string(), Json::Obj(b)); // 数组 插入 「数组」.to_string(), Json::Obj(b));
    let mut e = HashMap::new(); // 把 HashMap::new(); 写入 let mut e
    e.insert("e".to_string(), Json::Num(2)); // e 插入 「e」.to_string(), Json::Num(2));
    a.insert("d".to_string(), Json::Obj(e)); // 数组 插入 「d」.to_string(), Json::Obj(e));
    Json::Obj(a) // Json::Obj(数组)
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let data = sample(); // 把 sample() 存入 data
    assert_eq!(get_value(&data, &["a", "b", "c"]), Some(1), "p1"); // 断言校验
    assert_eq!(get_value(&data, &["a", "z"]), None, "p2"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
