from gtts import gTTS
import os
import sys


def createAudio(mytext,lingua):
	#print('inicio do createAudio')
	#int(lingua)
	if lingua == '1' :
		language = 'en'
	elif lingua == '2' :
		language = 'pt'
	else:
		language = 'en'

	print('lingua definida em: ',language)

	myobj = gTTS(text=mytext, lang=language, slow=False)
	fileName = 'audio.mp3'
	print('modelo de áudio criado')

	AudioFile = myobj.save(fileName)
	print(f'arquivo de audio criado com o nome: {fileName}')

	return fileName

def texto():
	print('Digite o texto aqui e pressione duas vezes Enter quando terminar:')
	lines = []
	while True:
	    line = input()
	    if not line:
	        break
	    lines.append(line)
	texto = ', '.join(lines)
	return texto

def startAudio(choice, CreateAudioreturn):
	if choice == 'y' or choice=='Y' or choice=='':
		os.startfile(CreateAudioreturn)
	else:
		pass

def main():
    while True:
        inicio = input('Se desejar criar um áudio, tecle qualquer tecla, se não tecle n ou N :')

        if inicio == 'N' or inicio=='n':
            program = False
        else:
            program = True

        try:
            mytext = texto()
            print('\nO texto para conversão será: \n',mytext,'\n')
            lingua = input('se desejar a transcrição em inglês digite 1 se quiser em portugues, digite 2: ')
	
            audio = createAudio(mytext,lingua)
            print('\nTexto convertido em audio')

            startAudio(input('\nAudio gerado, deseja iniciar no media player? y/Y: '),audio)
            

        except:
            print('erro1')
            break

main()
