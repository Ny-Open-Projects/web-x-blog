-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386116
-- LeetCode 1518. 换水问题 — Lua 版（方案2）
local function num_water_bottles(num_bottles, num_exchange) -- local function num_water_bottles(num_bottles, num_exchange)
	local ans, empty = num_bottles, num_bottles -- 把 num_bottles, num_bottles 写入 local ans, empty
	while empty >= num_exchange do -- 把 num_exchange do 写入 while empty >
		local new_b = math.floor(empty / num_exchange) -- 把 math.floor(empty 除以 num_exchange) 写入 local new_b
		ans = ans + new_b -- 把 答案 加 new_b 存入 答案
		empty = new_b + empty % num_exchange -- 把 new_b 加 empty 对…取模 num_exchange 存入 empty
	end -- 终点
	return ans -- 返回 答案
end -- 终点
assert(num_water_bottles(9, 3) == 13) -- 断言校验
assert(num_water_bottles(15, 4) == 19) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
