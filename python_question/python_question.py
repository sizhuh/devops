file = "/Users/sizhuhicks/Documents/test_python_question.txt"

def reverse_word_of_a_string(file):
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

        with open("output_file.txt", "w") as output_file:
            for line in lines[1:]:
                original_word = line.strip("\n").split(".")
                for word in original_word:
                    reverse_word = word[::-1]
                    line = line.replace(word, reverse_word)
                    new_line = line.replace(word, reverse_word)
                output_file.write(new_line)

reverse_word_of_a_string(file)
