-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130734875
-- LeetCode 682. 棒球比赛 — Lua 版（方案9）
local function cal_points(ops) -- local function cal_points(ops)
	local st = {} -- 把 {} 写入 local st
	for _, op in ipairs(ops) do -- 遍历取 op
		if op == "+" then -- 若 op 等于 「 加 」 then
			st[#st + 1] = st[#st] + st[#st - 1] -- 把 st[#st] 加 st[#st 减 1] 写入 st[#st + 1]
		elseif op == "D" then -- 把 赋值为 「D」 then 写入 elseif op
			st[#st + 1] = st[#st] * 2 -- 把 st[#st] 乘 2 写入 st[#st + 1]
		elseif op == "C" then -- 把 赋值为 「C」 then 写入 elseif op
			st[#st] = nil -- 把 nil 写入 st[#st]
		else -- 否则
			st[#st + 1] = tonumber(op) -- 把 tonumber(op) 写入 st[#st + 1]
		end -- 终点
	end -- 终点
	local sum = 0 -- 把 0 写入 local sum
	for _, v in ipairs(st) do
		sum = sum + v
	end -- 遍历取 值
	return sum -- 返回 累计和
end -- 终点
assert(cal_points({ "5", "2", "C", "D", "+" }) == 30) -- 断言校验
assert(cal_points({ "5", "-2", "4", "C", "D", "9", "+", "+" }) == 27) -- 断言校验
assert(cal_points({ "1", "C" }) == 0) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
