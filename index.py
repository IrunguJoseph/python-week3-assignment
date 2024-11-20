# creating a function named calculate_discount
def calculate_discount(price, discount_percent):
    # Check if discount is greater or equal to 20
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100);
        final_price = price - discount_amount;
    else:
        final_price = price ;
    # Printing the final price
    print(f"Final price: Ksh{final_price}");


original_price = int(input("Enter the original price: "));
discount = int(input("Enter the discount in percentage: "));

calculate_discount(original_price, discount);
