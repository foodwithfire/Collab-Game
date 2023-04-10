from curses import wrapper

ts_opt = [1, 2, 3, 4]

def title_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("welcome in ze game")
    stdscr.addstr(" ")
    title_screen_options(stdscr)
    stdscr.refresh()
    stdscr.getch()

def help_util(stdscr):
    stdscr.clear()
    stdscr.addstr("hello")
    stdscr.refresh()
    stdscr.getch()

def load_game(stdscr):
    stdscr.clear()
    stdscr.addstr("hello")
    stdscr.refresh()
    stdscr.getch()


def new_game(stdscr):
    stdscr.clear()
    stdscr.addstr("hello")
    stdscr.refresh()
    stdscr.getch()

def title_screen_options(stdscr):
    try:
        enter = int(input("> "))
        if enter == 1:
            new_game(stdscr)
        elif enter == 2:
            load_game(stdscr)
        elif enter == 3:
            help_util(stdscr)
        elif enter == 4:
            quit()
        while enter not in ts_opt:
            title_screen(stdscr)
            if enter == 1:
                new_game(stdscr)
            elif enter == 2:
                load_game(stdscr)
            elif enter == 3:
                help_util(stdscr)
            elif enter == 4:
                quit()
    except ValueError:
        stdscr.addstr("no good answer")
        title_screen(stdscr)
        stdscr.refresh()
        stdscr.getch()

def main(stdscr):
    stdscr.clear()
    title_screen(stdscr)
    stdscr.refresh()
    stdscr.getch()

wrapper(main)
