: สร้าง Virtual Enviroment
---
python -m venv env

: Activate Virtual Enviroment
---
env\Scripts\activate

: Export modules to file
---
pip freeze > requirements.txt

: install modules from file
---
pip install -r requirements.txt