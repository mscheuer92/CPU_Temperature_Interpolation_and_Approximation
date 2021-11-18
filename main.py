# # Michelle Scheuer
# # 11/12/2021

import sys
from calculate import Calculate, y_count, start_time, end_time, c0_value, c1_value
from approximation import Approximation, final_start_time, final_end_time, final_y_count, approx_c0, \
    approx_c1

formatted_output = []
counter = 0
final_output = []

while counter < 4:
    col = [x.split(' ')[counter] for x
           in open(sys.argv[1]).readlines()]

    remove_table = str.maketrans(' ', ' ', '+Â°C\n', )  # remove special characters if needed
    special_char_removed = [s.translate(remove_table) for s in col]  # store formatted temps in list

    col_results = list(map(float, special_char_removed))
    total_time_req = len(col) * 30

    # approx_time = [total_time_req]
    first_last = col_results[::len(col_results) - 1]
    approximation_x_values = [first_last]
    approximation_y_values = [total_time_req]

    for i in range(1, len(col_results)):
        temp_difference = col_results[i] - col_results[i - 1]
        formatted_output.append(temp_difference)

    calculate = Calculate()
    calculate.time_value(total_time_req)
    calculate.formatted_time(total_time_req)
    calculate.calculate_c1(formatted_output)
    calculate.calculate_c0(col_results)

    approx = Approximation()
    approx.matrix_x_calculations(approximation_x_values)
    approx.matrix_y_calculations(approximation_y_values)
    approx.combine_XTX_XTY()
    approx.calculate_rref()
    approx.store_c0_value()
    approx.store_c1_value()
    approx.final_output_values(total_time_req)

    for a, b, c, d, e in zip(start_time, end_time, y_count, c0_value, c1_value):
        zip_results = f"{a} <= x {b}; y_{c} = {d} + {e}x; interpolation \n"
        with open(sys.argv[1] + "-core-" + str(counter) + ".txt", "a") as f:
            f.write(zip_results)

    for a, b, c, d, e in zip(final_start_time, final_end_time, final_y_count, approx_c0, approx_c1):
        zip_results = f"{a} <= x {b}; y_{c} = {d} + {e}x; approximation \n"
        with open(sys.argv[1] + "-core-" + str(counter) + ".txt", "a") as f:
            f.write(zip_results)

    calculate.clear_lists()
    approx.clear_lists()
    del formatted_output[:]
    counter += 1

