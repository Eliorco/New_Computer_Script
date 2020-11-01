import os
import sys
import subprocess


def do_bash_command(command: str, is_output: bool) -> bool:
    try:
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, err = process.communicate()
    except subprocess.SubprocessError as se:
        print(se, err)
        return False
    return str(output).encode("utf-8") if is_output else True


def main():
    with open('commands.txt', 'r') as f:
        for command in f.readlines():
            print(do_bash_command(command, True))
    return True


if __name__ == '__main__':
    main()
