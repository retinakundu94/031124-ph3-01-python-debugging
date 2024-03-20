# Python Fundamentals and Debugging

## Learning Goals

- Running python files with `python3` and `python3 -i`

- Installing and importing packages with `pip`

- Using `ipdb` and `print` to debug issues

## Getting Started

Fork and clone this repository.

Get started with this series of commands:
```bash
pipenv install
pipenv shell
```

You should be able to run any of the `.py` files using `python filename.py` or `python3 filename.py`. You can also enter an interactive repl with the `-i` flag for example `python -i filename.py`.

## Debugging Workflow

There are a few golden rules when debugging but one of the most important is to **never make assumptions**.

1. **Test your code as you build it**. A common bad habit is to write hundreds of lines of code without running them one at a time to check whether they work. Ideally you should test your code after building each function or every 5 lines of code.

2. **Build small, modular functions**. If a function has multiple helper functions, it's easier to isolate problems than if you have a single, large function that breaks.

3. **Name your variables logically**. As an example, an object referencing a cat might be `cat` or `catObj` while a list of cat objects would be pluralized such as `cats` or `cats_list`. This can help avoid certain assumptions later down the line.

4. **Check for mispellings**. Code is very finicky and something as simple as a mispelled or even miscased word can lead to massive errors.

5. **Read the error message** when an error occurs. **Never assume** you know why your code broke. Use the error message to **identify where the error occured** and **what kind of error it is**.

6. Use debugging tools like **print to check your variables** right before the error occurs. **Never assume** a variable is coming through as you expect. Often times a variable type or unexpected value leads you on the thread towards fixing your error.

7. Debugging is hard but you'll get better with **practice**! Don't give up, take breaks when you need to, and remember that you've got this!