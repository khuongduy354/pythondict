print("\n")
x =input()
print("\n")
aray=x.split(',')
# đoạn code trên lấy thông tin vào, thông tin vào dạng a,b,c,d
# hàm split sẽ bỏ dấu phẩy và lưu mỗi phần tử vào trong list aray 

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
# cái đoạn selenium chỉ là copy and paste thôi, nó là tool hỗ trợ, đọc thêm cho vui trên 
# selenium documentation cũng đc 



def extractWiki(a):
    try:
        driver.get("https://en.wikipedia.org/wiki/"+a) 
        # truy cập trang web wiki, a là từ cần dịch, vd:
        # nhập https://en.wikipedia.org/wiki/abcxyz vào trang tìm kiếm
        # thì trang wiki nó sẽ search abcxyz

        driver.find_element_by_link_text("Tiếng Việt").click()
        # ở dưới wiki có phần ngôn ngữ, chọn tiếng việt
        driver.get(driver.current_url)
        # khi bấm chọn tiếng việt thì url thay đổi, nên phải lấy lại url 

        oUtput=driver.find_element_by_id('firstHeading').text
        # trang hiện giờ là tiếng việt, nên chỉ cần lấy cái tiêu đề tiếng việt là coi 
        # như dịch xong 
        print(oUtput)
    except:      
        print('none')

# hàm này sẽ dịch trên wiki,



for i in range(0, len(aray)):
    print(aray[i], end=" ")
    extractWiki(aray[i])
    # print(extractGlosbe(aray[i]))
    # ggTrans(extractGlosbe(aray[i]))
    print("\n")
driver.quit()




# từ đoạn này trở xuống nó bị lỗi r tại mấy trang từ điển nó update lại hết:gg dịch,glosbe,Rừng

# def ggTrans(a):
#     try:
#         driver.get("https://translate.google.com/?sl=en&tl=vi&text="+a+"&op=translate")
#         driver.implicitly_wait(150)
#         output1 = driver.find_element_by_xpath("/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]/span[1]/span/span")
#         print(output1.text)
#     except:
#         print('error')  

# def extractGlosbe(a):
#     try:
#         driver.get("https://vi.glosbe.com/en/vi/"+a)
#         value=driver.find_element_by_xpath("/html/body/div[2]/app-root/div/app-page-translate/app-ad-layout-top-right-bottom/div/div/article/div/div/app-translate-entry/section/app-translate-entry-summary/div/app-translate-entry-summary-definitions/div/app-translate-entry-definition-line/div[2]")
#         return value.text
#     except:
#         print('error')

# def extractRung(a):
#     try:
#         driver.get("https://www.rung.vn/dict/en_vn/"+a)
#         value=driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[2]/div[3]/div/div[2]/div[2]/div[1]/h5[2]/span").text
#         print(value)
#     except:
#         print('error')