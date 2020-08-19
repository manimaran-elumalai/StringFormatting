age = 23

print("My age is " + str(age) + " years")

print("My age is {} years".format(age))

print("My age is %d years" % age)

print("My age is %d %s %d %s" % (age, "years and",  6, "months"))

#  Below is how string formatting is done in the latest version of python

print("""There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}""".format
        (31, "Jan", "March", "May", "July", "Aug", "Oct", "Dec"))
print("""
Jan has {1} days
Feb has {0} days
Mar has {1} days
Apr has {2} days
May has {1} days
Jun has {2} days
Jul has {1} days
Aug has {1} days
Sep has {2} days
Oct has {1} days
Nov has {2} days
Dec has {1} days
""".format(28, 31, 30))

for i in range(1, 6):
    print("No. %2d squared is %4d and cubed is %4d" % (i, i ** 2, i ** 3))

for i in range(1,6):
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

print("Pi is approximately %12.50f" % (22 / 7))
print("Pi is approximately {0:12.50}".format(22 / 7))

# days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
# print(days[::5])

# data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F"
# print(data[:-1:5])

flower = "blue violet"
print('blue' in flower)
