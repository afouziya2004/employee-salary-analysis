import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\user\Desktop\ff\data\employee.csv")

# Basic overview
print("Dataset Preview:")
print(df.head())

# Salary statistics
print("\nSalary Statistics:")
print(df["Salary"].describe())

# Average salary by department
dept_salary = df.groupby("Department")["Salary"].mean()
print("\nAverage Salary by Department:")
print(dept_salary)

# High & low performers
high_performers = df[df["PerformanceRating"] >= 4]
low_performers = df[df["PerformanceRating"] <= 2]

print("\nHigh Performers:")
print(high_performers[["Name", "Department", "Salary"]])

print("\nLow Performers:")
print(low_performers[["Name", "Department", "Salary"]])

# Visualization
plt.figure()
dept_salary.plot(kind="bar")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.tight_layout()

# Save plot
plt.savefig("visuals/salary_plots.png")
plt.show()
