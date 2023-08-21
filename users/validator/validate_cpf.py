####  ---------------- in progress ----------------------------------#


# import re

# from django.core.exceptions import ValidationError


# class CPFValidator:

#     @staticmethod
#     def __get_cpf_digits(value):
#         digits = re.sub(r'\D', '', value)
#         return int(digits)

#     def __calculate_digits(self, cpf, weight, first_digit=None, second_digit=None):
#         if not first_digit:
#             first_digit = self.__calculate_digits(cpf, weight=10)
#             return self.__calculate_digits(cpf, weight=11, first_digit=first_digit)
#         if not second_digit:
#             second_digit = self.__calculate_digits(cpf, weight=11, first_digit=first_digit)  
#             return self.__calculate_digits(cpf, weight=0, first_digit=first_digit, second_digit=second_digit)

#         if first_digit and second_digit:
#             return (first_digit, second_digit)   
        
#         sum_digit = 0
#         for _, digit in enumerate(cpf):
#             sum_digit += int(digit) * weight
#             weight -= 1

#         digit = 11 - (sum_digit % 11)
#         return digit if digit <= 9 else 0
            
        


#     def validate(self):
#         if len(cpf) != 11:
#             raise ValidationError('CPF deve conter 11 números', 'invalid')

#         first_digit = self.calculate_digit(cpf, weight=10)
#         second_digit = self.calculate_digit(cpf, weight=11)

#         if cpf in INVALIDS_CPFS or (not cpf[-2:] == f'{first_digit}{second_digit}'):
#             raise ValidationError('Número de CPF inválido', 'invalid')


