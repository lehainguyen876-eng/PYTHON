import logging

logging.basicConfig(
    level=logging.DEBUG,  
)

logger = logging.getLogger(__name__)


def get_discount_rate(tier: str, quantity: int) -> float:

    logger.debug(
        f"Đang tính toán chiết khấu cho hạng {tier} "
        f"với số lượng {quantity}"
    )

    if quantity <= 0:
        logger.error("Quantity must be positive")
        raise ValueError("Quantity must be positive")

    if tier == "silver":
        rate = 0.05
    elif tier == "gold":
        rate = 0.10
    elif tier == "diamond":
        rate = 0.15
    else:
        rate = 0.0

    if quantity >= 50:
        rate += 0.05

    return rate


def calculate_agency_total(
    price: float,
    quantity: int,
    tier: str
) -> float:


    if price < 0:
        raise ValueError("Đơn giá không được âm")

    rate = get_discount_rate(tier, quantity)

    final_price = price * quantity * (1 - rate)

    logger.info(f"Kết quả: Tổng tiền = {final_price}")

    return final_price


if __name__ == "__main__":
    try:
        calculate_agency_total(100, 50, "gold")

        calculate_agency_total(100, -5, "silver")

    except ValueError as error:
        logger.error(error)