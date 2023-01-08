# Justpy Tutorial demo close_test 
# `on_disconnect(self, websocket=None)`       
#      
# generated by write_as_demo  at 2023-01-08T10:02:35.641395+00:00 
# 
# see https://justpy.io/reference/webpage#on_disconnectself-websocketnone
# see https://github.com/justpy-org/justpy/blob/master/docs/reference/webpage.md

import justpy as jp

class MyPage(jp.WebPage):

    async def on_disconnect(self, websocket=None):
        await super().on_disconnect()
        # Do what you want to do on disconnect here
        print('Page disconnected')


def close_test():
    wp = MyPage()
    for i in range(10):
        jp.Div(text=f'Div {i}', a=wp, classes='bg-blue-500 text-white m-2 p-2 w-32')
    return wp

# initialize the demo
from examples.basedemo import Demo
Demo("close_test", close_test)
