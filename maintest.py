#!/usr/bin/env python

from main import *
import unittest


class testGetFileNames(unittest.TestCase):
    def test_takingNames(self):
        c = getFileNames()
        c.sortNames()
        self.assertIn('testimg.jpg', c.fNames, msg="Blad pobierania nazw plikow")
"""
 Dopisać test do sortowania
    def test_ifSorted(self):
        c.getFileNames()
        c.sortNames()
        for name in c.fNames:
            self.assertTrue()
"""


class testImageAnalysis(unittest.TestCase):
    def test_getImages(self):
        c = imageAnalysis()
        c.getImages('testimg.jpg')
        # W komentarzu pokazanie obrazu
        """
        plt.imshow(c.img, cmap='gray', interpolation='bicubic')
        plt.show()
        """
        self.assertTrue(c.img is not None, msg="Blad pobrania obrazu")

    def test_matrixSum(self):
        c = imageAnalysis()
        matrix = [
            [0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 2, 0, 0, 0]
        ]
        c.matrixSum(matrix)
        self.assertEqual(c.NM_sum, 4, msg="Blad sumowania macierzy")
        self.assertEqual(c.productNM, 15, msg="Blad wyznaczania wielkosci macierzy")

    def test_matrixAvg(self):
        c = imageAnalysis()
        c.matrixAvg(15, 15)
        self.assertEqual(c.avg, 1, msg="Blad obliczania sredniej")

    def test_matrixVariance(self):
        c = imageAnalysis()
        matrix = [
            [0, 0, 0, 5, 0],
            [0, 0, 5, 0, 0],
            [0, 5, 0, 0, 0]
        ]
        c.matrixVariance(matrix, 1)
        self.assertEqual(c.variance, 4, msg="Blad wyliczania wariancji")

    def test_matrixStd(self):
        c = imageAnalysis()
        c.matrixStd(4)
        self.assertEqual(c.variance, 2, msg="Blad wyliczania odchylenia standardowego")

    def test_matrixHistogram(self):
        c = imageAnalysis()
        matrix = [
            [0, 0, 0, 5, 0],
            [0, 0, 5, 0, 0],
            [0, 5, 0, 0, 0]
        ]
        c.matrixHistogram(matrix)
        self.assertEqual(c.histogram[0], 12, msg="Blad wyznaczania histogramu")

    def test_imgEntropy(self):
        c = imageAnalysis()
        

if __name__ == '__main__':
    unittest.main()
