#函数的多返回值
# def return_number():
#     return 1,2
# x,y = return_number()
# print(x)
# print(y)
#位置参数的概念，用位置一一对应的方式传入参数
# def user_infor(name,age,gender):
#     print(f"名字是{name},年龄是{age},性别是{gender}")
# user_infor("小明",20,"男")
#关键字参数的概念：用键值对的方式传入参数
# def user_infor(name,age,gender):
#     print(f"名字是{name},年龄是{age},性别是{gender}")
# user_infor(name = "小明",gender = "男",age = 20)
#缺省参数的概念：在函数中赋予固定值，注意固定值要放在最后
# def user_infor(name = "小明",age = 20,gender = "男"):
#     print(f"名字是{name},年龄是{age},性别是{gender}")
# user_infor()
#不定长参数的概念：在函数中传入元组或字典
# def user_infor(*args):
#     print(args)
# user_infor(1,2,3,4,5)
# def user_infor2(**Keyargs):
#     print(Keyargs)
# user_infor2(name = "小明",age = 20,gender = "男")
#函数作为参数传入，传入的是该函数的计算逻辑
# def user_infor(computer):
#     result = computer(1,2)
#     print(result)
# def computer(x,y):
#     return x+y
# user_infor(computer)
#lambda函数的使用,意思是无名称函数，lambda 传入参数：运行逻辑   ，注意运行逻辑只能写一行
# def user_infor(computer):
#     result = computer(1,2)
#     print(result)
# user_infor(lambda x,y:x+y)

