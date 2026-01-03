import os
def printProcess(process):
    for x in process:
        print(f"Phase {process.index(x)+1} - {x}")

if __name__ == "__main__":
    process = []
    controlCharacter = True
    try:
        print("Enter the process name and a short description separated by a '-' " +
              "\n Press Enter to stop entering steps.\n")
        while controlCharacter:
            step = input()
            if step != "":
                process.append(step)
            else:
                controlCharacter = False

        printProcess(process)
    except Exception:
        print("Error", Exception)

