def module_file(module_name: str):
    content = f'''
from nest.common import Module


@Module()
class {module_name}Module:
    pass

'''
    
    newline_index = content.find('\n')
    return content[newline_index + 1:]
