import random

doors = [0, 0, 0]
user_choose = -1
cond_choose = -1
new_user_choose = -1

number_win = 0
number_loose = 0

log_mode = 0

def _map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

def log_game(string_to_print):
    if(log_mode == 1):
        print(string_to_print)

def winning_box():
    global doors
    right_choose = random.randint(0,2)
    doors[right_choose] = 1

def usr_choose():
    global user_choose
    user_choose = random.randint(0,2)
    

def tv_presenter_choose():
    global cond_choose
    global user_choose

    cond_choose = random.randint(0,2)
    if(doors[cond_choose] == 1):
        tv_presenter_choose()
    if(cond_choose == user_choose):
        tv_presenter_choose()

def and_the_winner_is():
    global user_choose
    global cond_choose
    global doors
    global number_loose
    global number_win

    if(doors[user_choose] == 1):
        number_win = number_win + 1
        log_game("User WIN!!!")
    elif(doors[user_choose] == 0):
        number_loose = number_loose + 1
        log_game("User LOOSE!!!")


def change_choose():
    global user_choose
    global cond_choose
    global number_loose
    global number_win
    global new_user_choose

    new_user_choose = random.randint(0, 2)
    if(new_user_choose == user_choose or new_user_choose == cond_choose):
        change_choose()

def print_door_selected_vector(vector_box):
    if(vector_box == 0):
        return "[X][ ][ ]"
    if(vector_box == 1):
        return "[ ][X][ ]"
    if(vector_box == 2):
        return "[ ][ ][X]"

def print_door_vector(vector_box):
    if(vector_box == [1, 0, 0]):
        return "[C][G][G]"
    if(vector_box == [0, 1, 0]):
        return "[G][C][G]"
    if(vector_box == [0, 0, 1]):
        return "[G][G][C]"

def run_game(game_mode, number_time_run, _log):
    global log_mode
    global doors
    global user_choose
    global new_user_choose

    log_mode = _log
    log_game("Running game with: " + game_mode + " game mode for " + str(number_time_run) + "time")

    if(number_time_run > 0):
        for run in range(number_time_run):
            log_game("====================")
            log_game("run: " + str(run + 1) + " | C=Car, G=Goat")
            #set vector to 0, 0, 0
            doors = [0, 0, 0]
            #selecting winning box
            winning_box()
            log_game("Doors vector:                 " + str(print_door_vector(doors))) #+ str(doors) + " (1 = car, 0 = goat)")
            #user select one box
            usr_choose()
            log_game("User choose a door:           " + str(print_door_selected_vector(user_choose)))# str(user_choose))
            #conductor select one box different from user choose and different from the winning box
            tv_presenter_choose()
            log_game("TV presenter reveals a goat:  " + str(print_door_selected_vector(cond_choose)))
            
            if(game_mode == "change"):
                #user change his choose after conductor choose
                change_choose()
                user_choose = new_user_choose
                log_game("User changes the choice to:   " + str(print_door_selected_vector(user_choose)))
            
            if(game_mode == "keep"):
                #user keep his choose
                log_game("User keep: " + str(user_choose))
            
            and_the_winner_is()

    else:
        print("Number run time [" + str(number_time_run) + "] input not valid")

    print("====================\n")
    print("Monty Hall runned in '" + str(game_mode) + "' mode for " + str(number_time_run) + " times:")
    print("The user won " + str(number_win) + " times [" + str(_map(number_win, 0 , number_time_run, 0, 100)) + "%] and lost " + str(number_loose) + " times [" + str(_map(number_loose, 0 , number_time_run, 0, 100)) + "%]")


#first arg["keep" or "change"], second arg[any number run > 0], third arg[1 = log, 0 = no log]
run_game("keep", 1000, 1)
