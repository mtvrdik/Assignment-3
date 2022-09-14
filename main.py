# Start your assignment here
print("Assignment 3")
# Problem 1: Lists, Sets and Coercion
one_a = [5, 6, 7, 2, 3, 6, 9, 2, 1, 7, 7, 7, 1]
print(one_a)
one_b = one_a[4] + 3
print(one_b)
one_c = [float(x) for x in one_a]
print(one_c)
one_d = set(one_a)
print(one_d)
one_e = one_d.add(10)
print(one_e)
# I'm a little confused why this returns 'None'
one_f = one_d.pop()
print(one_d)
one_g = len(one_d)
print(one_g)
one_h = len(one_d) == len(one_a)
print(one_h)
one_i = list(one_d) + one_a
print(one_i)
one_j = set(one_i)
print(one_j)
one_i = len(one_j)
print(one_i)
# Problem 2: Dictionary woes
two_patient_dictionary_kinoko = {
    "name": "Kinoko",
    "year": 2021
}
two_patient_dictionary_dango = {
    "name": "Dango",
    "year": 2019
}
two_patient_dictionary_mochi = {
    "name": "Mochi",
    "year": 2020
}
two_a = {
    "two_patient_dictionary_kinoko": two_patient_dictionary_kinoko,
    "two_patient_dictionary_dango": two_patient_dictionary_dango,
    "two_patient_dictionary_mochi": two_patient_dictionary_mochi
}
print(two_a)
two_b = two_patient_dictionary_dango["name"]
print(two_b)
two_patient_dictionary_mochi["year"] = 2018
print(two_a)
two_d = {
    "kinoko": 2021,
    "dango": 2019,
    "mochi": 2019
}
print(two_d)
two_e = (list(two_d))
print(two_e)
two_f = two_d.values()
print(two_f)
two_g = dict(zip(two_f, two_e))
print(two_g)
# Problem 3: Set combinations
three_setA = {1, 2, 3, 4, 5}
three_setB = {2, 3, 4, 5, 6}
three_setC = {3, 5, 7, 9}
three_setD = {2, 4, 6, 8}
three_setE = {1, 2, 3, 4}
three_a = three_setE.issubset(three_setA)
print(three_a)
three_b = three_setE < three_setA
print(three_b)
three_c = three_setA.intersection(three_setB)
print(three_c)
three_d = three_setC.union(three_setD, three_setE)
print(three_d)
three_e = three_d.add(3)
print(three_e)
three_f = three_e == one_a
print(three_f)
# these are not the same because three_e is a set and one_a is a list. We would need to change types and values'''
# Problem 4: Changing variable types
four_a = 8
four_b = []
four_b.append(type(four_a))
print(four_b)
four_b.append(0.39)
print(four_b)
four_b.append(type(0.39))
print(four_b)
four_b.append(round(pow(0.39, -10)))
print(four_b)
four_b.append(type(four_b[3]))
print(four_b)
# Problem 5: More variable type changes
five_a = {
    0: "<class 'int'>",
    1: 0.39,
    2: "<class 'float'>",
    3: 12284,
    4: "<class 'int'>"
}
print(five_a)
five_a[5]=str(300)
print(five_a)
four_b.append(five_a[5])
four_b.append(type(five_a[5]))
print(four_b)
slice(five_a)
print(five_a)
# I got quite confused with the instructions on number 5 but the rest of the instructions for the assigment make sense

