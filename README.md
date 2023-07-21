Scenario

A laptop shop buys laptops/computers from manufacturers and sells it to various customers which may be individuals or companies. 
Orders for computers can be placed for the manufacturers. Likewise, customers can place orders for computers to our laptop shop 
(distributor):
The laptop rental shop manages information about the available computers in a text file. 
A program that can read the text file to display all the laptops available and make changes to the text file according to the nature 
of the transaction (ordering from manufacturer/selling to customer) needs to be developed, With each order or sale made, a note/recelpt 
should be generated with the details of the transaction. The stock of a particular laptop should also be updated in the main text file 
itself. For example, if the shop currently has 19 pieces of Razer Blade, and a customer buys 2 of it, the stock should be updated to 17. 
In case the rental shop purchases 5 Razer Blade laptops, the stock should then be updated from 17 to 22 ie. the stock should be 
increased by 5. A sample format of the text file containing the information about the laptop is as follows: 

Razer Blade, Razer. $2000, 20, I7 7th Gen. GTX 3060
XPS, Dell, $1976, 15, I5 9th Gen, GTX 3070
Alienware, Alienware, $1978, 24, I5 9th Gen, GTX 3070
Swift 7, Acer, $900, 12, I5 9th Gen. GTX 3070
Macbook Pro 16, Apple, $3500, 10, I5 9th Gen, GTX 3070

“1” column contains the name of the laptop. 2nd column contains name of brand, 3rd column contains the price of laptop 4th column 
contains the quantity avallable. 5th column contains the processor details. 6th column contains details regarding the graphic card.
Note: You can use your own format and add other information too.

A note/invoice should be generated for each transaction. When a laptop is sold to a customer, a note/invoice should be generated
(as a txt file) which must contain the name of the laptop, name of brand, name of customer, date and time of purchase, 
total amount without the shipping cost, the shipping cost itself and the total amount to be paid for the laptops which should include 
the shipping cost.

When laptops are to be ordered, a note/invoice should be generated again which should include the name of the distributor (company) 
name of the laptop, name of brand, date and time of purchase, net amount (total amount without VAT), VAT amount applicable ie: 
13% of the total amount, and the gross amount(total amount with VAT.)
* The format of the notes/invoices is up to you. But each file should have a unique name
