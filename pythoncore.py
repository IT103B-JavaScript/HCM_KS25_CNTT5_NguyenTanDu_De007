# Phần 1: Python Core và Tư duy thuật toán

raw_apartments = [
    {"apartment_code": "A301", "type": "two_bedroom", "monthly_rent": 12000000, "status": "available"},
    {"apartment_code": " a101 ", "type": "studio", "monthly_rent": 5500000, "status": "available"},
    {"apartment_code": "A202", "type": "one_bedroom", "monthly_rent": 8000000, "status": "rented"},
    {"apartment_code": "A102", "type": "studio", "monthly_rent": 6000000, "status": "reserved"},
    {"apartment_code": "A302", "type": "two_bedroom", "monthly_rent": 13500000, "status": "available"},
]


# Yêu cầu 1.1: Chuẩn hóa & validate dữ liệu
def clean_and_validate_apartments(apartments):
    cleaned = []
    for apartment in apartments:
        code = str(apartment.get("apartment_code", "")).strip().upper()

        is_valid = len(code) > 1 and code[0] == "A" and code[1:].isdigit()
        if not is_valid:
            continue

        new_apartment = apartment.copy()
        new_apartment["apartment_code"] = code
        cleaned.append(new_apartment)
    return cleaned


# Yêu cầu 1.2: Tìm kiếm tuyến tính
def search_apartments(apartments, max_rent, status=None):
    result = []
    for apartment in apartments:
        if apartment["monthly_rent"] <= max_rent:
            if status is None or apartment["status"] == status:
                result.append(apartment)
    return result


# Yêu cầu 1.3: Sắp xếp nổi bọt (Bubble Sort) - giá thuê giảm dần
def sort_apartments_by_monthly_rent_desc(apartments):
    arr = apartments.copy()
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j]["monthly_rent"] < arr[j + 1]["monthly_rent"]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    print("=== 1.1 Chuẩn hóa & validate ===")
    clean_apartments = clean_and_validate_apartments(raw_apartments)
    for a in clean_apartments:
        print(a)

    print("\n=== 1.2 Tìm kiếm: giá <= 8.000.000, status = available ===")
    for a in search_apartments(clean_apartments, 8000000, "available"):
        print(a)

    print("\n=== 1.2 Tìm kiếm: giá <= 8.000.000, status = None ===")
    for a in search_apartments(clean_apartments, 8000000):
        print(a)

    print("\n=== 1.3 Bubble Sort giá thuê giảm dần ===")
    for a in sort_apartments_by_monthly_rent_desc(clean_apartments):
        print(a)