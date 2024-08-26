from shiny import ui

with open("about.md", "r") as file:
    about = file.read()

with open("instructions.md", "r") as file:
    instructions = file.read()


app_ui = ui.page_navbar(
    ui.nav_panel(
        "Interference",
        ui.div(
            ui.row(
                ui.column(
                    10,
                    ui.div(
                        ui.input_action_button("new_game", "New Game"),
                        ui.input_action_button("new_round", "New Round"),
                    ),
                    ui.div(
                        ui.output_text("game_info_output"),
                        style="margin-bottom: 10px; font-size: 120%",
                    ),
                    ui.output_ui("cards"),
                    # ui.output_text("debug_output"),
                    offset=1
                )
            ),
        ),
        ui.tags.link(rel="stylesheet", href="styles.css"),
        ui.tags.link(rel="stylesheet", href="https://fonts.googleapis.com/css?family=Figtree"),
        ui.tags.script(src="drag-drop.js"),
        ui.tags.script(src="md-navigation.js")
    ),
    ui.nav_panel(
        "Instructions", 
        ui.row(
            ui.column(
                8, 
                ui.markdown(instructions), 
                offset=2
            )
        )
    ),
    ui.nav_panel(
        "About", 
        ui.row(
            ui.column(
                8, 
                ui.markdown(about), 
                offset=2
            )
        )
    )
)
