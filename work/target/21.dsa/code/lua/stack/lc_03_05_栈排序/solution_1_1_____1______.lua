-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397311
-- LeetCode 面试题 03.05. 栈排序 — Lua 版（方案1）
local function sorted_stack(input) -- local function sorted_stack(input)
	local stk, temp, output = {}, {}, {} -- 把 {}, {}, {} 写入 local stk, temp, output
	for _, v in ipairs(input) do
		stk[#stk + 1] = v
	end -- 遍历取 值
	while #stk > 0 do -- while #栈 超过 0 do
		local v = table.remove(stk) -- 把 table 弹出 栈) 写入 local v
		while #temp > 0 and temp[#temp] > v do -- while #临时变量 超过 0 and 临时变量[#临时变量] 超过 值 do
			output[#output + 1] = table.remove(temp) -- 把 table 弹出 临时变量) 写入 output[#output + 1]
		end -- 终点
		temp[#temp + 1] = v -- 把 值 写入 temp[#temp + 1]
	end -- 终点
	while #temp > 0 do
		output[#output + 1] = table.remove(temp)
	end
	table.sort(output) -- 排序
	return output -- 返回 输出
end -- 终点
assert(table.concat(sorted_stack({ 5, 2, 1, 4, 3 }), ",") == "1,2,3,4,5") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
