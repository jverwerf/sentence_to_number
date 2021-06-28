# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def sentence_to_number(input_txt):
    import sys
    with open(input_txt) as f:
        temp_input = f.readlines()[0]
    list_of_numbers = ["0","1","2","3","4","5","6","7","8","9"]
    dict_of_numbers = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    conv_of_numbers = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 
                       10:"ten", 11:"eleven", 12:'twelve',13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",
                      18:"eigteen",19:"nineteen",20:"twenty",30:"thirty",40:"fourty",50:"fifty",60:"sixty",70:"seventy",
                       80:"eighty",90:"ninety",100:"hundred",1000:"thousand",1000000:"million",1000000000:"billion"}
    conv_of_str = {"1":"one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine", 
                       "10":"ten", "11":"eleven", "12":'twelve',"13":"thirteen","14":"fourteen","15":"fifteen","16":"sixteen","17":"seventeen",
                      "18":"eigteen","19":"nineteen","20":"twenty","30":"thirty","40":"fourty","50":"fifty","60":"sixty","70":"seventy",
                       "80":"eighty","90":"ninety"}
    
    template_for_conv = [1,1,1,1]
    template_full_number = ['0','0','0','0','0','0','0','0','0','0','0','0']
    
    def string_to_number(string):
        temp_output_str_to_number = 0
        for digit in string:
            temp_output_str_to_number = 10 * temp_output_str_to_number + dict_of_numbers[digit]
        return temp_output_str_to_number
    
    def convert_hundred(number):
        output_string=''
        def tens(number):
            string = ''
            if string_to_number(number) < 20:
                string += conv_of_str[number]
            if string_to_number(number) > 20 and string_to_number(number) < 100:
                for count, digit in enumerate(reversed(number)):
                    temp_digit = dict_of_numbers[digit] * (10**count)
                    if temp_digit > 0 and temp_digit < 19:
                        string = '-' + conv_of_numbers[temp_digit] + string
                    if temp_digit > 19 and temp_digit < 100:
                        string = conv_of_numbers[temp_digit] + string
            return string
        if string_to_number(number) < 99:
            output_string += tens(number)
        if string_to_number(number) > 99 and string_to_number(number)%100==0:
            output_string += conv_of_str[number[0]] + ' hundred'
        if string_to_number(number) > 99 and string_to_number(number)%100!=0:
            output_string += conv_of_str[number[0]] + ' hundred and ' + tens(number[1:].lstrip('0'))
        return output_string

    #get int out of string
    numbers_str = []
    numbers_int = []
    numbers_dict = {}
    for word in temp_input.split():
        for letter in word:
            if letter in list_of_numbers:
                if word not in numbers_str:
                    numbers_str.append(word)
    
    if len(numbers_str) > 1:
        return "invalid input"
    
    for word in numbers_str:
        for letter in word:
            if letter not in list_of_numbers:
                return "invalid input"
    
    for count, digit in enumerate(reversed(numbers_str[0])):
        template_full_number[-count-1] = digit
    
    billions = ''
    millions = ''
    thousands = ''
    hundreds = ''
    for number in template_full_number[:3]:
        billions += number
    for number in template_full_number[3:6]:
        millions += number
    for number in template_full_number[6:9]:
        thousands += number
    for number in template_full_number[9:12]:
        hundreds += number
    list_of_hundred_numbers = [billions.lstrip('0'),millions.lstrip('0'),thousands.lstrip('0'),hundreds.lstrip('0')]
    
    output_string = ''
    if list_of_hundred_numbers[0] != '':
        output_string+= convert_hundred(list_of_hundred_numbers[0]) + ' billion, '
    if list_of_hundred_numbers[1] != '':
        output_string+= convert_hundred(list_of_hundred_numbers[1]) + ' million, '
    if list_of_hundred_numbers[2] != '':
        output_string+= convert_hundred(list_of_hundred_numbers[2]) + ' thousand, '
    if list_of_hundred_numbers[3] != '':
        if len(list_of_hundred_numbers[3])<3:
            output_string = output_string[:-2]
            output_string+=' and '
        output_string+= convert_hundred(list_of_hundred_numbers[3])
    sys.stdout.write(output_string)