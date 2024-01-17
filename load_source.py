from selenium_page import UseSelenium

def main():
    url = "https://www.ozon.ru/category/sim-karty-15514/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=сим+карта"
    # Ограничим парсинг первыми 10 страницами
    MAX_PAGE = 100
    i = 1
    while i <= MAX_PAGE:
        filename = f'page_' + str(i) + '.html'
        print(filename)
        if i == 1:
            UseSelenium(url, filename).save_page()
            print(url)
        else:
            url_param = url.replace("&text", f"&page={i}&text")
            print(url_param)
            UseSelenium(url_param, filename).save_page()

        print()
        i += 1

if __name__ == '__main__':
    main()