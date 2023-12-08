SENTINEL = False
#change the text below as per your needs, or just change it to a string input for variability
string = """Frosty_the_Snowman;_Was_a_jolly_happy_soul;_With_a_corncob_pipe_and_a_button_nose;_And_two_eyes_made_out_of_coal;_Frosty_the_Snowman;_Is_a_fairytale,_they_say;_He_was_made_of_snow;_But_the_children_know;_How_he_came_to_life_one_day;_There_must_have_been_some_magic_in;_That_old_silk_hat_they_found;_For_when_they_placed_it_on_his_head;_He_began_to_dance_around;_Oh,_Frosty,_the_Snowman;!"""
print(string)
symbols = [
    "😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "😊", "😇",
    "🙂", "🙃", "😉", "😌", "😍", "🥰", "😘", "😗", "😙", "😚",
    "😋", "😛", "😜", "🤪", "😝", "🤑", "🤗", "🤭", "🤫", "🤔",
    "🤐", "🤨", "😐", "😑", "😶", "😏", "😒", "🙄", "😬", "😮",
    "😯", "😲", "😳", "🥺", "😦", "😧", "😨", "😰", "😥", "😢",
    "😭", "😱", "😖", "😣", "😞", "😓", "😩", "😫", "🥱", "😤",
    "😡", "😠", "🤬", "😈", "👿", "💀", "☠️", "💩", "🤡", "👻",
    "👽", "👾", "🤖", "😺", "😸", "😹", "😻", "😼", "😽", "🙀",
    "😿", "😾", "🙈", "🙉", "🙊", "💋", "💌", "💘", "💝", "💖",
    "💗", "💓", "💞", "💕", "💟", "❣️", "💔", "❤️", "🧡", "💛",
    "💚", "💙", "💜", "🤎", "🖤", "🤍", "💯", "💢", "💥", "💫",
    "💦", "💨", "🕳️", "💣", "💬", "👁️‍🗨️", "🗨️", "🗯️", "💭",
    "💤", "👋", "🤚", "🖐️", "✋", "🖖", "👌", "🤌", "🤏", "✌️",
    "🤞", "🤟", "🤘", "🤙", "👈", "👉", "👆", "🖕", "👇", "☝️",
    "👍", "👎", "✊", "👊", "🤛", "🤜", "👏", "🙌", "👐", "🤲",
    "🤝", "🙏", "✍️", "💅", "🤳", "💪", "🦵", "🦶", "👂", "🦻",
    "👃", "🧠", "🦷", "🦴", "👀", "👁️", "👅", "👄", "💋", "🩸",
    "🦷", "🦴", "🦵", "🦶", "👂", "👃", "👁️", "👀", "👅", "👄",
    "👶", "👧", "🧒", "👦", "👩", "🧑", "👱‍♀️", "👱‍♂️", "🧔",
    "🧔‍♀️", "🧔‍♂️", "👨‍🦰", "👩‍🦰", "👨‍🦱", "👩‍🦱", "👨‍🦲",
    "👩‍🦲", "👨‍🦳", "👩‍🦳", "👨‍🦯", "👩‍🦯", "👵", "👴", "👲",
    "👳", "👳‍♀️", "👳‍♂️", "🧕", "🤵", "👰", "🤰", "🤱", "👩‍🍼",
    "👨‍🍼", "🧑‍🍼", "👼", "🎅", "🤶", "🦸", "🦸‍♀️", "🦸‍♂️", "🦹",
    "🦹‍♀️", "🦹‍♂️", "🧙", "🧙‍♀️", "🧙‍♂️", "🧚", "🧚‍♀️", "🧚‍♂️",
    "🧛", "🧛‍♀️", "🧛‍♂️", "🧜", "🧜‍♀️", "🧜‍♂️", "🧝", "🧝‍♀️", "🧝‍♂️",
    "🧞", "🧞‍♀️", "🧞‍♂️", "🧟", "🧟‍♀️", "🧟‍♂️", "💆", "💆‍♂️", "💆‍♀️",
    "💇", "💇‍♂️", "💇‍♀️", "🚶", "🚶‍♂️", "🚶‍♀️", "🏃", "🏃‍♂️", "🏃‍♀️",
    "💃", "💃‍♂️", "💃‍♀️", "🕺", "🕴️", "👯", "👯‍♂️", "👯‍♀️", "🧖",
    "🧖‍♂️", "🧖‍♀️", "🧘", "🧘‍♂️", "🧘‍♀️", "🛀", "🛌", "🕐", "🕑",
    "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚", "🕛",
    "🕜", "🕝", "🕞", "🕟", "🕠", "🕡", "🕢", "🕣", "🕤", "🕥",
    "🕦", "🕧", "🏁", "🏳️", "🏴", "🏴‍☠️", "🏳️‍🌈", "🏁", "🚩",
    "🎌", "🇦🇫", "🇦🇽", "🇦🇱", "🇩🇿", "🇦🇸", "🇦🇩", "🇦🇴", "🇦🇮",
    "🇦🇶", "🇦🇬", "🇦🇷", "🇦🇲", "🇦🇼", "🇦🇺", "🇦🇹", "🇦🇿", "🇧🇸",
    "🇧🇭", "🇧🇩", "🇧🇧", "🇧🇾", "🇧🇪", "🇧🇿", "🇧🇯", "🇧🇲", "🇧🇹",
    "🇧🇴", "🇧🇦", "🇧🇼", "🇧🇷", "🇮🇴", "🇻🇬", "🇧🇳", "🇧🇬", "🇧🇫",
    "🇧🇮", "🇰🇭", "🇨🇲", "🇨🇦", "🇮🇨", "🇨🇻", "🇧🇶", "🇰🇾", "🇨🇫",
    "🇹🇩", "🇨🇱", "🇨🇳", "🇨🇽", "🇨🇨", "🇨🇴", "🇰🇲", "🇨🇬", "🇨🇩",
    "🇨🇰", "🇨🇷", "🇨🇮", "🇭🇷", "🇨🇺", "🇨🇼", "🇨🇾", "🇨🇿", "🇩🇰",
    "🇩🇯", "🇩🇲", "🇩🇴", "🇪🇨", "🇪🇬", "🇸🇻", "🇬🇶", "🇪🇷", "🇪🇪",
    "🇪🇹", "🇪🇺", "🇫🇰", "🇫🇴", "🇫🇯", "🇫🇮", "🇫🇷", "🇬🇫", "🇵🇫",
    "🇹🇫", "🇬🇦", "🇬🇲", "🇬🇪", "🇩🇪", "🇬🇭", "🇬🇮", "🇬🇷", "🇬🇱",
    "🇬🇩", "🇬🇵", "🇬🇺", "🇬🇹", "🇬🇬", "🇬🇳", "🇬🇼", "🇬🇾", "🇭🇹",
    "🇭🇳", "🇭🇰", "🇭🇺", "🇮🇸", "🇮🇳", "🇮🇩", "🇮🇷", "🇮🇶", "🇮🇪",
    "🇮🇲", "🇮🇱", "🇮🇹", "🇯🇲", "🇯🇵", "🎌", "🇯🇪", "🇯🇴", "🇰🇿",
    "🇰🇪", "🇰🇮", "🇽🇰", "🇰🇼", "🇰🇬", "🇱🇦", "🇱🇻", "🇱🇧", "🇱🇸",
    "🇱🇷", "🇱🇾", "🇱🇮", "🇱🇹", "🇱🇺", "🇲🇴", "🇲🇰", "🇲🇬", "🇲🇼",
    "🇲🇾", "🇲🇻", "🇲🇱", "🇲🇹", "🇲🇭", "🇲🇶", "🇲🇷", "🇲🇺", "🇾🇹",
    "🇲🇽", "🇫🇲", "🇲🇩", "🇲🇨", "🇲🇳", "🇲🇪", "🇲🇸", "🇳🇦", "🇳🇵",
    "🇳🇱", "🇳🇨", "🇳🇿", "🇳🇮", "🇳🇪", "🇳🇬", "🇳🇺", "🇳🇫", "🇰🇵",
    "🇲🇵", "🇳🇴", "🇴"]
