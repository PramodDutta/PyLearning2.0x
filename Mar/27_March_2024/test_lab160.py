# Env File - .(dot.env)
# How do you store you password or credentials in the framework
# pip install python-dotenv

from dotenv import  load_dotenv
import os
def test_login():
    load_dotenv()
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    print(username, password)
    
