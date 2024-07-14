import google.generativeai as genai
from .models import *
import os


def generate_content_bot(msg):
    i = 0
    while 1 == 1:
        try:
            print("Avrobot yozmoqda....")
            genai.configure(api_key='AIzaSyA9G7mUl8mXSZTWxZfQfTe50pssw6H-Uok')
            model = genai.GenerativeModel('gemini-1.0-pro-001')
            response = model.generate_content(msg)
            yanit = response.text
            print(yanit)
            return yanit.replace('•', '  *')
        except ValueError:
            i = i + 1
            print("utils -> Has got ValueError. Tried: " + str(i))
            if i > 3:
                return """Has got ValueError. <br><span class="placeholder col-12 bg-danger"></span>"""
            else:
                continue
        except Exception as e:
            return str(e) + """<br><span class="placeholder col-12 bg-danger"></span>"""
