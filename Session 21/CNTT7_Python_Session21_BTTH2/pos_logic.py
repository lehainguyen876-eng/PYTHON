import logging

DRINK_MENU = {
    "P1": {"name": "Phin Sữa Đá", "price": 35000},
    "F1": {"name": "Freeze Trà Xanh", "price": 55000},
    "T1": {"name": "Trà Sen Vàng", "price": 45000}
}


class ItemNotFoundError(Exception):
    pass


class InvalidQuantityError(Exception):

    pass


def add_item_to_order(order_list: list, drink_code: str, quantity: int) -> list:

    clean_code = drink_code.strip().upper()

    if clean_code not in DRINK_MENU:
        logging.warning(f"ItemNotFoundError - Code: {clean_code}")
        raise ItemNotFoundError()

    if quantity <= 0:
        logging.warning(f"InvalidQuantityError - Quantity: {quantity}")
        raise InvalidQuantityError()

    item_data = {
        "code": clean_code,
        "name": DRINK_MENU[clean_code]["name"],
        "price": DRINK_MENU[clean_code]["price"],
        "quantity": quantity
    }
    order_list.append(item_data)
    
    logging.info(f"Added {quantity} of {clean_code} to order")
    return order_list


def calculate_total(order_list: list) -> int:
    total = 0
    for item in order_list:
        total += item["price"] * item["quantity"]
    return total