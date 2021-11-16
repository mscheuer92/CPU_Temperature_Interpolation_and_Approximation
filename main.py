# # Michelle Scheuer
# # 417 Semester Project
# # 11/12/2021

import sys
from calculate import Calculate, begin, end, y_count, c0, c1

output = []
counter = 0

while counter < 4:
    col = [x.split(' ')[counter] for x
           in open(sys.argv[1]).readlines()]  # https://newbedev.com/reading-specific-columns-from-a-text-file-in-python

    results = list(map(float, col))
    results1 = ['%.3f' % elem for elem in results]
    formatted_results = list(map(float, results1))
    total_time_req = len(col) * 30

    for i in range(1, len(results1)):
        a = formatted_results[i] - formatted_results[i - 1]
        output.append(a)

    calculate = Calculate()
    calculate.time_value(total_time_req)
    calculate.formatted_time(total_time_req)
    calculate.calculate_c1(output)
    calculate.calculate_c0(formatted_results)

    for a, b, c, d, e in zip(begin, end, y_count, c0, c1):
        results = f"{a} <= x {b}; y_{c} = {d} + {e}x; interpolation \n"
        with open(sys.argv[1] + "-core-" + str(counter) + ".txt", "a") as f:
            f.write(results)

    calculate.clear()

    del output[:]

    counter += 1
