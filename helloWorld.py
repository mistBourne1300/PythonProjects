"""myString = "helloworld_dark"
index = myString.find("_")
print(index)
theme = myString[:index]
print(myString[:index])
myString = myString.replace(theme, "default")
print(myString)"""

import Statistics.stats_tests as st
from Statistics.stats_tests import calc_independent_samples_t_test, calc_one_mean_t_test, calc_pearsons_r, difference_scores, related_samples_t_test

numbers = [9,3,3,1,3,5,6,19,5,2,9,33,93,0,19,19,19,19,19]
print(f'numbers: {numbers}')
print("\n*************************\n\n")

print("Measures of Central Tendency:")
print(f'mean = {st.calc_mean(numbers)}')
print(f'median = {st.calc_median(numbers)}')
print(f'mode = {st.calc_mode(numbers)}')

print("\nMeasures of Variability:")
print(f'range = {st.calc_range(numbers)}')
print(f'variance = {st.calc_variance(numbers)}')
print(f'standard deviation = {st.calc_standard_deviation(numbers)}')

Xs = [20, 18, 17, 17, 16, 14]
Ys = [13, 11, 9, 7, 5, 3]
print("\n\nRegression:", Xs, "\n", Ys)
print(f'covariance: {st.calc_covariance(Xs, Ys)}')
print(f'r: {st.calc_pearsons_r(Xs, Ys)}')
b, a = st.calc_regression_line(Xs, Ys)
print(f'regression: b={b}, a={a}')
print(f'unexplained vari: {st.calc_unexplained_variation(Xs, Ys)}')
print(f'explained vari: {st.calc_explained_variation(Xs, Ys)}')
print(f'total vari: {st.calc_total_variation(Xs, Ys)}')
print(f'r squared: {st.calc_r_squared(Xs, Ys)}')


print("\n\n T tests:\n")
Xs = [134, 129, 125, 125, 121, 116]
print(f"One Sample mean: {Xs}")
print(f"t sig = 15: {calc_one_mean_t_test(Xs, 100, sig = 15)}")
print(f't sig = None: {calc_one_mean_t_test(Xs, 110)}', end = "\n\n")
x1 = [28, 26, 25, 25, 24, 22]
x2 = [21, 19, 17, 17, 15, 13]
print(x1, x2)
print(f"\nIndependent Samples t-test: {calc_independent_samples_t_test(x1, x2)}", end="\n\n")
x1 = [86, 84, 83, 83, 82, 80]
x2 = [83, 81, 79, 77, 77, 75, 73, 71]
print(x1, x2)

print(f'Independent Samples t-test: {calc_independent_samples_t_test(x1, x2)}')

print("Related samples t-test:")

before = [81, 79, 77, 77, 75, 73]
after = [86, 84, 83, 83, 82, 80]
print("Difference: ", difference_scores(before, after))
print(f'Related samples t-test: {related_samples_t_test(before, after)}')


print("\n\n\nANOVA:")
observations = [[88, 85, 95, 65, 60, 75], [45, 54, 65, 75, 70, 60], [95, 90, 80, 70, 80, 80]]
print(f'between SS: {st.between_SS(observations)}')
print(f'withing SS: {st.within_SS(observations)}')
print(f'total SS: {st.total_SS(observations)}')
print(f'One-way ANOVA: {st.One_Way_ANOVA(observations)}')

print("\n\n\nChi-Squared")
observations = [[75, 60, 80, 50]]
print(f'single-row chi-squared: {st.chi_squared(observations)}')
observations = [[50, 40, 20, 35],
                [25, 60, 8, 40]]
print(f'multi-row chi-squared: {st.chi_squared(observations)}')