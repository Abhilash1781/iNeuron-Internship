#  Prediction of LC50 value using Quantitative    Structure Activity Relationship models

## Table of contents
* [Demo](#demo)
* [Overview](#overview)
* [Project Goal](#project-goal)
* [Technical Aspects](#technical-aspects)
* [Installation](#installation)
* [Feature Request](#feature-request)
* [Used Technologies](#used-technologies)
* [Appendix](#appendix)
* [Author](#author)
* [License](#license)
* [Feedback](#feedback)

  ## Demo
  Link for web application : https://aquatic-toxicity.streamlit.app/

  ## Overview
  The prediction of LC50 (Lethal Concentration, 50%) for fish toxicity, specifically towards
   fathead minnows, is a critical aspect of environmental monitoring and risk assessment in
  aquatic ecosystems. LC50 represents the concentration of a substance in water that is expected
  to cause mortality in 50% of the exposed fish population over a specified duration.
  This predictive modeling plays a pivotal role in understanding and mitigating the impact of
  various pollutants and contaminants on aquatic life, and it serves as a cornerstone in
  environmental management for several reasons.

  ## Dataset
  Dataset was used to develop quantitative regression QSAR models to predict acute aquatic toxicity 
  towards the fish Pimephales promelas (fathead minnow) on a set of 908 chemicals. LC50 data, which is the
  concentration that causes death in 50% of test fish over a test duration of 96 hours, was used as model response. 
  The model comprised 6 molecular descriptors: MLOGP (molecular properties), CIC0 (information indices), GATS1i (2D autocorrelations),
  NdssC (atom-type counts), NdsCH ((atom-type counts), SM1_Dz(Z) (2D matrix-based descriptors). Details can be found in the quoted reference: 
  M. Cassotti, D. Ballabio, R. Todeschini, V. Consonni. A similarity-based QSAR model for predicting acute toxicity towards the fathead minnow (Pimephales promelas)

  6 molecular descriptors and 1 quantitative experimental response:
1) CIC0
2) SM1_Dz(Z)
3) GATS1i
4) NdsCH
5) NdssC
6) MLOGP
7) quantitative response, LC50 [-LOG(mol/L)]

## Installation
To install the required packages and libraries, run this command in the project directory after cloning the repository:
```bash
pip install -r requirements.txt
```
Run on your Command prompt :

```bash
streamlit run app.py
```

## Technology used:
- #### Language
    - ![PYTHON](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen)

- #### Libraries
  - ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
  - ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
  - ![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
  - ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
 

- #### IDE
  - ![Jupyter Notebook](https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white)


