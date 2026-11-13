// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
// LeetCode 133270489. 原型链原理 — C++ 版（方案2：get 沿原型链查找属性）
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

int main() {                                // 程序入口：跑内嵌自测用例
    Proto object_proto("Object.prototype"); // Proto object_proto(「Object.prototype」);
    object_proto.set("x", "x");             // object_proto.set(「x」, 「x」);
    Proto function_proto("Function.prototype", &object_proto);
    function_proto.set("y", "y"); // function_proto.set(「y」, 「y」);
    Proto array_proto("Array.prototype",
                      &object_proto);    // Proto array_proto(「Array.prototype」, 按位与 object_proto);
    array_proto.set("z", "z");           // array_proto.set(「z」, 「z」);
    Proto obj("obj", &object_proto);     // Proto obj(「obj」, 按位与 object_proto);
    Proto func("func", &function_proto); // Proto func(「func」, 按位与 function_proto);
    Proto arr("arr", &array_proto);      // Proto 数组(「数组」, 按位与 array_proto);

    if (obj.get("x") != "x") {
        std::cout << "case 0 failed" << std::endl;
        return 1;
    }
    if (func.get("y") != "y") {
        std::cout << "case 1 failed" << std::endl;
        return 1;
    }
    if (arr.get("z") != "z") {
        std::cout << "case 2 failed" << std::endl;
        return 1;
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
