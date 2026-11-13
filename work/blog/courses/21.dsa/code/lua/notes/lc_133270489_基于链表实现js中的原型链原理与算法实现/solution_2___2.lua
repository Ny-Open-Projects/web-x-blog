-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
-- LeetCode 133270489. 原型链原理 — Lua 版（方案2：get 沿原型链查找属性）
local Proto = {} -- 把 {} 写入 local Proto
Proto.__index = Proto -- 把 Proto 写入 Proto.__index
function Proto.new(name, parent) -- function Proto.new(name, parent)
	return setmetatable({ name = name, props = {}, parent = parent }, Proto)
end -- 终点
function Proto:set(key, value) -- function Proto:set(key, value)
	self.props[key] = value -- 把 value 写入 self.props[key]
end -- 终点
function Proto:get(key) -- function Proto:get(key)
	local cur = self -- 把 self 写入 local cur
	while cur ~= nil do -- 把 nil do 写入 while cur ~
		if cur.props[key] ~= nil then
			return cur.props[key]
		end -- 若 当前值.props[key] ~ 赋值为 nil then return 当前值.props[key] 终点
		cur = cur.parent -- 把 当前值.parent 存入 当前值
	end -- 终点
	return nil -- 返回 nil
end -- 终点

local object_proto = Proto.new("Object.prototype") -- 把 Proto.new(「Object.prototype」) 写入 local object_proto
object_proto:set("x", "x") -- object_proto:set(「x」, 「x」)
local function_proto = Proto.new("Function.prototype", object_proto)
function_proto:set("y", "y") -- function_proto:set(「y」, 「y」)
local array_proto = Proto.new("Array.prototype", object_proto)
array_proto:set("z", "z") -- array_proto:set(「z」, 「z」)
local obj = Proto.new("obj", object_proto) -- 把 Proto.new(「obj」, object_proto) 写入 local obj
local func = Proto.new("func", function_proto) -- 把 Proto.new(「func」, function_proto) 写入 local func
local arr = Proto.new("arr", array_proto) -- 把 Proto.new(「数组」, array_proto) 写入 local arr

assert(obj:get("x") == "x", "case 0 failed") -- 断言校验
assert(func:get("y") == "y", "case 1 failed") -- 断言校验
assert(arr:get("z") == "z", "case 2 failed") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
