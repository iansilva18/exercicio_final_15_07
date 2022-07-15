from tkinter import *


opcoes = [
'Listar Todas as Tabelas',
'Listar Tabelas Por Nomes',
'Cadastrar Fabriante',
'Cadastrar Produto',
'Comprar Produto',
'Vender Produto',
'Excluir',
'Sair'
]

root = Tk()
altura = root.winfo_screenheight()
largura = root.winfo_screenwidth()
root.geometry('800x900')
root.config(background='white')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
#Funções
 

var =StringVar()
def caps(*args):
    var.set(var.get().title())
var.trace("w", caps)
#fabricante

var1 =StringVar()
def caps(*args):
    var1.set(var1.get().title())
var1.trace("w", caps)
#produto

var2 =StringVar()
def caps(*args):
    var2.set(var2.get().title())
var2.trace("w", caps)
#inserir coluna

var3 =StringVar()
def caps(*args):
    var3.set(var3.get().title())
var3.trace("w", caps)
#inserir novo valor

var4 =StringVar()
def caps(*args):
    var4.set(var4.get().title())
var4.trace("w", caps)
#excluir atributo da tabela
var5 =StringVar()
def caps(*args):
    var5.set(var5.get().title())
var5.trace("w", caps)
#Cadastrar Produto 
def numerico(event=None):
    x=in4_1.get().replace(' ','')
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if not x[i] in '0123456789': continue
        else:
            y+=x[i]
    in4_1.delete(0, 'end')
    in4_1.insert(0, y)

#Escolha de Opção no Menu
def escolha():
    if variable.get() == opcoes[0]: #Listar Todas as Tabelas
        fr0.grid_remove(), fr1.grid(row=0, column=0)
        estoque.listar_tabelas()
        lb1_0['text']=estoque.msg
    elif variable.get() == opcoes[1]: #Listar Tabelas Por Nomes
        fr0.grid_remove(), fr2.grid(row=0, column=0)
        estoque.listar_tabelas()
        lb2_0['text']=estoque.msg
    elif variable.get() == opcoes[2]: #Cadastrar Fabriante
        fr0.grid_remove(), fr3.grid(row=0, column=0)
    elif variable.get() == opcoes[3]: #Cadastrar Produtos
        fr0.grid_remove(), fr4.grid(row=0, column=0)

    elif variable.get() == opcoes[4]:
        fr0.grid_remove(), fr5.grid(row=0, column=0) #Alterar Atributos de Uma Tabela
        estoque.listar_tabelas()
        lb5_0_0['text']=estoque.msg
        estoque.listar("Produtos")
        lb5_0_1['text']=estoque.msg
    elif variable.get() == opcoes[5]:
        fr0.grid_remove(), fr6.grid(row=0, column=0)
    elif variable.get() == opcoes[6]:
        fr0.grid_remove(), fr7.grid(row=0, column=0)
    elif variable.get() == opcoes[7]:
        fr0.grid_remove(), fr8.grid(row=0, column=0)
    elif variable.get() == opcoes[8]:
        fr0.grid_remove(), fr9.grid(row=0, column=0)

#Cadastro do Fabricante:
def cadastro1():
    if in3_0.get() == '':
        lb3_3['text']='Tente novamente.'
    else:
        cod=None
        nome=in3_0.get()
        estoque.salvar_fabricantes(cod,nome)
        lb3_3['text']=f'Cadastro do "{in3_0.get()}" realizado.'
#Cadastro dos Produtos:
def cadastro2():
    if in4_0.get() == '' and in4_1.get() == '':
        lb4_4['text']='Algum campo vazio.'
    else:
        cod=None
        nome=in4_0.get()
        fabricante=in4_1.get()
        quantidade=0
        estoque.salvar_produtos(cod, nome, fabricante, quantidade)
        lb4_4['text']=f'Cadastro do "{in4_0.get()}" realizado.'
