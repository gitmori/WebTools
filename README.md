# WebTools

<p align="center">
  <img src="/pict/WebTools.jpg?raw=true" width="150px" alt="Sublime's custom image"/>
</p>

**Main Systems**

form_test.py (Web Browser Automation System: Selenium)  
blog.py (Web Scraper: CSS Selectors)  
otoku.py (Web Scraper: xPath)

**Self-Made Modules**

common/chrome_get.py  
common/system_info.py (for macOS only)  
my_module/get_info.py

**.gitignore**

config/my_info.py  
config/site_url.py

## Description

`form_test.py` is an automation system dedicated to specific websites that use Selenium.  
`blog.py` is a scraper dedicated to certain specific websites that use CSS Selectors.  
`otoku.py` is a scraper dedicated to certain specific websites that use xPath.  

***DEMO:***

```bash
python ~/WebTools/form_test.py
```

![form_test.py DEMO Pict](/pict/form_test.png)

## Requirement

macOS 10.11.6 or later  
Python 3.6.5  
Selenium 3.141.0  
Google Chrome 89.0.4389.90  
ChromeDriver 89.0.4389.23

## Usage

```bash
git clone https://github.com/gitmori/WebTools.git ~/WebTools
python ~/WebTools/form_test.py
python ~/WebTools/blog.py
python ~/WebTools/otoku.py
```

## Installation 1 - Python Libraries -

```bash
pip install selenium  
pip install urllib  
pip install lxml  
pip install fake_useragent  
pip install bs4  
pip install requests  
```

## Installation 2 - ChromeDriver -

Check the version of Google Chrome.

![Google Chrome Ver1](/pict/chromever1.png)

![Google Chrome Ver1](/pict/chromever2.png)

![Google Chrome Ver1](/pict/chromever3.png)

Go to the following website: [ChromeDriver - WebDriver for Chrome](https://chromedriver.chromium.org/downloads)

Download a version of the file that is close to the version of Chrome you are using.

![Google Chrome Ver1](/pict/chromever4.png)

![Google Chrome Ver1](/pict/chromever5.png)

Unzip the zip file on your desktop.

Execute the following command.

```bash
mv ~/Desktop/chromedriver /usr/local/bin  
```

# Note

All tools and modules contain Japanese comments.  
These tools can only be run by anyone other than me because the target URL is hidden (.gitignore) .

## Author

Yuki Moriya ([gitmori](https://github.com/gitmori/))  
ym19820219@gmail.com

## Licence

Copyright (c) 2021 Yuki Moriya  
This software is released under the MIT License, see LICENSE.
