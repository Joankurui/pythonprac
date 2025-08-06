# 1. create function calculate_discount
def calculate_discount(price, discount_percentage):
    """
    Calculates the final price after applying discount.
    if the discount is 20% or higher,apply the discount;otherwise , return original price.
    """
    if discount_percentage >= 20:
        discount_amount = price * (discount_percentage / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    # 2. using calculate_discount function
def main():
    """
    prompts user for price and discount,
    then prints the final or original price.
    """
    try:
        original_price = float(input("Enter the original price: "))
        discount_percentage = float(input("Enter the discount percentage: "))       
        final_price = calculate_discount(original_price, discount_percentage)
        
        if final_price_after_discount != original_price:
            print(f"The final price after applying the discount is: {final_price}")
        else:
            print(f"No discount applied. The original price remains: {final_price}")
    except ValueError:
        print("Invalid input. Please enter numeric values for price and discount percentage.")

if __name__ == "__main__":
           main()
# #End of functions.py