e = 0
keydict = {}
while not SENTINEL:
    divis = (len(string) % 2) / 2
    maxval = 1
    maxind = 0
    strreplace = ""
    place = 0
    c = 0
    d = 0
    multmaxcol = [1]
    matches = 0
    loc = []
    locmatches = []
    for j in range(int((len(string))/2 - divis - 1)):
        subloc = []
        sublocmatches = []
        for i in range(len(string) - (1+j)):
            sub = string[i:i+2+j]
            addthing = 0
            matches = 0
            if sub not in subloc:
                for k in range(len(string) - 1):
                    cyclesub = string[k+addthing:k+2+j+addthing]
                    if sub == cyclesub:
                        addthing += len(sub) - 1
                        matches+=1
                subloc.append(sub)
                sublocmatches.append(matches)
            else:
                pass
        loc.append(subloc)
        locmatches.append(sublocmatches)

    while d<len(locmatches):
        c=0
        maxval = 1
        a=locmatches[len(locmatches) - d - 1]
        while c < len(a):
            if a[c] > maxval:
                maxval = a[c]
                maxind = c
            c += 1
        if maxval != 1:
            trystr = loc[len(loc)-1-place][maxind]
            if maxval*len(trystr) > max(multmaxcol):
                strreplace = loc[len(loc)-1-place][maxind]
            multmaxcol.append(maxval*len(trystr))
        d+=1
        place += 1
    if maxval == 1:
        SENTINEL = True
    else:
        string = string.replace(strreplace,(symbols[e]))
        keydict[symbols[e]] = strreplace
        e += 1
print(string)
print(keydict)
