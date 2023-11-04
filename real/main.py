from fake_useragent import UserAgent
import requests
import json

ua = UserAgent()
# print(ua.random)

def collect_data(cat_type=2):

    # response = requests.get(
    #     url='https://cs.money/1.0/market/sell-orders?limit=60&minPrice=1000&offset=0&type=2', 
    #     headers={'user-agent': f'{ua.random}'}
    # )

    # with open('result.json', 'w', encoding='utf-8') as file:
    #     json.dump(response.json(), file, indent=4, ensure_ascii=False)

    offset = 0
    batch_size = 60
    result = []
    count = 0

    while True:
        for item in range(offset, offset + batch_size, 60):
            url = f'https://cs.money/1.0/market/sell-orders?limit=60&minPrice=2000&offset={item}&type={cat_type}'
            response = requests.get(
                url=url,
                headers={'user-agent': f'{ua.random}'}
            )

            offset += batch_size

            data = response.json()
            items = data.get('items')

            for i in items:
                if i.get('pricing').get('discount') > 0.1500 and i.get('links').get('3d') is not None:
                    item_full_name = i.get('asset').get('names').get('full')
                    item_3d = i.get('links').get('3d')
                    item_discount = i.get('pricing').get('discount')
                    item_default = i.get('pricing').get('priceBeforeDiscount')
                    item_computed_price = i.get('pricing').get('computed')
                    item_float = i.get('asset').get('float')

                    result.append(
                        {
                            'full_name': item_full_name,
                            '3d': item_3d,
                            'discount': item_discount * 100,
                            'price_before_Discount': item_default,
                            'computed_price': item_computed_price,
                            'float': item_float
                        }
                    )

        count += 1
        print(f'Page #{count} is done')
        print(url)

        if len(items) < 60:
            break

    with open('result1.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

    print(len(result))
    

def main():
    collect_data()


if __name__ == '__main__':
    main()

