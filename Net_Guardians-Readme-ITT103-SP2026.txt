Python Project Information
Authors: Net Guardians (Jemoi Walker)
Date Created: April 3, 2026
Course: ITT103 (Programming Techniques)
GitHub Public URL to Code: https://github.com/jemoi-walker-UCC/Net_Guardians_Best_Buy_Retail_Store_POS.git 

 Program Purpose
The Best Buy Retail POS System is a Python-based solution designed to modernize the sales operations of a growing retail business. The primary goal is to transition from manual ledger-keeping to a digital interface, thereby reducing human calculation errors, providing real-time inventory alerts, and ensuring consistent tax and discount applications.

How to Run the Program
1.	Install a python IDE n your machine such as Pycharm.
2.	Download the pos_system.py file from this repository.
3.	Open the using the Python IDE
4.	And then select run
5.	Follow the on-screen menu prompts by entering the corresponding numbers (1-5)
A.  Adding Items (Option 1)
1.	Select 1 from the main menu.
2.	Enter the Product name: Type the name of the item (e.g., rice). The system is programmed to recognize the name regardless of whether you use capital letters.
3.	Enter the Product Quantity: Enter the number of units the customer wants.
-	Constraint Check: If you enter a number higher than what is in stock, the system will display an error: " Not enough stock available!” and return you to the menu.
-	Validation: If you accidentally type a letter instead of a number, the system will   catch the error and ask you to try again.
B. Managing the Cart (Options 2 & 3)
•	Remove Items (Option 2): If a customer changes their mind, select 2 and enter the product name. The system will remove the item entirely and add the quantity back to the store's inventory. And print the message “Item has been removed!”
•	View Cart (Option 3): Select 3 at any time to see a summary of what has been added so far, including the running total for each specific item.
C. Checkout & Receipt (Option 4)
1.	Select 4 when the customer is ready to pay.
2.	Automatic Logic: The system will instantly calculate the subtotal, check if the total is over $5,000 to apply a 5% discount, and then add the 10% Sales Tax.
3.	Payment: The system will prompt: "Enter payment".
4.	If you enter an amount less than the Total Due, the system will say "Insufficient payment made!" and keep asking until the full amount is covered.
5.	Final Output: Once paid, a formatted receipt prints to the console, showing the itemized list, the savings from the discount, and the exact change to be returned.
D. Ending or Restarting (Option 5)
•	After a receipt is printed, the system automatically prepares for a new transaction.
•	To shut down the system completely, select 5 from the main menu to "Exit Session."

 Assumptions & Limitations
Assumptions:
•	The system assumes the currency is always going to be in Jamaican Dollars (JMD).
•	It assumes a single-user environment or one cashier at a time.
•	The system assume the user can use python 
Limitations:
•	Currently, inventory resets if the program is closed.
•	The system is Command Line Interface based rather than GUI-based.
• While the system doesn't handle casing (e.g., "bread" vs "Bread"), it requires correct spelling of the product names.
