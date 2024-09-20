import reflex as rx
from .icon_button import icon_button
from .icon_badge import icon_badge
from Portfolio.styles.styles import EmSize, Size, IMAGE_HEIGHT

def project()-> rx.Component:
    return rx.flex(
        rx.hstack(
            icon_badge("cloud-download"),
            rx.vstack(
                rx.text.strong("Software random"),
                rx.text("Subtitle"),
                rx.text(
                    "This is a random software, con el que puedes hacerte rico en tan solo 3 meses",
                    size=Size.SMALL.value,
                    color_scheme="gray"
                ),
                rx.flex(
                    rx.badge(rx.icon("braces", size=18), "Python", variant="soft",radius="full"),
                    rx.badge(rx.icon("brackets", size=18), "FastAPI", variant="soft",radius="full"),
                    spacing="1",
                ),
                rx.hstack(
                    icon_button(
                        icon="link",
                        variant="surface"
                    ),
                    icon_button(
                        icon="github",
                        variant="surface"
                    ),
                ),
                spacing=Size.SMALL.value,
                width="100%"
            )
        ),
        rx.image(
            src="/favicon.ico",
            height=IMAGE_HEIGHT,
            width="auto",
            border_radius=EmSize.DEFAULT.value,
            object_fit="cover"
        ),
        flex_direction=["column-reverse", "row"],
        spacing=Size.DEFAULT.value,
        width="100%"
    )