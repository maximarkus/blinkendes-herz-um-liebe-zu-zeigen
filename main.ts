input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showIcon(IconNames.Heart)
    music.setBuiltInSpeakerEnabled(true)
    music.playTone(Note.C, music.beat(30))
})
