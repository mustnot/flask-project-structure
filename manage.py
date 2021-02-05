import sys

sys.path.append("myproject")

def main():
    from myproject.contrib.management import execute_command
    execute_command(sys.argv)

if __name__ == "__main__":
    main()