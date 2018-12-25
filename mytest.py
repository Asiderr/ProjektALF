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


if __name__ == '__main__':
    unittest.main()
