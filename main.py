#!/usr/bin/env python

import os
import cv2
import numpy as np
from matplotlib import pyplot as plt


# klasa pobierająca nazy i sortujaca je
class getFileNames:
    def sortNames(self):
        self.fNames = os.listdir("./images")
"""
Dopisać funkcję sortującą
"""


class imageAnalysis:
    # pobranie obrazu
    def getImages(self, name):
        self.img = cv2.imread('./images/' + name, 0)

    # suma macierzy (Proponowane rozwiązanie podpunkt 2.)
    def matrixSum(self, matrix):
        # wyznaczenie wielkosci macierzy
        N_size = len(matrix)
        M_size = len(matrix[0])
        temp_sum = 0

        # sumowanie wszystkich wartosci w macierzy
        for i in range(0, N_size):
            for j in range(0, M_size):
                temp_sum += matrix[i][j]

        # przypisanie sumy tymczasowej do zmiennej klasowej
        self.NM_sum = temp_sum
