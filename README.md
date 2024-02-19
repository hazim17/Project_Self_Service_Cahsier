# Project Self Service Cashier

## **Background Project**
In this project, I created a self-service cashier system for a supermarket so customers can enter, update and delete the items purchased, the quantity and the price by themself. 

## **Goals**
Create a CRUD self-service cashier program according to the requested requirements (create an ID transaction, add items, update items, delete items, reset transaction, check order and calculate total shopping price)

## **Objectives**
- Create a flowchart for the program. 
- Create CRUD programs in a modular system with a clean code and has trial and error when using branching.

## **Flowchart**
<p align="center">
<img src="Images/Flowchart self cashier project.jpg" alt="flow_chart" >
</p>
<p align="center">
Image 1. Flowchart
</p>

### Flowchart Explanation:
Flowchart Explanation.
1. To run the program, the customer imports the module first.
<p align="center">
<img src="/Images/Import module.png" alt="import_module" >
</p>
<p align="center">
Image 2. Import module
</p>

2. Create an Object from class Transaction. When an object is created, an id transaction is automatically generated. 
<p align="center">
<img src="/Images/Check ID.png" alt="check_id" >
</p>
<p align="center">
Image 3. Check ID transaction
</p>

3. The Customer can choose a method according to the action they want to take.
    The methods in Transaction class are:
    ```
    - __init__     : it's an instance method for initializing the newly created object.
    - add_item     : Add new item name, price and quantity.
    - update_name  : Update the item name
    - update_price : Update the item price
    - update_qty   : Update the item quantity
    - delete_item  : Delete one item (including name, price and quantity)
    - reset        : Reset transaction, delete all history input transaction
    - check_order  : Check if there all the data is correct, based on database that we have (database_product)
    - total_price  : Give total all the item price, including discount.
    ```

4. Then the output of each method varies, it could be messages or a data table. The customer can call any method in the Transaction class as many times as they want.

## **Test Case**
**Table of Product**

Item Name | Price |
--- | --- |
"vegetable oil"| Rp 30.000|
"rice"| Rp 20.000|
"egg"| Rp 25.000|
"soap"| Rp 11.000|
"shampoo"| Rp 16.000|
"tooth paste"| Rp 15.000|
"fried chicken"| Rp 20.000|

1. Test 1
A Customer wants to add 3 new items.
- Name: fried chicken, qty: 2, price: 20.000
- Name: toothpaste, qty: 2, price: 15.000
- Name: shampoo, qty: 1, price: 20.000

Result: 
<p align="center">
<img src="/Images/test_1.png" alt="test_1">
</p>

2. Test 2
The Customer wants to delete `toothpaste` from its transaction.
 
Result: 
<p align="center">
<img src="/Images/test_2.png" alt="test_2">
</p>

3. Test 3
The Customer wants to reset the transaction.

Result: 
<p align="center">
<img src="/Images/test_3.png" alt="test_3">
</p>

4. Test 4
The Customer wants to make the same transaction in `Test 1` and check the order.

Result: 
<p align="center">
<img src="/Images/test_41.png" alt="test_41">
</p>
<p align="center">
<img src="/Images/test_42.png" alt="test_42">
</p>

5. Test 5
Update the wrong order from the `Test 4` result. Then, check again the order.

Result: 
<p align="center">
<img src="/Images/test_51.png" alt="test_51">
</p>
<p align="center">
<img src="/Images/test_52.png" alt="test_52">
</p>

6. Test 6
The customer has finished shopping. Calculate the total price of purchases.

Result: 
<p align="center">
<img src="/Images/test_6.png" alt="test_6">


## **This Repository Organization**
```
_
|── Images                 : Contain all the image using in README.md
├── main_demonstrasi.ipynb : This file is used to run the module transaction and Test Case. 
├── module_transaction.py  : A module that contain class Transaction. In that class there are many methods to do the transaction like add, update and delete an item.
└── README.md              : Readme File
```

<!-- Shoutout to Grammarly for correcting the grammar.  -->

<!-- Instruction Python Project https://docs.google.com/document/d/1TyWrKr4xPFJu3IFwt4vUW5gLXgbNRcQjSYkpGVc376I/preview#heading=h.a7e393npqdkt
 -->

Muhammad Hazim M

Pacmann - Analystics & Data Science
Batch 14
