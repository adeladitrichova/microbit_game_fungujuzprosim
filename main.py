play_for = 0
hold_for = 0
def on_button_pressed_a():
    global play_for
    play_for = randint(500, 2000)
    basic.show_icon(IconNames.EIGTH_NOTE)
    music.play_tone(Note.C, play_for)
input.on_button_pressed(Button.A, on_button_pressed_a)
def on_logo_event_touched():
    global hold_for
    if play_for > 0:
        hold_for = control.millis()
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_event_touched)
def on_logo_event_released():
    global hold_for, play_for
    if hold_for > 0:
        duration = control.millis() - hold_for
        difference = duration - play_for
        led.plot_bar_graph(difference, play_for)
        play_for = 0
        hold_for = 0
input.on_logo_event(TouchButtonEvent.RELEASED, on_logo_event_released)
