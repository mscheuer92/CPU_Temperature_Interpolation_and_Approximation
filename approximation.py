# Michelle Scheuer
# 11/17/2021

import numpy
import numpy as np
from sympy import Matrix

approx_c0 = []
approx_c1 = []
final_start_time = []
final_end_time = []
final_y_count = []


class Approximation:

    def __init__(self):
        self.XTX = []
        self.XTY = []
        self.XT = []
        self.X = []
        self.XTX_XTY = []
        self.matrix_rref = []
        self.approx_c0 = []
        self.approx_c1 = []

    def matrix_x_calculations(self, approximation_x_values):
        matrix = numpy.array([1, 1])
        for i in approximation_x_values:
            matrix_x = np.append(matrix, i)
            # Define XT matrix
            self.XT = np.reshape(matrix_x, (2, 2))
            # Define X matrix
            self.X = np.transpose(self.XT)
            # Calculate XTX
            self.XTX = np.dot(self.X, self.XT)

    def matrix_y_calculations(self, approximation_y_values):
        matrix = numpy.array([0])
        for i in approximation_y_values:
            matrix_y = np.append(matrix, i)

            # Reshape the matrix to be 2 x 1
            matrix_y = np.reshape(matrix_y, (2, 1))

            # Multiple XT * Y
            self.XTY = np.multiply(self.XT, matrix_y)

            # Delete the row of 0's that was added
            self.XTY = np.delete(self.XTY, obj=0, axis=0)

            # Reshape into a 2 * 1 matrix
            self.XTY = np.reshape(self.XTY, (2, 1))


    def combine_XTX_XTY(self):
        self.XTX_XTY = numpy.concatenate((self.XTX, self.XTY), axis=1)

    def calculate_rref(self):
        M = Matrix(self.XTX_XTY)
        self.matrix_rref = M.rref()

    def store_c0_value(self):
        self.approx_c0 = (self.matrix_rref[0])
        approx_c0.append(self.approx_c0[2])

    def store_c1_value(self):
        self.approx_c1 = (self.matrix_rref[0])
        approx_c1.append(self.approx_c1[5])

    def final_output_values(self, total_time_required):
        final_start_time.append("35610")
        final_end_time.append(total_time_required)
        final_y_count.append("1188")

    def clear_lists(self):
        approx_c0.clear()
        approx_c1.clear()
        final_start_time.clear()
        final_end_time.clear()
        final_y_count.clear()
