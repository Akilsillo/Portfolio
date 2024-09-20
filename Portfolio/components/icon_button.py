import reflex as rx

def icon_button(icon: str, variant:str, url:str="", text: str="") -> rx.Component:
    return rx.link(
        rx.button(
            rx.icon(icon),
            text,
            variant=variant,
        ),
        href=url,
        is_external=True
    )
    
def email_icon_button(icon: str, variant:str, url:str="", text: str="") -> rx.Component:
    return rx.link(
        rx.button(
            rx.icon(icon),
            text,
            variant=variant,
            on_click= rx.set_clipboard(text)
        ),
        href=url,
        is_external=False
    )