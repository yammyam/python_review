def solution(sizes):
    return max(max(w, h) for w, h in sizes) * max(min(w, h) for w, h in sizes)
# def solution(sizes):
#     a = 0;
#     b = 0;
#     for i in range(len(sizes)):
#         sizes[i].sort()
#     for i in sizes:
#         if(a==0):
#             a = i[0]
#         if(b == 0):
#             b = i[1]
#         if(a < i[0]):
#             a = i[0]
#         if(b< i[1]):
#             b = i[1]
#     return a*b;