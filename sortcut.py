import tkinter

def app():
    root = tkinter.Tk()
    root.title("Keyboard sortcut")
    root.resizable(0, 0)
    root.configure(bg="black")
    root.geometry("700x300")
    tkinter.Label(root,text="keyboard sortcut:-", font=("Arial Black", 16), fg="white", bg="black").grid()
    tkinter.Label(root,text="Close - alt+f4", font=("Arial Black", 16), fg="white", bg="black").grid()
    tkinter.Label(root,text="change window color - ctrl+w", font=("Arial Black", 16), fg="white", bg="black").grid()
    tkinter.Label(root,text="Change frame color - ctrl+f", font=("Arial Black", 16), fg="white", bg="black").grid()
    tkinter.Label(root,text="next - right arrow", font=("Arial Black", 16), fg="white", bg="black").grid()
    tkinter.Label(root,text="previous - left arrow", font=("Arial Black", 16), fg="white", bg="black").grid()
    tkinter.Label(root,text="fullscreen - F", font=("Arial Black", 16), fg="white", bg="black").grid()
    tkinter.Label(root,text="exit fullscreen - Esc", font=("Arial Black", 16), fg="white", bg="black").grid()
    root.mainloop()

if __name__ == "__main__":
    app()