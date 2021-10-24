import os
import sys
import time


def translator():
    input0 = input("Press 1 for English to ascii translation. Press 2 for ascii to English translation: ")
    if input0 == "1":
        input1 = input("Input: ")
        ascii = ""
        if input1 == "":
            input2 = input("Please Enter Input: ")
            if input2 != "":
                for words in input2:
                    ascii += str(ord(words)).zfill(3)
                print(ascii)  # Having trouble with my code here. It won't print complete ascii!
                prompt = input("Would you like to translate anything else? >")
                if prompt == "yes":
                    if __name__ == "__main__":
                        translator()
                        os.execv(__file__, sys.argv)
                elif prompt == "y":
                    if __name__ == "__main__":
                        translator()
                        os.execv(__file__, sys.argv)
                else:  # Continues with yes path, won't take no for an answer!
                    print("Process Completed.")
            else:
                print("You big galoot! I thought I asked you to enter an input!")
                print("\n")
                time.sleep(5)
                if __name__ == "__main__":
                    translator()
                    os.execv(__file__, sys.argv)
        else:
            for words in input1:
                ascii += str(ord(words)).zfill(3)
            print(ascii)  # Is the multiple lines because of the for loop?
            prompt = input("Would you like to translate anything else? >")
            if prompt == "yes":
                if __name__ == "__main__":
                    translator()
                    os.execv(__file__, sys.argv)
            elif prompt == "y":
                if __name__ == "__main__":
                    translator()
                    os.execv(__file__, sys.argv)
            else:  # Continues with yes path, won't take no for an answer!
                print("Process Completed.")
    elif input0 == "2":
        input_ascii = input("Enter ascii values separated by a space: ")
        lst = input_ascii.split()
        for i in range(len(lst)):
            lst[i] = int(lst[i])
        res = ''.join(map(chr, lst))
        print(str(res))
        prompt = input("Would you like to translate anything else? >")
        if prompt == "yes":
            if __name__ == "__main__":
                translator()
                os.execv(__file__, sys.argv)
        elif prompt == "y":
            if __name__ == "__main__":
                translator()
                os.execv(__file__, sys.argv)
        else:  # Continues with yes path, won't take no for an answer!
            print("Process Completed.")
    else:
        print("You broke the code! Rerunning now...")
        print("\n")
        time.sleep(5)
        if __name__ == "__main__":
            translator()
            os.execv(__file__, sys.argv)


translator()
