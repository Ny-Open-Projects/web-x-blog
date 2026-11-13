-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385760
-- LeetCode 1114. 按序打印 — Lua 版（方案1）
local function print_in_order() -- local function print_in_order()
	local out = {} -- 把 {} 写入 local out
	local step = 1 -- 把 1 写入 local step
	local function first() -- local function first()
		out[#out + 1] = "first" -- 把 「first」 写入 out[#out + 1]
		step = 2 -- 把 2 存入 步数
	end -- 终点
	local function second() -- local function second()
		while step < 2 do
		end -- 忙等（确定性模拟）
		out[#out + 1] = "second" -- 把 「second」 写入 out[#out + 1]
		step = 3 -- 把 3 存入 步数
	end -- 终点
	local function third() -- local function third()
		while step < 3 do
		end -- while 步数 小于 3 do 终点
		out[#out + 1] = "third" -- 把 「third」 写入 out[#out + 1]
	end -- 终点
	first() -- first()
	second() -- second()
	third() -- third()
	return table.concat(out) -- 返回 table.concat(out)
end -- 终点
assert(print_in_order() == "firstsecondthird") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
