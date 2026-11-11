-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133657416
-- LeetCode 92. 反转链表II — Lua 版（方案3）
local function reverse_between(vals, left, right) -- local function reverse_between(vals, 左边界, 右边界)
	local v = { table.unpack(vals) } -- 把 {table.unpack(vals)} 写入 local v
	local seg = {} -- 把 {} 写入 local seg
	for i = right, left, -1 do
		seg[#seg + 1] = v[i]
	end -- 把 右边界, 左边界, 减 1 do seg[#seg 加 1] 赋值为 值[下标 i] 终点 写入 for i
	for i = 1, #seg do
		v[left + i - 1] = seg[i]
	end -- 把 1, #seg do 值[左边界 加 下标 i 减 1] 赋值为 seg[下标 i] 终点 写入 for i
	return v -- 返回 值
end -- 终点
assert(table.concat(reverse_between({ 1, 2, 3, 4, 5 }, 2, 4), ",") == "1,4,3,2,5") -- 打印输出
assert(table.concat(reverse_between({ 1, 2, 3, 4, 5 }, 1, 4), ",") == "4,3,2,1,5") -- 打印输出
assert(table.concat(reverse_between({ 5 }, 1, 1), ",") == "5") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
