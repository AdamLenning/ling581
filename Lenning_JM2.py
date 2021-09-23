# Adam Lenning
# Ling 581

# 2.1 REGEX
# 2.1.1 /[A-Za-z]*/
# 2.1.2 /[a-z]*b/
# 2.1.3 /[b*[bab]b*]*/

# 2.2 PATTERN MATCHING  
# 2.2.1 /(\b.*\b) \1/
# 2.2.2 /^\d.*\b\w+\b/
# 2.2.3 /(.*\bgrotto\b.*\braven\b.*)|(.*\braven\b.*\bgrotto\b.*)/
# 2.2.4 /(\w+)\b.*\b\1/

import sys
print(sys.path)
import re
import pandas as pd

def eliza_2_3():
    """Simulates the chatbot Eliza
    """

    in_1 = input('(Type \'done\' at any time to exit.) How are you feeling today? ')
    while in_1.lower() != "done":
        sad_match = re.search('.*(?:I am|I\'m) (depressed|sad).*', in_1, re.IGNORECASE)
        happy_match = re.search('.*(?:I am|I\'m) (excited|happy).*', in_1, re.IGNORECASE)
        mad_match = re.search('.*(?:I am|I\'m) (angry|mad).*', in_1, re.IGNORECASE)


        if sad_match:
            feeling = sad_match.group(1)
            in_1 = input('I\'m sorry you are feeling {}. Why are you feeling that way? '.format(feeling))
            query = re.search('.*because (.*)', in_1, re.IGNORECASE)
            if query:
                reason = query.group(1)
                print("I'm really sorry to hear that {}.".format(reason))

        elif happy_match:
            feeling = happy_match.group(1)
            in_1 = input('I\'m happy you are feeling {}! Why are you feeling that way? '.format(feeling))
            query = re.search('.*because (.*)', in_1, re.IGNORECASE)
            if query:
                reason = query.group(1)
                print("That is great to hear that {}.".format(reason))

        elif mad_match:
            feeling = mad_match.group(1)
            in_1 = input('That is unfortunate that you are feeling {}! Why are you feeling that way? '.format(feeling))
            query = re.search('.*because (.*)', in_1, re.IGNORECASE)
            if query:
                reason = query.group(1)
                print("That is infuriating to hear that {}.".format(reason))

        else:
            print("I'm sorry. I don't recognize that feeling. I can tell if you sad, happy or mad?")
        
        
        in_1 = input("How else are you feeling today?")

# 2.4 leda -> deal
#       -   d   e   a   l 
#   -   0   1   2   3   4
#   l   1   1   2   3   4
#   e   2   2   1   2   3   
#   d   3   3   2   2   3
#   a   4   4   3   3   3   -> edit distance 3

# 2.5 drive -> brief, drive -> dives
#       -   b   r   i   e   f
#   -   0   1   2   3   4   5
#   d   1   1   2   3   4   5
#   r   2   2   1   2   3   4   
#   i   3   3   2   1   2   3
#   v   4   4   3   2   2   3
#   e   5   5   4   3   3   3   -> edit distance 3
# 
#       -   d   i   v   e   s
#   -   0   1   2   3   4   5   
#   d   1   0   1   2   3   4
#   r   2   1   1   2   3   4
#   i   3   2   1   2   3   4   
#   v   4   3   2   1   2   3
#   e   5   4   3   2   3   3   ->  edit distance 3

# Both are the same



def edit_distance_alg(s1:str, s2:str, m:int, n:int):
    """Computes the edit distance between 2 strings

    Args:
        s1 (str): string 1 to compare
        s2 (str): strin 2 to compare
        m (int): length of s1
        n (int): length of s2

    Returns:
        int: shortest edit distance between s1 to s2 
    """
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
 
    for i in range(m + 1):
        for j in range(n + 1):

            if i == 0:
                dp[i][j] = j
 
            elif j == 0:
                dp[i][j] = i
 
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
 
            else:
                dp[i][j] = 1 + min(dp[i][j-1],
                                   dp[i-1][j],
                                   dp[i-1][j-1])
    return dp[m][n]


def edit_distance_comp(s1:str, s2:str, s3:str):
    """Compares the edit distance between one string to 2 others and returns which string is closer

    Args:
        s1 (str): string 1 to be compared with the other strings
        s2 (str): string 2 to be compared with string 1
        s3 (str): string 3 to be compared with string 1

    Returns:
        int/str: either the distance between the closer of the strings or a statement saying they are equal
    """

    d1 = edit_distance_alg(s1, s2, len(s1), len(s2))
    d2 = edit_distance_alg(s1, s3, len(s1), len(s3))
    if (d1 < d2):
        return d1
    elif (d2 < d1):
        return d2
    else:
        return "Edit distance equal"


def edit_distance_2_6():
    """Uses the edit distance algorithm to check edit distance of 2.4 and 2.5
    """
    print(edit_distance_alg("leda", "deal", 4, 4))
    print(edit_distance_comp("drive", "brief", "divers"))


COST_IN = 1
COST_DEL = 1
COST_SUB = 1


def get_cost_direction(left, up, diagonal):
    """[summary]

    Args:
        left ([type]): [description]
        up ([type]): [description]
        diagonal ([type]): [description]

    Returns:
        [type]: [description]
    """
    if (left[0] + COST_IN <= up[0] + COST_DEL) and (left[0] + COST_IN <= diagonal[0] + COST_SUB):
        return (left[0] + COST_IN, "Left")
    elif (up[0] + COST_DEL <= left[0] + COST_IN) and (up[0] + COST_DEL <= diagonal[0] + COST_SUB):
        return (up[0] + COST_DEL, "Up")    
    else:
        return (diagonal[0] + COST_IN, "Diagonal") 


def edit_distance_2_7(s1:str, s2:str, m:int, n:int):
    """Computes the edit distance between 2 strings and gives the backtrace

    Args:
        s1 (str): string 1 to compare
        s2 (str): strin 2 to compare
        m (int): length of s1
        n (int): length of s2

    Returns:
        int: shortest edit distance between s1 to s2 
    """
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
 
    for i in range(m + 1):
        for j in range(n + 1):

            if i == 0: # come from left
                # add direction
                dp[i][j] = (j, "Left")
 
            elif j == 0: # Come from up
                # add direction
                dp[i][j] = (i, "Up")
 
            elif s1[i-1] == s2[j-1]: # Check equal, Come from diagonal
                # add direction
                dp[i][j] = dp[i-1][j-1]
 
            else:
                # need to change the min function to also store the direction
                dp[i][j] = get_cost_direction(dp[i][j-1], 
                                                dp[i-1][j],
                                                dp[i-1][j-1])
    
    # implement list of changes
    # return backtrace(dp[m][n])
    # return dp
    col_names = ["-"] + [s for s in s2[::]]
    row_names = ["-"] + [s for s in s1[::]]
    df = pd.DataFrame(dp, columns=col_names)
    df.index = row_names
    return df
        

def main():
    eliza_2_3()
    edit_distance_2_6()
    print(edit_distance_2_7("leda", "deal", 4, 4))


if __name__ == "__main__":
    main()