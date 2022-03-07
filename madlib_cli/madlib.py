import re

def instructions():
     """
                    Madlib is a game where the player will be asked to fill up a template without knowing its content.
                    - with the collected user inputs, each provided input will be placed in its right position.
                    - then the complete response will be sent back to the user in the command line
     """
   



def read_template(path):
    """
    This function is for reading the template file 
    """
    try:
        with open(path, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        raise FileNotFoundError("The file is not found")
 
read_template("assets/read_test.txt")


def parse_template(text):
    """
    This function returns a list of the provided words inside {}
    """
    print("Please submit the following words:")

    user_input_list = []
    user_input = re.findall(r'\{.*?\}', text)
    for i in user_input:
        user_input_list.append(i[1:-1])

    user_list = tuple(user_input_list)
    content = re.sub(r'\{.*?\}', "{}", text)
    
    return(content, user_list)
 



def merge(text, user_text):
    """
    This function insures that each provided input is placed into the correct position within the template.
    """
    return text.format(*user_text)




def copy(template):
    file = open("assets/user_template.txt", "w")
    file.write(template)
    print(template)



def Matlib_game():
    print(instructions())
    content = read_template("assets/template.txt")
    text, user_list = parse_template(content)

    user_text = [input(f"Enter {i}: ") for i in user_list]

    merge(text, user_text)

    


if __name__ == "__main__":
    Matlib_game()