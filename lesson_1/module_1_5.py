immutable_var = 3, "string", True
immutable_var[1] = 5
# Попытка измененить кортеж приводит к ошибке (TypeError: 'tuple' object does not support item assignment),
# потому что кортеж - неизменяемый объект

mutable_list = [45, 77, "string",False]
mutable_list[2] = "Modified"
mutable_list[1] = True
print("Immutable tuple:", immutable_var)
print("Mutable list:", mutable_list)