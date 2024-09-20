import reflex as rx

def about()-> rx.Component:
    return rx.vstack(
        rx.heading("Sobre mí"),
        rx.text("Soy desarrollador de software con experiencia en Python"),
        width="100%"
    )