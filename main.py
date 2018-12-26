#!/usr/bin/env python
import os
import cv2
import numpy as np
from math import log2
from matplotlib import pyplot as plt


# klasa pobierająca nazy i sortujaca je
class getFileNames:
    def sortNames(self):
        # pobranie nazwy plików do listy
        self.fNames = os.listdir("./images")
        tempFloatList = []
        dictFloatName = {}
        unsortable = []
        sortNames = []

        # posortowanie od najmniejszej do najwiekszej
        # wartosci chropowatosci
        # WAŻNE ŻEBY PLIK BYŁ W FORMACIE XXX_Rough_X.XXXXXnm.png
        for i in self.fNames:
            # Wyodrebnienie wartosci chropowatosci z nazwy pliku
            tempName = i.split("_Rough_")
            if tempName[0] is i:
                unsortable.append(i)
            else:
                tempName = tempName[1].split("nm.png")
                tempFloatList.append(float(tempName[0]))
                # Stworzenie słownika klucz chropowatość : nazwa pliku
                dictFloatName[float(tempName[0])] = i

        # sortowanie babelkowe
        for j in range(0, len(tempFloatList)):
            for i in range(0, len(tempFloatList)):
                if i is (len(tempFloatList)-1):
                    break
                if tempFloatList[i] > tempFloatList[i+1]:
                    temp = tempFloatList[i]
                    tempFloatList[i] = tempFloatList[i+1]
                    tempFloatList[i+1] = temp

        # lista posortowanych chropowatosci
        self.sortedFl = tempFloatList.copy()

        # stworzenie listy posortowanych nazw
        for i in tempFloatList:
            sortNames.append(dictFloatName[i])

        for i in unsortable:
            sortNames.append(i)

        self.sortedNames = sortNames.copy()


class imageAnalysis:
    # pobranie obrazu
    def getImages(self, name):
        self.img = cv2.imread('./images/' + name, 0)

    # suma macierzy (Proponowane rozwiązanie podpunkt 2.)
    def matrixSum(self, matrix):
        # wyznaczenie wielkosci macierzy
        N_size = len(matrix)
        M_size = len(matrix[0])

        # iloczyn N i M potrzebny do sredniej
        self.productNM = N_size * M_size
        temp_sum = 0

        # sumowanie wszystkich wartosci w macierzy
        for i in range(0, N_size):
            for j in range(0, M_size):
                temp_sum += matrix[i][j]

        # przypisanie sumy tymczasowej do zmiennej klasowej
        self.NM_sum = temp_sum

    # Wyznaczenie sredniej (Proponowane rozwiązanie podpunkt 3.)
    # (iloczyn NM wykorzystany z funkcji matrixSum)
    def matrixAvg(self, prodNM, sumNM):
        self.avg = (1/prodNM)*sumNM

    # Wyliczanie wariancji (Proponowane rozwiązanie podpunkt 4.)
    def matrixVariance(self, matrix, mAvg):
        # wyznaczenie wielkosci macierzy
        N_size = len(matrix)
        M_size = len(matrix[0])
        prod_NM = N_size * M_size
        temp_sum = 0

        # wyliczenie sumy kwadratow
        for i in range(0, N_size):
            for j in range(0, M_size):
                temp_sum += pow((matrix[i][j] - mAvg), 2)

        # wyliczenie wariancji
        self.variance = (1/prod_NM)*temp_sum

    # wyliczanie odchylenia standardowego (Proponowane rozwiązanie podpunkt 5.)
    def matrixStd(self, variance):
        self.std = pow(variance, 0.5)

    # wyznaczenie histogramu (Proponowane rozwiązanie podpunkt 6.)
    def matrixHistogram(self, matrix):
        # tworzenia slownika kluczy od 0 do 255
        temp_hist = {}
        for i in range(0, 256):
            temp_hist[i] = 0

        # wyznaczenie wielkosci macierzy
        N_size = len(matrix)
        M_size = len(matrix[0])

        # wyznaczenie histogramu
        for i in range(0, N_size):
            for j in range(0, M_size):
                temp_hist[matrix[i][j]] += 1

        self.histogram = dict(temp_hist)

    # wyliczenie entropii (Proponowane rozwiązanie podpunkt 7.)
    # funkcja przyjmuje liste wartości histogramu unormowanego
    def imgEntropy(self, val_hist):
        temp_entropy = 0
        # wyznaczenie sumy kolejnych wartości histogramu unormowanego
        # sprawdzenie czy wartość histogramu nie jest równa 0
        for i in range(0, 256):
            if val_hist[i] is not 0:
                temp_entropy += val_hist[i]*log2(val_hist[i])
            # jeśli jest to ominięcie
            else:
                pass

        self.entropy = -temp_entropy


def main():
    pass
