import tkinter as tk
from PIL import Image, ImageTk
import os

class PathwayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pathway Interactive App")

        self.label = tk.Label(root, text="Select a pathway:")
        self.label.pack()

        self.pathway_var = tk.StringVar()
        self.pathway_var.set("")

        self.pathways = ["Krebs Cycle", "Glycolysis", "Electron Transport Chain"]
        self.pathway_menu = tk.OptionMenu(root, self.pathway_var, *self.pathways)
        self.pathway_menu.pack()

        self.show_button = tk.Button(root, text="Show Pathway", command=self.show_pathway)
        self.show_button.pack()

        self.textbox = tk.Text(root, wrap=tk.WORD, height=5, width=50)
        self.textbox.pack()

        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.pathway_descriptions = {
            "Krebs Cycle": "Description of Krebs Cycle...",
            "Glycolysis": "Description of Glycolysis...",
            "Electron Transport Chain": "Description of Electron Transport Chain..."
        }

        self.pathway_images = {
            "Krebs Cycle": "krebs_cycle.png",
            "Glycolysis": "glycolysis.png",
            "Electron Transport Chain": "electron_transport_chain.png"
        }

        # Set the working directory to the script's directory
        script_directory = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_directory)

    def show_pathway(self):
        selected_pathway = self.pathway_var.get()
        if selected_pathway in self.pathway_descriptions:
            self.textbox.delete(1.0, tk.END)
            self.textbox.insert(tk.END, self.pathway_descriptions[selected_pathway])

            image_path = self.pathway_images.get(selected_pathway)
            if image_path:
                self.show_image(image_path)
            else:
                self.hide_image()

    def show_image(self, image_path):
        image = Image.open(image_path)
        image = image.resize((500, 500), Image.LANCZOS)  # Use Image.LANCZOS for resizing
        photo = ImageTk.PhotoImage(image)

        self.image_label.config(image=photo)
        self.image_label.image = photo

        

    def hide_image(self):
        self.image_label.config(image="")
        self.image_label.image = None

def main():
    root = tk.Tk()
    app = PathwayApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
