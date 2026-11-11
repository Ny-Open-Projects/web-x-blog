-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107435426
-- 字典序最大问题分析 — Lua 版（方案2）
local function lexicographically_largest(n, arr) -- local function lexicographically_largest(元素个数, 数组)
	local v = { table.unpack(arr) } -- 把 {table.unpack(数组)} 写入 local v
	table.sort(v, function(a, b)
		return a > b
	end) -- 排序
	while #v > n do
		v[#v] = nil
	end -- 把 nil 终点 写入 while #v > n do v[#v]
	return v -- 返回 值
end -- 终点
assert(table.concat(lexicographically_largest(3, { 1, 2, 3 }), ",") == "3,2,1") -- 打印输出
assert(table.concat(lexicographically_largest(4, { 4, 2, 9, 7 }), ",") == "9,7,4,2") -- 打印输出
assert(table.concat(lexicographically_largest(2, { 5, 1 }), ",") == "5,1") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
