class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        self.stack.pop()
    
    def isempty(self):
        return len(self.stack) == 0

def get_first_left_bracket_index(string):
    print("----------------", string)
    for idx, char in enumerate(string):
        if char == '[':
            return idx

def get_closing_bracket_idx(string, open_bracket_index):
    stack = Stack()
    stack.push("[")

    print("here : ", string[open_bracket_index + 1:])

    for idx, char in enumerate(string[open_bracket_index + 1:]):
        print("stack :", stack.stack)

        if stack.isempty():
            print("empty: ", open_bracket_index + idx)

            return open_bracket_index + idx
        
        elif char == '[':
            stack.push(char)
            print("push", char)

        elif char == ']':
            stack.pop()
            print("pop")

    return len(string) - 1
        
def get_add_on_string(string):
    output = ""
    for char in string:
        if not char.isalpha():
            return output
        output += char

def get_multipier(string):
    output = ""
    for idx, char in enumerate(string):
        if char.isnumeric():
            return string[idx:]

def decode_string(string):
    if "[" not in string:
        return string

    first_left_bracket_index = get_first_left_bracket_index(string)
    closing_bracket_idx_to_match_the_first_left_bracket = get_closing_bracket_idx(string, first_left_bracket_index)
    # pre_bracket_first_alpha_idx = 
    # pre_bracket_first_num_idx 

    print("first_left_bracket_index :", first_left_bracket_index)
    print("closing_bracket_idx_to_match_the_first_left_bracket :", closing_bracket_idx_to_match_the_first_left_bracket)

    pre_bracket = string[0:first_left_bracket_index]
    inner_bracket = string[first_left_bracket_index + 1 : closing_bracket_idx_to_match_the_first_left_bracket]
    post_bracket = string[closing_bracket_idx_to_match_the_first_left_bracket+1:]

    print("prebracket :" + pre_bracket)
    print("inner_bracket : " + inner_bracket)
    print("post_bracket : " + post_bracket)

    if pre_bracket[0].isalpha():
        add_on = get_add_on_string(string)
    else:
        add_on = ""
    
    multiplier = int(get_multipier(pre_bracket))

    print(multiplier)

    return add_on + multiplier * decode_string(inner_bracket) + decode_string(post_bracket)

# print("ANSWER: ", decode_string("3[a]"))
print("ANSWER: ", decode_string("a2[um2[key]]a2[b13[hi]]"))