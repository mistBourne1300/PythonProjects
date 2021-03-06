import stats_tests as st
from scipy import stats

data = [   [7.75, 6.5, 7.0, 8.25, 6.0, 10.25, 8.0, 8.75, .75, 6.25, 6.75, 6.5, 8.25, 8.75, 9.5, 9.0, 8.0, 6.0, 4.5], 
            [6.5, 9.5, 8.25, 10.25, 6.5, 6.5, 10.0, 8.0, 8.5, 8.5, 6.25, 8.25, 8.0, 13.25, 8.25, 5.5, 5.5, 12.0, 2.5, 10.5],
            [10.0, 8.25, 10.0, 6.75, 6.5, 7.0, 7.5, 5.0, 7.5, 6.5, 6.5, 6.0, 7.0, 8.0, 7.5, 9.0, 6.5], 
            [11.0, 6.0, 8.75, 8.75, 9.25, 10.0, 5.0, 8.75, 5.0, 5.0, 5.75, 8.25, 6.5, 8.5, 4.0, 8.25, 5.75, 7.25, 6.25, 10.75],
            [6.75, 6.25, 8.75, 5.0, 10.25, 2.25, 8.25, 5.0, 7.5, 8.0, 8.5, 11.0, 7.5, 8.5, 5.0, 6.0, 9.75, 9.0, 9.0, 9.5]]

print("\n\n\nANOVA:")
observations = data
print(f'between SS: {st.between_SS(observations)}')
print(f'withing SS: {st.within_SS(observations)}')
print(f'total SS: {st.total_SS(observations)}')
print(f'One-way ANOVA: {st.One_Way_ANOVA(observations)}')

p_value = 1 - stats.f.cdf(st.One_Way_ANOVA(observations), st.between_SS(observations)[1], st.within_SS(observations)[1])
print(p_value)