from jinja2 import Environment, FileSystemLoader

# Setup Jinja2 environment with loader for 'fragments' directory
env = Environment(loader=FileSystemLoader('fragments'))


def index() -> str:
    template = env.get_template('index.html')
    return template.render()