def alterar1():
    if in5_0.get() == '' or in5_1.get() == '' or in5_2.get() == '' or in5_3.get() == '':
        lb5_5['text']='Algum campo vazio.'
    else:
        tabela=in5_0.get()
        atributo=in5_1.get()
        valor=in5_2.get()
        cod=in5_3.get()
        estoque.alterar_tabela(tabela, atributo, valor, cod)
        lb5_5['text']=f'{estoque.msg}'
def excluir1():
    tabela=in8_0.get()
    cod=in8_1.get()
    estoque.excluir(tabela,cod)
    lb8_3['text']=f'{estoque.msg}'
def limpar1():
    lb1_0['text']=''
    lb2_0['text']=''
    lb2_1_0['text']=''
    lb3_3['text']='Mensagem de Confirmação'
    lb4_4['text']='Mensagem de Confirmação'
    lb5_5['text']='Mensagem de Confirmação'
#Cadastro dos Produtos:
#Frame0
fr0 = LabelFrame(root, bg= 'white')
fr0.grid(row=1,column=0)
lb0 = Label(fr0, text='Escolha Uma Opção ', font='Arial 25', fg='white', bg='black').grid(row=0, column=0, sticky=S)
variable = StringVar(fr0)
variable.set(opcoes[0])
opc0 = OptionMenu(fr0, variable, *opcoes).grid(row=1,column=0)
bt0 = Button(fr0, text='Confirmar', font='Arial 25', fg='white', bg='green', command= lambda: escolha()).grid(row=2,column=0, sticky=N)

#Frame1 - Listar Todas as Tabelas
fr1 = LabelFrame(root, bg= 'white')
lb1_0= Label(fr1, text='', font='Arial 25', fg='white', bg='black')
lb1_0.grid(row=0,column=1)
bt1_1 = Button(fr1, text='Voltar', font='Arial 25', fg='white', bg='red', command= lambda: [limpar1(), fr1.grid_remove(), fr0.grid()])
bt1_1.grid(row=1, column=0, columnspan=2)

#Frame2 - Listar Tabelas Por Nomes
fr2 = LabelFrame(root, bg= 'white')
lb2_0=Label(fr2, text='', font='Arial 25', fg='white', bg='black')
lb2_0.grid(row=0, column=0, columnspan=2)
lb2_1= Label(fr2, text='Insira o Nome da Tabela: ', font='Arial 25', fg='black', bg='white')
lb2_1.grid(row=1, column=0)
in2_1 = Entry(fr2, font='Arial 25', fg='black', bg='white', textvariable=var)
in2_1.grid(row=1, column=1)
bt2_3 = Button(fr2, text='Confirmar', font='Arial 25', fg='white', bg='green', command= lambda: [escolha1(), in2_1.delete(0, 'end')])
bt2_3.grid(row=2, column=0, columnspan=2)
bt2_4 = Button(fr2, text='Voltar', font='Arial 25', fg='white', bg='red', command= lambda: [limpar1(), in2_1.delete(0, 'end'), fr2.grid_remove(), fr0.grid(row=0,column=0)])
bt2_4.grid(row=3, column=0, columnspan=2)


#Frame3 - Cadastrar Fabriante
fr3 = LabelFrame(root, bg= 'white')
lb3_0 = Label(fr3, text='Insira o Nome do Fabricante:', font='Arial 25', fg='black', bg='white')
lb3_0.grid(row=0, column=0)
in3_0 = Entry(fr3, font='Arial 25', fg='black', bg='white', textvariable=var1)
in3_0.grid(row=0,column=1)
bt3_1 = Button(fr3, text='Confirmar', font='Arial 25', fg='white', bg='green', command= lambda: [cadastro1(), in3_0.delete(0,'end')])
bt3_1.grid(row=1, column=0, columnspan=2)
bt3_2 = Button(fr3, text='Voltar', font='Arial 25', fg='white', bg='red', command= lambda: [limpar1(), fr3.grid_remove(), fr0.grid(row=0,column=0)])
bt3_2.grid(row=2, column=0, columnspan=2)
lb3_3 = Label(fr3, text='Mensagem de Confirmação', font='Arial 25', fg='green', bg='white')
lb3_3.grid(row=3, column=0, columnspan=2)

