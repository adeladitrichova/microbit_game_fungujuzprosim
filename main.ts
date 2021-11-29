let play_for = 0
let hold_for = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    play_for = randint(500, 2000)
    basic.showIcon(IconNames.EigthNote)
    music.playTone(Note.C, play_for)
})
input.onLogoEvent(TouchButtonEvent.Touched, function on_logo_event_touched() {
    
    if (play_for > 0) {
        hold_for = control.millis()
    }
    
})
input.onLogoEvent(TouchButtonEvent.Released, function on_logo_event_released() {
    let duration: number;
    let difference: number;
    
    if (hold_for > 0) {
        duration = control.millis() - hold_for
        difference = duration - play_for
        led.plotBarGraph(difference, play_for)
        play_for = 0
        hold_for = 0
    }
    
})
