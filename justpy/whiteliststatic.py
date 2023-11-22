from starlette.staticfiles import StaticFiles
import os.path
from starlette.exceptions import HTTPException

class WhiteListStatic(StaticFiles):
  def __init__(self,ext_list=None,**kwargs):
    super().__init__(**kwargs)
    self.ext_list=ext_list
  async def get_response(self,path,scope):
    name,ext=os.path.splitext(path)
    ext=ext.removeprefix(".")
    if self.ext_list and ext not in self.ext_list:
      raise HTTPException(status_code=403)
    return await super().get_response(path,scope)
