from . import decorators


@decorators.solution_equation('lib_files/tst_csv.csv')
@decorators.save_params
def quadratic_roots(a=1, b=1, c=1):

    d = b ** 2 - 4 * a * c
    if d < 0:
        return 0
    if d == 0:
        if a:
            x1 = x2 = -b / (2 * a)
        else:
            x1 = x2 = 0
    else:
        if a:
            x1 = (-b - d ** 0.5) / (2 * a)
            x2 = (-b + d ** 0.5) / (2 * a)
        else:
            x1 = x2 = 0
    return x1, x2

