# Import libraries
import pandas as pd
import itertools

# Database product
database_product = {
    "vegetable oil": 30_000,
    "rice": 20_000,
    "egg": 25_000,
    "soap": 11_000,
    "shampoo": 16_000,
    "tooth paste": 15_000,
    "fried chicken": 20_000,
    "null data": 0}

# save data user
data_user = {}

class Transaction:
    """
    This Class is to Create - Update - Delete transaction.
    The methods in this class are:
        - __init__        : it's an instance method for initializing
                            the newly created object.
        - add_item        : Add new item name, price and quantity.
        - update_name     : Update the item name
        - update_price    : Update the item price
        - update_qty      : Update the item quantity
        - delete_item     : Delete one item (including name, price and quantity)
        - reset           : Reset transaction, delete all history input
                            transaction
        - check_order     : Check if there all the data is correct, based on
                            database that we have (database_product)
        - total_price     : Give total all the item price, including discount.
    """

    # id transaction
    # reference: https://stackoverflow.com/questions/1045344/how-do-you-create-an-incremental-id-in-a-python-class
    id_iter = itertools.count(start=1, step=1)

    def __init__(self):
        """
        Initialize object.
        instance variable:
            - data_user  : to save user data transaction
            - id_trx     : id transaction
            - n          : iterator each item
            - is_ok      : check if all transaction correct
        """
        self.data_user = data_user
        self.id_trx = f'{next(Transaction.id_iter)}_idtrx'
        self.n = 1
        self.is_ok = False

        # Update data_user to store new id transaction
        data_user.update({f'{self.id_trx}':{}})

    def add_item(self, name_item="null data",
                 price_item=0, qty_item=0):
        """
        method to add new item (item name, item price, item quantity)
        :param name_item     : <string> name of the item
        :param price_item    : <int> price of the item
        :param qty_item      : <int> quantity of the item
        :return output data  : <dictionary> data output
        """
        try:
            # check if there is an id_trx in data_user
            if self.id_trx in list(self.data_user.keys()):
                # add data to data_user dictionary
                self.data_user[self.id_trx].update({self.n: [name_item,
                                                            price_item,
                                                            qty_item]})
                # Iteration n, key for data_user dictionary
                self.n += 1
                # print the result
                print(self.data_user[self.id_trx])

            else:
                print("Can't Find ID Transaction")

        except Exception as error:
            print("An error occurred:", type(error).__name__)

    def update_name(self, old_name_item, new_name_item):
        """
        method to update item name in data user dictionary
        :param old_name_item : <string> old name of the item
        :param new_name_item : <string> new name of the item
        :return output data  : <dictionary> data output
        """
        try:
            # check if there is an id_trx in data_user
            if self.id_trx in list(self.data_user.keys()):
                # Iterate to find existing item name, then update it
                for key, val in self.data_user[self.id_trx].items():
                    if old_name_item == val[0]:
                        self.data_user[self.id_trx][key][0] = new_name_item
                    else:
                        pass

                # print the result
                print(self.data_user[self.id_trx])

            else:
                print("Can't Find ID Transaction")

        except Exception as error:
            print("An error occurred:", type(error).__name__)

    def update_price(self, name_item, new_price):
        """
        method to update item price in data user dictionary
        :param name_item     : <string> name of the item
        :param new_price     : <int> new price of the item
        :return output data  : <dictionary> data output
        """
        try:
            # check if there is an id_trx in data_user
            if self.id_trx in list(self.data_user.keys()):
                # Iterate to find existing item name, then update its price
                for key, val in self.data_user[self.id_trx].items():
                    if name_item == val[0]:
                        self.data_user[self.id_trx][key][2] = new_price
                    else:
                        pass

                # print the result
                print(self.data_user[self.id_trx])

            else:
                print("Can't Find ID Transaction")

        except Exception as error:
            print("An error occurred:", type(error).__name__)

    def update_qty(self, name_item, new_qty):
        """
        method to update item quantity in data user dictionary
        :param name_item     : <string> name of the item
        :param new_price     : <int> new quantity the item
        :return output data  : <dictionary> data output
        """
        try:
            # check if there is an id_trx in data_user
            if self.id_trx in list(self.data_user.keys()):
                 # Iterate to find existing item name, then update its quantity
                for key, val in self.data_user[self.id_trx].items():
                    if name_item == val[0]:
                        self.data_user[self.id_trx][key][1] = new_qty
                    else:
                        pass

                # print the result
                print(self.data_user[self.id_trx])

            else:
                print("Can't Find ID Transaction")

        except Exception as error:
            print("An error occurred:", type(error).__name__)

    def delete_item(self, name_item):
        """
        method to delete item based on its name in data user dictionary
        :param name_item     : <string> name of the item
        :return output data  : <dictionary> data output
        """
        try:
            # check if there is an id_trx in data_user
            if self.id_trx in list(self.data_user.keys()):
                # delete data based on name item
                for key, val in self.data_user[self.id_trx].items():
                    if name_item == val[0]:
                        self.data_user[self.id_trx].update({key: ['null data',
                                                                0, 0]})
                    else:
                        pass

                # print the result
                print(self.data_user[self.id_trx])

            else:
                print("Can't Find ID Transaction")

        except Exception as error:
            print("An error occurred:", type(error).__name__)

    def reset(self):
        """
        method to delete all item on its id transaction in data user dictionary
        :return output data  : <dictionary> data output
        """
        try:
            # check if there is an id_trx in data_user
            if self.id_trx in list(self.data_user.keys()):
                # Make sure customer want to delete all history
                user_dec = input("Are you sure you want to delete all history?, \
                                    type ya/yes: ")

                # Reset Transaction
                if user_dec == "yes" or user_dec == "ya":
                    self.data_user[self.id_trx].clear()
                else:
                    pass

                # print the result
                print(self.data_user[self.id_trx])

            else:
                print("Can't Find ID Transaction")

        except Exception as error:
            print("An error occurred:", type(error).__name__)

    def check_order(self):
        """
        method to check if all items on its id transaction has already correct
        item name and price according to the database
        :return output massage : <string> wrong or right order massage
        :return output table  : <pandas dataframe> data output table
        """
        try:
            # check if there is an id_trx in data_user
            if self.id_trx in list(self.data_user.keys()):
                # check name and price
                for key, val in self.data_user[self.id_trx].items():
		                # check if the name is not correct
                    if val[0] not in list(database_product.keys()):
                        print(f"Item {val[0]} has wrong name, please check again.")
                        # # check if the name and price is not correct
                        # if val[2] != database_product[val[0]]:
                        #     print(f"Item {val[0]} has wrong name and price, please check again.")
                        # else:
                        #     pass
                    # check if the price is not correct
                    elif val[2] != database_product[val[0]]:
                        print(f"Item {val[0]} has wrong price, please check again.")
                    else:
                        print(f"Item {val[0]} is correct.")
            
                # print the result table
                df = pd.DataFrame.from_dict(self.data_user[self.id_trx],
                                        orient='index',
                                        columns=['Item Name',
                                                'Quantity Item',
                                                'Price Item'])
                df['sum_price'] = df['Quantity Item'].astype(int) * df['Price Item'].astype(int)
                print(df)
                
            else:
                print("Can't Find ID Transaction")

        except Exception as error:
            print("An error occurred:", type(error).__name__)

    def total_price(self):
        """
        method to know total price (price already includes discount if eligible)
        :return total price  : <string> total price
        """
        try:
            # check if there is an id_trx in data_user
            if self.id_trx in list(self.data_user.keys()):
                # Create data table
                df = pd.DataFrame.from_dict(self.data_user[self.id_trx],
                                        orient='index',
                                        columns=['Item Name',
                                                'Quantity Item',
                                                'Price Item'])
                df['sum_price'] = df['Quantity Item'].astype(int) * df['Price Item'].astype(int)

                # check if the order correct or not
                for key, val in self.data_user[self.id_trx].items():
                    if val[0] not in list(database_product.keys()) and \
                        val[2] != database_product[val[0]]:
                        print(f"Item has wrong name or price, please check again.")
                        self.is_ok = False
                    else:
                        self.is_ok = True

                # Menghitung total diskon sesuai total belanja
                if self.is_ok == True:
                    if df['sum_price'].sum() > 200_000 and df['sum_price'].sum() < 300_000:
                        total_price = df['sum_price'].sum() - (df['sum_price'].sum() * 0.05)
                        print(f"You should pay Rp{total_price:,}.")

                    elif df['sum_price'].sum() > 300_000 and df['sum_price'].sum() < 500_000:
                        total_price = df['sum_price'].sum() - (df['sum_price'].sum() * 0.08)
                        print(f"You should pay Rp{total_price:,}.")

                    elif df['sum_price'].sum() > 500_000:
                        total_price = df['sum_price'].sum() - (df['sum_price'].sum() * 0.1)
                        print(f"You should pay Rp{total_price:,}.")

                    else:
                        total_price = df['sum_price'].sum()
                        print(f"You should pay Rp{total_price:,}.")
                else:
                    pass

            else:
                print("Can't Find ID Transaction")

        except Exception as error:
            print("An error occurred:", type(error).__name__)

