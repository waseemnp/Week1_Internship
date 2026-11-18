products=[]
categories=("Accessories","Stationery","Storage")
def add_product():
    print("\n========== ADD PRODUCT ==========")
    try:
        product_id=int(input("Enter Product ID: "))
        if product_id<=0:
            print("Error: Product ID must be positive.")
            return
        for product in products:
            if product["id"]==product_id:
                print("Error: Product ID already exists.")
                return

        name=input("Enter Product Name: ").strip()
        if name=="":
            print("Error: Product name cannot be empty.")
            return

        print("Categories:",categories)
        category=input("Enter Category: ").strip()
        if category not in categories:
            print("Error: Invalid Category. ")
            return

        price=float(input("Enter Selling Price: "))
        if not price>0:
            print("Error: Price must be positive. ")
            return

        stock=int(input("Enter Stock Quantity: "))
        if stock<0:
            print("Error: Stock cannot be negative. ")
            return

        reorder=int(input("Enter Reorder Level: "))
        if reorder<0:
            print("Error: Reorder level cannot be negative. ")
            return

        product={"id":product_id,"name":name,"category":category,"price":price,"stock":stock,"reorder":reorder}
        products.append(product)

        print("\nProduct added successfully!")
    except ValueError:
        print("Error: Please enter valid values.")

def display_products():
    print("\n========== ALL PRODUCTS ==========")
    if len(products)==0:
        print("No products available.")
        return
    print("\nAll Products:")
    for product in products:
        print("ID:",product["id"])
        print("Name:",product["name"])
        print("Category:",product["category"])
        print("Price:",product["price"])
        print("Stock:",product["stock"])
        print("Reorder Level:",product["reorder"])
        print("----------------------")

def search_product():
    print("\n========== SEARCH PRODUCT ==========")
    try:
        product_id=int(input("Enter Product ID to Search: "))
        found=False
        for product in products:
            if product["id"]==product_id:
                print("\nProduct Found!")
                print("ID:",product["id"])
                print("Name:",product["name"])
                print("Category:",product["category"])
                print("Price:",product["price"])
                print("Stock:",product["stock"])
                print("Reorder Level:",product["reorder"])
                found=True
                break
        if found==False:
            print("Product not found.")
    except ValueError:
        print("Error: Please enter a valid Product ID.")

def update_product():
    print("\n========== UPDATE PRODUCT ==========")
    try:
        product_id=int(input("Enter Product ID to Update: "))
        for product in products:
            if product["id"]==product_id:
                print("Product Found!")
                name=input("Enter New Name: ").strip()
                if name=="":
                    print("Error: Name cannot be empty.")
                    return
                price=float(input("Enter New Price: "))
                if price<=0:
                    print("Error: Price must be positive.")
                    return
                stock=int(input("Enter New Stock: "))
                if stock<0:
                    print("Error: Stock cannot be negative.")
                    return
                product["name"]=name
                product["price"]=price
                product["stock"]=stock
                print("Product Updated Successfully!")
                return
        print("Product not found.")
    except ValueError:
        print("Error: Please enter valid values.")

def delete_product():
    print("\n========== DELETE PRODUCT ==========")
    try:
        product_id=int(input("Enter Product ID to Delete: "))
        for product in products:
            if product["id"]==product_id:
                print("Product Found!")
                print("Product Name:",product["name"])
                confirm=input("Are you sure you want to delete? (yes/no): ").lower()
                if confirm=="yes":
                    products.remove(product)
                    print("Product Deleted Successfully!")
                else:
                    print("Delete Cancelled.")
                return
        print("Product not found.")
    except ValueError:
        print("Error: Please enter a valid Product ID.")

def low_stock_report():
    print("\n========== LOW STOCK REPORT ==========")
    print("\nLow Stock Products:")
    found=False
    for product in products:
        if product["stock"]<=product["reorder"]:
            print("Product ID:",product["id"])
            print("Product Name:",product["name"])
            print("Available Stock:",product["stock"])
            print("Reorder Level:",product["reorder"])
            print("----------------------")
            found=True
    if found==False:
        print("No low stock products found.")

def inventory_summary():
    print("\n========== INVENTORY SUMMARY ==========")
    total_products=len(products)
    total_stock=0
    total_value=0
    for product in products:
        total_stock=total_stock+product["stock"]
        total_value=total_value+(product["price"]*product["stock"])
    print("\n===== INVENTORY SUMMARY =====")
    print("Total Products:",total_products)
    print("Total Stock:",total_stock)
    print("Total Inventory Value: Rs.",total_value)

def main():

    while True:
        print("\n====================================")
        print("       SMART RETAIL MANAGER")
        print("====================================")
        print("1. Add Product")
        print("2. Display Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Low Stock Report")
        print("7. Inventory Summary")
        print("8. Exit")
        choice=input("Enter your choice: ")
        if choice=="1":
            add_product()
        elif choice=="2":
            display_products()
        elif choice=="3":
            search_product()
        elif choice=="4":
            update_product()
        elif choice=="5":
            delete_product()
        elif choice=="6":
            low_stock_report()
        elif choice=="7":
            inventory_summary()
        elif choice=="8":
            print("\n====================================")
            print("   THANK YOU FOR USING OUR SYSTEM")
            print("====================================")
            break
        else:
            print("Invalid choice! Please try again.")



main()
