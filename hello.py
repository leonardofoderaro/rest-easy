import hug

@hug.get('/hello')
def hello():
    return {'message': 'Hello World!'}
