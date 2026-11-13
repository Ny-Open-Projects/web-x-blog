-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136838836
-- LeetCode 791. 自定义字符串排序 — Lua 版（方案2）
local function custom_sort_string(order, s) -- local function custom_sort_string(order, 字符串)
	local count = {} -- 把 {} 写入 local count
	for c in s:gmatch("[%a]") do -- for 字符 in 字符串:gmatch(「[ 对…取模 数组]」) do
		count[c] = (count[c] or 0) + 1 -- 把 (计数[字符] or 0) 加 1 写入 count[c]
	end -- 终点
	local out = {} -- 把 {} 写入 local out
	for c in order:gmatch("[%a]") do -- for 字符 in order:gmatch(「[ 对…取模 数组]」) do
		if count[c] then -- 若 计数[字符] then
			for _ = 1, count[c] do
				out[#out + 1] = c
			end -- 让 _ 从 1 走到 计数（Lua 1 基）
			count[c] = nil -- 把 nil 写入 count[c]
		end -- 终点
	end -- 终点
	local rest = {} -- 把 {} 写入 local rest
	for c, n in pairs(count) do -- 遍历取 元素个数
		for _ = 1, n do
			rest[#rest + 1] = c
		end -- 让 _ 从 1 走到 元素个数（Lua 1 基）
	end -- 终点
	table.sort(rest) -- 排序
	for _, c in ipairs(rest) do
		out[#out + 1] = c
	end -- 遍历取 字符
	return table.concat(out) -- 返回 table.concat(out)
end -- 终点
assert(custom_sort_string("cba", "abcd") == "cbad") -- 断言校验
assert(custom_sort_string("bcafg", "abcd") == "bcad") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