#Frame4 - Cadastrar Produto
fr4 = LabelFrame(root, bg= 'white')
lb4_0_0= Label(fr4, text='', font='Arial 25', fg='black', bg='white')
lb4_0_0.grid(row=0, column=0)
lb4_0= Label(fr4, text='Insira o Nome do Produto:', font='Arial 25', fg='black', bg='white')
lb4_0.grid(row=0, column=0)
in4_0 = Entry(fr4, font='Arial 25', fg='black', bg='white', textvariable=var2)
in4_0.grid(row=0, column=1)
lb4_1= Label(fr4, text='Insira o Cod. do Fabricante:', font='Arial 25', fg='black', bg='white')
lb4_1.grid(row=1, column=0)
in4_1 = Entry(fr4, font='Arial 25', fg='black', bg='white')
in4_1.grid(row=1,column=1)
in4_1.bind('<KeyRelease>', numerico)
bt4_2 = Button(fr4, text='Confirmar', font='Arial 25', fg='white', bg='green', command= lambda: [cadastro2(), in4_0.delete(0,'end'), in4_1.delete(0,'end')])
bt4_2.grid(row=2, column=0, sticky=E)
bt4_3 = Button(fr4, text='Voltar', font='Arial 25', fg='white', bg='red', command= lambda: [limpar1(), in4_0.delete(0,'end'), in4_1.delete(0,'end'), fr4.grid_remove(), fr0.grid(row=0,column=0)])
bt4_3.grid(row=2, column=1, sticky=W)
lb4_4= Label(fr4, text='Mensagem de Confirmação', font='Arial 25', fg='green', bg='white')
lb4_4.grid(row=3, column=0, columnspan=2)

#

#
##Frame6 - Comprar Produto
#fr6 = LabelFrame(root, bg= 'red')
#lb6= Label(fr6, text='Teste6', font='Arial 25', fg='#18ab4e', bg='#2b2d94')
#lb6.grid()
#
##Frame7 - Vender Produto
#fr7 = LabelFrame(root, bg= '#b05193')
#lb7= Label(fr7, text='Teste7', font='Arial 25', fg='#18ab4e', bg='#2b2d94')
#lb7.grid()

#Frame8 - Excluir
fr8 = LabelFrame(root, bg= 'white')
lb8_0_0 = Label(fr8, text='', font='Arial 25', fg='black', bg='white')
lb8_0_0.grid(row=0, column=0, columnspan=2)
lb8_0 = Label(fr8, text='Insira o Nome da Tabela:', font='Arial 25', fg='black', bg='white')
lb8_0.grid(row=1, column=0)
in8_0 = Entry(fr8, font='Arial 25', fg='#18ab4e', bg='white', textvariable=var5)
in8_0.grid(row=1, column=1)
lb8_1 = Label(fr8, text='Insira o Cod a Excluir:', font='Arial 25', fg='black', bg='white')
lb8_1.grid(row=2, column=0)
in8_1 = Entry(fr8, font='Arial 25', fg='black', bg='white')
in8_1.grid(row=2, column=1)

bt8_2 = Button(fr8, text='Confirmar', font='Arial 25', fg='white', bg='green', command= lambda: [excluir1(), in8_0.delete(0,'end'),in8_1.delete(0,'end')])
bt8_2.grid(row=3, column=0, columnspan=2)
lb8_3= Label(fr8, text='Mensagem de Confirmação', font='green', fg='white')
lb8_3.grid(row=4, column=0, columnspan=2)


##Frame9 - Sair
#fr9 = LabelFrame(root, bg= '#b05193')
#lb9= Label(fr9, text='Teste9', font='Arial 25', fg='#18ab4e', bg='#2b2d94')
#lb9.grid()









root.mainloop()