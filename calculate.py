# Michelle Scheuer
# 417 Semester Project
# 11/12/2021
import sys

time_list = []
c1 = []
products = []
c0 = []
formatted = []
begin = []
end = []
y_count = []


class Calculate:

    def time_value(self, total_time_req):
        for i in range(0, total_time_req, 30):
            time_list.append(i)

    def formatted_time(self, total_time_req):
        count = 0
        for i in range(0, total_time_req, 30):
            time1 = i + 30
            begin.append(i)
            end.append(time1)
            count += 1
            y_count.append(count)

    def calculate_c1(self, output):
        for i in output:
            time1 = i / 30
            c1x = (round(time1, 4))
            c1.append(c1x)

    def calculate_c0(self, formatted_results):
        for C1, y0 in zip(c1, time_list):
            products.append(round((C1 * y0),1))

        for C0, prod in zip(formatted_results, products):
            c0.append(C0 - prod)

    def clear(self):
        time_list.clear()
        c1.clear()
        products.clear()
        c0.clear()
        formatted.clear()
        begin.clear()
        end.clear()
        y_count.clear()
