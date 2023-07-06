## Starbucks_menu
starbucks_menu를 db에 저장, 간단한 검색 기능 구현 
<br><br>

## Stack
<div>
<img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white">
<img src="https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=MySQL&logoColor=white">
</div>
<br>

## Requirements
To connect mysql Workbench, make db_password.py

ex)
```python
import pymysql

def password():
    account = pymysql.connect(host = 'localhost', user = "root", password="******", db = "starbucks_menu")
    return account
```
<br>

## Installation
```python
pip install pymysql
pip install pandas
pip install tabulate
```
<br>

## Main Function
<div>
  <h4>옵션 목록</h4>
  <img witdh = 400, height = 120 src = "https://github.com/choijian/Starbucks_menu/assets/43908014/4b7e05c7-451b-4cbf-b13d-2683ead329d5">
  <h4>메뉴 목록<h4>
  <p align="left">
  <img width = "800", height = "150" src="https://github.com/choijian/Starbucks_menu/assets/43908014/23703000-0004-490a-bbd9-b3c74b5826d2">
</p>

</div>

