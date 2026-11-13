// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
// LeetCode 133270489. 原型链原理 — C++ 版（方案3：get 查找 + instanceOf 判定）
#include <iostream>      // 引入头文件
#include <string>        // 引入头文件
#include <unordered_map> // 引入头文件

struct Proto {        // 定义类型
    std::string name; // std::string name;
    std::unordered_map<std::string, std::string>
        props;     // std::unordered_map 小于 std::string, std::string 超过 props;
    Proto *parent; // Proto 乘 parent;
    explicit Proto(const std::string &n, Proto *p = nullptr) : name(n), parent(p) {}
    void set(const std::string &key, const std::string &value) { props[key] = value; }
    bool has(const std::string &key) const { // bool has(const std::string 按位与 key) const {
        const Proto *cur = this;             // 把 this; 写入 const Proto *cur
        while (cur != nullptr) {             // 循环，直到不满足「当前值 不等于 nullptr」
            if (cur->props.count(key))
                return true;   // 若 当前值 减 超过 props.计数(key)，直接返回 true
            cur = cur->parent; // 把 当前值 减 超过 parent; 写入 当前值
        }
        return false; // 返回 false
    }
    std::string get(const std::string &key) const { // std::string get(const std::string 按位与 key) const {
        const Proto *cur = this;                    // 把 this; 写入 const Proto *cur
        while (cur != nullptr) {            // 循环，直到不满足「当前值 不等于 nullptr」
            auto it = cur->props.find(key); // 把 当前值 减 超过 props 查找 key) 存入 it
            if (it != cur->props.end())
                return it->second; // 若 it 不等于 当前值 减 超过 props.终点()，直接返回 it 减 超过 second
            cur = cur->parent; // 把 当前值 减 超过 parent; 写入 当前值
        }
        return ""; // 返回 「」
    }
};

static bool instance_of(const Proto *obj, const Proto *prototype) { // 定义函数/方法 instance_of
    const Proto *p = obj;                                           // 把 obj; 写入 const Proto *p
    while (p != nullptr) { // 循环，直到不满足「节点 不等于 nullptr」
        if (p == prototype)
            return true; // 若 节点 等于 prototype，直接返回 true
        p = p->parent;   // 把 节点 减 超过 parent; 写入 节点
    }
    return false; // 返回 false
}

int main() {                                // 程序入口：跑内嵌自测用例
    Proto object_proto("Object.prototype"); // Proto object_proto(「Object.prototype」);
    object_proto.set("a", "aaa");           // object_proto.set(「数组」, 「数组」);
    Proto function_proto("Function.prototype", &object_proto);
    function_proto.set("b", "bbb");      // function_proto.set(「b」, 「b」);
    Proto obj("obj", &object_proto);     // Proto obj(「obj」, 按位与 object_proto);
    Proto func("func", &function_proto); // Proto func(「func」, 按位与 function_proto);

    if (obj.get("a") != "aaa") {
        std::cout << "case 0 failed" << std::endl;
        return 1;
    }
    if (obj.has("b")) {
        std::cout << "case 1 failed" << std::endl;
        return 1;
    }
    if (func.get("a") != "aaa") {
        std::cout << "case 2 failed" << std::endl;
        return 1;
    }
    if (func.get("b") != "bbb") {
        std::cout << "case 3 failed" << std::endl;
        return 1;
    }
    if (!instance_of(&func, &object_proto)) {
        std::cout << "case 4 failed" << std::endl;
        return 1;
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
