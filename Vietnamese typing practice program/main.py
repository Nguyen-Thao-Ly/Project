import time, random, string, json, os
from PrintFile import *

TIME_PER_LEVEL = [60,55,50,45,40,35,30,25,20,15,10,5]
MAX_LEVEL = 12
SAVE_FILE = "save.json"
TEXT_FILE = "texts.txt"

LANG = {
    "vi" : {
        "welcome" : "Chào mừng bạn đến với chương trình luyện gõ tiếng Việt.",
        "creator" : "Người tạo lập : Rikim",
        "contact" : "Liên hệ Discord : Rikim_cute",
        "start" : "Nhấn Enter để bắt đầu...",
        "label_example" : "Văn bản mẫu : ",
        "label_user" : "Bạn đã gõ   : ",
        "upgrade" : "Bạn đã đủ điều kiện thăng cấp. Bạn có muốn thăng cấp không?",
        "level max" : "Bạn đã ở cấp cao nhất rồi.",
        "level up" : "Đã lên cấp!",
        "win" : "Bạn đã hoàn thành xuất sắc.",
        "tle" : "TLE - Quá thời gian!",
        "WA" : "WA - GÕ SAI.",
        "lose 5" : "Chuỗi thua của bạn đã vượt quá 5, cấp độ của bạn đã bị giảm.",
        "continue" : "Nhấn Enter để tiếp tục, gõ 'End' để thoát",
        "end" : "Hẹn gặp lại. Luyện gõ đều nhé. \nSee ya!"
    },
    "en" : {
        "welcome" : "Welcome to the Vietnamese typing practice program.",
        "creator" : "Creator : Rikim",
        "contact" : "Discord : Rikim_cute",
        "start" : "Press Enter to start...",
        "label_example" : "Example text : ",
        "label_user" : "Your text    : ",
        "upgrade" : "You are eligible for level up. Do you want to upgrade?",
        "level up" : "Leveled up!",
        "level max" : "You're already at the highest level.",
        "win" : "Excellent completion!",
        "tle" : "TLE - Time limit exceeded!",
        "WA" : "WA - TYPING INCORRECT.",
        "lose 5" : "Your losing streak has exceeded 5, your level has been reduced.",
        "continue" : "Press Enter to continue, type 'End' to quit",
        "end" : "See you again. Practice typing regularly!"
    }
}




def count_words(text) :
    text = text.translate(str.maketrans("", "", string.punctuation))
    return len(text.split())

def load_game() :
    if not os.path.exists(SAVE_FILE) or os.path.getsize(SAVE_FILE) == 0:
        return dict(level = 1, win = 0, lose = 0, max_win = 0, words = 0, completed_times = 0)
    with open(SAVE_FILE, "r", encoding = "utf-8") as f :
        return json.load(f)

def save_game(s) :
    with open(SAVE_FILE, "w", encoding = "utf-8") as f :
        json.dump(s, f, ensure_ascii = False, indent = 4)


def main() :
    lang = input("Please choose the language for the interface (vi/en) : ").strip().lower()
    if lang == "english" : lang = "en"
    if lang not in LANG :
        lang = "vi"
    T = LANG[lang]

    print("="*50)
    slow_print(T["welcome"])
    slow_print(T["creator"])
    slow_print(T["contact"])
    print("="*50)
    print_color(GREY, T["start"])
    input()
    

    texts = [l.strip() for l in open(TEXT_FILE, encoding = "utf-8") if l.strip()]
    s = load_game()

    while True :
        allowed = TIME_PER_LEVEL[s["level"]-1]
        text = random.choice(texts)

        print("-"*50)
        fast_print(f"Level : {s['level']} | Time/word : {allowed}s")
        print_color(YELLOW, text)
        print("-"*50)

        start = time.time()
        user_input = input(">>> ").strip()
        end = time.time()

        limit = allowed * count_words(text)
        used = end - start
        success = user_input == text and used <= limit

        if success :
            s["win"] += 1
            s["lose"] = 0
            s["max_win"] = max(s["max_win"], s["win"])
            s["words"] += count_words(text)
            s["completed_times"] += 1
            print_color(GREEN, T["win"])
        else :
            s["lose"] += 1
            s["win"] = 0
            
            if user_input != text :
                print_color(RED, T["WA"])
                show_mistake(text, user_input, T["label_example"], T["label_user"])
                
            if used > limit :
                print_color(RED, T["tle"])
            

        if lang == "vi" : print_color(GREY, f"Chuỗi thắng : {s['win']} | Chuỗi thua : {s['lose']}")
        else : print_color(GREY, f"Streak win : {s['win']} | Streak lose : {s['lose']}")

        if s["lose"] > 5 :
            s["level"] = max(1, s["level"]-1)
            s["lose"] = 0
            print_color(RED, T["lose 5"])

        if success and s["completed_times"] >= 5:
            print_color(GREEN, T["upgrade"])
            if s["level"] == 12  :
                print_color(BLUE, T["level max"])

            else :
                if input("(Yes/No) : ").lower() in ["yes","y","co","có"] :
                    clear_screen()
                    if s["level"] < MAX_LEVEL :
                        s["level"] += 1
                        s["words"] = s["completed_times"] = 0
                        print_color(GREEN, T["level up"])
               

        save_game(s)
        
        print_color(GREY, T["continue"] + " : ")
        cmp = input().lower()
        if cmp == "end" :
            
            print("-"*50)
            slow_print(T["end"])
            print("-"*50)
            break


if __name__ == "__main__" :
    main()
