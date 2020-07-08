#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 16:26:06 2020

@author: yashanand
"""
import fractions

class Sqrt2:
    def __init__(self, const, coeff):
        self.const = const
        self.coeff = coeff
    
    def __str__(self):
        return "{} + {} sqrt(2)".format(self.const, self.coeff)
    
    def __add__(self, other):
        add_const = self.const + other.const
        add_coeff = self.coeff + other.coeff
        return Sqrt2(add_const, add_coeff)
    
    def __sub__(self, other):
        sub_const = self.const - other.const
        sub_coeff = self.coeff - other.coeff
        return Sqrt2(sub_const, sub_coeff)
    
    def __mul__(self, other):
        mult_const = self.const*other.const + self.coeff*other.coeff*2
        mult_coeff = self.const*other.coeff + self.coeff*other.const
        return Sqrt2(mult_const, mult_coeff)
    
    def __truediv__(self, other):
        a = self.const
        b = self.coeff
        c = other.const
        d = other.coeff
        
        div_const = fractions.Fraction(a*c-2*b*d, c*c - 2*d*d)
        div_coeff = fractions.Fraction(b*c-a*d, c**2 - 2*d**2)
        
        return Sqrt2(div_const, div_coeff)
    
