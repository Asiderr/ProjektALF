#!/usr/bin/env python
import os
import cv2
import numpy as np
from math import log2
from matplotlib import pyplot as plt


# klasa pobierająca nazy i sortujaca je
class getFileNames:
    # funkcja sortujaca  (Proponowane rozwiązanie podpunkt 1.)
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
            if val_hist[i] > 0:
                temp_entropy += val_hist[i]*log2(val_hist[i])
            # jeśli jest to ominięcie
            else:
                pass

        self.entropy = -temp_entropy


class plots:
    def figure1(self, nhist, num):
        # okreslenie osi natezenia jasnosci pikseli
        p = np.arange(0, 256)
        # zainicjowanie wykresu
        fig = plt.figure()
        # sklejenie wykresow
        fig.subplots_adjust(hspace=0.000)
        # stworzenie odpowiedniej liczby wykresow do ilosci plikow w folderze
        for i, v in enumerate(range(0, num)):
            v += 1
            # okreslenie miejsca wyswietlania ax
            ax1 = plt.subplot(num, 1, v)
            # okreslenie danych wyswietlanych
            ax1.bar(p, nhist[i], color='r')
            # wstawienie podtytulow osi
            if i is int(num/2):
                ax1.set_xlabel('Pixel propability [-]')
                ax1.set_ylabel('Pixel intensity [-]')
            # wstawienie jednej podzialki osi o wartosci polowy max value
            y = [(max(nhist[i])/2)]
            ax1.set_yticks(y)
        plt.show()

    def figure2(self, avg, std, ent, rough):
        # sprawdzenie czy w folderze images zanjdują sie pliki bez wartosci chropowatosci
        # jesli tak to usuniecie ich z listy
        if len(rough) is not len(avg):
            pop_n = len(avg)-len(rough)
            for i in range(0, pop_n):
                avg.pop()
                std.pop()
                ent.pop()
        # zainicjowanie wykresow
        fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
        # sklejenie wykresow
        fig.subplots_adjust(hspace=0.000)
        # zainicjowanie sredniej jasnosci
        ax1.plot(rough, avg, marker='o', linestyle=':', label='Brightness')
        # stworzenie zakresu zacieniowanego obszaru
        std_l = []
        std_h = []
        for i in range(0, len(avg)):
            std_l.append(avg[i]-std[i])
            std_h.append(avg[i]+std[i])
        # zainicjowanie zacieniowanego obszaru
        ax1.fill_between(rough, std_l, std_h, alpha=0.4, label=r"Standard deviation $\sigma$")
        # zainicjowanie entropii
        ax2.plot(rough, ent, marker='o', linestyle=':', label='Entropy', color='r')
        # stworzenie opisow osi
        ax1.legend()
        ax2.legend()
        # wlaczenie siatki wykresu
        ax1.grid()
        ax2.grid()
        # ustalenie zakresu osi y w pierwszym wykresie
        ax1.set_yticks(range(0, 256, 50))
        ax1.set_yticks(range(0, 256, 5), minor=True)
        plt.show()


def main():
    gfn = getFileNames()
    gfn.sortNames()
    # Wyciągnięcie chropowatości i posegregowanych nazw
    rough = gfn.sortedFl
    fileNames = gfn.sortedNames

    # Lista wszystkich macierzy obrazow
    imgMatrix = []
    ima = imageAnalysis()
    for i in fileNames:
        ima.getImages(i)
        imgMatrix.append(ima.img)

    # lista sumy elementow
    sumNM = []
    # lista z iloczynami N*M
    prodNM = []
    for i in imgMatrix:
        ima.matrixSum(i)
        sumNM.append(ima.NM_sum)
        prodNM.append(ima.productNM)

    # Lista wynikowa [[sredniaJasnosc_1, odchylenieStd_1, entropia_1],
    # [sredniaJasnosc_2, odchylenieStd_2, entropia_2],
    # ...,
    # [Lista slowników histogramow] ]
    vecsResult = []
    # lista srednich jasnosci do stworzenia wykresu
    avgfig = []
    for i in range(0, len(sumNM)):
        ima.matrixAvg(prodNM[i], sumNM[i])
        temp = [ima.avg]
        avgfig.append(ima.avg)
        vecsResult.append(temp)

    # lista z wynikami wariancji
    varian = []
    for i in range(0, len(imgMatrix)):
        ima.matrixVariance(imgMatrix[i], vecsResult[i])
        varian.append(ima.variance)

    stdfig = []
    # umieszczenie odchylenia standardowego w liscie wynikow
    for i in range(0, len(varian)):
        ima.matrixStd(varian[i])
        vecsResult[i].append(ima.std[0])
        stdfig.append(ima.std[0])

    histograms = []
    # okreslenie histogramow i umieszczenie ich w liscie wynikowej
    for i in imgMatrix:
        ima.matrixHistogram(i)
        histograms.append(ima.histogram)
    vecsResult.append(histograms)

    # stworzenie list wartosci histogramow unormowanych
    histNVal = []
    for i in range(0, len(histograms)):
        hist_temp = []
        for j in range(0, 256):
            hist_temp.append((histograms[i][j]/prodNM[i]))
        histNVal.append(hist_temp)

    entfig = []
    # umieszczenie entropii w liscie wynikow
    for i in range(0, len(histNVal)):
        ima.imgEntropy(histNVal[i])
        vecsResult[i].append(ima.entropy)
        entfig.append(ima.entropy)

    # Zapisanie wyników do pliku
    f = open('vecsResult.txt', 'w')
    f.write(str(vecsResult))
    f.close()

    # Uruchomienie rysunków
    pl = plots()
    pl.figure1(histNVal, len(histNVal))
    pl.figure2(avgfig, stdfig, entfig, rough)
    return vecsResult

main()
