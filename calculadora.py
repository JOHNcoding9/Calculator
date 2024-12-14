from tkinter import *
import re # O módulo re fornece a função re.split(), que aceita uma expressão regular como delimitador. Isso permite que você defina múltiplos caracteres delimitadores (de separação).
from sympy import sympify # Parser matemático só avalia valores literais seguros Ela não executa nenhum comando ou código arbitrário.  (execução de código malicioso)
import math



# cores
cor_1 = "#000000"  # preta
cor_2 = "#636163"  # cinza
cor_3 = "#e6e6e6"  # branca
cor_4 = "#0676b8"  # azul carregado
cor_5 = "#ffb114"  # laranja

# configurações da janela
janela = Tk() 
janela.title("Calculadora Suprema")
janela.geometry("240x414")

# configuração dos frames
frame_tela = Frame(janela, width=240, height=50, bg=cor_4) 
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=240, height=365, bg=cor_2) 
frame_corpo.grid(row=1, column=0)


# criando label ( o que mostra o resultado na tela)
app_label = Label(frame_tela, text="", width=17, height=2, padx=8, relief=FLAT, anchor='e', justify=RIGHT,font=('Ivy 16 bold'),bg=cor_4 ,fg=cor_3,)
app_label.place(x=0,y=0)

# funções dos botões
def atualizar_display(texto):
    max_caracteres = 17  # Limite do display
    if app_label['text']=='Erro':
        limpar()
    novo_texto = str(app_label['text']) + texto
    if len(novo_texto) > max_caracteres:
        app_label['text'] = novo_texto[:max_caracteres] + '...'
    else:
        app_label['text'] = novo_texto

def calcular():
    try:
        expressao = sympify(app_label['text'])
        resultado = float(expressao)
        app_label['text'] = str(resultado)

    except Exception:
        app_label['text'] = "Erro"

def limpar():
    app_label['text'] = ""

def back():    
    app_label['text'] =  app_label['text'][:-1] # retorna todos os caracteres da string exceto o último.
  

def variancia():
    try:
     soma = 0
     contador = 0
     armazem = []

     label_dividida = re.findall(r'-?\d+(?:\.\d+)?', app_label["text"]) #  é usado para expressões regulares  O re.findall() procura por todas as correspondências de um padrão (pattern) em uma string e retorna todas as ocorrências em uma lista.

     # -?: Permite números negativos.
     #\d+: Captura a parte inteira do número.
     # (?:\.\d+)?: Captura a parte decimal, se existir.
     

     for i in label_dividida:
            num = float(i)
            soma += num
            contador += 1
            

     if contador > 1:
      media = soma / contador


      for i in label_dividida:
            num = float(i)
            dif_quadrado =  (num - media)**2
            armazem.append(dif_quadrado)
            
    
      variancia = sum(armazem)/ (contador -1)
      arredondamento = round(variancia,4)
      app_label['text'] = str(arredondamento)
      return variancia

    
    except ZeroDivisionError:
         app_label['text'] = "Erro: Divisão por zero"

    except Exception:
        app_label['text'] = "Erro"
    
def desvio_padrao():
   try:
    var = variancia()
    if var is not None:
     desvio =  math.sqrt(var) #(raíz quadrada)
     arredondamento = round(desvio,4)
     print(desvio)
     app_label['text'] = str(arredondamento)

   except Exception:
        app_label['text'] = "Erro"

def fatorial():
    try:
     label_dividida = re.findall(r'\d+(?:\.\d+)?', app_label["text"])
     num = int(app_label['text'])

     if num == 0 :
        app_label['text'] = '1'

     else:
      if len(label_dividida) == 1:
        fatorial = 1
        for i in range(1,num + 1):
         fatorial *= i
         fatorial_str = str(fatorial)
         if len(fatorial_str) >= 18: # caso o numero ocupe mais de 18 digitos
            fatorial_str = fatorial_str[:17] + '...'  # Mantém os primeiros 17 dígitos + ...
    
        
       
         app_label['text'] = str(fatorial_str)


    except Exception:
        app_label['text'] = "Erro"

   
