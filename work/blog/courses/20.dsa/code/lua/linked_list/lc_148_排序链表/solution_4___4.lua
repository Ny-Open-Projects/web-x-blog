-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133904873
-- LeetCode 148. 排序链表 — Lua 版（方案4）
local function sort_list(vals) -- local function sort_list(vals)
	local v = { table.unpack(vals) } -- 把 {table.unpack(vals)} 写入 local v
	table.sort(v) -- 排序
	return v -- 返回 值
end -- 终点
assert(table.concat(sort_list({ 4, 2, 1, 3 }), ",") == "1,2,3,4") -- 打印输出
assert(table.concat(sort_list({ -1, 5, 3, 4, 0 }), ",") == "-1,0,3,4,5") -- 打印输出
assert(#sort_list({}) == 0) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
