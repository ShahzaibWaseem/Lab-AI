# Lab 01: Introduction to Python
(CS188 Assignment)
Download Files from: [tutorial.zip](https://s3-us-west-2.amazonaws.com/cs188websitecontent/projects/release/tutorial/v1/001/tutorial.zip)

## Tasks
1. Complete the code in addition.py
2. Add a buyLotsOfFruit(orderList) function to buyLotsOfFruit.py which takes a list of (fruit,pound) tuples and returns the cost of your list. If there is some fruit in the list which doesn't appear in fruitPrices it should print an error message and return None. Please do not change the fruitPrices variable.
Run python autograder.py until question 2 passes all tests and you get full marks. Each test will confirm that buyLotsOfFruit(orderList) returns the correct answer given various possible inputs. For example, test_cases/q2/food_price1.test tests whether:
Cost of [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)] is 12.25
3. Fill in the function shopSmart(orders,shops) in shopSmart.py, which takes an orderList (like the kind passed in to FruitShop.getPriceOfOrder) and a list of FruitShop and returns the FruitShop where your order costs the least amount in total. Don't change the file name or variable names, please. Note that we will provide the shop.py implementation as a "support" file, so you don't need to submit yours.

All The Test Cases MUST Pass