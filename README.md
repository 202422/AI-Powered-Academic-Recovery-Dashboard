# AI-Powered-Academic-Recovery-Dashboard
The project consists of building an AI-powered dashboard to help schools prioritize students in need of academic support. It leverages academic results and behavioral indicators to assess intervention value and complexity, enabling data-driven pedagogical decision-making



# **Summary of Insights**

## **1. Exploratory Data Analysis (EDA)**

### **Numerical features**

* **Positive correlations with FinalGrade**:

  * `Medu` (+0.19) and `Fedu` (+0.16) show the strongest positive associations.
  * `studytime` (+0.13) also contributes positively.
  * `famrel` (+0.038) has a very weak positive effect.

* **Negative correlations**:

  * `failures` (−0.29) and `absences` (−0.21) have the strongest negative relationships.
  * Alcohol consumption: `Walc` (−0.19), `Dalc` (−0.14).
  * Social activity: `goout` (−0.18).
  * Weaker negative effects observed for `age`, `traveltime`, `health`, and `freetime`.

---

### **Categorical features**

Out of 17 categorical variables, only the following show a significant relationship with `FinalGrade`:

* `address`
* `Mjob`
* `schoolsup`
* `higher`
* `internet`

---

## **2. Modeling Results (XGBoost Feature Importance)**

Top predictive features:

* `failures` (0.067)
* `schoolsup` (0.057)
* `internet` (0.048)
* `absences` (0.046)
* `studytime` (0.044)
* `Walc` (0.043)
* `sex` (0.043)
* `health` (0.038)

These features dominate model predictions.

---

## **3. SHAP Interpretation**

* `absences`: strong negative impact at high values.
* `failures`: consistently large negative contribution.
* `schoolsup`: strong positive contribution when present.
* `studytime`: clear positive and near-linear effect.
* `internet`: positive contribution when available.
* `Walc`: high values strongly decrease predictions.
* `goout`: moderate negative effect.
* `health`: poor values reduce predicted grades.

---

## **Overall Conclusion**

`failures`, `absences`, `studytime`, `schoolsup`, `internet`, and `Walc` are the most influential variables affecting `FinalGrade`.
Behavioral and academic engagement features outweigh demographic variables in predictive importance.

