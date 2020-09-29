#python house hunting exercise 
annual_salary = float(input("What is your annual salary "))
total_cost = float(input("What is the total cost of your dream home "))
portion_down_payment = 0.25 * total_cost
portion_saved = float(input("Enter the percent of your salary to save, as decimal "))
monthly_salary_saved = (annual_salary/12) * portion_saved
def road_to_the_bag(annual_salary, total_cost, portion_down_payment, portion_saved):
  current_savings = 0
#   months_passed = 0 
  while current_savings < portion_down_payment:
     #each month will take a portion of salary saved and earned interest
     #stop when savings equals money_needed
    current_savings += monthly_salary_saved
    investment_return = monthly_salary_saved*(0.04/12)
    current_savings += investment_return
    #count number of months that pass
    months_passed += 1 
    print(current_savings, months_passed)
    #return months 
    # return