# 🧠 Alzheimer's Disease Visualization Project

## 📊 Project Overview

This project uses a dataset of over 2,000 patient records to explore patterns in Alzheimer's disease diagnoses through interactive data visualizations. We aim to uncover trends related to demographics, comorbidities, cognitive assessments, and familial risk factors. By making the data explorable, this project supports a deeper understanding of Alzheimer's risk and its broader healthcare context.

---

## 🛠 Tools & Technologies

- **Database**: MongoDB 
- **Backend**: Flask (API routes for interactive visualizations)
- **Python Libraries**:
  - `Pandas`, `Matplotlib`, `Seaborn`
  -  **New Library**: `Altair`
- **Frontend/Interactivity**:
  - HTML with dropdowns and filters
  - Flask API dynamically serving charts based on user input

---

## 📈 Core Questions Explored

1. **What patterns, if any, emerge in the distribution of Alzheimer’s diagnoses across different racial groups in the dataset, and how might these patterns inform future research on health equity and access to care?**
   - *Purpose:* Examine potential disparities in diagnosis distribution across races
   - *Visualization:* Normalized bar chart or percentage-based comparison

2. **What comorbid conditions (e.g., diabetes, hypertension, cardiovascular disease) are most common among diagnosed patients?**
   - *Purpose:* Identify overlap between chronic illnesses and Alzheimer's
   - *Visualization:* Stacked bar chart or heatmap comparing diagnosis vs. comorbidity presence

3. **Are patients with a family history of Alzheimer’s more likely to be diagnosed?**
   - *Purpose:* Explore family history as a contributing factor to diagnosis
   - *Visualization:* Grouped bar chart or logistic comparison with/without family history

4. **What are the strongest predictors of an Alzheimer’s diagnosis?**
   - *Purpose:* Evaluate which variables (e.g. age, MMSE, family history) correlate most strongly with diagnosis
   - *Visualization:* Correlation matrix, feature importance plots

5. **Group Comparisons:**
   - *Compare cognitive test scores between diagnosed and non-diagnosed groups*
   - *Compare prevalence of symptoms (Forgetfulness, Disorientation, etc.) by age or gender*
   - *Purpose:* Understand clinical and demographic patterns
   - *Visualization:* Box plots, bar charts, grouped visuals by age/gender

---

## ⚖️ Ethical Considerations

We acknowledge the importance of ethical data use in healthcare research. This project makes every effort to:
- Use anonymized and non-identifiable data
- Avoid implying causation from observational patterns
- Frame demographic analyses with care, especially around race and gender
- Disclose the dataset’s limitations and representativeness
- Use colorblind-accessible palettes and readable formatting for inclusivity

---

## 📚 Data & References

Dataset: cleaned_alzheimers_disease_data.csv provided via Kaggle

## 👥 Contributors
- **Haby Sarr**

- **Krishna Sigde**

- **Rache Morris**

- **Esteban Ortega**
