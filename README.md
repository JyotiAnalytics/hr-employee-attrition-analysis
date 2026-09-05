
# Corporate HR Employee Attrition & Turnover Analysis

## 📌 Overview
An end-to-end HR analytics project analyzing employee attrition patterns using the IBM HR Analytics Employee Attrition dataset. The project combines Python-based exploratory data analysis with interactive Power BI and Excel dashboards, helping HR and business stakeholders identify the key drivers of employee turnover and flag high-risk employee segments.

## 🗂️ Dataset
- **Source:** IBM HR Analytics Employee Attrition dataset (`WA_Fn-UseC_-HR-Employee-Attrition.csv`)
- **Size:** 1,470 employee records across 35 attributes covering demographics, compensation, job role, satisfaction scores, and tenure

## 🛠️ Tools & Technologies
- **Python** — Pandas, NumPy, Matplotlib, Seaborn (data cleaning, EDA, correlation analysis)
- **Power BI** — interactive drill-down dashboard
- **Excel** — KPI dashboard and summary reporting

## 🔍 Project Workflow
1. **Data Cleaning** — checked for missing values and removed duplicate rows
2. **Exploratory Data Analysis** — attrition rate broken down by department, job role, overtime, job satisfaction, work-life balance, business travel, salary band, tenure, age band, distance from home, job level, marital status, and education field
3. **Correlation Analysis** — full correlation matrix and heatmap; ranked the numeric factors most associated with attrition
4. **High-Risk Segmentation** — flagged employees working overtime, with low job satisfaction (≤2), and ≤5 years of tenure as a high-risk group
5. **Business Summary Report** — key metrics and breakdowns exported to a formatted Excel workbook
6. **Dashboarding** — built both a Power BI dashboard and an Excel dashboard for non-technical stakeholders

## 📊 Key Insights
- **1,470** total employees analyzed — **237** left, **1,233** stayed, for an overall attrition rate of **16.12%**
- **Sales** is the highest-attrition department at **20.63%**
- **Sales Representative** is the highest-attrition job role by far, at **39.76%**
- Employees who work **overtime** attrit at **30.53%** — nearly double the company-wide rate
- **Single** employees show higher attrition than married or divorced employees
- **Younger employees** show a noticeably higher attrition rate than older, more tenured staff
- Job satisfaction, work-life balance, and years with current manager rank among the strongest factors associated with lower attrition

## 📁 Repository Structure
```
HR_Employee_Attrition_Analysis/
├── Dataset/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv
├── Analysis.py
├── Output/
│   └── HR_Attrition_Analysis.xlsx
├── Dashboards/
│   ├── IBM_HR_Analytics_Dashboard.pbix
│   └── HR_Attrition_Excel_Dashboard.xlsx
└── README.md
```

## ▶️ How to Run
```bash
pip install pandas numpy matplotlib seaborn openpyxl
python Analysis.py
```

## 📌 Business Recommendation
Since overtime and low job satisfaction are among the strongest predictors of attrition, HR should prioritize workload redistribution and satisfaction interventions for employees with under 5 years of tenure — the segment this analysis flags as highest-risk for turnover.

## 👤 Author
Jyoti Ranjan Bhanja — Aspiring Data Scientist / Data Analyst

