#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  # Your code here

  def combinations(n, currentList):
    choices = ["rock", "paper", "scissors"]

    if len(currentList) == 0:
        return combinations(n - 1, [[c] for c in choices])
    if n == 0:
        return currentList

    newList = []
    for combo in currentList:
        for choice in choices:
            newCombo = combo.copy()
            newCombo.append(choice)
            newList.append(newCombo)

    return combinations(n - 1, newList)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')