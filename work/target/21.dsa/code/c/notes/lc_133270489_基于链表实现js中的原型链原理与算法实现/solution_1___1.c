/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
 * LeetCode 133270489. 原型链原理 — C 版（方案1：instanceOf 沿原型链判定）
 */
#include <stdio.h>  // 引入头文件
#include <string.h> // 引入头文件

typedef struct Proto {    // typedef struct Proto {
    const char *name;     // const char 乘 name;
    struct Proto *parent; // 定义类型
} Proto;                  // } Proto;

static int instance_of(const Proto *obj, const Proto *prototype) { // 定义函数/方法 instance_of
    const Proto *p = obj;                                          // 把 obj; 写入 const Proto *p
    while (p != NULL) { // 循环，直到不满足「节点 不等于 NULL」
        if (p == prototype)
            return 1;  // 若 节点 等于 prototype，直接返回 1
        p = p->parent; // 把 节点 减 超过 parent; 写入 节点
    }
    return 0; // 返回 0
}

int main(void) { // 程序入口：跑内嵌自测用例
    Proto object_proto = {"Object.prototype",
                          NULL}; // 把 {「Object.prototype」, NULL}; 写入 Proto object_proto
    Proto function_proto = {"Function.prototype", &object_proto};
    Proto array_proto = {"Array.prototype", &object_proto};
    Proto obj = {"obj", &object_proto};     // 把 {「obj」, 按位与 object_proto}; 写入 Proto obj
    Proto func = {"func", &function_proto}; // 把 {「func」, 按位与 function_proto}; 写入 Proto func
    Proto arr = {"arr", &array_proto};      // 把 {「数组」, 按位与 array_proto}; 写入 Proto arr

    int g0 = instance_of(&obj, &object_proto); // 把 instance_of( 按位与 obj, 按位与 object_proto) 存入 g0
    int g1 =
        instance_of(&func, &function_proto); // 把 instance_of( 按位与 func, 按位与 function_proto) 存入 g1
    int g2 = instance_of(&func, &object_proto); // 把 instance_of( 按位与 func, 按位与 object_proto) 存入 g2
    int g3 = instance_of(&arr, &array_proto); // 把 instance_of( 按位与 数组, 按位与 array_proto) 存入 g3
    int g4 = instance_of(&arr, &object_proto); // 把 instance_of( 按位与 数组, 按位与 object_proto) 存入 g4
    if (!g0 || !g1 || !g2 || !g3 || !g4) {
        printf("FAIL\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
