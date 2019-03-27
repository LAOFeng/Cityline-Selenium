from splinter import Browser


def MAYDAY(website):
    browser1= Browser('chrome')
    browser1.visit(website)
    #login
    browser1.find_by_name('username').fill('liaozefeng@hotmail.com')
    browser1.find_by_name('password').fill('LZF24685')
    browser1.find_by_name('submit').click()

if __name__=='__main__':
    website='https://www.cityline.com/Login.do?targetUrl=https%3A%2F%2Fwww.cityline.com%2FEvents.do'
    MAYDAY(website)
