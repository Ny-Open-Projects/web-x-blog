// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
// LeetCode 133270489. 原型链原理 — Rust 版（方案1：instanceOf 沿原型链判定）
use std::cell::RefCell; // 引入依赖
use std::collections::HashMap; // 引入依赖
use std::rc::Rc; // 引入依赖

struct Proto {
    // 定义类型
    name: String,
    props: RefCell<HashMap<String, String>>,
    parent: Option<Rc<Proto>>,
}

impl Proto {
    // 实现块
    fn new(name: &str, parent: Option<Rc<Proto>>) -> Rc<Proto> {
        // 定义函数/方法 new
        Rc::new(Proto {
            // Rc::new(Proto {
            name: name.to_string(),
            props: RefCell::new(HashMap::new()),
            parent,
        }) // })
    }
}

fn instance_of(obj: &Rc<Proto>, prototype: &Rc<Proto>) -> bool {
    // 定义函数/方法 instance_of
    let mut p: Option<&Rc<Proto>> = Some(obj); // 把 Some(obj); 写入 let mut p: Option<&Rc<Proto>>
    while let Some(cur) = p {
        // 边取边处理，取空即停
        if std::ptr::eq(cur.as_ref(), prototype.as_ref()) {
            // 若 std::ptr::eq(当前值.as_ref(), prototype.as_ref(
            return true; // 返回 true
        }
        p = cur.parent.as_ref(); // 把 当前值.parent.as_ref(); 写入 节点
    }
    false // false
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let object_proto = Proto::new("Object.prototype", None); // 把 Proto::new(「Object.prototype」, None) 存入 object_proto
    let function_proto = Proto::new("Function.prototype", Some(object_proto.clone()));
    let array_proto = Proto::new("Array.prototype", Some(object_proto.clone()));
    let obj = Proto::new("obj", Some(object_proto.clone())); // 把 Proto::new(「obj」, Some(object_proto.clone())) 存入 obj
    let func = Proto::new("func", Some(function_proto.clone())); // 把 Proto::new(「func」, Some(function_proto.clone())) 存入 func
    let arr = Proto::new("arr", Some(array_proto.clone())); // 把 Proto::new(「数组」, Some(array_proto.clone())) 存入 数组

    let cases = [
        (instance_of(&obj, &object_proto), true),
        (instance_of(&func, &function_proto), true),
        (instance_of(&func, &object_proto), true),
        (instance_of(&arr, &array_proto), true),
        (instance_of(&arr, &object_proto), true),
    ];
    for (idx, (got, want)) in cases.iter().enumerate() {
        // for (idx, (got, want)) in cases.iter().enumerate() {
        assert_eq!(got, want, "case {} failed", idx); // 断言校验
    }
    println!("PASS"); // 全部用例通过，输出 PASS
}
