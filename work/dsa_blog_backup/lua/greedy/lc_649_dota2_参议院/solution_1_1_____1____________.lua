-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138684407
-- LeetCode 649. Dota2参议院 — Lua 版（方案1）
local function predict_party_victory(senate) -- local function predict_party_victory(senate)
	local n = #senate -- 把 #senate 写入 local n
	local radiant, dire = {}, {} -- 把 {}, {} 写入 local radiant, dire
	local rh, dh = 1, 1 -- 把 1, 1 写入 local rh, dh
	for i = 1, n do -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
		if senate:sub(i, i) == "R" then
			radiant[#radiant + 1] = i - 1
		else
			dire[#dire + 1] = i - 1
		end
	end -- 终点
	while rh <= #radiant and dh <= #dire do -- 把 #radiant and dh 不超过 #dire do 写入 while rh <
		local r = radiant[rh]
		rh = rh + 1 -- 把 radiant[rh]; rh 赋值为 rh 加 1 写入 local r
		local d = dire[dh]
		dh = dh + 1 -- 把 dire[dh]; dh 赋值为 dh 加 1 写入 local d
		if r < d then
			radiant[#radiant + 1] = r + n
		else
			dire[#dire + 1] = d + n
		end
	end -- 终点
	if rh > #radiant then
		return "Dire"
	else
		return "Radiant"
	end -- 若 rh 超过 #radiant then return 「Dire」 else return 「Dire」 终点
end -- 终点
assert(predict_party_victory("RD") == "Radiant") -- 断言校验
assert(predict_party_victory("DDR") == "Dire") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
