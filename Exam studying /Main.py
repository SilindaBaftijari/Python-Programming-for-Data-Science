{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Main Python Data Types \n",
    "every value in Python is called an obejct, and every object has a specific data type. The hree most-used data types are as follows \n",
    "\n",
    "- Integers(int) - an integer number to represent an object such as number 3 \n",
    "    integers examples : -2, -1, 0, 1, 2, 3, 4, 5 \n",
    "\n",
    "- Floating point numbers(float) - use them to represent floating point numbers \n",
    "    floating point numbers : -1.25, -1.0, --0.5, 0.0, 0.5, 1.0, 1.25 \n",
    "\n",
    "- Strings - Codify a sequence of characters using a string, For example the word \"hello\". strings are immutable, if you already defined one, you cannot change it later on. while you can modify a string with commands such as \"replace()\" or join(), they will create a copy of a string and apply modification to it, rather than rewrite the original one. \n",
    "    strings : \"yo\", \"hey\", \"Hello!\", \"whats up!\" "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# How to create a string in python \n",
    "you can create a string in three ways using single, double or triple quotes. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "## Basig Python String "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "my_string = \"Lets learn python!\"\n",
    "another_string =\"it may seem difficult at first but you can do it!\" \n",
    "a_long_string = \"Yes, you can even master multi-line strings, that cover more than one line with some practice \""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The next step is to use the print function to output your string in the console window. This lets you review your code and ensure that all functions well. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "lets print out a string!\n"
     ]
    }
   ],
   "source": [
    "print(\"lets print out a string!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## String Concatenation \n",
    "The next thing you can master is concatenation - a way to add two things together using the \"+\" operator. Heres how its done: "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "i am readinga new great book!\n"
     ]
    }
   ],
   "source": [
    "string_one = \"i am reading\" \n",
    "string_two = \"a new great book!\" \n",
    "string_three = string_one + string_two \n",
    "print(string_three)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## String Replication \n",
    "\n",
    "As the name implies, this command lets you repeat the same string several times. This is done using the * operator. Mind that this operator acts as a replicator only with the string data types. When applied to numbers it acts as a multiplier. \n",
    "\n",
    "String replication example: "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'AliceAliceAliceAliceAlice'"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'Alice' * 5 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "AliceAliceAliceAliceAlice\n"
     ]
    }
   ],
   "source": [
    "print('Alice'*5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Math Operators \n",
    "For reference heres a list of other math operations you can apply towards numbers \n",
    "\n",
    "| Operators | Operation | Example |\n",
    "| :- | -: | :-: |\n",
    "| ** | Exponent | 2 ** 3 = 8 |\n",
    "| % | Modulus/Remainder | 22 % 8 = 6 |\n",
    "|// | Integer division | 22 // 8 = 2 | \n",
    "| / | Division | 22 / 8 = 2.75 | \n",
    "| * | Multiplication | 3 * 3 = 9 | \n",
    "| - | Substraction | 5 - 2 = 3 | \n",
    "| + | Addition | 2 + 2 = 4 | \n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## How to Store String in Variables \n",
    "\n",
    "Variables are special symbols that assign a specific storafe location to a value thats tied to it. In essence, variables are like special labels that you place on some value to know where its stored. \n",
    "\n",
    "Strings incorporate data. So you can \"pack\" them inside a variabel. Doing so makes it easier to work with complex Python programs. \n",
    "\n",
    "Heres how you can store a string inside a variable "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "my_str = \"hello world\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Lets break it down a bit further \n",
    "- my_str is a variable name \n",
    "- = is the assignment operatior \n",
    "- \"just a random string\" is a value you tie to the variable name \n",
    "\n",
    "Now lets print this out, you receive the string output "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello world\n"
     ]
    }
   ],
   "source": [
    "my_str = \"hello world\"\n",
    "print(my_str)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Built-in Functions in Python \n",
    "\n",
    "You already know the most popular function in Python - print(). another popular one is input() \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Input() function \n",
    "Input() function is a simple way to proomt the user for some input (e.g provide their name) all user input is stored as a string \n",
    "\n",
    "Snippet "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "name = input(\"hi whats your name?\") \n",
    "print(\"nice to mee you\" + name + \"!\") \n",
    "\n",
    "age = input(\"how old are you\") \n",
    "print(\"so you are already \" + str(age)+\"years old,\"+ name + \"!\") "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Len() Function \n",
    "\n",
    "Len() functions helps you find the length of any string, list, tuple, dictionary or another data type \n",
    "\n",
    "example :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The lenght of the string is: 39\n"
     ]
    }
   ],
   "source": [
    "#Testing len() \n",
    "str1 = \"This is an example for testing out len!\"\n",
    "print(\"The lenght of the string is:\", len(str1))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### filter() \n",
    "You can use the filter function to exclude items in an iterable object ( lists, tuples, dictionaries ect.) \n",
    "exaple : "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "18\n",
      "24\n",
      "32\n"
     ]
    }
   ],
   "source": [
    "ages = [5, 12, 17, 18, 24, 32] \n",
    "\n",
    "def myFunc(x): \n",
    "    if x < 18:\n",
    "        return False\n",
    "    else: \n",
    "        return True\n",
    "\n",
    "adults = filter(myFunc, ages)\n",
    "\n",
    "for x in adults: \n",
    "    print(x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## How to Define a Function \n",
    "\n",
    "First use def keyword, followed by the functions name(). the paran"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.9.13 ('base')",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "7c9459ed114c5b17f42de1a9d08fe33e74f39cfbcb6ece8051ae4de86a3c1d74"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
