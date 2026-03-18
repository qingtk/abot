from skills import hello, summarize

skills_map = {
    "hello": hello.run,
    "summarize": summarize.run,
}

def execute(skill, *args):
    return skills_map[skill](*args)