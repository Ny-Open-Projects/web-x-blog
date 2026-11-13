/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
 * LeetCode 133270489. 原型链原理 — C 版（方案3：get 查找 + instanceOf 判定）
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
    Proto object_proto = {"Object.prototype", {}, {}, 0, NULL};
    set_prop(&object_proto, "a", "aaa"); // set_prop( 按位与 object_proto, 「数组」, 「数组」);
    Proto function_proto = {"Function.prototype", {}, {}, 0, &object_proto};
    set_prop(&function_proto, "b", "bbb"); // set_prop( 按位与 function_proto, 「b」, 「b」);
    Proto obj = {
        "obj", {}, {}, 0, &object_proto}; // 把 {「obj」, {}, {}, 0, 按位与 object_proto}; 写入 Proto obj
    Proto func = {"func",
                  {},
                  {},
                  0,
                  &function_proto}; // 把 {「func」, {}, {}, 0, 按位与 function_proto}; 写入 Proto func

    if (strcmp(get_prop(&obj, "a"), "aaa") != 0) {
        printf("case 0 failed\n");
        return 1;
    }
    if (get_prop(&obj, "b") != NULL) {
        printf("case 1 failed\n");
        return 1;
    } // 若 get_prop( 按位与 obj, 「b」) 不等于 NULL) { 输出「b」); return 1; }
    if (strcmp(get_prop(&func, "a"), "aaa") != 0) {
        printf("case 2 failed\n");
        return 1;
    }
    if (strcmp(get_prop(&func, "b"), "bbb") != 0) {
        printf("case 3 failed\n");
        return 1;
    }
    if (!instance_of(&func, &object_proto)) {
        printf("case 4 failed\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
