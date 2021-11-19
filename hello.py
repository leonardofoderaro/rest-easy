import hug

@hug.get('/hello', versions=1)
def hello():
    """Returns a generic 'Hello World' message"""
    return {'message': 'Hello World!'}

@hug.get('/hello', versions=2)
def helloName(name):
    """Returns a custom message using the name passed as parameter, or an error if it's missing"""
    return {'message': 'Hello {}!'.format(name)}
