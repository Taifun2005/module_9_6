def all_variants(text):
    for i in range(len(text) + 1):
        for j in range(i + 1, len(text) + 1):
            yield text[i:j]



a = all_variants("abc")
for i in a:
    print(i)

# def func_generator(n):
#     i = 0
#     while i != n:
#         yield i
#         i +=1
#
# obj = func_generator(10)
#
# for i in obj:
#     print(i)