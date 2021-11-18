# Michelle Scheuer
# 11/12/2021


time_list = []
c1_value = []
products = []
c0_value = []
formatted = []
start_time = []
end_time = []
y_count = []


class Calculate:

    def time_value(self, total_time_req):
        for i in range(0, total_time_req, 30):
            time_list.append(i)

    def formatted_time(self, total_time_req):
        count = 0
        for i in range(0, total_time_req, 30):
            time1 = i + 30
            start_time.append(i)
            end_time.append(time1)
            count += 1
            y_count.append(count)

    def calculate_c1(self, formatted_output):
        for i in formatted_output:
            time1 = i / 30
            c1x = (round(time1, 4))
            c1_value.append(c1x)

    def calculate_c0(self, col_results):
        for C1, y0 in zip(c1_value, time_list):
            products.append(round((C1 * y0), 1))

        for C0, prod in zip(col_results, products):
            c0_value.append(C0 - prod)

    def clear_lists(self):
        time_list.clear()
        c1_value.clear()
        products.clear()
        c0_value.clear()
        formatted.clear()
        start_time.clear()
        end_time.clear()
        y_count.clear()
