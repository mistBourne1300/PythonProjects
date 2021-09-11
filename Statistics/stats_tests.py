#import data.csv
import math

#TODO: Measures of central tendency

def calc_mean(numbers):
    return sum(numbers) / len(numbers)

def calc_median(numbers):
    numbers.sort()
    if (len(numbers) % 2 == 0):
        median_loc = int(len(numbers) / 2)
        return calc_mean([numbers[median_loc], numbers[median_loc + 1]])
    median_loc = int((len(numbers) + 1)/ 2)
    return numbers[median_loc]

def calc_mode(numbers):
    modes = []
    mode_freq = []
    for num in numbers:
        if(num not in modes):
            modes.append(num)
            mode_freq.append(1)
        else:
            mode_freq[modes.index(num)] += 1
    
    return modes[mode_freq.index(max(mode_freq))]


#TODO: Measures of variability

def calc_range(numbers):
    numbers.sort()
    return numbers[-1] - numbers[0]

def calc_variance(numbers):
    average = calc_mean(numbers)
    df = len(numbers) - 1
    sum_of_squares = 0
    for num in numbers:
        sum_of_squares += (num - average)**2
    return sum_of_squares / df

def calc_standard_deviation(numbers):
    return math.sqrt(calc_variance(numbers))

#TODO: Correlation and Regression

def calc_covariance(x_nums, y_nums):
    if len(x_nums) is not len(y_nums):
        raise ValueError("Covariance Error: X and Y of diff length")
    x_avg = calc_mean(x_nums)
    y_avg = calc_mean(y_nums)
    product_sum = 0
    for i in range(len(x_nums)):
        product_sum += (x_nums[i] - x_avg) * (y_nums[i] - y_avg)
    return product_sum / (len(x_nums) - 1)

def calc_pearsons_r(x_nums, y_nums):
    return calc_covariance(x_nums, y_nums) / (calc_standard_deviation(x_nums) * calc_standard_deviation(y_nums))

def calc_regression_line(x_nums, y_nums):
    b = calc_covariance(x_nums, y_nums) / calc_variance(x_nums)
    a = calc_mean(y_nums) - (b * calc_mean(x_nums))
    return b, a

def calc_unexplained_variation(x_nums, y_nums):
    b, a = calc_regression_line(x_nums, y_nums)
    y_avg = calc_mean(y_nums)
    unexplained_variation = 0.0
    for i in range(len(x_nums)):
        y_pred = b*x_nums[i] + a
        unexplained_variation += (y_nums[i] - y_pred) ** 2
    return unexplained_variation

def calc_explained_variation(x_nums, y_nums):
    b, a = calc_regression_line(x_nums, y_nums)
    y_avg = calc_mean(y_nums)
    explained_variation = 0.0
    for i in range(len(x_nums)):
        y_pred = b*x_nums[i] + a
        explained_variation += (y_pred - y_avg) ** 2
    return explained_variation

def calc_total_variation(x_nums, y_nums):
    y_mean = calc_mean(y_nums)
    total_variation = 0.0
    explained_variation = 0.0
    for y in y_nums:
        total_variation += (y - y_mean) ** 2
    return total_variation

def calc_r_squared(x_nums, y_nums):
    return calc_explained_variation(x_nums, y_nums) / calc_total_variation(x_nums, y_nums)


#TODO: Hypothesis testing

def calc_one_mean_t_test(numbers, meu, sig = None): #if sigma is known, use that to calculate the t-test
    if not sig:
        sig = calc_standard_deviation(numbers)
    x_avg = calc_mean(numbers)
    t = (x_avg - meu) / (sig / math.sqrt(len(numbers)))
    return t

def do_pool_variances(x1, x2):
    if(len(x1) == len(x2)):
        return False
    x1_variance = calc_variance(x1)
    x2_variance = calc_variance(x2)
    if (x2_variance * 4 <= x1_variance) or (x1_variance * 4 <= x2_variance):
        return True
    return False

def calc_pooled_variance(x1, x2):
    x1_variance = calc_variance(x1)
    x2_variance = calc_variance(x2)
    return (((len(x1)-1) * x1_variance) + ((len(x2)-1) * x2_variance)) / (len(x1) + len(x2) - 2)

