-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233913
-- LeetCode 739. 每日温度 — Lua 版（方案2）
local function daily_temperatures(temps) -- local function daily_temperatures(temps)
	local n = #temps -- 把 #temps 写入 local n
	local res = {} -- 把 {} 写入 local res
	for i = 1, n do
		res[i] = 0
	end -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
	local st = {} -- 把 {} 写入 local st
	for i = 1, n do -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
		while #st > 0 and temps[st[#st]] < temps[i] do -- while #st 超过 0 and temps[st[#st]] 小于 temps[下标 i] do
			res[st[#st]] = i - st[#st] -- 把 下标 i 减 st[#st] 写入 res[st[#st]]
			st[#st] = nil -- 把 nil 写入 st[#st]
		end -- 终点
		st[#st + 1] = i -- 把 下标 i 写入 st[#st + 1]
	end -- 终点
	return res -- 返回 结果
end -- 终点
assert(table.concat(daily_temperatures({ 73, 74, 75, 71, 69, 72, 76, 73 }), ",") == "1,1,4,2,1,1,0,0") -- 打印输出
assert(table.concat(daily_temperatures({ 30, 40, 50, 60 }), ",") == "1,1,1,0") -- 打印输出
assert(table.concat(daily_temperatures({ 30, 60, 90 }), ",") == "1,1,0") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
