import re

def snake_to_camel(snake_str):
    a = snake_str.split('_')
    return a[0] + ''.join(word.capitalize() for word in a[1:])

snake_text = "hello_world_example"
camel_text = snake_to_camel(snake_text)
print(camel_text)
#elloHelloWorldExample