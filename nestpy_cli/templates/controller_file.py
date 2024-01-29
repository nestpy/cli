def controller_file(controller_name: str):
    content = f'''
from nest.common.decorators import Controller, Get


@Controller("/")
class {controller_name}Controller:

    @Get("/")
    def findAll(self):
        return {"Hello": "World"}


'''
    
    newline_index = content.find('\n')
    return content[newline_index + 1:]
