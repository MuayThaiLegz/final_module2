# Loan Qualifier Application 

**Welcome our Home Loan Qualifying App! Enjoy our new and improved Software** 

This loan qualifier application is a modularized application with the main objective to simplify and maximize options for the home mortgage loan application process.
It has a command line interface ready for easy use and high user satifaction and helps us best serve our clients. 

---

## Technologies
`print("Hello World!")`
*Built using Python 3.7.9 64-bit

This Loan Qualifier Application imports makes use of the Python Programming language and the Command Line Interface. The following Libraries need import in the traditional sense [SYS, Fire, Questionary, CVS. 
The follwing Libraries require the (From, Import) method of import(load_csv, calculate_monthly_debt_ratio, calculate_loan_to_value_ratio, filter_max_loan_size, filter_credit_score, filter_debt_to_income, filter_loan_to_value)


---

## Installation Guide and Examples

```python
import sys
import csv
import fire
import questionary
import csv 


from pathlib import Path

from qualifier.utils.fileio import load_csv, save_csv

from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
)

from qualifier.filters.max_loan_size import filter_max_loan_size

from qualifier.filters.credit_score import filter_credit_score

from qualifier.filters.debt_to_income import filter_debt_to_income

from qualifier.filters.loan_to_value import filter_loan_to_value
```


## Contributors

** This Loan Qualifier app was cntributed to by the entire UC Berkeley FinTech BootCamp 
[UC Berkeley Extension](https://bootcamp.berkeley.edu/fintech/)

---

## License

This is a open source project take it and improve it 10000 X
