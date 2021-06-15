from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep
class Product():
    name: str = None;
    price: float = 0.0;
    is_available: bool = 0

def start_driver():
    driver = webdriver.Chrome('D:\\chromedriver.exe')
    driver.get("https://www.ecwid.ru/demo/search")
    driver.implicitly_wait(10);
    return driver;


def parse_data(str_):
    product = Product();
    for j in str_:
        if('В наличии' in j):
            product.is_available = 1; 
    return product;
                   
def find_product_in_stock(href, driver):
    driver.get(href);

    a = driver.find_element_by_class_name("product-details__sidebar");
    b = a.text.split('\n');

    return parse_data(b)

def find_filtred_in_stock(driver):
    products_list = driver.find_elements_by_class_name("grid-product");
    a_href_list = [];

    for i in products_list:
        a = i.find_element_by_class_name("grid-product__title");
        a_href_list.append(a.get_attribute("href"))

    parsed_data_array = [];
    for i in a_href_list:
        a = find_product_in_stock(i, driver);
        parsed_data_array.append(a);
    return parsed_data_array
      
def press_checkbox_in_stock(driver):

    driver.find_element_by_id("checkbox-in_stock").click();




def find_filtred_price(browser_url):
    a = browser_url.find_element_by_class_name("grid__products");
    b = a.text.split('\n');
    parsed_data_array = [];

    for n, val in enumerate(b):
        product = Product();
        if n % 2:
            product.price = float(val[1:]);
            parsed_data_array.append(product);
    browser_url.close();
    return parsed_data_array;

def find_filtred_name(browser_url):
    a = browser_url.find_element_by_class_name("grid__products");
    b = a.text.split('\n');
    parsed_data_array = [];

    for n, val in enumerate(b):
        product = Product();
        if n % 2 == 1:
            product.name = val;
        parsed_data_array.append(product);
    return parsed_data_array;


def press_filter_price_to(driver, price):
    a = driver.find_element_by_class_name("ec-filter__price-to");
    b = a.find_element_by_class_name("form-control__text");
    b.send_keys(price); 
    b.send_keys(Keys.ENTER);
    return driver;

def press_filter_price_from(driver, price):
    a = driver.find_element_by_class_name("ec-filter__price-from");
    b = a.find_element_by_class_name("form-control__text");
    b.send_keys(price); 
    b.send_keys(Keys.ENTER);
    return driver;


def filtred_data_in_stock():
    browser_url = start_driver();
    press_checkbox_in_stock(browser_url);
    return find_filtred_in_stock(browser_url);

def filtred_data_price_to(price):
    browser_url = start_driver();
    browser_url = press_filter_price_to(browser_url, price);
    sleep(15)
    return find_filtred_price(browser_url);

def filtred_data_price_from(price):
    browser_url = start_driver();
    browser_url = press_filter_price_from(browser_url, price);
    sleep(15)
    return find_filtred_price(browser_url);

