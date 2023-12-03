# import typer
# import os
# from typing_extensions import Annotated

# # @ccwc.command()
# # def c(file_name:  str):
# #         bytes = os.path.getsize("./" + file_name)
# #         print(f"{bytes} {file_name}")

# # @ccwc.command()
# # def l(file_name: str):
# #         with open(r"./"+file_name, "r", encoding="utf-8") as fp:
# #             lines = len(fp.readlines())
# #             print(f"{lines} {file_name}")

# # @ccwc.command()
# # def w(file_name: str):
# #       with open (file_name, "r", encoding="utf-8") as fp:
# #             data = fp.read()
# #             words = len(data.split())
# #             print(f"{words} {file_name}")

# # @ccwc.command()
# # def m(file_name: str):
# #       with open (file_name, "rb") as fp:
# #             data = fp.read()
# #             count = 0
# #             for char in data:
# #                 if char != "\n":
# #                     count += 1
# #             print(f"{count} {file_name}")

# # @ccwc.command()
# def main(
#     file_name: str,
#     c: Annotated[bool, typer.Option("--bytes", "-c")] = False,
#     l: Annotated[bool, typer.Option("--lines", "-l")] = False,
#     m: Annotated[bool, typer.Option("--chars", "-m")] = False,
#     w: Annotated[bool, typer.Option("--words", "-w")] = False,
# ):
    
#     bytes = os.path.getsize(file_name)
#     with open(r"./"+file_name, "r", encoding="utf-8") as fp:
#         lines = len(fp.readlines())
#     with open (file_name, "r", encoding="utf-8") as fp:
#         data = fp.read()
#         words = len(data.split())
        
#     if c:
#         print(f"{bytes} {file_name}")
#     elif l:
#         print(f"{lines} {file_name}")
#     elif m:
#         with open (file_name, "rb") as fp:
#             data = fp.read()
#             count = 0
#             for char in data:
#                 if char != "\n":
#                     count += 1
#             print(f"{count} {file_name}")
#     elif w:
#         print(f"{words} {file_name}")
#     else:
#         print(f"{lines}  {words} {bytes} {file_name}")

# if __name__ == "__main__":
#     typer.run(main)

import click
import os
import sys

@click.command()
@click.argument('filename', nargs=-1, type=click.Path(exists=True))
@click.option('-c', '--bytes', 'bytes', is_flag=True, help="Returns the number of bytes in the given file.")
@click.option('-l', '--lines', 'lines', is_flag=True, help="Returns the number of lines in the given file.")
@click.option('-w', '--words', 'words', is_flag=True, help="Returns the number of words in the given file.")
@click.option('-m', '--chars', 'chars', is_flag=True, help="Returns the number of chars in the given file.")
def main(filename, bytes, lines, words, chars):

    if not filename:
        filename = ""
        data = sys.stdin.buffer
        noOfBytes = noOfLines = noOfWords = noOfChars = 0
        for line in data:
            noOfWords += len(line.split())
            noOfBytes += len(line)
            noOfLines += 1
            noOfChars += len(line.decode())
    else:
        noOfBytes = os.path.getsize(filename)
        with open(r"./"+filename, "r", encoding="utf-8") as fp:
            noOfLines = len(fp.readlines())
        with open (filename, "r", encoding="utf-8") as fp:
            data = fp.read()
            noOfWords = len(data.split())
        with open (filename, "rb") as fp:
            data = fp.read()
            noOfChars = 0
            for char in data:
                if char != "\n":
                    noOfChars += 1
    
    if bytes:
        click.echo(f"{noOfBytes} {filename}")
    elif lines:
        click.echo(f"{noOfLines} {filename}")
    elif words:
        click.echo(f"{noOfWords} {filename}")
    elif chars:
        click.echo(f"{noOfChars} {filename}")
    else:
        click.echo(f"{noOfLines} {noOfWords} {noOfBytes} {filename}")

if __name__ == '__main__':
    main()