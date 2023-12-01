from jinja2 import Environment, FileSystemLoader

# Setup Jinja2 environment with loader for 'fragments' directory
env = Environment(loader=FileSystemLoader('fragments'))


def base(as_frag: bool = False):
    if as_frag:
        return env.get_template('fragment.html')
    else:
        return env.get_template('page.html')


def index(as_frag: bool = False) -> str:
    template = env.get_template('index.html', )
    return template.render(layout=base(as_frag))


def new(as_frag: bool = False) -> str:
    template = env.get_template('new.html')
    return template.render(layout=base(as_frag))
