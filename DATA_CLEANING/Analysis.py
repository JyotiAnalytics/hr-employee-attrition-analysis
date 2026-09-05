# ============================================================
# HR EMPLOYEE ATTRITION ANALYSIS
# ============================================================


# -----------------------------
# 1. IMPORT LIBRARIES
# -----------------------------

import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# -----------------------------
# 2. LOAD DATASET
# -----------------------------

# Path to the directory where the script is located
# Example:
# HR_Employee_DA/
#     Data/
#         analysis.py

script_dir = os.path.dirname(
    os.path.abspath(__file__)
)

# Move up one level to project root
# HR_Employee_DA/
project_root = os.path.dirname(script_dir)

# Construct absolute path to CSV
file_path = os.path.join(
    project_root,
    "Dataset",
    "WA_Fn-UseC_-HR-Employee-Attrition.csv"
)

print("CSV Path:", file_path)


# Read CSV file
df = pd.read_csv(file_path)


# -----------------------------
# 3. BASIC DATA INFORMATION
# -----------------------------

print("\n========== FIRST 5 ROWS ==========")
print(df.head())

print("\n========== LAST 5 ROWS ==========")
print(df.tail())

print("\n========== SHAPE ==========")
print(df.shape)

print("\n========== COLUMNS ==========")
print(df.columns.tolist())

print("\n========== DATA TYPES ==========")
print(df.dtypes)

print("\n========== INFORMATION ==========")
df.info()

print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())

print("\n========== CATEGORICAL SUMMARY ==========")
print(df.describe(include="object"))


# -----------------------------
# 4. MISSING VALUE ANALYSIS
# -----------------------------

print("\n========== MISSING VALUES ==========")

missing_values = df.isnull().sum()

print(missing_values)

print("\nTotal Missing Values:")
print(df.isnull().sum().sum())


# -----------------------------
# 5. DUPLICATE ANALYSIS
# -----------------------------

print("\n========== DUPLICATE ROWS ==========")

duplicate_count = df.duplicated().sum()

print("Duplicate Rows:", duplicate_count)


# Remove duplicates
df = df.drop_duplicates()

print("Shape after removing duplicates:", df.shape)


# -----------------------------
# 6. UNIQUE VALUES
# -----------------------------

print("\n========== UNIQUE VALUES ==========")

for column in df.columns:
    print("\nColumn:", column)
    print(df[column].unique())


# -----------------------------
# 7. ATTRITION ANALYSIS
# -----------------------------

print("\n========== ATTRITION COUNT ==========")

print(
    df["Attrition"].value_counts()
)


print("\n========== ATTRITION PERCENTAGE ==========")

attrition_percentage = (
    df["Attrition"]
    .value_counts(normalize=True)
    * 100
)

print(attrition_percentage)


# -----------------------------
# 8. OVERALL ATTRITION RATE
# -----------------------------

total_employees = len(df)

employees_left = (
    df["Attrition"] == "Yes"
).sum()

employees_stayed = (
    df["Attrition"] == "No"
).sum()

attrition_rate = (
    employees_left
    / total_employees
    * 100
)

print("\n========== OVERALL ATTRITION ==========")

print("Total Employees:", total_employees)
print("Employees Left:", employees_left)
print("Employees Stayed:", employees_stayed)

print(
    "Overall Attrition Rate:",
    round(attrition_rate, 2),
    "%"
)


# -----------------------------
# 9. ATTRITION VISUALIZATION
# -----------------------------

plt.figure(figsize=(7, 5))

sns.countplot(
    data=df,
    x="Attrition"
)

plt.title(
    "Employee Attrition Count"
)

plt.xlabel("Attrition")

plt.ylabel(
    "Number of Employees"
)

plt.show()


# -----------------------------
# 10. DEPARTMENT ANALYSIS
# -----------------------------

print("\n========== DEPARTMENT COUNT ==========")

print(
    df["Department"].value_counts()
)


# Department-wise attrition
department_attrition = (
    df.groupby("Department")["Attrition"]
    .apply(
        lambda x:
        (x == "Yes").mean() * 100
    )
    .sort_values(
        ascending=False
    )
)

print(
    "\n========== DEPARTMENT ATTRITION RATE =========="
)

print(
    department_attrition
)


# -----------------------------
# 11. DEPARTMENT VISUALIZATION
# -----------------------------

plt.figure(figsize=(9, 5))

sns.barplot(
    x=department_attrition.index,
    y=department_attrition.values
)

plt.title(
    "Attrition Rate by Department"
)

plt.xlabel("Department")

