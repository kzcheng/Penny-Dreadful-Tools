import os
import sys

LINT_PATHS = [o for o in os.listdir('.') if os.path.isdir(o) and os.path.exists(os.path.join(o, '__init__.py'))]
LINT_PATHS.extend([o for o in os.listdir('.') if os.path.isfile(o) and os.path.splitext(o)[1] == '.py'])

def run() -> None:
    cmd = sys.argv[1].lower()

    if cmd in ('lint', 'pylint'):
        lint()

    if cmd in ('types', 'mypy'):
        mypy()

def lint() -> None:
    args = sys.argv[2:] or ['--rcfile=.pylintrc', # Load rcfile first.
                            '--ignored-modules=alembic,MySQLdb,flask_sqlalchemy', # override ignored-modules (codacy hack)
                            '--load-plugins', 'pylint_quotes',
                            '--reports=n', '-f', 'parseable'
                           ]
    args.extend(LINT_PATHS)
    import pylint.lint
    pylint.lint.Run(args)

def mypy() -> None:
    args = sys.argv[2:] or [
        '--ignore-missing-imports',     # Don't complain about 3rd party libs with no stubs
        '--disallow-untyped-calls',     # Strict Mode.  All function calls must have a return type.
        # "--disallow-incomplete-defs", # All parameters must have type definitions.
        '.'                             # Invoke on the entire project.
        ]
    from mypy import api
    result = api.run(args)

    if result[0]:
        print(result[0])  # stdout

    if result[1]:
        print(result[1])  # stderr

    print('\nExit status: {code} ({english})'.format(code=result[2], english='Failure' if result[2] else 'Success'))
    sys.exit(result[2])

if __name__ == '__main__':
    run()