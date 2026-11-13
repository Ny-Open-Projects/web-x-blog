-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135167617
-- LeetCode 860. 柠檬水找零 — Lua 版（方案6）
local function lemonade_change(bills) -- local function lemonade_change(bills)
	local f5, f10 = 0, 0 -- 把 0, 0 写入 local f5, f10
	for _, b in ipairs(bills) do -- 遍历取 b
		if b == 5 then -- 若 b 等于 5 then
			f5 = f5 + 1 -- 把 f5 加 1 存入 f5
		elseif b == 10 then -- 把 赋值为 10 then 写入 elseif b
			f10 = f10 + 1
			f5 = f5 - 1 -- 把 f10 加 1; f5 赋值为 f5 减 1 存入 f10
		else -- 否则
			if f10 > 0 then
				f10 = f10 - 1
				f5 = f5 - 1
			else
				f5 = f5 - 3
			end
		end -- 终点
		if f5 < 0 then
			return false
		end -- 若 f5 小于 0 then return false 终点
	end -- 终点
	return true -- 返回 true
end -- 终点
assert(lemonade_change({ 5, 5, 5, 10, 20 }) == true) -- 断言校验
assert(lemonade_change({ 5, 5, 10, 10, 20 }) == false) -- 断言校验
assert(lemonade_change({ 5, 5, 5, 5, 20 }) == true) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
