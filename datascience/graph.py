import matplotlib.pyplot as plt
#from collections import Counter

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(years, gdp, 'green', 'o', '-')
plt.axis([1950, 2010,0,16000])

plt.title("Nominal GDP")
plt.ylabel("Billions of $")
plt.show()
#막대그래프
movies=["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]
#xs = [i + 0.1 for i, _ in enumerate(movies)]
plt.bar(movies, num_oscars)
plt.ylabel("# of Academy Awards")
plt.title("My Favorite Movies")

plt.xticks(movies)
plt.show()

#히스토그램
grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]
#decile = lambda grade: grade // 10 * 10
#histogram = Counter(decile(grade) for grade in grades)
#plt.bar([0,10,20,30,40,50,60,70,80,90,100], histogram.values(), 8)
plt.hist(grades)
plt.axis([-5, 105, 0, 5])

plt.xticks([0,10,20,30,40,50,60,70,80,90,100])
plt.xlabel("Decile")
plt.ylabel("# of students")
plt.title("Distribution of Exam 1 Grades")
plt.show()

#선 그래프
variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error= [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]
plt.plot(xs, variance, 'g-', label='variance')
plt.plot(xs, bias_squared, 'r-.',label='bias^2')
plt.plot(xs, total_error, 'b:', label='total error')
plt.legend(loc=9)
plt.xlabel("model complexity")
plt.title("The Bias-Varience Tradeoff")
plt.show()

#산점도
friends = [70,65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

for i, txt in enumerate(labels):
    plt.annotate(txt, (friends[i], minutes[i]), xytext=(friends[i]+0.2, minutes[i]+0.2))

plt.title("Daily Minutes vs. Number of Friends")
plt.xlabel("# of friends")
plt.ylabel("daily minutes spent on the site")
plt.show()