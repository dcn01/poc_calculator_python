import os
import unittest
import time
from appium import webdriver
from base_tests.base_test import BaseTest
from tests.pages import CalculatorPage



class CalculatorTest(BaseTest):

    UM   = "1"
    DOIS = "2"
    TRES = "3"
    QUATRO = "4"
    CINCO = "5"
    SEIS = "6"
    SETE = "7"
    OITO = "8"
    NOVE = "9"
    DEZ = "10"


    def setUp(self):
        BaseTest.setUp(self)
        self.calculator = CalculatorPage(self.driver)

    def test_mult(self):
        self.calculator.click_number(self.NOVE)
        self.calculator.click_mult()
        self.calculator.click_number(self.NOVE)
        self.calculator.click_equal()
        element = self.driver.find_element_by_id(self.calculator.DISPLAY).get_attribute("text")
        self.driver.implicitly_wait(0.5)
        assert element == "81"
        self.calculator.click_clear()
        self.driver.implicitly_wait(2)

    def test_sum(self):
        self.calculator.click_number(self.NOVE)
        self.calculator.click_sum()
        self.calculator.click_number(self.NOVE)
        self.calculator.click_equal()
        element = self.driver.find_element_by_id(self.calculator.DISPLAY).get_attribute("text")
        self.driver.implicitly_wait(0.5)
        assert element == "18"
        self.calculator.click_clear()
        self.driver.implicitly_wait(2)

    def test_sub(self):
        self.calculator.click_number(self.NOVE)
        self.calculator.click_sub()
        self.calculator.click_number(self.NOVE)
        self.calculator.click_equal()
        element = self.driver.find_element_by_id(self.calculator.DISPLAY).get_attribute("text")
        self.driver.implicitly_wait(0.5)
        assert element == "0"
        self.calculator.click_clear()
        self.driver.implicitly_wait(2)

    def test_div(self):
        self.calculator.click_number(self.NOVE)
        self.calculator.click_div()
        self.calculator.click_number(self.NOVE)
        self.calculator.click_equal()
        element = self.driver.find_element_by_id(self.calculator.DISPLAY).get_attribute("text")
        self.driver.implicitly_wait(0.5)
        assert element == "1"
        self.calculator.click_clear()
        self.driver.implicitly_wait(2)
