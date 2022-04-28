# ──────────────────────────────────────────────────────────────────────────────

from sys import argv, exit

# ──────────────────────────────────────────────────────────────────────────────

def makergb(a):

    return tuple(int(a.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))

def makex1b(a:tuple):

    return f'\\x1b[38;2;{a[0]};{a[1]};{a[2]}m'

# ──────────────────────────────────────────────────────────────────────────────

def main():

    try:

        _a = argv[1]

        try:

            _b = argv[2]

        except IndexError:

            _b = 'fg'

        if _b == 'fg':

            if (len(_a) == 6, len(_a) == 7):

                print('\n' +\
                    makex1b(
                        makergb(_a)
                        )
                    + '\n')

            elif len(_a.split()) == 3:

                print('\n' +\
                    makex1b(
                        tuple(
                            _a.replace('(', '').replace(')', '').replace(',', '')
                            )
                    )
                    + '\n')

        elif _b == 'bg':

            if (len(_a) == 6, len(_a) == 7):

                print('\n' +\
                    makex1b(
                        makergb(_a)
                        ).replace('3', '4', 1)
                    + '\n')

            elif len(_a.split()) == 3:

                print('\n' +\
                    makex1b(
                        tuple(
                            _a.replace('(', '').replace(')', '').replace(',', '')
                            ).replace('3', '4', 1)
                    )
                    + '\n')

    except IndexError:

        while True:

            _a = input('\x1b[33m\n input the color code\n\n\x1b[34m ❯ \x1b[m')

            if _a:

                break

            else:

                print('\n\x1b[31m ! Error, please input at least the color code\n  (RGB/HEX)(examples: #ffffff [hex] 255 255 255 [rgb])')
                continue

        _b = input('\x1b[33m\n Foreground or background?[FG/bg]\n\n\x1b[34m ❯ \x1b[m')

        if not _b:

            _b = 'fg'

        if _b == 'fg':

            if len(_a) == 6 or len(_a) == 7:

                print('\n' +\
                    makex1b(
                        makergb(_a)
                        )
                    + '\n')

            elif len(_a.split()) == 3:

                print('\n' +\
                    makex1b(
                        tuple(
                            _a.replace('(', '').replace(')', '').replace(',', '')
                            )
                    )
                    + '\n')

            else:

                print('\nError\n')
                exit(1)

        elif _b == 'bg':

            if len(_a) == 6 or len(_a) == 7:

                print('\n' +\
                    makex1b(
                        makergb(_a)
                        ).replace('3', '4', 1)
                    + '\n')

            elif len(_a.split()) == 3:

                print('\n' +\
                    makex1b(
                        tuple(
                            _a.replace('(', '').replace(')', '').replace(',', '')
                            )
                    ).replace('3', '4', 1)
                    + '\n')

            else:

                print('\nError\n')
                exit(1)

# ──────────────────────────────────────────────────────────────────────────────

try:

    main()

except KeyboardInterrupt:

    exit(130)