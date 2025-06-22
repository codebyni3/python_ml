
# def compare_pdfs_binary(file1, file2):
#     with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
#         return f1.read() == f2.read()

# # Usage
# result = compare_pdfs_binary('file1.pdf', 'file2.pdf')
# print("Are PDFs identical?", result)


def f(x):
    return x + 2
def g(x):
    return x* 2.0
def h(x):
    return f(g(x))
print(h(3))

def func(a , b=5 , c=10):
    return a+b+c
print(func(1,2,3))