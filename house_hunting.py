#python house hunting exercise 
annual_salary = float(input("what is your annual salary "))
total_cost = float(input("what is the total cost of your dream home "))
portion_down_payment = 0.25 * total_cost
portion_saved = float(input("how much of your salary will you save each month...for your dream home "))
def road_to_the_bag(annual_salary, total_cost, portion_down_payment, portion_saved):
current_savings = 0
months_passed = 0 
while current_savings < portion_down_payment:
    current_savings = current_savings + annual_salary / 12 + current_savings * 0.04 / 12:
    months_passed += 1 
    print(current_savings, months_passed)


    #each month will take a portion of salary saved and earned interest
    #stop when savings equals money_needed
    #count number of months that pass
    #return months 