def fibonacci():
   try:
    label_dividida = re.findall(r'\d+(?:\.\d+)?', app_label["text"])
    a , b = 0 , 1
    num = int(app_label['text'])

    if  len(label_dividida) == 1 and num <= 90:
     for _ in range(num): # usar _ para mostrar claramente que o valor está sendo ignorado
        a, b = b, a + b

     app_label['text'] = str(a)

    else:
     app_label['text'] = "Erro"

   except Exception:
    app_label['text'] = "Erro"

def log_base10():
    try:
     label_dividida = re.findall(r'\d+(?:\.\d+)?', app_label["text"])
     if  len(label_dividida) == 1:
      num = float(app_label['text'])
      resultado = math.log10(num)
      app_label['text'] = str(resultado)

    except Exception:
     app_label['text'] = "Erro"

def log_natural():
    try:
     label_dividida = re.findall(r'\d+(?:\.\d+)?', app_label["text"])
     if  len(label_dividida) == 1:

      num = float(app_label['text'])
      resultado = math.log(num)
      app_label['text'] = str(resultado)

    except Exception:
     app_label['text'] = "Erro"


# Configuração dos botões calculadora
    # (nome, width, cor_botao, cor_letra, x, y, comando)
botoes = [
    ("C", 11, cor_3, cor_1, 0, 0, limpar),
    ("Back", 5, cor_3, cor_1, 120, 0, back),
    ('/', 5, cor_5, cor_1 , 180, 0, lambda: atualizar_display("/")),
    ('7', 5, cor_3, cor_1, 0, 52, lambda: atualizar_display("7")),
    ('8', 5, cor_3, cor_1, 60, 52, lambda: atualizar_display("8")),
    ('9', 5, cor_3, cor_1, 120, 52, lambda: atualizar_display("9")),
    ('*', 5, cor_5, cor_1 , 180, 52, lambda: atualizar_display("*")),
    ('4', 5, cor_3, cor_1, 0, 104, lambda: atualizar_display("4")),
    ('5', 5, cor_3, cor_1, 60, 104, lambda: atualizar_display("5")),
    ('6', 5, cor_3, cor_1, 120, 104, lambda: atualizar_display("6")),
    ('-', 5, cor_5, cor_1 , 180, 104, lambda: atualizar_display("-")),
    ('1', 5, cor_3, cor_1, 0, 156, lambda: atualizar_display("1")),
    ('2', 5, cor_3, cor_1, 60, 156, lambda: atualizar_display("2")),
    ('3', 5, cor_3, cor_1, 120, 156, lambda: atualizar_display("3")),
    ('+', 5, cor_5, cor_1 , 180, 156, lambda: atualizar_display("+")),
    ("0", 11, cor_3, cor_1, 0, 208, lambda: atualizar_display("0")),
    ('.', 5, cor_3, cor_1, 120, 208, lambda: atualizar_display(".")),
    ('=', 5, cor_5, cor_1 , 180, 208, calcular),
    ('Variance',11,cor_5,cor_1,0,260,variancia),
    ('Deviation',11,cor_5,cor_1,120,260,desvio_padrao),
    ('!', 5, cor_1, cor_3, 0, 312, fatorial),
    ('Fib', 5, cor_1, cor_3, 60, 312, fibonacci),
    ('Log', 5, cor_1, cor_3, 120, 312, log_base10),
    ('Ln', 5, cor_1, cor_3, 180, 312, log_natural)
]

# impressão dos botões
for (nome,comprimento,cor_botao,cor_letra, vetor_x,vetor_y,comando) in botoes:
   
    botao = Button(frame_corpo, text=nome, width=comprimento,height=2,bg=cor_botao,fg=cor_letra,font=('Ivy 13 bold'),relief=RAISED , overrelief=RIDGE,command=comando)
    
    botao.place(x=vetor_x,y=vetor_y)


janela.mainloop() # para a Interface aparecer