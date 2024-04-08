import pywhatkit as kit

def handle_message(message):
    # Verifica se a mensagem contém o comando '/toimg'
    if "/toimg" in message:
        try:
            # Obtém o índice do comando na mensagem
            index = message.index("/toimg")
            # Extrai o caminho do sticker após o comando '/toimg'
            caminho_sticker = message[index + len("/toimg"):].strip()
            # Converte o sticker em imagem PNG
            kit.sticker_to_png(caminho_sticker, 'imagem_converted.png')
            return "Aqui está a imagem PNG do sticker."
        except ValueError:
            return "Formato de comando '/toimg' inválido."

    # Verifica se a mensagem contém o comando '/togif'
    elif "/togif" in message:
        try:
            # Obtém o índice do comando na mensagem
            index = message.index("/togif")
            # Extrai o caminho do sticker após o comando '/togif'
            caminho_sticker = message[index + len("/togif"):].strip()
            # Converte o sticker animado em GIF
            kit.sticker_to_gif(caminho_sticker, 'animacao_converted.gif')
            return "Aqui está o GIF animado do sticker."
        except ValueError:
            return "Formato de comando '/togif' inválido."

    # Caso nenhum comando seja reconhecido
    else:
        return "Comando inválido. Use '/toimg caminho_do_sticker' para converter sticker em PNG ou '/togif caminho_do_sticker' para GIF."

# Exemplo de uso
mensagem_do_usuario = input("Digite sua mensagem: ")
resposta_bot = handle_message(mensagem_do_usuario)
print(resposta_bot)
