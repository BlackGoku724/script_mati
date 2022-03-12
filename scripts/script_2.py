#hello world

def hello_world(name):
    try:
        name= input('ingrese su nombre')
        print(f'hello world {name}')
        return 1
    except Exception as e:
        print(f'error: {e}')
        return 0