plt.ylabel(
    "Attrition Rate (%)"
)

plt.xticks(rotation=20)
plt.savefig("Attrition Rate by Department")
plt.show()


# -----------------------------
# 12. JOB ROLE ANALYSIS
# -----------------------------

jobrole_attrition = (
    df.groupby("JobRole")["Attrition"]
    .apply(
        lambda x:
        (x == "Yes").mean() * 100
    )
    .sort_values(
        ascending=False
    )
)

print(
    "\n========== JOB ROLE ATTRITION RATE =========="
)

print(jobrole_attrition)


# -----------------------------
# 13. JOB ROLE VISUALIZATION
# -----------------------------

plt.figure(figsize=(10, 6))

sns.barplot(
    x=jobrole_attrition.values,
    y=jobrole_attrition.index
)

plt.title(
    "Attrition Rate by Job Role"
)

plt.xlabel(
    "Attrition Rate (%)"
)
plt.savefig(
    "Attrition Rate by Job Role"
)
plt.ylabel("Job Role")

plt.show()


# -----------------------------
# 14. OVERTIME ANALYSIS
# -----------------------------

overtime_attrition = (
    df.groupby("OverTime")["Attrition"]
    .apply(
        lambda x:
        (x == "Yes").mean() * 100
    )
    .sort_values(
        ascending=False
    )
)

print(
    "\n========== OVERTIME ATTRITION RATE =========="
)

print(overtime_attrition)


# -----------------------------
# 15. OVERTIME VISUALIZATION
# -----------------------------

plt.figure(figsize=(7, 5))

sns.barplot(
    x=overtime_attrition.index,
    y=overtime_attrition.values
)

plt.title(
    "Attrition Rate by Overtime"
)

plt.xlabel("Overtime")

plt.ylabel(
    "Attrition Rate (%)"
)
plt.savefig(
    "Attrition Rate by Overtime"
)
plt.show()


# -----------------------------
# 16. JOB SATISFACTION
# -----------------------------

job_satisfaction_attrition = (
    df.groupby("JobSatisfaction")["Attrition"]
    .apply(
        lambda x:
        (x == "Yes").mean() * 100
    )
)

print(
    "\n========== JOB SATISFACTION ATTRITION =========="
)

print(
    job_satisfaction_attrition
)


# -----------------------------
# 17. JOB SATISFACTION VISUALIZATION
# -----------------------------

plt.figure(figsize=(8, 5))

sns.barplot(
    x=job_satisfaction_attrition.index,
    y=job_satisfaction_attrition.values
)

plt.title(
    "Attrition Rate by Job Satisfaction"
)

plt.xlabel(
    "Job Satisfaction Level"
)

plt.ylabel(
    "Attrition Rate (%)"
)
plt.savefig(
    "Attrition Rate by Job Satisfaction"
)

plt.show()


# -----------------------------
# 18. WORK-LIFE BALANCE
# -----------------------------

worklife_attrition = (
    df.groupby("WorkLifeBalance")["Attrition"]
    .apply(
        lambda x:
        (x == "Yes").mean() * 100
    )
)

print(
    "\n========== WORK-LIFE BALANCE ATTRITION =========="
)

print(worklife_attrition)


# -----------------------------
# 19. BUSINESS TRAVEL
# -----------------------------

travel_attrition = (
    df.groupby("BusinessTravel")["Attrition"]
    .apply(
        lambda x:
        (x == "Yes").mean() * 100
    )
    .sort_values(
        ascending=False
    )
)

print(
    "\n========== BUSINESS TRAVEL ATTRITION =========="
)

print(travel_attrition)


# -----------------------------
# 20. SALARY BAND
# -----------------------------

df["SalaryBand"] = pd.cut(
    df["MonthlyIncome"],
    bins=[
        0,
        3000,
        6000,
        10000,
        np.inf
    ],
    labels=[
        "Low",
        "Medium",
        "High",
        "Very High"
    ]
)

print(
    "\n========== SALARY BAND COUNT =========="
)

print(
    df["SalaryBand"].value_counts()
)


# -----------------------------
# 21. SALARY VS ATTRITION
# -----------------------------

salary_attrition = (
    df.groupby(
        "SalaryBand",
        observed=False
    )["Attrition"]
    .apply(
        lambda x:
        (x == "Yes").mean() * 100
    )
)

print(
    "\n========== SALARY BAND ATTRITION =========="
)

print(salary_attrition)


# -----------------------------
# 22. SALARY VISUALIZATION
# -----------------------------

plt.figure(figsize=(8, 5))

