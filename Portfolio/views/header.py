import reflex as rx
from Portfolio.components.media import media
from Portfolio.components.heading import heading
from Portfolio.styles.styles import Size

def header() -> rx.Component:
    return rx.hstack(
        rx.avatar("Andrés Vargas",
                  radius="full",
                  src="avatar1.jpg",
                  size=Size.BIG.value,
        ),
        rx.vstack( 
            heading("Andrés Vargas", True),
            heading("Dios del front-end"),
            rx.hstack(
                rx.text(
                    rx.icon("map-pin"),
                    "Santiago, Chile",
                    display = "inherit"
                )
            ),
            media(),
            spacing=Size.SMALL.value
        ),
        width="100%",
        spacing=Size.DEFAULT.value
    )