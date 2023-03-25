# 1) def series_resistance(resistance):
#     total_resistance = sum(resistance)
#     return str(round(total_resistance)) + " ohms"
#     series_resistance(1,2,3,4,5,6) 
# print(series_resistance([1,3,4,5,6,8,7]))
# 2) def number_split(num):
#     half = num // 2
#     return [half, num - half] if num % 2 == 0 else [half, half + 1]
# print(number_split(5))
# 4) def find_odd(list):
#     out = 0 
#     for num in list:
#         out ^= num
#     return out
# print(find_odd([1,2,3,4,6,7,8,9,0,1,2,3,4,6,5]))
# 5) def sum_odd_and_even(list):
#     sum_even = 0
#     sum_odd = 0
#     for num in list:
#         if num % 2 == 0:
#             sum_even += num
#         else:
#             sum_odd += num
#     return(["Even", sum_even, "Odd", sum_odd])
# print(sum_odd_and_even([1,2,3,4,5,6,7,8,9]))