sns.barplot(
    x=salary_attrition.index,
    y=salary_attrition.values
)

plt.title(
    "Attrition Rate by Salary Band"
)

plt.xlabel("Salary Band")

plt.ylabel(
    "Attrition Rate (%)"
)
plt.savefig(
    "Attrition Rate by Salary Band"
)
plt.show()


# -----------------------------
# 23. TENURE ANALYSIS
# -----------------------------

df["TenureBand"] = pd.cut(
    df["YearsAtCompany"],
    bins=[
        -1,
        2,
        5,
        10,
        np.inf
    ],
    labels=[
        "0-2 Years",
        "3-5 Years",
        "6-10 Years",
        "10+ Years"
    ]
)

print(
    "\n========== TENURE BAND COUNT =========="
)

print(
    df["TenureBand"].value_counts()
)


# -----------------------------
# 24. TENURE VS ATTRITION
# -----------------------------

tenure_attrition = (
    df.groupby(
        "TenureBand",
        observed=False
    )["Attrition"]
    .apply(
        lambda x:
        (x == "Yes").mean() * 100
    )
)

print(
    "\n========== TENURE ATTRITION =========="
)

print(tenure_attrition)


# -----------------------------
# 25. TENURE VISUALIZATION
# -----------------------------

plt.figure(figsize=(9, 5))

sns.barplot(
    x=tenure_attrition.index,
    y=tenure_attrition.values
)

plt.title(
    "Attrition Rate by Tenure"
)

plt.xlabel(
    "Years at Company"
)

plt.ylabel(
    "Attrition Rate (%)"
)


plt.savefig(
    "Attrition Rate by Tenure"
)
plt.show()


# -----------------------------
# 26. AGE BAND ANALYSIS
# -----------------------------

df["AgeBand"] = pd.cut(
    df["Age"],
    bins=[
        0,
        25,
        35,
        45,
        100
    ],
    labels=[
        "Under 25",
        "25-35",
        "36-45",
        "46+"
    ]
)

age_attrition = (
    df.groupby(
        "AgeBand",
        observed=False
    )["Attrition"]
    .apply(
        lambda x:
        (x == "Yes").mean() * 100
    )
)

print(
    "\n========== AGE BAND ATTRITION =========="
)

print(age_attrition)


# -----------------------------
# 27. DISTANCE FROM HOME
# -----------------------------

df["DistanceBand"] = pd.cut(
    df["DistanceFromHome"],
    bins=[
        0,
        5,
        10,
        20,
        np.inf
    ],
    labels=[
        "0-5 km",
        "6-10 km",
        "11-20 km",
        "20+ km"
    ]
)

distance_attrition = (
    df.groupby(
        "DistanceBand",
        observed=False
    )["Attrition"]
    .apply(
        lambda x:
        (x == "Yes").mean() * 100
    )
)

print(
    "\n========== DISTANCE VS ATTRITION =========="
)

print(distance_attrition)


# -----------------------------
# 28. JOB LEVEL VS ATTRITION
# -----------------------------

joblevel_attrition = (
    df.groupby("JobLevel")["Attrition"]
    .apply(
        lambda x:
        (x == "Yes").mean() * 100
    )
)

print(
    "\n========== JOB LEVEL ATTRITION =========="
)

print(joblevel_attrition)


# -----------------------------
# 29. MARITAL STATUS
# -----------------------------

marital_attrition = (
    df.groupby("MaritalStatus")["Attrition"]
    .apply(
        lambda x:
        (x == "Yes").mean() * 100
    )
)

print(
    "\n========== MARITAL STATUS ATTRITION =========="
)

print(marital_attrition)


# -----------------------------
# 30. EDUCATION FIELD
# -----------------------------

education_attrition = (
    df.groupby("EducationField")["Attrition"]
    .apply(
        lambda x:
        (x == "Yes").mean() * 100
    )
    .sort_values(
        ascending=False
    )
)

print(
    "\n========== EDUCATION FIELD ATTRITION =========="
)

print(education_attrition)


# -----------------------------
# 31. ATTRITION NUMERIC ENCODING
# -----------------------------

df["AttritionNumeric"] = (
    df["Attrition"]
    .map({
        "No": 0,
        "Yes": 1
    })
)


# -----------------------------
# 32. CORRELATION ANALYSIS
# -----------------------------

numeric_columns = df.select_dtypes(
    include=np.number
).columns

correlation = (
    df[numeric_columns]
    .corr()
)

print(
    "\n========== CORRELATION MATRIX =========="
)

