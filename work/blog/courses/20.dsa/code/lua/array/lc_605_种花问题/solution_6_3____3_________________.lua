-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134638462
-- LeetCode 605. 种花问题 — Lua 版（方案6）
local function can_place_flowers(bed, n) -- local function can_place_flowers(bed, 元素个数)
	local v = { table.unpack(bed) } -- 把 {table.unpack(bed)} 写入 local v
	local count = 0 -- 把 0 写入 local count
	for i = 1, #v do -- 把 1, #值 do 写入 for i
		if v[i] == 0 and (i == 1 or v[i - 1] == 0) and (i == #v or v[i + 1] == 0) then
			v[i] = 1 -- 把 1 写入 v[i]
			count = count + 1 -- 把 计数 加 1 存入 计数
		end -- 终点
	end -- 终点
	return count >= n -- 返回 计数 不低于 元素个数
end -- 终点
assert(can_place_flowers({ 1, 0, 0, 0, 1 }, 1) == true) -- 断言校验
assert(can_place_flowers({ 1, 0, 0, 0, 1 }, 2) == false) -- 断言校验
assert(can_place_flowers({ 0, 0, 1, 0, 0 }, 1) == true) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
