#! /usr/bin/env python

def check_constraints(file):
    with open(file, "r") as f:
        lines = f.readlines()
        # add constraints
        # number of testcases should be 1<=T<=10
        t = int(lines[0])
        msg = "Expect Number of testcases T should be 1<=T<=10, actual T is {}".format(t)
        assert 1<=t<=10, msg

        # add constraints
        # lengh of string should be 1<=Length of String<=2000
        l = int(len(lines) - 1)
        msg = "Expect 1<=Length of String<=2000, actual Length of String is {}".format(l)
        assert 1<=l<=2000, msg

        # add check for mismatch t and l
        msg = "Mismatch number of testcases {} and lengh of strings {}".format(t,l)
        assert t == l, msg

        return lines

def reverse_word_of_a_string(file):
    lines = check_constraints(file)
    with open("output_file.txt", "wa") as output_file:
        # start read 2nd line in the file
        for line in lines[1:]:
            # sptrip newline and spearte word by speartor "."
            original_word = line.strip("\n").split(".")

            # start reverse word in each line
            reverse_word = [word[::-1] for word in original_word]

            # join the list of reversed words use "."
            new_line = ".".join(reverse_word) + '\n'

            # append the new line to the file
            output_file.write(new_line)


def reverse_word_of_a_string_use_replace_method(file):

    # check constraints for the given file, assert errors
    lines = check_constraints(file)
    with open("output_file.txt", "w") as output_file:
        for line in lines[1:]:
            original_word = line.strip("\n").split(".")
            for word in original_word:
                reverse_word = word[::-1]

                # replace original word in the line by reserved word one by one
                line = line.replace(word, reverse_word)

                # get the final reversed string
                new_line = line.replace(word, reverse_word)
            output_file.write(new_line)

file = "/Users/sizhuhicks/Documents/ucsc_class/DevOps/devops/python_question/test_python_question.txt"
#reverse_word_of_a_string(file)
reverse_word_of_a_string_use_replace_method(file)