def calc_independent_samples_t_test(x1, x2):
    std_err = math.sqrt((calc_variance(x1) / len(x1)) + (calc_variance(x2) / len(x2)))
    x1_avg = calc_mean(x1)
    x2_avg = calc_mean(x2)
    if do_pool_variances(x1, x2):
        print(f'pooling variances: {calc_variance(x1)}, {calc_variance(x2)}')
        pooled_variance = calc_pooled_variance(x1, x2)
        #print(pooled_variance)
        std_err = math.sqrt((pooled_variance / len(x1)) + (pooled_variance / len(x2)))
    return (x1_avg - x2_avg) / std_err

def difference_scores(before, after):
    if len(before) is not len(after):
        raise ValueError("Diff Scores Error: X and Y of diff length")
    diff = []
    for i in range(len(before)):
        diff.append(after[i] - before[i])
    return diff

def related_samples_t_test(before, after):
    diff = difference_scores(before, after)
    diff_mean = calc_mean(diff)
    diff_std_dev = calc_standard_deviation(diff)
    t = diff_mean / (diff_std_dev / math.sqrt(len(diff)))
    return t


#TODO: ANOVA

def between_SS(observations):
    row_means = []
    for row in observations:
        row_means.append(calc_mean(row))
    grand_mean = calc_mean(row_means)
    between_sum_of_squares = 0
    for i in range(len(observations)):
        num_scores_in_row = len(observations[i])
        between_sum_of_squares += num_scores_in_row * ((row_means[i] - grand_mean)**2)
    degrees_of_freedom = len(observations) - 1
    return between_sum_of_squares, degrees_of_freedom

def within_SS(observations):
    within_sum_of_squares = 0
    num_observations = 0
    for row in observations:
        row_mean = calc_mean(row)
        for num in row:
            num_observations += 1
            within_sum_of_squares += (num - row_mean)**2
    degrees_of_freedom = num_observations - len(observations) # (N - C)
    return within_sum_of_squares, degrees_of_freedom

def total_SS(observations):
    total_sum_of_sqaures = 0
    row_means = []
    for row in observations:
        row_means.append(calc_mean(row))
    grand_mean = calc_mean(row_means)
    degrees_of_freedom = 0
    for row in observations:
        for num in row:
            degrees_of_freedom += 1
            total_sum_of_sqaures += (num - grand_mean)**2
    degrees_of_freedom -= 1
    return total_sum_of_sqaures, degrees_of_freedom

def One_Way_ANOVA(observations): #accepts a list of lists, and calculates an ANOVA for them
    SS_between, df_between = between_SS(observations)
    SS_within, df_within = within_SS(observations)
    SS_total, df_total = total_SS(observations)
    if(df_within + df_between != df_total):
        raise ValueError("One way ANOVA: Error in df calculations")
    MS_between = SS_between / df_between
    MS_within = SS_within / df_within
    F_ratio = MS_between / MS_within
    return F_ratio


#TODO: Chi-squared

def chi_squared(frequencies): #accepts a list of frequency lists (the rows of a chi-squared table)
    if (len(frequencies) == 1): #there is only one row, the expected value is the mean of the list.
        freq = frequencies[0]
        expected_value = calc_mean(freq)
        chi_sqrd= 0
        for observed in freq:
            chi_sqrd += ((observed - expected_value)**2) / expected_value
        return chi_sqrd
    else: # there is a table of observations, we need to calculate the totals of the rows and columns
        row_totals = [] # goes from top(0) to bottom(n-1)
        column_totals = [] # from left (0) to right(n-1)
        grand_total = 0
        for row in frequencies:
            row_totals.append(sum(row))
        
        for i in range(len(frequencies[0])): 
            # this will only work if each row has the same number of observations
            # which they should
            column_sum = 0
            for j in range(len(frequencies)):
                #print(i, j, sep = ",")
                column_sum += frequencies[j][i]
            column_totals.append(column_sum)
        
        
        if(sum(column_totals) != sum(row_totals)):
            raise ValueError("Chi-squared error: row totals and columns totals not equal")
        grand_total = sum(row_totals)
        """print(column_totals)
        print(row_totals)
        print(grand_total)"""
        expected_values = []
        for i in range(len(frequencies)):
            expected_values.append([])
            for j in range(len(frequencies[0])):
                expected_values[i].append([])
        #print(expected_values)
        for i in range(len(frequencies)):
            for j in range(len(frequencies[0])):
                expected_values[i][j] = (row_totals[i] * column_totals[j]) / grand_total
        #print(expected_values)

        chi_sqrd = 0
        for i in range(len(frequencies)):
            for j in range(len(frequencies[0])):
                chi_sqrd += ((frequencies[i][j] - expected_values[i][j]) ** 2) / expected_values[i][j]
        return chi_sqrd

        



