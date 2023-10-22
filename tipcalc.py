def calculate_tip(bill_amount, tip_percentage):
  """Calculates the tip for a restaurant bill based on the total bill amount and the desired tip percentage.

  Args:
    bill_amount: The total bill amount.
    tip_percentage: The desired tip percentage.

  Returns:
    The amount of the tip.
  """

  tip = bill_amount * tip_percentage / 100
  return tip

# Example usage:

bill_amount = 100
tip_percentage = 20

tip = calculate_tip(bill_amount, tip_percentage)

print(f"The tip is ${tip}.")