print(correlation)


# -----------------------------
# 33. CORRELATION WITH ATTRITION
# -----------------------------

attrition_correlation = (
    correlation["AttritionNumeric"]
    .drop("AttritionNumeric")
    .sort_values(
        ascending=False
    )
)

print(
    "\n========== CORRELATION WITH ATTRITION =========="
)

print(attrition_correlation)


# -----------------------------
# 34. TOP 5 NUMERIC FACTORS
# -----------------------------

top_5_factors = (
    attrition_correlation
    .abs()
    .sort_values(
        ascending=False
    )
    .head(5)
)

print(
    "\n========== TOP 5 NUMERIC FACTORS =========="
)

print(top_5_factors)


# -----------------------------
# 35. CORRELATION HEATMAP
# -----------------------------

plt.figure(
    figsize=(16, 12)
)

sns.heatmap(
    correlation,
    cmap="coolwarm",
    center=0
)

plt.title(
    "HR Employee Correlation Heatmap"
)

plt.savefig(
    "HR Employee Correlation Heatmap"
)
plt.show()


# -----------------------------
# 36. HIGH-RISK EMPLOYEE ANALYSIS
# -----------------------------

high_risk = df[
    (df["OverTime"] == "Yes") &
    (df["JobSatisfaction"] <= 2) &
    (df["YearsAtCompany"] <= 5)
]

print(
    "\n========== HIGH-RISK EMPLOYEES =========="
)

print(
    "Number of High-Risk Employees:",
    len(high_risk)
)


if len(high_risk) > 0:

    high_risk_rate = (
        high_risk["Attrition"]
        .eq("Yes")
        .mean()
        * 100
    )

    print(
        "High-Risk Attrition Rate:",
        round(high_risk_rate, 2),
        "%"
    )


# -----------------------------
# 37. DEPARTMENT + OVERTIME
# -----------------------------

department_overtime = pd.crosstab(
    [
        df["Department"],
        df["OverTime"]
    ],
    df["Attrition"],
    normalize="index"
) * 100

print(
    "\n========== DEPARTMENT + OVERTIME =========="
)

print(department_overtime)


# -----------------------------
# 38. FINAL BUSINESS SUMMARY
# -----------------------------

print(
    "\n=============================================="
)

print(
    "FINAL BUSINESS SUMMARY"
)

print(
    "=============================================="
)

print(
    "Total Employees:",
    total_employees
)

print(
    "Employees Left:",
    employees_left
)

print(
    "Employees Stayed:",
    employees_stayed
)

print(
    "Overall Attrition Rate:",
    round(attrition_rate, 2),
    "%"
)

print(
    "\nHighest Attrition Department:"
)

print(
    department_attrition.idxmax(),
    "->",
    round(
        department_attrition.max(),
        2
    ),
    "%"
)

print(
    "\nHighest Attrition Job Role:"
)

print(
    jobrole_attrition.idxmax(),
    "->",
    round(
        jobrole_attrition.max(),
        2
    ),
    "%"
)

print(
    "\nHighest Attrition Overtime Group:"
)

print(
    overtime_attrition.idxmax(),
    "->",
    round(
        overtime_attrition.max(),
        2
    ),
    "%"
)


# -----------------------------
# 39. SAVE ANALYSIS RESULTS
# -----------------------------

output_path = os.path.join(
    project_root,
    "Output",
    "HR_Attrition_Analysis.xlsx"
)

# Create Output folder if it doesn't exist
os.makedirs(
    os.path.dirname(output_path),
    exist_ok=True
)


with pd.ExcelWriter(
    output_path
) as writer:

    summary = pd.DataFrame({
        "Metric": [
            "Total Employees",
            "Employees Left",
            "Employees Stayed",
            "Attrition Rate (%)"
        ],

        "Value": [
            total_employees,
            employees_left,
            employees_stayed,
            round(attrition_rate, 2)
        ]
    })

    summary.to_excel(
        writer,
        sheet_name="Summary",
        index=False
    )

    department_attrition.to_excel(
        writer,
        sheet_name="Department"
    )

    salary_attrition.to_excel(
        writer,
        sheet_name="Salary"
    )

    tenure_attrition.to_excel(
        writer,
        sheet_name="Tenure"
    )

    overtime_attrition.to_excel(
        writer,
        sheet_name="Overtime"
    )

    attrition_correlation.to_excel(
        writer,
        sheet_name="Correlation"
    )


print(
    "\nExcel report saved at:"
)

print(output_path)


# ============================================================
# END OF PROJECT
# ============================================================