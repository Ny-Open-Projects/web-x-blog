/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
 * LeetCode 133270489. 原型链原理 — C 版（方案2：get 沿原型链查找属性）
 */
#include <stdio.h>  // 引入头文件
#include <string.h> // 引入头文件

#define MAX_PROPS 8           // #define MAX_PROPS 8
typedef struct Proto {        // typedef struct Proto {
    const char *name;         // const char 乘 name;
    char keys[MAX_PROPS][16]; // char keys[MAX_PROPS][16];
    char vals[MAX_PROPS][32]; // char vals[MAX_PROPS][32];
    int nprops;               // int nprops;
    struct Proto *parent;     // 定义类型
} Proto;                      // } Proto;

static void set_prop(Proto *p, const char *key, const char *value) { // 定义函数/方法 set_prop
    strcpy(p->keys[p->nprops], key);   // strcpy(节点 减 超过 keys[节点 减 超过 nprops], key);
    strcpy(p->vals[p->nprops], value); // strcpy(节点 减 超过 vals[节点 减 超过 nprops], value);
    p->nprops++;                       // 节点 减 超过 nprops 加一 ;
}

static const char *get_prop(const Proto *p, const char *key) {
    const Proto *cur = p; // 把 节点; 写入 const Proto *cur
    while (cur != NULL) { // 循环，直到不满足「当前值 不等于 NULL」
        for (int i = 0; i < cur->nprops;
             i++) // 让 下标 i 从 0 开始计数，下标 i 小于 当前值 减 超过 nprops 就继续
            if (strcmp(cur->keys[i], key) == 0)
                return cur->vals[i];
        cur = cur->parent; // 把 当前值 减 超过 parent; 写入 当前值
    }
    return NULL; // 返回 NULL
}

int main(void) { // 程序入口：跑内嵌自测用例
    Proto object_proto = {"Object.prototype", {}, {}, 0, NULL};
    set_prop(&object_proto, "x", "x"); // set_prop( 按位与 object_proto, 「x」, 「x」);
    Proto function_proto = {"Function.prototype", {}, {}, 0, &object_proto};
    set_prop(&function_proto, "y", "y"); // set_prop( 按位与 function_proto, 「y」, 「y」);
    Proto array_proto = {"Array.prototype", {}, {}, 0, &object_proto};
    set_prop(&array_proto, "z", "z"); // set_prop( 按位与 array_proto, 「z」, 「z」);
    Proto obj = {
        "obj", {}, {}, 0, &object_proto}; // 把 {「obj」, {}, {}, 0, 按位与 object_proto}; 写入 Proto obj
    Proto func = {"func",
                  {},
                  {},
                  0,
                  &function_proto}; // 把 {「func」, {}, {}, 0, 按位与 function_proto}; 写入 Proto func
    Proto arr = {
        "arr", {}, {}, 0, &array_proto}; // 把 {「数组」, {}, {}, 0, 按位与 array_proto}; 写入 Proto arr

    if (strcmp(get_prop(&obj, "x"), "x") != 0) {
        printf("case 0 failed\n");
        return 1;
    }
    if (strcmp(get_prop(&func, "y"), "y") != 0) {
        printf("case 1 failed\n");
        return 1;
    }
    if (strcmp(get_prop(&arr, "z"), "z") != 0) {
        printf("case 2 failed\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
