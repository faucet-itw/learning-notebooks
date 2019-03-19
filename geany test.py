
# Bar plot.

# Importing matplotlib to plot the graphs.
import matplotlib.pyplot as plt

# Importing pandas for using pandas dataframes.
import pandas as pd

# Reading the input file.
df = pd.read_csv("property_tax_report_2018.csv")

# Removing the null values in PROPERTY_POSTAL_CODE.
df = df[(df['PROPERTY_POSTAL_CODE'].notnull())]

# Grouping by YEAR_BUILT and aggregating based on PID to count the number of properties for each year.
df = df[['PID', 'YEAR_BUILT']].groupby('YEAR_BUILT', as_index = False).count().astype('int').rename(columns = {'PID':'No_of_properties_built'})

# Filtering YEAR_BUILT and keeping only the values between 1900 to 2018.
df = df[(df['YEAR_BUILT'] >= 1900) & (df['YEAR_BUILT'] <= 2018)]

# X-axis: YEAR_BUILT
x = df['YEAR_BUILT']

# Y-axis: Number of properties built.
y = df['No_of_properties_built']

# Change the size of the figure (in inches).
plt.figure(figsize=(17,6))

# Plotting the graph using x and y with 'dodgerblue' color.
# Different labels can be given to different bar plots in the same plot.
# Linewidth determines the width of the line.
plt.bar(x, y, label = 'Number of properties built', color = 'dodgerblue',  width = 1, alpha = 0.7) #align = 'center' not working
# plt.bar(x2, y2, label = 'Bar 2', color = 'red',  width = 1)

# X-axis label.
plt.xlabel('YEAR', fontsize = 16)

# Y-axis label.
plt.ylabel('Number of properties built', fontsize = 16)

# Title of the plot.
plt.title('Number of houses built between\n1900 and 2018', fontsize = 16)

# Grid
# plt.grid(True)
plt.grid(axis='y')

# Legend for the plot.
plt.legend()

# Saving the figure on disk. 'dpi' and 'quality' can be adjusted according to the required image quality.
plt.savefig('Bar_plot.jpeg', dpi = 400, quality = 100)

# Displays the plot.
plt.show()



