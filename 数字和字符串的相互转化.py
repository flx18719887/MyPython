# float:将其他类型数据转换为浮点数
float(1)    # 1.0
float('1.23')    # 1.23
float('1.2e-3')  # 0.0012
float('1.2e3')   # 1200.0
# str:将其他类型数据转换为字符串
str(1)   # '1'
str(1.0)  # '1.0'
str(1.0e-5)  # '1e-05'
# 将其他类型数据转换为整数
int(3.14)   # 3
int(True)   # 1
# int('3.5')   # 报错
int(float('3.5'))   # 3
# 将其他类型数据转换为布尔类型
bool(0)    # False
bool(-1)   # True   所有非0数值都为真
bool('a')   # True
bool('')    # False
# chr和ord   整数和字符
chr(65)    # 'A'
ord('a')   # 97