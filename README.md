# Rotational-Shift-Assignment-Algorithm
Automatically generates a fair, preference-aware weekly 24/7 rotational shift schedule.
https://github.com/OmarGamill/Rotational-Shift-Assignment-Algorithm/blob/main/Algorithm.PNG
![Project Diagram](https://github.com/OmarGamill/Rotational-Shift-Assignment-Algorithm/blob/main/Algorithm.PNG)

---

##  Project Overview

This project implements a Python-based scheduling algorithm to assign agents to three daily shifts (Morning, Afternoon, Overnight) across a 7-day rotation. It ensures:
- Fair experience-level spread across all shifts.
- Respect for preferred shifts.
- Balanced distribution of overnight and weekend assignments
- Fairness in the number of total shifts, weekends, and overnights.
- Easy re-runability with updated workforce data

---
##  Repository Structure

```bash
├── new_dataset.xlsx      # Sample input dataset
├── Pipeline.py           # Main pipeline execution
├── ProcessData.py        # Preprocessing and data preparation
├── Utilis.py             # Utility functions
├── run.py                # Entry point — 
├── requirements.txt      # Python dependencies
├── writeHere.py          # Contains several variables used for configuration
└── README.md             # Project documentation
```
---

##  Getting Started

```bash
git clone https://github.com/OmarGamill/Rotational-Shift-Assignment-Algorithm.git

cd your_project_name

pip install -r requirements.txt

python run.py

```
