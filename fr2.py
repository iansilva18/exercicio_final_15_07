from tkinter import *

root = Tk()
root.title('Estoque')
root.geometry('500x300')
root.config(background='#00c')
root.mainloop()


# # def noCommand():
#     print('oi')

# def open():
#     root.destroy()
#     fr1 = Tk()
#     fr1.title('hahaha')
#     fr1.geometry('500x300')
#     fr1.config(background='#00ed00')
#     fr1.mainloop()
# def home():
#     root = Tk()
#     root.title('Estoque')
#     root.geometry('500x300')
#     root.config(background='#00c')

#     barraMenu = Menu(root)
#     menuHome = Menu(barraMenu, tearoff=0)
#     menuHome.add_command(label="Novo", command= open)
#     menuHome.add_command(label="Pesquisar", command= noCommand)
#     menuHome.add_command(label="Deletar", command= noCommand)
#     menuHome.add_separator()
#     menuHome.add_command(label="Sair", command= root.quit)
#     barraMenu.add_cascade(label= "Produto", menu =menuHome )
#     root.config(menu= barraMenu)


#     root.mainloop()



# Vai ter uma tela padrão simples pra começo para entrad ado usuario
#Ela vai ser padrão depois disso o user vai navegar entre funções que se criam e se destroem
#  https://www.figma.com/file/h6CqqNImmkvrdYblYgifdh/Untitled?node-id=1%3A2