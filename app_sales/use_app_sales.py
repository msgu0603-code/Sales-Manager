from app_sales.sales_manager import SalesManager

def main():
    price_base = 100.0
    Tax_percentage = 0.05 #5%
    discount_percentage = 0.10 #10%
    
    manager = SalesManager(price_base, Tax_percentage, discount_percentage)
    price_final = manager.calculate_final_price()
    
    print(f"Base price: ${price_base}")
    print(f"Tax: {Tax_percentage * 100}%")
    print(f"Discount: {discount_percentage * 100}%")
    print(f"The final price is: ${price_final}")

if __name__ == "__main__":
    main()