def main_file():
    content = f'''
from nest.core import NestFactory
from app_module import AppModule


def bootstrap():
    app = NestFactory.create(AppModule)

    app.listen()

if __name__ == "__main__":
    bootstrap()

'''
    
    newline_index = content.find('\n')
    return content[newline_index + 1:]