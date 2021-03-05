def on_button_pressed_a():
        basic.show_icon(IconNames.HEART)
        music.set_built_in_speaker_enabled(True)
        music.play_tone(Note.C, music.beat(30))
input.on_button_pressed(Button.A, on_button_pressed_a)