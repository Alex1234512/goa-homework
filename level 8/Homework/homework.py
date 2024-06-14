#დავალება 2
num1 = 10
num2 = 64

print(num1 != num2)
print(num1 >= num2)
print(num1 <= num2)

#დავალება 3
num1 = 7
num2 = 20

print(num1 == num2 and num1 != num2)
#ეს გამოიტანს error-ს რადგან პირველი არასწორია. ორივე უნდა იყოს სწორი რომ გამოიტანოს true
print(num1 == num2 or num1 != num2)
#ეს გამოიტანს true-ს რადგან მეორე სწორია. ერთერთი უნდა იყოს სწორი რომ გამოიტანოს true

print(num1 >= num2 and num1 <= num2)
#ეს გამოიტანს error-ს რადგან პირველი არასწორია. ორივე უნდა იყოს სწორი რომ გამოიტანოს true
print(num1 >= num2 or num1 <= num2)
#ეს გამოიტანს true-ს რადგან პირველი სწორია. ერთერთი უნდა იყოს სწორი რომ გამოიტანოს true

print(num1 > num2 and num1 < num2)
#ეს გამოიტანს error-ს რადგან პირველი არასწორია. ორივე უნდა იყოს სწორი რომ გამოიტანოს true
print(num1 > num2 or num1 < num2)
#ეს გამოიტანს true-ს რადგან მეორე სწორია. ერთერთი უნდა იყოს სწორი რომ გამოიტანოს true

#დავალება 4

# and ოპერატორს როცა ვწერთ print(num1 == num2 and num1 != num2) ორივე უნდა იყოს სწორი, თუ ერთერთი მაინც იქნება არასწორი მაშინ ეს გამოიტანს ერორს
# or ოპერატორს როცა ვწერთ print(num1 == num2 or num1 != num2) ერთერთი მაინც უნდა იყოს სწორი, თუ ორივე არასწორი იქნება გამოიტანს ერორს

#დავალება 5

num1 = int(input("Enter a first number"))
num2 = int(input("Enter a second number"))

print(num1 > num2)

print(num1 < num2)

print(num1 == num2)