# Justpy Tutorial demo javascript_test 
# Simple run_javascript example       
#      
# generated by write_as_demo  at 2023-01-08T10:02:47.668980+00:00 
# 
# see https://justpy.io/reference/webpage#simple-run_javascript-example
# see https://github.com/justpy-org/justpy/blob/master/docs/reference/webpage.md

import justpy as jp

async def my_click(self, msg):
    await msg.page.run_javascript("""
    for (var i = 0; i<10; i++) {
        console.log('Line: ' + i);
        }
    """)

def javascript_test():
    wp = jp.WebPage()
    d = jp.Div(a=wp, classes='m-2')
    b = jp.Button(text='Run Script', a=d, classes=jp.Styles.button_simple, click=my_click)
    return wp

# initialize the demo
from examples.basedemo import Demo
Demo("javascript_test", javascript_test)
