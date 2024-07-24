# Constants
units_purchased = 2000
purchase_price_per_unit = 40
purchase_commission_rate = 0.03
selling_price_per_unit = 42.75
selling_commission_rate = 0.03

# Calculations
total_purchase_cost = units_purchased * purchase_price_per_unit
purchase_commission = total_purchase_cost * purchase_commission_rate
total_purchase_cost_with_commission = total_purchase_cost + purchase_commission

total_selling_price = units_purchased * selling_price_per_unit
selling_commission = total_selling_price * selling_commission_rate
total_selling_price_with_commission = total_selling_price - selling_commission

profit_margin = total_selling_price_with_commission - total_purchase_cost_with_commission

# Output
print("The cost of purchasing the entire stock holding in Google LLC: $", total_purchase_cost_with_commission)
print("The amount of money paid in commission during the purchase: $", purchase_commission)
print("The selling price of the entire stock holding in Google LLC: $", total_selling_price_with_commission)
print("The amount of money paid in commission during the sale: $", selling_commission)
print("The profit margin made by James in the entire transaction (purchase & sale, including commissions paid): $", profit_margin)
