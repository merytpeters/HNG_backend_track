#!/usr/bin/env python3
"""Number Classification"""
import requests


class ClassifyNumber:
    """Function that defines properties of a number"""

    def is_prime(self, num):
        """Prime number function"""
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            """Check the number up to its square root
            if it is divisble by any other number"""
            if num % i == 0:
                return False
        return True

    def is_perfect(self, num):
        """Perfect number is a number whose divisor sums up to it"""
        if num <= 1:
            return False
        total = 0
        for i in range(1, num):
            if (num % i == 0):
                total += i
        return total == num

    def digit_sum(self, num):
        """Check the sum of its digit"""
        total = 0
        if num:
            for digit in str(abs(num)):
                total += int(digit)
        return total

    def is_armstrong(self, num):
        """A number equal to the sum of its
        digit raise to the number of digits"""
        if num < 0:
            return
        num_of_digits = len(str(num))
        total = 0
        for digit in str(num):
            digit = int(digit) ** num_of_digits
            total += digit
        return total == num

    def is_odd_or_even(self, num):
        """Checks odd or even numbers"""
        if abs(num) % 2 == 0:
            return "even"
        return "odd"

    def fun_fact(self, num):
        """Calls numbersapi math type and checks if it's an Armstrong number"""
        try:
            response = requests.get(f"http://numbersapi.com/{num}/math")
            if response.status_code == 200:
                return response.text
            else:
                return "Could not retrieve fun fact"
        except requests.exceptions.RequestException:
            return "Error retrieving fun fact"
