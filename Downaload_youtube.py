
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog 

root =Tk() #Criando tela

video_Link = StringVar() 
download_Path = StringVar()

class Backend():
    def baixar_video(self):
        self.DESTINO = self.destino.get()
        self.VIDEO_URL = self.entrar_url.get()
        self.downaload_pasta = download_Path.get()
        try:
            if self.VIDEO_URL == '':
                messagebox.showinfo('ERROR', 'Pencha todos os campos')
            
            youtube = YouTube(self.VIDEO_URL)
            for stream in youtube.streams:
                    print(stream)
            youtube.streams.get_highest_resolution().download(self.downaload_pasta)
            #videoStream.download(self.downaload_pasta)
            #youtube.streams.get_highest_resolution().download()
            messagebox.showinfo("CONCLUIDO",  "DOWNLOAD SALVO EM:\n" + self.DESTINO)
            
        except Exception as e:
            print('Deu o seguinte erro:', e)


class Downaload_Youtube(Backend):
    def __init__(self):
        self.janela_tela = root
        self.janela()
        
        root.mainloop()

    # COnfiguracoes da tela
    def janela(self):
        self.janela_tela.title = ('Download do youtube')
        self.janela_tela.geometry("500x300")
        self.janela_tela.resizable(False, False)
        BACKGOUND = '#1A226F'
        self.janela_tela['background'] = BACKGOUND

        self.label_1 = Label(self.janela_tela, text='DOWNALOAD VIDEOS DO YOUTUBE', bg=BACKGOUND, fg='yellow', font='arial 18 bold')
        self.label_1.pack()

        self.label_url = Label(self.janela_tela, text='Link do video aqui', bg=BACKGOUND, fg='yellow', font='arial 10')
        self.label_url.place(x=21, y=40)

        self.entrar_url = Entry(self.janela_tela,fg='black',width=40, font='arial 12')
        self.entrar_url.place(x=25, y=60)
        #self.entrar_url.insert(0, 'https://youtu.be/2nsT9uQPIrk')

        self.baixar = Button(self.janela_tela, 
                            cursor='hand2', 
                            text= 'Downaload', 
                            bg='darkgreen', 
                            fg='white',
                            command=self.baixar_video)
        self.baixar.place(x=400, y=60)

        self.label_destino = Label(self.janela_tela, text='Local onde quer salvar', bg=BACKGOUND, fg='yellow', font='arial 10')
        self.label_destino.place(x=21, y=100)

        self.salvar_em = Button(self.janela_tela,  
                            text= 'Browse in', 
                            bg='silver', 
                            fg='black',
                            command=self.Browse)
        self.salvar_em.place(x=400, y=120)

        self.destino = Entry(self.janela_tela,fg='black',width=51, font='arial 10',
                                    textvariable=download_Path) 
        self.destino.place(x=25, y=120)

    def Browse(self):
        self.download_Directory = filedialog.askdirectory(initialdir="DIRETÓRIO DA PASTA")
        download_Path.set(self.download_Directory) 

Downaload_Youtube()