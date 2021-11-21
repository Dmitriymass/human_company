import datetime
import json
import requests


headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Is-Ajax-Request": "X-Is-Ajax-Request",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
}


def get_data():
    start_time = datetime.datetime.now()

    url = "https://oscarseregyfevis.ru/catalog/legkovye/?q=list_of_companies_url"
    r = requests.get(url=url, headers=headers)

    # with open("index.html", "w") as file:
    #     file.write(r.text)

    # print(r.json())

    # with open("r.json", "w") as file:
    #     json.dump(r.json(), file, indent=4, ensure_ascii=False)

    urls_count = r.json()["urlCount"]

    data_list = []
    for item_url in range(1, urls_count + 1):
        url = f"https://oscarsegrervis.ru/catalog/legkovye/?q=list_of_companies_url={item_url}"

        r = requests.get(url=url, headers=headers)
        data = r.json()
        items = data["items"]

        possible_urls = ["person_url", "list_of_persons_url"]
        for item in items:
            total_amount = 0
            item_company_url = item["company_url"]
            item_profile_url = item["profile_url"]
            urls = []
            for pu in possible_urls:
                if pu in item:
                    if item[pu] is None or len(item[pu]) < 1:
                        continue
                    else:
                        for urls in item[pu]:
                            urls_name = urls["URL_NAME"]
                            urls_amount = urls["AMOUNT"]
                            total_amount += int(urls["AMOUNT"])

                            stores.append(
                                {
                                    "urls_name": urls_name,
                                    "urls_amount": urls_amount
                                }
                            )

            data_list.append(
                {
                    "company_url": item_company_url,
                    "profile_url": item_profile_url,
                    "urls": urls,
                    "total_amount": total_amount
                }
            )
    cur_time = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M")

    with open(f"data_{cur_time}.json", "a") as file:
        json.dump(data_list, file, indent=4, ensure_ascii=False)

    diff_time = datetime.datetime.now() - start_time
    print(diff_time)


def main():
    get_data()


if __name__ == '__main__':
    main()