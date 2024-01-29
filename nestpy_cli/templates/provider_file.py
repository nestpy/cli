def provider_file(provider_name: str, type: str = 'Provider'):
    content = f'''
from nest.common import Injectable


@Injectable()
class {provider_name}{type}:
    pass

'''
    
    newline_index = content.find('\n')
    return content[newline_index + 1:]
