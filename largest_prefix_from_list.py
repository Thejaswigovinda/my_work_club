# string_list = ["thejaswi", "theju", "thejas"]
# min_string = min(string_list, key=len)
# print(min_string)
# prefix = " "
#
# for i in range(len(min_string)):
#     current_charecter = min_string[i]
#     print(current_charecter)
#
#     if all(s[i] == current_charecter for s in string_list):
#         prefix = prefix + current_charecter
#
# print(prefix)

def myfunc(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("*", end = " ")
        print("\r")
n = 5
myfunc(n)