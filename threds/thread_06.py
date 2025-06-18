from concurrent.futures import ThreadPoolExecutor
from threading import Lock
from time import sleep

account_balance_db = 1000


def update_money(lock, transaction, amount):
    global account_balance_db
    print(f"Transaction: {transaction}, Amount: {amount}")
    with lock:
        account_balance_db_copy = account_balance_db
        account_balance_db_copy += amount
        sleep(1)
        account_balance_db = account_balance_db_copy


if __name__ == "__main__":
    lock = Lock()
    trasactions = [("deposit", 1000), ("withdraw", -2000)]
    with ThreadPoolExecutor(max_workers=2) as executor:
        for transaction, amount in trasactions:
            executor.submit(update_money, lock, transaction, amount)

    print(f"Final money: {account_balance_db}")
