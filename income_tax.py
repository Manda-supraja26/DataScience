AI=int(input("the anual income = "))
HRA=int(input("the hra per month="))
Other=int(input("other deductions are"))
taxable_income=AI-HRA*12-Other
actual_taxable_income=taxable_income-300000
print(actual_taxable_income)
if actual_taxable_income>300000 and actual_taxable_income<600000:
    result=actual_taxable_income*(0.1)
if actual_taxable_income>600000 and actual_taxable_income<1000000:
    result=actual_taxable_income*(15/100)
if actual_taxable_income>1000000:
    result=actual_taxable_income*(20/100)
print(result)

