from rules import rules
from draw_ball import ball


def main():
    random = ball(5)
    print(sorted(rules(random)))


if __name__ == '__main__':
    main()
