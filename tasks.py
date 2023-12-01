from invoke import task

@task
def test(c):
    """run the tests"""
    c.run("mypy .")

@task
def run(c):
    """run the development server"""
    c.run("uvicorn main:app --reload")
